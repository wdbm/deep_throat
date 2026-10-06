import re
from dataclasses import dataclass

from .phoneme_waveforms import phonemes_dictionary


def _normalise_translation_input(text: str) -> str:
    """
    Replace unsupported characters, normalise line endings and keep punctuation
    representing pauses.
    """
    allowed_chars = set(
        " \t\r\n0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.,;:!?\"()-"
    )
    cleaned = "".join(character if character in allowed_chars else " " for character in text)
    return cleaned.replace("\r\n", "\n").replace("\r", "\n")

# rule-pattern symbols
rules_English_to_phonemes_special_symbols = {
    "#": r"[AEIOUY]+",               # one or more vowels
    ".": r"[BVDGJLMNRWZ]",           # voiced consonant (B, V, D, G, J, L, M, N, R, W, Z)
    "%": r"(?:ING|ELY|ER|ES|ED|E)",  # suffix
    "&": r"(?:CH|SH|[SCGZXJ])",      # sibilant
    "@": r"(?:TH|CH|SH|[TSRDLZNJ])", # consonant affecting following long "U"
    "^": r"[BCDFGHJKLMNPQRSTVWXZ]",  # single consonant
    "+": r"[EIY]",                   # front vowel (E, I, Y)
    ":": r"[BCDFGHJKLMNPQRSTVWXZ]*", # zero or more consonants
}


