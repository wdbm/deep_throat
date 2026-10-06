#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
################################################################################
#                                                                              #
# deep throat                                                                  #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This is a speech program.                                                    #
#                                                                              #
# copyright (C) 2016 William Breaden Madden, name by Liam Moore                #
#                                                                              #
# This software is released under the terms of the GNU General Public License  #
# version 3 (GPLv3).                                                           #
#                                                                              #
# This program is free software: you can redistribute it and/or modify it      #
# under the terms of the GNU General Public License as published by the Free   #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# This program is distributed in the hope that it will be useful, but WITHOUT  #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or        #
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for     #
# more details.                                                                #
#                                                                              #
# For a copy of the GNU General Public License, see                            #
# <http://www.gnu.org/licenses/>.                                              #
#                                                                              #
################################################################################

usage:
    deep_throat [options]

options:
    -h, --help               show this help message and exit
    --version                show program version and exit
    -v, --verbose            enable verbose logging (explain translation steps)

    --interactive            run in interactive mode (type text and play speech)
    --text=TEXT              input text to speak
    --phonemes=TEXT          input phoneme string to speak (e.g. "H-EH-L-OH")
    --phonemesout            output phoneme translation of given text (no sound)

    --infile=FILENAME        read input text from file
    --outfile=FILENAME       output sound filename [default: speech.wav]
    --savetowavefile         save the speech audio to a WAV file instead of playing
    --translatenumbers=BOOL  convert numeric digits to words [default: true]

    --pause-scale=FACTOR     scale pause duration; zero disables pauses [default: 1.0]
    --voice-rate=FACTOR      scale playback speed and pitch together [default: 0.9]
"""

import sys

import docopt

from . import __version__
from . import synthesizer
from . import text_to_phoneme


def _timing_option(value, option_name, allow_zero=False):
    """
    Parse and validate a command line timing factor.
    """
    try:
        parsed_value = float(value)
    except (TypeError, ValueError):
        print(f"{option_name} must be a number")
        sys.exit(1)

    minimum_is_valid = parsed_value >= 0.0 if allow_zero else parsed_value > 0.0
    if not minimum_is_valid:
        comparison = "zero or greater" if allow_zero else "greater than zero"
        print(f"{option_name} must be {comparison}")
        sys.exit(1)
    return parsed_value


def main(options):
    filename_input         = options["--infile"]
    filename_output        = options["--outfile"]
    text_input             = options["--text"]
    phonemes_input         = options["--phonemes"]
    mode_interactive       = options["--interactive"]
    mode_phonemes_out      = options["--phonemesout"]
    mode_save_to_file      = options["--savetowavefile"]
    mode_translate_numbers = (options["--translatenumbers"] or "").lower() != "false"
    verbose                = options["--verbose"]

    pause_scale = _timing_option(options["--pause-scale"], "--pause-scale", allow_zero=True)
    voice_rate = _timing_option(options["--voice-rate"], "--voice-rate")

    if mode_phonemes_out:
        if verbose:
            print("\nmode: phonemes output")

        if text_input is not None:
            input_text = text_input
        elif not sys.stdin.isatty():
            input_text = "".join(sys.stdin.readlines())
        else:
            print("no input text specified for phoneme output")
            sys.exit(1)

        input_text = synthesizer.prepare_text_for_translation(
            input_text,
            translate_numbers=mode_translate_numbers,
        )
        phoneme_str = text_to_phoneme.text_to_phonemes(text=input_text, explain=verbose)
        print(phoneme_str)
        return

    if text_input is not None:
        if verbose:
            print("\nmode: say text")

        synthesizer.say(
            text=text_input,
            save_to_file=mode_save_to_file,
            filename_output=filename_output,
            explain=verbose,
            translate_numbers=mode_translate_numbers,
            pause_scale=pause_scale,
            voice_rate=voice_rate,
        )
        return

    if phonemes_input is not None:
        if verbose:
            print("\nmode: say phonemes")

        synthesizer.say(
            phonemes=phonemes_input,
            save_to_file=mode_save_to_file,
            filename_output=filename_output,
            explain=verbose,
            pause_scale=pause_scale,
            voice_rate=voice_rate,
        )
        return

    if filename_input is not None:
        if verbose:
            print("\nmode: say file")

        try:
            with open(filename_input, "r", encoding="utf-8") as f:
                file_text = f.read()
        except FileNotFoundError:
            print(f"file {filename_input} not found")
            sys.exit(1)

        synthesizer.say(
            text=file_text,
            save_to_file=mode_save_to_file,
            filename_output=filename_output,
            explain=verbose,
            translate_numbers=mode_translate_numbers,
            pause_scale=pause_scale,
            voice_rate=voice_rate,
        )
        return

    if mode_interactive:
        if verbose:
            print("\nmode: interactive")

        print("Deep throat interactive mode. Type text and press Enter (Ctrl+C to exit).")
        try:
            while True:
                user_text = input("> ")
                if user_text.strip() == "":
                    continue
                synthesizer.say(
                    text=user_text,
                    save_to_file=mode_save_to_file,
                    filename_output=filename_output,
                    explain=verbose,
                    translate_numbers=mode_translate_numbers,
                    pause_scale=pause_scale,
                    voice_rate=voice_rate,
                )
        except KeyboardInterrupt:
            print("\nExiting interactive mode.")
            sys.exit(0)

    if not sys.stdin.isatty():
        standard_input_text = sys.stdin.read()
        if standard_input_text.strip():
            if verbose:
                print("\nmode: say standard input")

            synthesizer.say(
                text=standard_input_text,
                save_to_file=mode_save_to_file,
                filename_output=filename_output,
                explain=verbose,
                translate_numbers=mode_translate_numbers,
                pause_scale=pause_scale,
                voice_rate=voice_rate,
            )
            return

    if verbose:
        print("\nmode: no operations specified")

    print("no operations specified.\n")
    print(__doc__.strip())
    sys.exit(0)


def run(argv=None):
    options = docopt.docopt(__doc__, argv=argv, version=__version__)
    main(options)


if __name__ == "__main__":
    run()
