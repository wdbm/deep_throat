# deep throat

## credits

- name by Liam Moore

## introduction

Deep throat is a program that can synthesise speech. A simple approach to unrestricted text-to-speech translation uses a small set of letter-to-sound rules, each rule specifying a pronunciation for one or more letters in some context. Deep throat features a small set of letter-to-sound rules that translate English text to phonemes, producing usably accurate pronunciations of words. Deep throat can produce sounds by combining stored representations of phoneme sounds in accordance with generated phoneme translations. It can output these sounds to computer sound hardware using PortAudio and it can save them to sound file. Deep throat can accept text as a command line option argument, from a pipe, and it can be set into an interactive mode. Deep throat can be used by other programs for speech output.

## setup

```bash
sudo apt install python3-dev python3-venv portaudio19-dev
python3 -m pip install "deep_throat[audio]"
```

Alternatively, setup can use a Python virtual environment.

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -e ".[audio,dev]"
```

## usage

|**command**                                                                                 |**comment**                                                                |
|--------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
|`deep_throat --help`                                                                        |help with options and arguments                                            |
|`deep_throat --text="hello world"`                                                          |speak specified text                                                       |
|`deep_throat --infile="text.txt"`                                                           |speak input text file                                                      |
|`deep_throat --text="hello world" --savetowavefile --outfile="test.wav"`                    |save text to WAVE file                                                     |
|`echo "test" \| deep_throat`                                                                |speak text piped from standard input                                       |
|`deep_throat --text="hello doctor name continue yesterday tomorrow" --phonemesout --verbose`|translate text to phonemes with verbose tracing                            |
|`deep_throat --interactive`                                                                 |engage interactive mode                                                    |

```Python
from deep_throat import say

say(text="hello world")
```

## phonemes

There are data for 36 phonemes and one silent space entry defined in deep throat:

|**phonemes**|
|------------|
|A           |
|B           |
|D           |
|F           |
|G           |
|H           |
|I           |
|J           |
|K           |
|L           |
|M           |
|N           |
|P           |
|R           |
|S           |
|T           |
|U           |
|V           |
|W           |
|Y           |
|Z           |
|AE          |
|AH          |
|AW          |
|CH          |
|EE          |
|EH          |
|IH          |
|OH          |
|OO          |
|SH          |
|TZ          |
|TH          |
|UH          |
|WH          |
|ZH          |

## letter-to-sound rules

Deep throat letter-to-sound rules are defined in strings in a form easy for humans to read and write. Rules have the form `A/B/C/D`: the character string `A` occurring with left context `B` and right context `C` gets the pronunciation `D`. Some simple example rules are as follows:

```
HELLO/ //H-EH-L-OH
DOCTOR/ //D-AH-K-T-U-R
NAME/ //N-A-EE-M
CONTINUE/ //K-UH-N-T-IH-N-Y-OO
YESTERDAY/ //Y-EH-S-T-U-R-D-A-EE
TOMORROW/ //T-OO-M-AW-R-OH
ARE/ / /AH-R
COMPUTER/ //K-AH-M-P-Y-OO-T-U-R
SHITFACED/ //S-H-IH-T-F-A-S-D
```

## references

- H. S. Elovitz, R. W. Johnson, A. McHugh and J. E. Shore, Automatic Translation of English Text to Phonetics by Means of Letter-to-Sound Rules, Naval Research Laboratory Report 7948 (21 January 1976)
- H. S. Elovitz, R. Johnson, A. McHugh and J. Shore, Letter-to-Sound Rules for Automatic Translation of English Text to Phonetics, IEEE Transactions on Acoustics, Speech, and Signal Processing, Volume ASSP-24, Number 6 (December 1976)