# Letter-to-sound rules are defined in strings in a form easy for humans to read
# and write. Rules have the form A/B/C/D. The character string occurring with
# left context A and right context C gets the pronunciation D. The rules follow
# the 1976 NRL papers and the 1985 implementation by John A. Wasser and include
# number, ordinal, letter-name and bespoke word rules.
#
# A/B/C/D fields:
#
# - A: character string to match
# - B: left context pattern (can use special symbols)
# - C: right context pattern (can use special symbols)
# - D: phoneme string output
rules_English_to_phonemes = [
    "A// /UH",
    "ARE/ / /AH-R",
    "AR/ /O/UH-R",
    "AR//#/EH-R",
    "AS/^/#/A-EE-S",
    "A//WA/UH",
    "AW///AW",
    "ANY/ ://EH-N-EE",
    "A//^+#/A-EE",
    "ALLY/#://UH-L-EE",
    "AL/ /#/UH-L",
    "AGAIN///UH-G-EH-N",
    "AG/#:/E/IH-J",
    "A//^+:#/AE",
    "A/ :/^+ /A-EE",
    "A//^%/A-EE",
    "ARR/ //UH-R",
    "ARR///AE-R",
    "AR/ :/ /AH-R",
    "AR// /U-R",
    "AR///AH-R",
    "AIR///EH-R",
    "AI///A-EE",
    "AY///A-EE",
    "AU///AW",
    "AL/#:/ /UH-L",
    "ALS/#:/ /UH-L-Z",
    "ALK///AW-K",
    "AL//^/AW-L",
    "ABLE/ ://A-EE-B-UH-L",
    "ABLE///UH-B-UH-L",
    "ANG//+/A-EE-N-J",
    "ATHE/ C/ /AE-TH-EE",
    "A///AE",
    "BE/ /^#/B-IH",
    "BEING///B-EE-IH-N-G",
    "BOTH/ / /B-OH-TH",
    "BUS/ /#/B-IH-Z",
    "BUIL///B-IH-L",
    "B/ / /B-EE",
    "B///B",
    "CH/ /^/K",
    "CH/^E//K",
    "CH///CH",
    "CI/ S/#/S-AH-EE",
    "CI//A/SH",
    "CI//O/SH",
    "CI//EN/SH",
    "CC//+/K-S",
    "CC///K",
    "C//+/S",
    "CK///K",
    "COM//%/K-UH-M",
    "C/ / /S-EE",
    "C///K",
    "DED/#:/ /D-IH-D",
    "D/.E/ /D",
    "D/#:^E/ /T",
    "DE/ /^#/D-IH",
    "DO/ / /D-OO",
    "DOES/ //D-UH-Z",
    "DOING/ //D-OO-IH-N-G",
    "DOW/ //D-AH-OH",
    "DU//A/J-OO",
    "D/ / /D-EE",
    "DOUGH///D-OH",
    "D///D",
    "E/#:/ /",
    "E/':^/ /",
    "E/ :/ /EE",
    "ED/#/ /D",
    "E/#:/D /",
    "EV//ER/EH-V",
    "EVEN/ EL//EH-V-EH-N",
    "EVEN/ S//EH-V-EH-N",
    "E//^%/EE",
    "E//PH%/EE",
    "ERI//#/EE-R-EE",
    "ERI///EH-R-IH",
    "ER/#:/#/U-R",
    "ER//#/EH-R",
    "ER///U-R",
    "EVEN/ //EE-V-EH-N",
    "E/#:/W/",
    "EW/@//OO",
    "EW///Y-OO",
    "E//O/EE",
    "ES/#:&/ /IH-Z",
    "E/#:/S /",
    "ELY/#:/ /L-EE",
    "EMENT/#://M-EH-N-T",
    "EFUL///F-U-L",
    "EE///EE",
    "EARN///U-R-N",
    "EAR/ /^/U-R",
    "EAD///EH-D",
    "EA/#:/ /EE-UH",
    "EA//SU/EH",
    "EA///EE",
    "EIGH///A-EE",
    "EI///EE",
    "EYE/ //AH-EE",
    "EY///EE",
    "EU///Y-OO",
    "E/ / /EE",
    "E/^/ /",
    "E///EH",
    "FUL///F-U-L",
    "F/F//",
    "F/ / /EH-F",
    "F///F",
    "GIV///G-IH-V",
    "G/ /I^/G",
    "GE//T/G-EH",
    "GGES/SU//G-J-EH-S",
    "GG///G",
    "G/ B#//G",
    "G//+/J",
    "GREAT///G-R-A-EE-T",
    "GH/#//",
    "G/ / /J-EE",
    "G///G",
    "HAV/ //H-AE-V",
    "HERE/ //H-EE-R",
    "HOUR/ //AH-OH-U-R",
    "HOW///H-AH-OH",
    "H//#/H",
    "H/ / /A-EE-CH",
    "H///",
    "IN/ //IH-N",
    "I/ / /AH-EE",
    "IN//D/AH-EE-N",
    "IER///EE-U-R",
    "IED/#:R//EE-D",
    "IED// /AH-EE-D",
    "IEN///EE-EH-N",
    "IE//T/AH-EE-EH",
    "I/ :/%/AH-EE",
    "I//%/EE",
    "IE///EE",
    "INE/N//AH-EE-N",
    "IME/T//AH-EE-M",
    "I//^+:#/IH",
    "IR//#/AH-EE-R",
    "IS//%/AH-EE-Z",
    "IX//%/IH-K-S",
    "IZ//%/AH-EE-Z",
    "I//D%/AH-EE",
    "I/+^/^+/IH",
    "I//T%/AH-EE",
    "I/#:^/^+/IH",
    "I//^+/AH-EE",
    "IR///U-R",
    "IGH///AH-EE",
    "ILD///AH-EE-L-D",
    "IGN// /AH-EE-N",
    "IGN//^/AH-EE-N",
    "IGN//%/AH-EE-N",
    "IQUE///EE-K",
    "I///IH",
    "J/ / /J-A-EE",
    "J///J",
    "K/ /N/",
    "K/ / /K-A-EE",
    "K///K",
    "LO//C#/L-OH",
    "L/L//",
    "L/#:^/%/UH-L",
    "LEAD///L-EE-D",
    "L/ / /EH-L",
    "L///L",
    "MOV///M-OO-V",
    "M/ / /EH-M",
    "M///M",
    "NG/E/+/N-J",
    "NG//R/N-G-G",
    "NG//#/N-G-G",
    "NGL//%/N-G-G-UH-L",
    "NG///N-G",
    "NK///N-G-K",
    "NOW/ / /N-AH-OH",
    "N/ / /EH-N",
    "N/N//",
    "N///N",
    "OF// /UH-V",
    "OROUGH///U-R-OH",
    "OR/ F/TY/OH-R",
    "OR/#:/ /U-R",
    "ORS/#:/ /U-R-Z",
    "OR///AW-R",
    "ONE/ //W-UH-N",
    "OW//EL/AH-OH",
    "OW///OH",
    "OVER/ //OH-V-U-R",
    "OV///UH-V",
    "O//^%/OH",
    "O//^EN/OH",
    "O//^I#/OH",
    "OL//D/OH-L",
    "OUGHT///AW-T",
    "OUGH///UH-F",
    "OU/^/^L/UH",
    "OU/ //AH-OH",
    "OU/H/S#/AH-OH",
    "OUS///UH-S",
    "OUR/ F//OH-R",
    "OUR///AW-R",
    "OULD///U-D",
    "OUP///OO-P",
    "OU///AH-OH",
    "OY///AW-EE",
    "OING///OH-IH-N-G",
    "OI///AW-EE",
    "OOR///AW-R",
    "OOK///U-K",
    "OOD///U-D",
    "OO///OO",
    "O//E/OH",
    "O// /OH",
    "OA///OH",
    "ONLY/ //OH-N-L-EE",
    "ONCE/ //W-UH-N-S",
    "ON'T///OH-N-T",
    "O/C/N/AH",
    "O//NG/AW",
    "O/ :^/N/UH",
    "ON/I//UH-N",
    "ON/#:/ /UH-N",
    "ON/#^//UH-N",
    "O//ST /OH",
    "OF//^/AW-F",
    "OTHER///UH-TH-U-R",
    "OSS// /AW-S",
    "OM/#:^//UH-M",
    "O///AH",
    "PH///F",
    "PEOP///P-EE-P",
    "POW///P-AH-OH",
    "PUT// /P-U-T",
    "P/ / /P-EE",
    "P/P//",
    "P///P",
    "QUAR///K-W-AW-R",
    "QU/ //K-W",
    "QU///K-W",
    "Q/ / /K-Y-OO",
    "Q///K",
    "RE/ /^#/R-EE",
    "R/ / /AH-R",
    "R/R//",
    "R///R",
    "SH///SH",
    "SION/#//ZH-UH-N",
    "SOME///S-UH-M",
    "SUR/#/#/ZH-U-R",
    "SUR//#/SH-U-R",
    "SU/#/#/ZH-OO",
    "SSU/#/#/SH-OO",
    "SED/#/ /Z-D",
    "S/#/#/Z",
    "SAID///S-EH-D",
    "SION/^//SH-UH-N",
    "S//S/",
    "S/./ /Z",
    "S/#:.E/ /Z",
    "S/#:^##/ /Z",
    "S/#:^#/ /S",
    "S/U/ /S",
    "S/ :#/ /Z",
    "SCH/ //S-K",
    "S//C+/",
    "SM/#//Z-M",
    "SN/#/'/Z-UH-N",
    "S/ / /EH-S",
    "S///S",
    "THE/ / /TH-UH",
    "TO// /T-OO",
    "THAT// /TH-AE-T",
    "THIS/ / /TH-IH-S",
    "THEY/ //TH-A-EE",
    "THERE/ //TH-EH-R",
    "THER///TH-U-R",
    "THEIR///TH-EH-R",
    "THAN/ / /TH-AE-N",
    "THEM/ / /TH-EH-M",
    "THESE// /TH-EE-Z",
    "THEN/ //TH-EH-N",
    "THROUGH///TH-R-OO",
    "THOSE///TH-OH-Z",
    "THOUGH// /TH-OH",
    "THUS/ //TH-UH-S",
    "TH///TH",
    "TED/#:/ /T-IH-D",
    "TI/S/#N/CH",
    "TI//O/SH",
    "TI//A/SH",
    "TIEN///SH-UH-N",
    "TUR//#/CH-U-R",
    "TU//A/CH-OO",
    "TWO/ //T-OO",
    "T/ / /T-EE",
    "T/T//",
    "T///T",
    "UN/ /I/Y-OO-N",
    "UN/ //UH-N",
    "UPON/ //UH-P-AW-N",
    "UR/@/#/U-R",
    "UR//#/Y-U-R",
    "UR///U-R",
    "U//^ /UH",
    "U//^^/UH",
    "UY///AH-EE",
    "U/ G/#/",
    "U/G/%/",
    "U/G/#/W",
    "U/#N//Y-OO",
    "UI/@//OO",
    "U/@//OO",
    "U///Y-OO",
    "VIEW///V-Y-OO",
    "V/ / /V-EE",
    "V///V",
    "WERE/ //W-U-R",
    "WA//S/W-AH",
    "WA//T/W-AH",
    "WHERE///WH-EH-R",
    "WHAT///WH-AH-T",
    "WHOL///H-OH-L",
    "WHO///H-OO",
    "WH///WH",
    "WAR///W-AW-R",
    "WOR//^/W-U-R",
    "WR///R",
    "W/ / /D-UH-B-UH-L-Y-OO",
    "W///W",
    #"X//^/EH-K-S",
    "X/ / /EH-K-S",
    "X/ /#/Z-EH",
    "X///K-S",
    "YOUNG///Y-UH-N-G",
    "YOU/ //Y-OO",
    "YES/ //Y-EH-S",
    "Y/ / /W-I",
    "Y/ //Y",
    "Y/IF//AH-EE",
    "Y/#:^/ /EE",
    "Y/#:^/I/EE",
    "Y/ :/ /AH-EE",
    "Y/ :/#/AH-EE",
    "Y/ :/^+:#/IH",
    "Y/ :/^#/AH-EE",
    "Y///IH",
    "ZZ///T-Z",
    "Z/ / /Z-EH-D",
    "Z///Z",
    # apostrophe and possessive rules
    "'S/.//Z",
    "'S/#:.E//Z",
    "'S/#//Z",
    "'///",
    # cardinal numbers
    "0/ / /Z-EE-R-OH",
    "1/ / /W-UH-N",
    "2/ / /T-OO",
    "3/ / /TH-R-EE",
    "4/ / /F-OH-R",
    "5/ / /F-I-V",
    "6/ / /S-IH-K-S",
    "7/ / /S-EH-V-EH-N",
    "8/ / /A-EE-T",
    "9/ / /N-I-N",
    "10/ / /T-EH-N",
    "11/ / /EH-L-EH-V-UH-N",
    "12/ / /T-W-EH-L-V",
    "13/ / /TH-U-R-T-EE-N",
    "14/ / /F-OH-R-T-EE-N",
    "15/ / /F-IH-F-T-EE-N",
    "16/ / /S-IH-K-S-T-EE-N",
    "17/ / /S-EH-V-EH-N-T-EE-N",
    "18/ / /A-EE-T-EE-N",
    "19/ / /N-I-N-T-EE-N",
    "20/ / /T-W-EH-N-T-EE",
    "30/ / /TH-U-R-T-EE",
    "40/ / /F-OH-R-T-EE",
    "50/ / /F-IH-F-T-EE",
    "60/ / /S-IH-K-S-T-EE",
    "70/ / /S-EH-V-EH-N-T-EE",
    "80/ / /A-EE-T-EE",
    "90/ / /N-I-N-T-EE",
    "HUNDRED/ / /H-UH-N-D-R-EH-D",
    "THOUSAND/ / /TH-AH-OH-Z-UH-N-D",
    "MILLION/ / /M-IH-L-Y-UH-N",
    # ordinals
    "FIRST/ / /F-U-R-S-T",
    "SECOND/ / /S-EH-K-UH-N-D",
    "THIRD/ / /TH-U-R-D",
    "FOURTH/ / /F-OH-R-TH",
    "FIFTH/ / /F-IH-F-TH",
    "SIXTH/ / /S-IH-K-S-TH",
    "SEVENTH/ / /S-EH-V-EH-N-TH",
    "EIGHTH/ / /A-EE-T-TH",
    "NINTH/ / /N-I-N-TH",
    "TENTH/ / /T-EH-N-TH",
    # letter names (A and I use article and pronoun rules)
    "A/ / /A-EE",
    "B/ / /B-EE",
    "C/ / /S-EE",
    "D/ / /D-EE",
    "E/ / /EE",
    "F/ / /EH-F",
    "G/ / /J-EE",
    "H/ / /A-EE-CH",
    "I/ / /I",
    "J/ / /J-A-EE",
    "K/ / /K-A-EE",
    "L/ / /EH-L",
    "M/ / /EH-M",
    "N/ / /EH-N",
    "O/ / /OH",
    "P/ / /P-EE",
    "Q/ / /K-Y-OO",
    "R/ / /AH-R",
    "S/ / /EH-S",
    "T/ / /T-EE",
    "U/ / /Y-OO",
    "V/ / /V-EE",
    "W/ / /D-UH-B-UH-L-Y-OO",
    "X/ / /EH-K-S",
    "Y/ / /W-I",
    "Z/ / /Z-EH-D",
    # currency unit names
    "BITCOIN/ / /B-IH-T-K-AW-EE-N",
    "BITCOINS/ / /B-IH-T-K-AW-EE-N-Z",
    "CENT/ / /S-EH-N-T",
    "CENTS/ / /S-EH-N-T-S",
    "CENTAVO/ / /S-EH-N-T-AH-V-OH",
    "CENTAVOS/ / /S-EH-N-T-AH-V-OH-S",
    "EURO/ / /Y-OO-R-OH",
    "EUROS/ / /Y-OO-R-OH-Z",
    "FEN/ / /F-EH-N",
    "JIAO/ / /J-AW",
    "KOBO/ / /K-OH-B-OH",
    "KOPECK/ / /K-OH-P-EH-K",
    "KOPECKS/ / /K-OH-P-EH-K-S",
    "MONERO/ / /M-UH-N-EH-R-OH",
    "NAIRA/ / /N-AH-EE-R-UH",
    "PAISA/ / /P-AH-EE-S-UH",
    "PAISE/ / /P-AH-EE-S-A-EE",
    "PICONERO/ / /P-EE-K-OH-N-EH-R-OH",
    "REAL/ / /R-A-EE-AH-L",
    "REAIS/ / /R-A-EE-AH-EE-S",
    "ROUBLE/ / /R-OO-B-UH-L",
    "ROUBLES/ / /R-OO-B-UH-L-Z",
    "RUPEE/ / /R-OO-P-EE",
    "RUPEES/ / /R-OO-P-EE-Z",
    "SATOSHI/ / /S-UH-T-OH-SH-EE",
    "SATOSHIS/ / /S-UH-T-OH-SH-EE-Z",
    "YUAN/ / /Y-OO-AH-N",
    "ZATOSHI/ / /Z-UH-T-OH-SH-EE",
    "ZATOSHIS/ / /Z-UH-T-OH-SH-EE-Z",
    "ZCASH/ / /Z-EE-K-AE-SH",
    # bespoke words
    "A/ / /UH",
    "ABILITY/ / /AE-B-IH-L-IH-T-EE",
    "ABOARD/ / /UH-B-OH-R-D",
    "ABORT/ / /UH-B-OH-R-T",
    "AFFIRMATIVE/ / /AH-F-EH-R-M-AH-T-IH-V",
    "ALL/ / /AW-L",
    "ALTER/ / /AH-L-T-U-R",
    "AN/ / /AE-N",
    "AND/ / /AE-N-D",
    "ANDY/ / /AE-N-D-EE",
    "ANY/ / /EH-N-EE",
    "ANYBODY/ / /EH-N-EE-B-AH-D-EE",
    "AT/ / /AE-T",
    "ATTACKED/ / /UH-T-AE-K-T",
    "BACKUP/ / /B-AH-K-UH-P",
    "BASIC/ / /B-A-EE-S-IH-K",
    "BAUD/ / /B-AW-D",
    "BE/ / /B-EE",
    "BEGIN/ / /B-IH-G-IH-N",
    "BOCCE/ / /B-AW-CH-EE",
    "BOCCIA/ / /B-AW-CH-UH",
    "BOOT/ / /B-OO-T",
    "BOSS/ / /B-AW-S",
    "BREAK/ / /B-R-A-EE-K",
    "BUG/ / /B-UH-G",
    "CALL/ / /K-AW-L",
    "CALLING/ / /K-AW-L-IH-N-G",
    "CAPABLE/ / /K-A-EE-P-UH-B-UH-L",
    "CAPPUCCINO/ / /K-AE-P-UH-CH-EE-N-OH",
    "CHARLIE/ / /CH-AH-R-L-EE",
    "CITY/ / /S-IH-T-EE",
    "COLD/ / /K-OH-L-D",
    "COMBINE/ / /K-UH-M-B-AH-EE-N",
    "COMBINED/ / /K-UH-M-B-AH-EE-N-D",
    "COMBINES/ / /K-UH-M-B-AH-EE-N-Z",
    "COMBINING/ / /K-UH-M-B-AH-EE-N-IH-N-G",
    "COMBINATIONS/ / /K-AH-M-B-IH-N-A-EE-SH-UH-N-Z",
    "COMES/ / /K-UH-M-Z",
    "COMMAND/ / /K-UH-M-AH-N-D",
    "COMPUTER/ / /K-AH-M-P-Y-OO-T-U-R",
    "CONFINE/ / /K-UH-N-F-AH-EE-N",
    "CONFINED/ / /K-UH-N-F-AH-EE-N-D",
    "CONFINES/ / /K-UH-N-F-AH-EE-N-Z",
    "CONFINING/ / /K-UH-N-F-AH-EE-N-IH-N-G",
    "CONSIDER/ / /K-UH-N-S-IH-D-U-R",
    "CONTINUE/ / /K-UH-N-T-IH-N-Y-OO",
    "COPYRIGHT/ / /K-AH-P-EE-R-I-T",
    "CRASH/ / /K-R-AH-SH",
    "DECLINE/ / /D-IH-K-L-AH-EE-N",
    "DECLINED/ / /D-IH-K-L-AH-EE-N-D",
    "DECLINES/ / /D-IH-K-L-AH-EE-N-Z",
    "DECLINING/ / /D-IH-K-L-AH-EE-N-IH-N-G",
    "DEFINE/ / /D-IH-F-AH-EE-N",
    "DEFINED/ / /D-IH-F-AH-EE-N-D",
    "DEFINES/ / /D-IH-F-AH-EE-N-Z",
    "DEFINING/ / /D-IH-F-AH-EE-N-IH-N-G",
    "HARDWARE/ / /H-AH-R-D-W-EH-R",
    "ENGLISH/ / /IH-N-G-L-IH-SH",
    "FOCACCIA/ / /F-UH-K-AE-CH-UH",
    "INCLINE/ / /IH-N-K-L-AH-EE-N",
    "INCLINED/ / /IH-N-K-L-AH-EE-N-D",
    "INCLINES/ / /IH-N-K-L-AH-EE-N-Z",
    "INCLINING/ / /IH-N-K-L-AH-EE-N-IH-N-G",
    "OUTLINE/ / /AH-OH-T-L-AH-EE-N",
    "OUTLINED/ / /AH-OH-T-L-AH-EE-N-D",
    "OUTLINES/ / /AH-OH-T-L-AH-EE-N-Z",
    "OUTLINING/ / /AH-OH-T-L-AH-EE-N-IH-N-G",
    "PROGRAM/ / /P-R-OH-G-R-AE-M",
    "PROGRAMS/ / /P-R-OH-G-R-AE-M-Z",
    "PYTHON/ / /P-AH-EE-TH-UH-N",
    "RECLINE/ / /R-IH-K-L-AH-EE-N",
    "RECLINED/ / /R-IH-K-L-AH-EE-N-D",
    "RECLINES/ / /R-IH-K-L-AH-EE-N-Z",
    "RECLINING/ / /R-IH-K-L-AH-EE-N-IH-N-G",
    "REFERENCE/ / /R-EH-F-U-R-UH-N-S",
    "REFERENCED/ / /R-EH-F-U-R-UH-N-S-T",
    "REFERENCES/ / /R-EH-F-U-R-UH-N-S-IH-Z",
    "REFERENCING/ / /R-EH-F-U-R-UH-N-S-IH-N-G",
    "REFINE/ / /R-IH-F-AH-EE-N",
    "REFINED/ / /R-IH-F-AH-EE-N-D",
    "REFINES/ / /R-IH-F-AH-EE-N-Z",
    "REFINING/ / /R-IH-F-AH-EE-N-IH-N-G",
    "SOCCER/ / /S-AW-K-U-R",
    "TOMORROW/ / /T-OO-M-AW-R-OH",
    "UNDERLINE/ / /UH-N-D-UH-R-L-AH-EE-N",
    "UNDERLINED/ / /UH-N-D-UH-R-L-AH-EE-N-D",
    "UNDERLINES/ / /UH-N-D-UH-R-L-AH-EE-N-Z",
    "UNDERLINING/ / /UH-N-D-UH-R-L-AH-EE-N-IH-N-G",
    "UNDERMINE/ / /UH-N-D-UH-R-M-AH-EE-N",
    "UNDERMINED/ / /UH-N-D-UH-R-M-AH-EE-N-D",
    "UNDERMINES/ / /UH-N-D-UH-R-M-AH-EE-N-Z",
    "UNDERMINING/ / /UH-N-D-UH-R-M-AH-EE-N-IH-N-G",
    "X/ / /EH-K-S",
    "YOUR/ / /Y-OH-R"
]

