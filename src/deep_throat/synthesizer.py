import os
import re
import struct
import sys
import wave
from contextlib import contextmanager
from dataclasses import dataclass
from typing import List, Optional, Sequence

try:
    import pyaudio
except ModuleNotFoundError:
    pyaudio = None

from .phoneme_waveforms import phonemes_dictionary
from .text_to_phoneme import text_to_phonemes


PACKED_PHONEME_BYTES = 575
DECODED_PHONEME_SAMPLES = PACKED_PHONEME_BYTES * 8
SOURCE_SAMPLE_RATE = 44100
SILENCE_SAMPLES = 5765


################################################################################
# basic phoneme waveform access                                                #
################################################################################

def _resize_nearest(values: Sequence[int], new_length: int) -> List[int]:
    if new_length < 0:
        raise ValueError("length must not be negative")
    if new_length == 0 or not values:
        return []
    if new_length == len(values):
        return list(values)

    return [values[min(len(values) - 1, index * len(values) // new_length)] for index in range(new_length)]


def phoneme_values(phoneme: str, length: Optional[int] = None, dimensions: int = 1):
    """
    Decode packed one-bit speaker states for one phoneme. Expand each of 575
    bytes most-significant bit first into eight chronological samples. If a
    length is requested, resize with nearest-neighbour sampling.
    """
    packed_data = phonemes_dictionary[phoneme]
    decoded_values: List[int] = []

    if phoneme == "space":
        decoded_values = [0] * DECODED_PHONEME_SAMPLES
    else:
        for packed_byte in packed_data:
            for bit_index in range(8):
                mask = 0x80 >> bit_index
                decoded_values.append(1 if packed_byte & mask else -1)

    if length is not None:
        decoded_values = _resize_nearest(decoded_values, length)

    if dimensions == 1:
        return decoded_values
    if dimensions == 2:
        return (list(range(len(decoded_values))), decoded_values)

    raise ValueError("dimensions must be 1 or 2")


def phonemes_values(phonemes_string: str):
    """
    Convert hyphen-separated phonemes to amplitude values.
    """
    values: List[int] = []
    for ph in phonemes_string.split("-"):
        if ph in phonemes_dictionary:
            values.extend(phoneme_values(phoneme=ph))
    return values


def phonemes_words_values(
    phonemes_words: str,
    silence_length: int = SILENCE_SAMPLES,
):
    """
    Convert a phoneme sentence to amplitude values. Treat hyphens as phoneme
    separators and each literal space as one pause unit. Concatenate decoded
    phonemes without further processing.
    """
    values: List[int] = []
    for segment_type, segment_value in _phoneme_stream_segments(phonemes_words):
        if segment_type == "pause":
            values.extend(phoneme_values(phoneme="space", length=silence_length))
        else:
            values.extend(phonemes_values(segment_value))

    if not phonemes_words.endswith(" "):
        values.extend(phoneme_values(phoneme="space", length=silence_length))

    return values


def _phoneme_stream_segments(phonemes_words: str):
    """
    Yield phoneme words and pause units without collapsing spaces.
    """
    position = 0
    while position < len(phonemes_words):
        if phonemes_words[position] == " ":
            yield ("pause", " ")
            position += 1
            continue

        end = phonemes_words.find(" ", position)
        if end < 0:
            end = len(phonemes_words)
        yield ("phonemes", phonemes_words[position:end])
        position = end


################################################################################
# audio output helpers                                                         #
################################################################################

@contextmanager
def _redirect_native_standard_error(to_null: bool):
    """
    Redirect process-level standard error to the null device during synchronous
    playback. PortAudio, ALSA and JACK write diagnostics directly to file
    descriptor 2, bypassing the Python standard-error stream.
    """
    if not to_null:
        yield
        return

    try:
        sys.stderr.flush()
    except (AttributeError, OSError):
        pass

    saved_standard_error = None
    null_descriptor = None
    try:
        saved_standard_error = os.dup(2)
        null_descriptor = os.open(os.devnull, os.O_WRONLY)
        os.dup2(null_descriptor, 2)
    except OSError:
        if null_descriptor is not None:
            os.close(null_descriptor)
        if saved_standard_error is not None:
            os.close(saved_standard_error)
        yield
        return

    try:
        yield
    finally:
        try:
            os.dup2(saved_standard_error, 2)
        finally:
            os.close(null_descriptor)
            os.close(saved_standard_error)

def amplitude_data_to_binary_data(values: Sequence[int]) -> bytes:
    """
    Normalise amplitude values to [-1.0, 1.0] as unsigned 8-bit audio bytes.
    """
    if not values:
        return b""

    min_val = min(values)
    max_val = max(values)

    if min_val == max_val:
        return bytes([128] * len(values))

    norm_factor = 2.0 / float(max_val - min_val)
    normalised = [(val - min_val) * norm_factor - 1.0 for val in values]
    byte_values = [int(sample * 127 + 128) for sample in normalised]
    return bytes(byte_values)


def play_audio(
    values: Sequence[int],
    sample_rate: int = SOURCE_SAMPLE_RATE,
    show_audio_diagnostics: bool = False,
) -> None:
    """
    Play the exact decoded two-level waveform through PyAudio as unsigned 8-bit
    audio.
    """
    audio_data = amplitude_data_to_binary_data(values)
    if not audio_data:
        return
    if pyaudio is None:
        raise RuntimeError("PyAudio is required for playback; WAV output remains available")

    with _redirect_native_standard_error(to_null=not show_audio_diagnostics):
        p = pyaudio.PyAudio()
        try:
            stream = p.open(
                format=p.get_format_from_width(1),
                channels=1,
                rate=sample_rate,
                output=True,
            )
            stream.write(audio_data)
            stream.stop_stream()
            stream.close()
        finally:
            p.terminate()


def save_wave(values: Sequence[int], filename: str, sample_rate: int = SOURCE_SAMPLE_RATE) -> None:
    """
    Save the exact decoded two-level waveform as a 16-bit mono WAV file.
    """
    wf = wave.open(filename, "w")
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(sample_rate)

    if not values:
        wf.writeframes(b"")
        wf.close()
        return

    min_val = min(values)
    max_val = max(values)

    if min_val == max_val:
        pcm_vals = [0] * len(values)
    else:
        min_target = -32768
        max_target = 32767
        scale = (max_target - min_target) / float(max_val - min_val)
        pcm_vals: List[int] = []
        for v in values:
            norm = (v - min_val) * scale + min_target
            if norm < -32768:
                norm = -32768
            elif norm > 32767:
                norm = 32767
            pcm_vals.append(int(norm))

    frames = b"".join(struct.pack("<h", val) for val in pcm_vals)
    wf.writeframes(frames)
    wf.close()


################################################################################
# text preprocessing and number translation                                    #
################################################################################

_SMALL_CARDINALS = (
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
    "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
    "sixteen", "seventeen", "eighteen", "nineteen",
)

_TENS_CARDINALS = (
    "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty",
    "ninety",
)

_SMALL_ORDINALS = (
    "zeroth", "first", "second", "third", "fourth", "fifth", "sixth", "seventh",
    "eighth", "ninth", "tenth", "eleventh", "twelfth", "thirteenth",
    "fourteenth", "fifteenth", "sixteenth", "seventeenth", "eighteenth",
    "nineteenth",
)

_TENS_ORDINALS = (
    "", "", "twentieth", "thirtieth", "fortieth", "fiftieth", "sixtieth",
    "seventieth", "eightieth", "ninetieth",
)

_NUMBER_SCALES = (
    (10 ** 18, "quintillion"),
    (10 ** 15, "quadrillion"),
    (10 ** 12, "trillion"),
    (10 ** 9, "billion"),
    (10 ** 6, "million"),
    (10 ** 3, "thousand"),
)


@dataclass(frozen=True)
class _FractionalCurrencyUnit:
    digit_count: int
    singular: str
    plural: str


@dataclass(frozen=True)
class _CurrencyDefinition:
    markers: tuple[str, ...]
    major_singular: str
    major_plural: str
    fractional_units: tuple[_FractionalCurrencyUnit, ...]


_CURRENCY_DEFINITIONS = (
    _CurrencyDefinition(
        markers=("R$", "BRL"),
        major_singular="real",
        major_plural="reais",
        fractional_units=(_FractionalCurrencyUnit(2, "centavo", "centavos"),),
    ),
    _CurrencyDefinition(
        markers=("€", "EUR"),
        major_singular="euro",
        major_plural="euros",
        fractional_units=(_FractionalCurrencyUnit(2, "cent", "cents"),),
    ),
    _CurrencyDefinition(
        markers=("₽", "RUB"),
        major_singular="rouble",
        major_plural="roubles",
        fractional_units=(_FractionalCurrencyUnit(2, "kopeck", "kopecks"),),
    ),
    _CurrencyDefinition(
        markers=("₦", "NGN"),
        major_singular="naira",
        major_plural="naira",
        fractional_units=(_FractionalCurrencyUnit(2, "kobo", "kobo"),),
    ),
    _CurrencyDefinition(
        markers=("₹", "INR"),
        major_singular="rupee",
        major_plural="rupees",
        fractional_units=(_FractionalCurrencyUnit(2, "paisa", "paise"),),
    ),
    _CurrencyDefinition(
        markers=("CN¥", "CNY", "¥"),
        major_singular="yuan",
        major_plural="yuan",
        fractional_units=(
            _FractionalCurrencyUnit(1, "jiao", "jiao"),
            _FractionalCurrencyUnit(1, "fen", "fen"),
        ),
    ),
    _CurrencyDefinition(
        markers=("₿", "BTC"),
        major_singular="bitcoin",
        major_plural="bitcoins",
        fractional_units=(_FractionalCurrencyUnit(8, "satoshi", "satoshis"),),
    ),
    _CurrencyDefinition(
        markers=("ZEC",),
        major_singular="zcash",
        major_plural="zcash",
        fractional_units=(_FractionalCurrencyUnit(8, "zatoshi", "zatoshis"),),
    ),
    _CurrencyDefinition(
        markers=("XMR",),
        major_singular="monero",
        major_plural="monero",
        fractional_units=(_FractionalCurrencyUnit(12, "piconero", "piconero"),),
    ),
    _CurrencyDefinition(
        markers=("$", "USD"),
        major_singular="dollar",
        major_plural="dollars",
        fractional_units=(_FractionalCurrencyUnit(2, "cent", "cents"),),
    ),
)


def expand_abbreviations(text: str) -> str:
    """
    Expand supported abbreviations and consume title full stops to avoid
    sentence pauses. Use fixed mappings rather than general acronym spelling.
    """
    replacements = (
        (r"\bMS\.", "miz"),
        (r"\bMRS\.", "missus"),
        (r"\bMR\.", "mister"),
        (r"\bDR\.", "doctor"),
        (r"\bPH\.?D(?:\.|\b)", "P H D"),
    )
    expanded = text
    for pattern, replacement in replacements:
        expanded = re.sub(pattern, replacement, expanded, flags=re.IGNORECASE)
    return expanded


def _separate_mixed_alphanumeric_tokens(text: str) -> str:
    """
    Separate adjacent letter and digit runs except ordinal suffixes, providing
    useful readings for forms such as "Model3", "B52" and "747B".
    """
    separated = re.sub(r"(?<=[A-Za-z])(?=\d)", " ", text)
    return re.sub(
        r"(?<=\d)(?!(?:st|nd|rd|th)\b)(?=[A-Za-z])",
        " ",
        separated,
        flags=re.IGNORECASE,
    )


def _digit_string_to_words(digits: str) -> str:
    return " ".join(_SMALL_CARDINALS[int(character)] for character in digits)


def _currency_marker_pattern(marker: str) -> str:
    escaped_marker = re.escape(marker)
    if marker[0].isalnum():
        return rf"(?<![A-Za-z0-9]){escaped_marker}"
    return escaped_marker


def _currency_unit_name(value: int, singular: str, plural: str) -> str:
    return singular if value == 1 else plural


def _format_currency_amount(
    whole_digits: str,
    fractional_digits: Optional[str],
    currency: _CurrencyDefinition,
) -> str:
    whole_value = int(whole_digits.replace(",", ""))
    major_name = _currency_unit_name(
        whole_value,
        currency.major_singular,
        currency.major_plural,
    )
    major_part = f"{number_to_words(whole_value)} {major_name}"

    decimal_places = sum(unit.digit_count for unit in currency.fractional_units)
    if fractional_digits is None:
        return major_part
    if len(fractional_digits) != decimal_places:
        decimal_words = _digit_string_to_words(fractional_digits)
        return f"{number_to_words(whole_value)} point {decimal_words} {currency.major_plural}"
    if fractional_digits == "0" * decimal_places:
        return major_part

    fractional_parts = []
    position = 0
    for unit in currency.fractional_units:
        end = position + unit.digit_count
        value = int(fractional_digits[position:end])
        position = end
        if value == 0:
            continue
        name = _currency_unit_name(value, unit.singular, unit.plural)
        fractional_parts.append(f"{number_to_words(value)} {name}")

    if len(fractional_parts) == 1:
        return f"{major_part} and {fractional_parts[0]}"
    return f"{major_part}, {' and '.join(fractional_parts)}"


def _replace_currency_amounts(text: str, number_pattern: str) -> str:
    transformed = text
    for currency in _CURRENCY_DEFINITIONS:
        marker_pattern = "|".join(
            _currency_marker_pattern(marker)
            for marker in sorted(currency.markers, key=len, reverse=True)
        )
        transformed = re.sub(
            rf"(?:{marker_pattern})\s*({number_pattern})(?:\.(\d+))?",
            lambda match, definition=currency: _format_currency_amount(
                match.group(1),
                match.group(2),
                definition,
            ),
            transformed,
            flags=re.IGNORECASE,
        )
    return transformed


def replace_numbers_in_text(text: str) -> str:
    """
    Replace cardinals, ordinals, decimals and currency amounts with words. Read
    unmatched decimal fractions digit by digit.
    """
    number_pattern = r"\d(?:\d|,(?=\d))*"
    transformed = _separate_mixed_alphanumeric_tokens(text)
    transformed = _replace_currency_amounts(transformed, number_pattern)

    def replace_decimal(match):
        whole_value = int(match.group(1).replace(",", ""))
        fractional_words = _digit_string_to_words(match.group(2))
        return f"{number_to_words(whole_value)} point {fractional_words}"

    transformed = re.sub(
        rf"(?<![A-Za-z0-9.])({number_pattern})\.(\d+)(?![A-Za-z0-9])",
        replace_decimal,
        transformed,
    )

    def replace_ordinal(match):
        value = int(match.group(1).replace(",", ""))
        return number_to_ordinal_words(value)

    transformed = re.sub(
        rf"(?<![A-Za-z0-9])({number_pattern})(?:st|nd|rd|th)(?![A-Za-z0-9])",
        replace_ordinal,
        transformed,
        flags=re.IGNORECASE,
    )

    def replace_cardinal(match):
        value = int(match.group(1).replace(",", ""))
        return number_to_words(value)

    return re.sub(
        rf"(?<![A-Za-z0-9])({number_pattern})(?![A-Za-z0-9])",
        replace_cardinal,
        transformed,
    )


def number_to_words(n: int) -> str:
    """
    Convert an integer to English cardinal words.
    """
    if n < 0:
        return "minus " + number_to_words(-n)
    if n == 0:
        return _SMALL_CARDINALS[0]
    if n < 20:
        return _SMALL_CARDINALS[n]
    if n < 100:
        tens_value, remainder = divmod(n, 10)
        result = _TENS_CARDINALS[tens_value]
        if remainder:
            result += " " + _SMALL_CARDINALS[remainder]
        return result
    if n < 1000:
        hundreds_value, remainder = divmod(n, 100)
        result = f"{_SMALL_CARDINALS[hundreds_value]} hundred"
        if remainder:
            result += " " + number_to_words(remainder)
        return result

    for scale_value, scale_name in _NUMBER_SCALES:
        if n >= scale_value:
            leading_value, remainder = divmod(n, scale_value)
            result = f"{number_to_words(leading_value)} {scale_name}"
            if remainder:
                result += " " + number_to_words(remainder)
            return result

    raise ValueError(f"number is too large to translate: {n}")


def number_to_ordinal_words(n: int) -> str:
    """
    Convert an integer to English ordinal words.
    """
    if n < 0:
        return "minus " + number_to_ordinal_words(-n)
    if n < 20:
        return _SMALL_ORDINALS[n]
    if n < 100:
        tens_value, remainder = divmod(n, 10)
        if remainder == 0:
            return _TENS_ORDINALS[tens_value]
        return f"{_TENS_CARDINALS[tens_value]} {_SMALL_ORDINALS[remainder]}"
    if n < 1000:
        hundreds_value, remainder = divmod(n, 100)
        prefix = f"{_SMALL_CARDINALS[hundreds_value]} hundred"
        if remainder == 0:
            return prefix + "th"
        return f"{prefix} {number_to_ordinal_words(remainder)}"

    for scale_value, scale_name in _NUMBER_SCALES:
        if n >= scale_value:
            leading_value, remainder = divmod(n, scale_value)
            prefix = f"{number_to_words(leading_value)} {scale_name}"
            if remainder == 0:
                return prefix + "th"
            return f"{prefix} {number_to_ordinal_words(remainder)}"

    raise ValueError(f"number is too large to translate: {n}")


def prepare_text_for_translation(text: str, translate_numbers: bool = True) -> str:
    """
    Apply deterministic abbreviation and optional numeric preprocessing.
    """
    prepared = expand_abbreviations(text)
    if translate_numbers:
        prepared = replace_numbers_in_text(prepared)
    return prepared


################################################################################
# high-level interface                                                         #
################################################################################

def say(
    text: str = None,
    phonemes: str = None,
    save_to_file: bool = False,
    filename_output: str = None,
    explain: bool = False,
    split_sentences: bool = True,
    translate_numbers: bool = True,
    pause_scale: float = 1.0,
    voice_rate: float = 0.9,
):
    """
    Speak text or a phoneme sequence. `pause_scale` changes pause duration;
    `voice_rate` changes playback speed and pitch together.
    """
    if text is not None:
        text_clean = prepare_text_for_translation(
            text,
            translate_numbers=translate_numbers,
        )

        if explain and text_clean != text:
            print("\npreprocess abbreviations and numbers:")
            print(f"input text:\n{text}")
            print(f"prepared text:\n{text_clean}")

        phoneme_seq = text_to_phonemes(text_clean, explain=explain)
        _say_phonemes_words(
            phoneme_seq,
            save_to_file=save_to_file,
            filename_output=filename_output,
            pause_scale=pause_scale,
            voice_rate=voice_rate,
            show_audio_diagnostics=explain,
        )
        return

    if phonemes is not None:
        _say_phonemes_words(
            phonemes,
            save_to_file=save_to_file,
            filename_output=filename_output,
            pause_scale=pause_scale,
            voice_rate=voice_rate,
            show_audio_diagnostics=explain,
        )
        return


def _say_phonemes_words(
    phonemes_words: str,
    save_to_file: bool,
    filename_output: Optional[str],
    pause_scale: float = 1.0,
    voice_rate: float = 0.9,
    show_audio_diagnostics: bool = False,
) -> None:
    if pause_scale < 0.0:
        raise ValueError("pause_scale must not be negative")
    if voice_rate <= 0.0:
        raise ValueError("voice_rate must be greater than zero")

    playback_sample_rate = max(1, int(round(SOURCE_SAMPLE_RATE * voice_rate)))
    silence_length = max(
        0,
        int(round(SILENCE_SAMPLES * pause_scale * voice_rate)),
    )

    audio_vals = phonemes_words_values(
        phonemes_words,
        silence_length=silence_length,
    )
    if save_to_file:
        if not filename_output:
            raise ValueError("filename_output must be provided when save_to_file is True")
        save_wave(audio_vals, filename_output, sample_rate=playback_sample_rate)
    else:
        play_audio(
            audio_vals,
            sample_rate=playback_sample_rate,
            show_audio_diagnostics=show_audio_diagnostics,
        )