@dataclass(frozen=True)
class TranslationRule:
    match: str
    left_context: str
    right_context: str
    phoneme_output: str
    source_text: str
    source_index: int


def make_regex_fragment(pattern: str) -> str:
    """
    Convert the supplied context pattern into regular-expression syntax. Escape
    literal characters and interpret eight documented context symbols.
    """
    fragments = []
    for character in pattern:
        fragments.append(
            rules_English_to_phonemes_special_symbols.get(character, re.escape(character))
        )
    return "".join(fragments)


def _parse_rule(rule_text: str, source_index: int) -> TranslationRule:
    match, left_context, right_context, phoneme_output = rule_text.split("/")
    return TranslationRule(
        match=match,
        left_context=left_context,
        right_context=right_context,
        phoneme_output=phoneme_output.strip(),
        source_text=rule_text,
        source_index=source_index,
    )


_translation_rules = tuple(
    _parse_rule(rule_text, source_index)
    for source_index, rule_text in enumerate(rules_English_to_phonemes)
)

_rules_by_initial = {}
for _rule in _translation_rules:
    _rules_by_initial.setdefault(_rule.match[0], []).append(_rule)

_number_rules_start = rules_English_to_phonemes.index("0/ / /Z-EE-R-OH")
_letter_names_start = rules_English_to_phonemes.index("A/ / /A-EE", _number_rules_start)
_bespoke_words_start = rules_English_to_phonemes.index("A/ / /UH", _letter_names_start)

_pause_widths = {
    ",": 1,
    ";": 1,
    "-": 1,
    ".": 2,
    ":": 2,
    "!": 2,
    "?": 2,
    '"': 2,
    "(": 2,
    ")": 2,
}

_digit_outputs = {
    rule.match: rule.phoneme_output
    for rule in _translation_rules[_number_rules_start:_letter_names_start]
    if len(rule.match) == 1 and rule.match.isdigit()
}


def _left_context_matches(pattern: str, text: str) -> bool:
    if pattern == "":
        return True
    return re.search(f"(?:{make_regex_fragment(pattern)})$", text) is not None


def _right_context_matches(pattern: str, text: str) -> bool:
    if pattern == "":
        return True
    return re.match(make_regex_fragment(pattern), text) is not None


def _rule_matches(rule: TranslationRule, padded_token: str, position: int) -> bool:
    if not padded_token.startswith(rule.match, position):
        return False
    if not _left_context_matches(rule.left_context, padded_token[:position]):
        return False
    right_start = position + len(rule.match)
    return _right_context_matches(rule.right_context, padded_token[right_start:])


def _is_prioritised_exact_rule(rule: TranslationRule, token: str) -> bool:
    """
    Prioritise exact number, ordinal and bespoke-word rules. Exclude letter-name
    rules so isolated A and I use article and pronoun rules.
    """
    is_prioritised_rule = (
        _number_rules_start <= rule.source_index < _letter_names_start
        or rule.source_index >= _bespoke_words_start
    )
    return is_prioritised_rule and rule.match == token


def _ordered_candidates(token: str, position: int, padded_token: str):
    candidates = _rules_by_initial.get(padded_token[position], ())
    prioritised = [
        rule
        for rule in candidates
        if _is_prioritised_exact_rule(rule, token)
        and _rule_matches(rule, padded_token, position)
    ]
    if not prioritised:
        return candidates
    prioritised_indexes = {rule.source_index for rule in prioritised}
    return prioritised + [
        rule for rule in candidates if rule.source_index not in prioritised_indexes
    ]


def _validated_output(rule: TranslationRule) -> str:
    if rule.phoneme_output == "":
        return ""
    phonemes = rule.phoneme_output.split("-")
    unknown = [phoneme for phoneme in phonemes if phoneme not in phonemes_dictionary]
    if unknown:
        unknown_text = ", ".join(unknown)
        raise ValueError(f"Rule {rule.source_text!r} contains unknown phonemes: {unknown_text}")
    return "-".join(phonemes)


def _translate_token(token: str, explain: bool, step_start: int):
    uppercase_token = token.upper()
    padded_token = f" {uppercase_token} "
    position = 1
    output_parts = []
    step = step_start

    while position <= len(uppercase_token):
        character = padded_token[position]

        matching_rule = None
        for rule in _ordered_candidates(uppercase_token, position, padded_token):
            if _rule_matches(rule, padded_token, position):
                matching_rule = rule
                break

        if matching_rule is None:
            if character.isdigit():
                output_parts.append(_digit_outputs[character])
                if explain:
                    step += 1
                    print(
                        f"step {step}: {uppercase_token}[{position - 1}] "
                        f"digit fallback {character} -> {_digit_outputs[character]}"
                    )
                position += 1
                continue
            raise ValueError(
                f"No pronunciation rule matched {character!r} at position "
                f"{position - 1} of {token!r}"
            )

        phoneme_output = _validated_output(matching_rule)
        if phoneme_output:
            output_parts.append(phoneme_output)
        if explain:
            step += 1
            consumed = matching_rule.match
            displayed_output = phoneme_output or "silent"
            print(
                f"step {step}: {uppercase_token}[{position - 1}] "
                f"consume {consumed!r} with {matching_rule.source_text!r} "
                f"-> {displayed_output}"
            )
        position += len(matching_rule.match)

    return "-".join(output_parts), step


def text_to_phonemes(text: str, explain: bool = False) -> str:
    """
    Translate text with ordered left-to-right rules. At each position, append
    the output of the first matching rule and advance past its match without
    rewriting input. Output space runs encode pause length.
    """
    cleaned_text = _normalise_translation_input(text)
    output_parts = []
    step = 0

    if explain:
        print("\ntranslation printout:")
        print(f"text: {cleaned_text}")

    token_pattern = re.compile(r"[A-Za-z0-9']+|\s+|[-]+|[.,;:!?\"()]")
    for match in token_pattern.finditer(cleaned_text):
        token = match.group(0)
        if token.isspace():
            output_parts.append(" ")
            continue
        if token[0] in _pause_widths:
            output_parts.append(" " * _pause_widths[token[0]])
            if explain:
                step += 1
                print(
                    f"step {step}: punctuation {token[0]!r} -> "
                    f"{_pause_widths[token[0]]} pause unit(s)"
                )
            continue

        phonemes, step = _translate_token(token, explain=explain, step_start=step)
        output_parts.append(phonemes)

    result = "".join(output_parts).lstrip()
    if explain:
        print(f"result: {result}\n")
    return result
