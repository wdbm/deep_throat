"""
Store each phoneme as 575 immutable bytes of packed one-bit speaker states.
"""

from __future__ import annotations


__all__ = [
    "PHONEME_BYTES",
    "PHONEME_DATA",
    "PHONEME_NAMES",
    "phonemes_dictionary",
]

PHONEME_BYTES = 575
PHONEME_NAMES = tuple("UAIBDGJPTKWYRLMNSVFHZ") + (
    "AW", "AH", "UH", "AE", "OH", "EH", "OO", "IH", "EE", "WH", "CH", "SH", "TZ", "TH", "ZH",
)

PHONEME_DATA: dict[str, bytes] = {
    "U": bytes.fromhex(
        """
            3f ff ff f0 fc fe fc 00 00 00 7f ff ff 80 00 01
            ff fc 00 00 7f ff ff fc 00 01 ff ff 00 00 00 1c
            1f ff ff f1 fc ff 80 00 00 00 3f ff ff f0 fc ff
            7c 00 00 00 3f ff ff 84 00 01 ff 00 00 00 7f ff
            ff fc 00 1f ff f0 00 00 00 03 83 ff ff ff ff 1f
            e0 00 00 00 07 ff ff ff 3f 9f 00 00 00 00 0f ff
            ff c0 c0 00 ff fe 00 00 47 ff ff fe 00 03 ff ff
            00 00 00 07 0f ff ff ff ff 3f c0 00 00 00 1f ff
            ff fc 3f 3f 06 00 00 00 1f ff ff 07 00 07 ff f0
            00 00 0f ff ff f0 00 0f ff fc 00 00 00 0f 9f ff
            ff ff ff 7f 80 00 00 00 3f ff ff fc 7f ff 00 00
            00 00 3f ff fc 30 00 ff ff c0 00 00 7f ff ff e0
            00 1f ff e0 00 00 00 0f 1f ff ff ff fe 7f 80 00
            00 00 7f ff ff f8 ff 3f 00 00 00 00 3f ff ff fe
            03 f0 f8 00 00 0f ff ff ff e1 c0 7f fe 00 00 00
            00 0f 0f ff ff ff fc 3f 80 00 00 00 1f ff ff fc
            fe 1c 00 00 00 00 3f ff fe 3c 00 7f ff c0 00 00
            7f ff ff e0 00 0f ff c0 00 00 00 3c 7f ff ff ff
            f8 ff 00 00 00 00 ff ff ff e1 fc fc 00 00 00 00
            ff ff ff e0 03 e7 ff 00 00 01 ff ff ff 00 00 ff
            ff 00 00 00 00 f1 ff ff ff ff c7 f8 00 00 00 03
            ff ff ff 87 e3 e0 00 00 00 03 ff ff ff e0 3e 3f
            80 00 00 ff ff ff fc 00 07 ff e0 00 00 00 03 c3
            ff ff ff ff 0f e0 00 00 00 07 ff ff ff 1f 87 80
            00 00 00 0f ff ff ff c0 78 3f 00 00 00 ff ff ff
            fc f0 1f f3 c0 00 00 00 07 07 ff ff ff ff 1f c0
            00 00 00 0f ff ff fe 3f 0e 00 00 00 00 0f ff ff
            ff c0 f0 7e 00 00 01 ff ff ff ff e0 1f cf 80 00
            00 00 07 0f ff ff ff fe 3f c0 00 00 00 1f ff ff
            fc 7e 1e 00 00 00 00 1f ff ff ff 01 e0 fc 00 00
            03 ff ff ff ff e0 7f ff 80 00 00 00 70 ff ff ff
            ff e1 fe 00 00 00 00 ff ff ff c3 f0 f0 00 00 00
            00 ff ff ff f8 0f 0f f0 00 00 0f ff ff ff fe 00
            ff fc 00 00 00 01 c1 ff ff ff ff 87 f8 00 00 00
            03 ff ff ff 0f e3 c0 00 00 00 03 ff ff f0 40 00
            7f fe 00 00 01 ff ff ff 00 03 ff ff 80 00 00
        """
    ),
    "A": bytes.fromhex(
        """
            f0 00 fc 03 ff 83 ff f8 00 7e 00 1f c0 07 ff 80
            1f e0 07 f0 01 ff 03 ff ff 7f ff 03 ff e0 c0 3f
            00 0f e0 3f f8 3f ff 80 01 f8 00 fe 03 ff c3 ff
            f8 00 3f 00 0f c0 03 f8 77 e7 f0 01 f8 00 ff 00
            ff ff 67 ff 80 ff fc 7c 07 e0 01 fc 07 ff 07 f3
            f8 00 3f 00 1f 80 7f f8 7e ff 00 07 c0 01 f8 00
            ff 0f f0 ff 00 3f 00 3f c0 3f ff cf ff e0 1f ff
            3f 80 fc 00 3f 80 ff e0 fe 7f 00 07 e0 01 f8 0f
            ff 07 ef f3 00 fc 00 3f 00 0f e0 7f 8f e0 03 f0
            01 fc 03 ff ff cf fe 00 ff e3 ff 00 fc 00 7f 00
            ff c0 fc 7f 00 0f c0 03 f0 1f fe 1f 8f fe 01 f8
            00 7e 00 3f c0 7f 1f 00 03 c0 03 f8 0f ff f0 ff
            fc 01 ff ff ff 00 f8 00 7f 00 ff c1 fc 7f 00 0f
            c0 03 f0 1f fe 1f 0f e6 00 f8 00 7f 00 1f ff 8c
            0f e0 07 f0 03 fc 07 ff e0 0f fc 00 ff 01 ff 80
            7e 00 1f 80 ff e0 fe 3f 00 07 e0 01 f8 0f ff 0f
            c7 fb 00 fc 00 1f 00 0f f0 7f 8f c0 01 e0 01 fe
            03 ff fe ff ff 00 ff e7 ff e0 1f 80 07 f0 1f fc
            1f c7 e0 00 fc 00 3f 00 ff e1 f0 fe 00 0f 80 03
            f0 01 fc 0f e0 3e 00 7f 00 7f c0 7f ff f7 ff c0
            1f fc 7f f0 0f c0 03 f8 0f fe 0f c7 f0 00 7e 00
            3f 00 ff f0 fc ff 00 0f 80 03 f0 01 fe 1f c0 fe
            00 3f 00 3f c0 7f ff cf ff e0 07 fe 3f fc 07 e0
            01 fc 07 ff 07 f1 f8 00 3f 00 1f 80 7f f8 7e 7f
            00 07 c0 01 f8 00 ff cc 03 f8 00 fe 00 ff 80 7f
            ff 01 ff 00 3f f3 ff f0 0f c0 07 f0 0f fc 0f e3
            f0 00 7e 00 3f 00 ff f0 fc ff 00 0f 80 03 f0 01
            fc 1f e0 38 00 1e 00 3f f0 ff ff fd 9f c0 07 f1
            ff fc 01 f8 00 fe 01 ff 81 fd fe 00 1f 80 07 e0
            1f fc 3f 3f c0 01 e0 00 7e 00 3f 09 f8 1f c0 07
            c0 0f fc 1f ff f1 ff fc 01 ff ff f8 07 e0 03 f8
            07 fe 07 f1 f8 00 3f 00 3f 80 ff f8 7f ff 00 07
            c0 01 f8 00 fe 1f c0 7c 00 0f 00 1f c0 ff ff e1
            ff e0 0f fb ff f8 07 e0 01 fc 07 ff 07 f3 f8 00
            7e 00 1f 80 ff f0 fc 7f 00 07 80 01 f8 00 ff 03
            e0 08 00 07 00 1f f8 3f ff e7 ff e0 0f ff ff
        """
    ),
    "I": bytes.fromhex(
        """
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
        """
    ),
    "B": bytes.fromhex(
        """
            00 00 00 00 00 00 00 00 00 00 00 00 03 ff ff 98
            38 00 ff 00 00 00 00 00 f8 38 00 00 7f ff ff ff
            e0 0f ff 0f 80 00 00 0f ff ff 00 07 ff ff ff ff
            1f ff ff 00 00 00 00 ff ff e7 ff ff ff 00 00 00
            00 7f ff ff ff ff fe 00 00 00 03 ff ff ff ff ff
            ff 00 00 00 ff 00 00 00 3f ff ff c0 f8 0f 1f 00
            00 03 ff ff fe 00 00 0c 00 00 00 07 ff ff ff e0
            07 8f ff f0 ff ff ff f0 00 00 0f ff ff e0 f8 0f
            00 00 00 01 ff ff ff 00 00 00 00 00 00 0f ff ff
            f0 00 00 10 3f ff ff ff ff c0 00 00 01 ff ff ff
            0f 80 60 00 00 00 ff ff ff c0 00 00 00 00 01 ff
            ff ff 00 00 00 1f 3f ff ff ff ff e0 00 00 00 03
            ff ff ff 03 80 00 00 00 01 ff ff ff 00 00 00 3e
            7f ff ff ff f8 00 00 07 ff ff ff 80 7f ff f8 00
            00 00 00 07 ff ff fe 07 00 20 1c 00 00 ff ff ff
            00 00 00 7f ff ff ff ff ff 00 00 01 ff ff ff 80
            00 0f 9f ff ff ff c0 00 01 e1 ff ff 03 80 38 0f
            00 00 3f ff ff e0 00 00 0f df ff f3 ff ff c0 00
            00 01 ff ff ff 00 00 0f ff ff ff ff f0 00 00 3c
            3f ff f0 78 03 00 e0 00 03 ff ff fc 00 00 01 ff
            ff ff bf ff f8 00 00 01 ff ff e7 80 10 70 00 00
            7f ff ff f8 00 00 00 07 c7 ff ff 0f 80 00 07 03
            c7 ff ff ff 80 00 00 3f ff ff f9 fc 0e 00 00 00
            0f ff ff e0 00 00 00 7f ff ff 9f 00 00 03 ff ff
            ff f0 0c 01 f0 ff ff 83 e0 3c 07 80 00 3f ff ff
            f8 00 00 0f c7 f0 fc 7f ff e0 00 00 01 ff ff e0
            c0 01 00 00 00 03 ff ff ff 00 00 00 1f f3 ff ff
            ff e0 00 00 0f ff 80 00 00 0f ff fc 18 00 40 3f
            00 00 07 ff ff e0 00 00 3f ff fc 00 ff ff e0 00
            00 3f ff ff 00 00 1f 9c 20 00 08 ff ff 00 00 00
            00 03 80 ff ff ff 00 00 00 00 ff 8c 20 00 00 00
            00 18 66 00 00 01 ff ff 80 00 00 0f ff fe f8 00
            60 00 00 03 ff ff e0 00 00 03 ff e0 04 06 80 00
            00 00 71 ff 00 00 00 00 00 00 00 0c 38 00 00 00
            10 30 01 00 0e 0c 10 40 63 04 00 00 00 0e 00 00
            00 00 21 e0 00 00 00 30 06 00 62 00 00 00 00
        """
    ),
    "D": bytes.fromhex(
        """
            c1 e0 fc f3 9f cf 19 c7 e1 9c 39 8e 38 1c e7 3f
            63 b8 71 e1 e1 c0 7e 1c 47 01 c7 70 1e 1b c3 c0
            38 1f 18 e0 f1 f0 fc 00 e0 e0 78 3c e3 1e 3c c0
            e1 c4 e3 98 78 e1 fc 78 0f c7 1c 71 c6 38 e7 87
            3c 38 e3 f8 1f 01 f0 7c 1f 1c f0 0f 87 00 e0 00
            1c 07 03 f0 7f 1f e3 f3 c7 18 f8 03 20 1c 1f 00
            70 83 c3 80 fc 47 ff cf fd ff fc 77 e0 00 00 0f
            00 40 78 1f 81 ff fc 7f 8f ff e0 1e 04 00 00 3f
            00 01 01 fc 01 ff e3 f0 7f ff c7 ff ff ff 8f f0
            00 01 e0 0e 01 ff fc 7f ff cf e0 3e 00 00 00 3c
            3e 0f ff fe 7e 00 00 00 08 07 ff ff ff ff ff ff
            f0 00 00 00 01 f0 0f 80 ff ff ff ff 83 e0 00 00
            00 7e ff ff ff f8 04 00 00 00 03 ff ff ff ff fc
            00 00 03 ff ff ff e0 03 e0 1f 00 3f ff ff fe 0f
            e0 00 00 3f e0 ff ff ff c0 00 00 00 01 ff ff ff
            ff ff 80 0e 00 1f ff ff ff 80 00 e0 07 e0 1f ff
            ff f0 01 e0 00 00 1f ff ff ff ff 80 00 00 01 e0
            7f ff ff 80 3c 00 00 0f ff ff ff ff f8 00 00 00
            7f c0 ff ff f8 00 00 00 00 00 ff ff ff 80 70 00
            00 00 ff ff ff ff f0 00 00 03 ff ff ff ff ff ff
            e0 00 00 00 1f fe 1f ff fe 00 00 00 01 fe 1f ff
            ff 80 00 00 00 00 3f ff ff e0 00 00 00 00 ff ff
            ff fc 3f f0 07 81 fe 00 08 03 ff 81 ff 7f fc 00
            00 1f ff 01 ff ff fc 00 00 00 00 03 ff ff f8 00
            00 00 00 3f ff ff f0 1e 00 3f 07 ff ff c0 00 00
            7f f0 3f 8f ff e0 00 00 c1 f0 1f ff ff c0 00 00
            00 00 73 ff ff c0 00 00 00 00 3f ff ff fc 00 38
            00 00 7f ff ff 80 00 00 ff f0 7f 8f ff 00 00 01
            e0 f8 ff ff ff 00 00 00 00 03 ff ff ff f0 00 00
            00 00 01 ff ff f0 00 00 00 00 1f ff ff ff f0 00
            00 0f ff 1f f1 ff f0 00 00 00 7f ff ff ff e0 00
            00 01 00 ff ff ff ff 80 00 00 00 30 1f ff ff c0
            00 00 0e 00 7f ff ff ef bf fc 00 00 1f ff 1f e0
            ff fc 00 00 03 ff ff ff ff e0 00 00 03 c7 ff ff
            ff ff c0 00 00 0f ff ff ff ff f0 00 00 1f ff ff
            f3 ff fc 00 00 ff ff f0 00 03 cf f0 7f 07 ff
        """
    ),
    "G": bytes.fromhex(
        """
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 7f f0
            00 ff c0 00 0f f8 00 ff f8 0f ff 00 3f fe 1e 07
            ef c0 f0 fc 18 00 ff e0 0f fc 00 1f e0 07 e1 0f
            fc 60 07 83 f0 00 7f 01 37 ee 70 7c 00 0f ff e1
            e0 3f ff 02 1f e0 01 fc 0e 02 00 ff f8 0f ff 01
            f0 00 7e 40 7f c0 1f f8 01 ff c0 ef f8 38 7f fe
            0f 00 c0 e0 3e 3f 1f ff 07 f0 00 3f f0 07 ff 0f
            fc ff ff 03 00 00 01 e0 3f fc 03 ff 00 1f e0 00
            fc 00 1f 86 01 f9 c0 08 07 0f c1 e3 ff f8 ff f0
            03 c0 80 00 00 06 00 00 0f 00 03 fc 3f ff ff ff
            81 fe 18 00 80 00 00 00 03 00 03 7c 7f ff ff f8
            ff ff 9f 3f ff f0 08 07 80 00 7c 00 07 e0 ff ff
            ff ff ff f8 00 0f 00 00 00 00 00 01 ff ff ff ff
            ff ff ff f2 00 00 01 c0 00 0f 00 f7 ff ff ff ff
            ff c0 7c 00 00 00 00 70 07 ff ff ff ff ff ff ff
            81 ff fe 00 00 0f 00 00 7e 07 ff ff ff f8 7f 80
            00 c0 00 00 01 ff e0 ff ff ff f0 3f c0 3f ff ff
            ff ff 00 00 78 00 01 f0 7f ff ff ff c3 f8 00 00
            00 00 00 3f ff ff ff ff c0 00 00 00 ff ff ff ff
            ff 80 00 70 00 00 f1 ff ff ff ff 81 e0 00 00 00
            1f 81 ff ff ff e0 00 00 00 00 1f ff ff ff ff ff
            00 00 03 00 00 3f ff ff ff ff e0 00 00 00 00 1f
            ff ff ff ff e0 00 00 00 00 3f ff ff ff ff fc 00
            00 00 00 e0 0f 3f ff ff ff fe 00 00 00 00 00 ff
            ff ff fe 0f 00 00 00 00 1f ff ff ff ff 80 00 00
            e0 00 00 00 3e 01 ff ff ff f8 3f 80 60 00 03 f8
            1f fd ff ff 00 80 00 00 00 00 7f ff ff ff ff c0
            00 1f ff ff ff 00 07 00 00 00 3f ff ff f0 1f 00
            00 00 03 fe 3f ff ff f0 00 00 00 00 7f ff ff ff
            c0 80 00 01 ff ff ff ff ff 00 06 00 00 00 ff ff
            ff e0 3e 00 00 00 3f fe 7f ff ff 80 00 00 00 00
            ff ff ff e0 00 00 00 00 ff ff ff ff ff c7 fe 00
            01 80 1f f0 7f ff ff f0 0e 00 00 00 ff ff bf e1
            ff 80 00 00 01 f0 7f ff ff c0 00 00 00 00 0f ff
            ff 87 cf 98 0c 00 ff fb ff ff 00 e0 00 78 07 e7
            fc fe 07 80 00 00 0f 0f ff fc 3f f0 01 80 00
        """
    ),
    "J": bytes.fromhex(
        """
            1f c0 3f 03 fc 03 f0 1f 07 c0 ff 83 fc 0f f8 3f
            c0 7f 03 c0 f0 0f f0 7f 83 1f 01 f0 07 c1 9f 80
            f8 73 c0 3f c3 e2 0f f8 3f 83 c7 1c 70 f8 f0 f8
            e0 fe 0f 00 ff 07 c3 c7 00 ef 0f 1f 0e 3e 11 e1
            fe 0f 0e 3f c1 f0 f8 07 81 f0 63 f0 3f 1e 0f f0
            ff 0f 1e 03 e0 3f 01 e0 7c 03 f0 1f 00 1f 07 f0
            3c 3e 07 f8 3f e1 f0 1c 63 f8 0f e0 1f 07 01 e1
            e1 f8 1f 80 7f c0 fc 1f 0f 03 f8 40 ff e0 7c 1f
            03 c1 e3 70 43 8f 0f f8 3f 80 f7 81 f0 3f 0f 00
            c7 c0 fe 04 78 78 0f c0 1f 03 f8 78 f0 f8 3e 1c
            3f 83 e0 c7 07 87 81 f8 3f 87 01 c3 c0 ff 03 de
            00 fc 0f 1c 3e 1e 0f 0f 80 fc 00 f1 c3 c3 cf 07
            86 0f 80 fe 10 3c 78 71 e0 0f 9c 07 f0 7c 07 81
            e1 f0 fc 3e 03 f0 fc f8 f8 1f f0 3c 06 7c 07 80
            00 00 f8 3f 00 ff 81 ff 8f 00 f8 1c 00 07 02 01
            fc 81 ff fc 3f fc ff e7 f9 c7 c3 80 80 78 00 c0
            00 01 ff 87 f0 ff 3f 1f ff 00 fc 00 00 00 00 00
            00 fc 3f ff ff ff ff ff ff ff e0 00 01 c0 00 08
            00 c3 f8 3f 9f ff ff ff 3c 00 e0 00 00 00 00 00
            0f ff ff ff ff ff ff ff fe fc 00 01 e0 00 0f 00
            1f ff ff ff ff fc 1f e0 00 00 00 00 c0 03 ff ff
            ff ff ff ff ff fe 1f fe 00 00 0f 00 00 7f 00 7f
            ff ff ff ff e0 07 c0 00 00 00 0f e0 ff ff ff ff
            ff f8 ff ff ff ff ff 00 00 3e 00 01 f8 01 ff ff
            ff ff ff 00 0f 00 00 00 00 ff ff ff ff ff c0 3e
            00 07 ff ff ff ff c0 00 0f 00 00 7e c0 3f ff ff
            ff ff e0 00 00 00 00 01 ff ff ff ff ff 80 00 00
            00 7f ff ff ff ff fc 00 0f 00 00 78 f8 7f ff ff
            fc ff e0 00 00 00 00 07 ff ff ff fe 00 00 00 00
            00 3f ff ff ff ff ff c0 00 0f 00 00 ff ff ff ff
            ff c0 00 00 00 00 00 7e 3f ff ff ff f8 00 00 00
            00 00 ff ff ff ff ff 80 00 c0 00 03 c0 00 7f ff
            ff c3 ff e0 00 00 00 00 1f ff ff ff ff f0 00 00
            00 00 7f c0 3f ff ff ff ff c0 00 ff ff ff 00 0f
            80 00 f8 7e 3f 07 ff c0 30 0e 00 00 3f fe 0f ff
            ff f0 00 1c 00 00 38 7c 1f ff 07 9f 00 f0 00
        """
    ),
    "P": bytes.fromhex(
        """
            01 83 f8 00 1f 7f cf 3f 80 c0 01 ff c0 00 78 03
            f8 38 c0 04 00 61 00 00 00 00 78 bf f8 8f 8f ff
            fe 7f ff fb ff fc 00 07 ff ff ff ff ff ff ff fe
            00 00 00 00 00 00 00 ff ff ff ff fe 00 e0 00 00
            07 ff ff ff fe 00 00 00 00 01 ff ff ff ff ff ff
            ff ff 00 00 00 00 00 00 00 f8 00 00 00 00 00 00
            3f ff ff ff ff ff ff ff ff ff ff ff ff 00 00 01
            ff ff 00 00 1e 00 00 00 00 00 1f ff 00 ff ff ff
            ff ff ff ff ff ff ff e0 00 3f 80 00 00 00 00 00
            00 00 1f ff fc 07 ff ff ff ff 00 00 03 fe 03 ff
            ff ff fc 03 f0 00 00 1f ff ff ff ff ff ff ff ff
            e0 00 00 00 00 00 00 00 00 00 00 01 ff ff ff ff
            c0 00 00 00 00 3f ff ff ff ff ff df ff ff c0 00
            00 0f ff e0 00 00 47 fc 3e 0e 00 00 00 63 ff fc
            00 00 78 3e 00 e1 c3 00 00 3c 03 ff f0 c0 03 ff
            ff fe 07 c0 1f ff 1f e0 1e 00 00 00 00 10 ff e0
            60 18 03 fc ff 00 00 00 00 00 00 0f 01 fc 00 1f
            01 fe 3f ff ff f8 0f 00 ff ff ff 81 e0 00 fe 08
            00 00 00 ff 9f c0 00 00 00 73 ff f8 e0 18 10 00
            3c 03 c7 cf f1 ff ff ff fc e0 3f ff ff ff ff c0
            00 00 00 00 00 00 03 c7 ff f0 00 00 1c 7f 7f c0
            c3 80 fc 00 7f f9 e2 01 f0 ff ff f1 fc 7f fc 3f
            ff e0 00 00 0f ff ff c0 80 00 00 00 fc 7f ff 00
            00 00 07 f3 fe 00 e7 ff ff ff ff f9 ff ff ff c0
            00 00 1f ff ff c0 00 00 00 00 7c ff ff f0 00 02
            03 e0 00 00 ff ff ff ff ff 80 07 0f ff ff c0 00
            00 1f ff ff e0 00 00 00 00 07 ff ff fc 00 00 71
            70 00 00 00 1f ff ff ff ff c7 fc 7f ff ff ff e0
            00 00 03 ff ff fe 00 00 00 00 00 ff ff ff c0 00
            00 00 f8 03 ff fe 00 00 00 ff ff ff ff ff ff fc
            3f 30 00 00 00 03 ff ff f0 00 00 00 00 01 ff ff
            fc 00 00 01 ff ff 07 ff ff e0 00 00 07 ff ff f0
            01 0f ff ff ff f3 c0 00 00 00 3f ff ff c0 00 00
            00 00 3f ff ff e0 00 00 03 ff ff ff ff f0 00 00
            00 1f ff ff ff f8 00 00 ff ff ff e0 00 00 00 00
            07 ff ff f0 00 00 03 00 01 ff ff f8 00 00 03
        """
    ),
    "T": bytes.fromhex(
        """
            1f 03 c1 e0 f8 07 c1 e0 f0 7c 1f 04 3f 1c e6 1c
            86 71 c1 f8 01 f8 87 1f 87 81 f0 f0 71 1f 8f 1e
            e3 e7 33 1c c7 3b 98 39 c9 9c 78 e7 39 c7 67 27
            c6 3a 39 99 b8 f0 78 f3 83 8e e7 71 cc 79 1f 1f
            1f 0f 03 89 e3 d8 f0 78 fc 0e 39 cc e0 ee 73 1c
            72 31 99 8f 1e 71 f0 78 78 cf 30 78 71 9c 3c ce
            7f 04 e0 f0 9e 0f 03 c3 e1 f8 8e 63 8e 1f 8e 39
            8e 0f 07 87 1c 0e 3f 07 0f c3 9f 1c 40 cc f2 38
            f6 3e 3e 07 30 f8 fe 7e 77 03 1e 03 c7 03 e0 71
            c7 8f 41 0f 07 e0 e1 9c 70 3c 1e 1e 43 e3 b8 dc
            78 67 03 0f 87 e0 f0 78 1c c7 1f 86 1f c7 e1 c0
            7c 1e 1e 33 81 c0 fe 66 71 9f 03 c1 f8 0f 07 00
            60 38 f0 3c c3 39 cf 87 c1 f0 0e 1e 38 f8 0f 00
            f8 f0 18 c7 98 3f 87 e1 c0 7f 0d c7 c1 c0 f0 fc
            7c 3f 01 f8 e1 e1 c0 f0 3e 0f 83 c0 e7 1f 83 f8
            f8 79 cf c1 f0 fc 00 18 00 38 00 00 00 00 00 f0
            7e 02 00 00 00 03 df ff ff ff ff ff ff ff ff 80
            00 00 00 00 38 70 00 00 00 00 00 03 ff ff ef e1
            00 00 00 00 00 00 30 06 3f fe fc 3f 1f 80 00 00
            00 00 00 00 03 fd ff ff ff f1 c0 00 00 00 00 00
            01 ff ff ff ff ff ff ff fe 00 20 00 00 00 00 01
            c0 00 00 00 00 00 00 00 00 00 00 00 01 ff ff ff
            ff ff ff ff 20 00 01 00 00 00 00 00 00 00 00 00
            00 00 03 ff ff ff ff ff ff ff f8 00 00 00 00 02
            7f ff ff ff ff f8 00 00 00 00 00 07 ff ff ff ff
            fc 00 38 ff ff f8 00 00 00 00 1f ff ff ff ff ff
            ff ff ff e0 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 0f ff ff ff ff ff ff ff ff ff ff ff ff
            ff fe 00 00 00 00 00 00 00 00 00 1f ff ff ff ff
            ff ff ff f8 70 00 00 00 00 03 c0 00 00 00 00 ff
            b8 01 7f f8 00 00 c0 fe 00 00 00 00 00 00 00 00
            00 ff ff ff ff ff ff ff ff ff f8 00 00 00 00 00
            00 00 00 40 ff 1f 7e 70 e0 3f e0 40 00 80 00 10
            00 ff ff ff ff ff ff df ff ff ff bf 0e 00 01 10
            00 01 e0 00 01 00 00 00 f0 00 03 c0 00 06 1c 80
            08 00 00 80 e0 70 00 8c 00 00 00 01 00 00 60
        """
    ),
    "K": bytes.fromhex(
        """
            00 00 00 00 00 00 00 00 00 00 00 00 01 40 00 00
            0c 00 00 00 20 00 00 00 01 00 00 02 00 00 00 00
            00 00 00 00 00 30 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
            00 00 00 00 00 00 00 00 00 00 40 c0 08 00 00 00
            00 00 04 01 00 00 00 00 08 02 04 01 00 00 00 00
            01 88 60 0f e3 83 f9 c3 f9 e0 0f fc 00 ff c0 07
            f8 06 3e 0f 03 f8 60 7e 00 e0 7e 78 07 f7 01 ff
            e0 03 ff 00 ff e0 01 fe 00 1f ff 00 ff c0 3f fc
            03 87 40 0f fe 00 ff 00 03 fb 00 ff 00 07 97 c0
            0f f0 0d ff 00 0f b8 01 fe 00 3f b8 03 3e c0 3f
            f8 06 7f 00 cf 80 03 fe 00 83 e0 00 7c 0f ff 01
            df c0 0f c7 e0 10 1e 07 87 c0 f1 f8 63 1c e0 00
            fc 00 1f 07 07 81 e7 e0 de 3c 0f 8f 01 fe 7c 3f
            bd 83 f1 c0 3d c4 78 3e 0e 7f 80 ff e0 03 dc 43
            07 fc 03 c0 70 f8 7e 1f 0f 07 c1 f0 78 3e 3f 07
            ef 81 c1 f0 f8 0f fc 07 fe 03 e0 00 38 1f 8f 87
            c0 f0 1f 07 c7 81 e0 fe 18 0f c0 07 ff 80 ff 80
            0f fe 07 cf c1 00 fc 04 0f 87 80 ff 78 1f fe 07
            7f 03 ef e0 00 ff 00 1f e0 1f 8f 0f 03 c1 e0 7c
            f8 38 7f 07 1f 8f 86 31 fe 00 0f f0 01 fc c0 1f
            cf 00 0f e0 30 7e 3c 1f fc 01 ff c0 3f f8 01 ff
            00 03 fc 00 07 c7 80 3f c0 f0 7c 00 1f e0 f0 70
            f8 3f 8c 07 83 e1 f0 fc 00 1f 80 07 c3 03 73 80
            76 78 3c 00 f0 38 38 1f 0e 1c f0 00 f0 c0 1c 38
            01 ce 38 ee 7f fc e0 7f 80 0f f0 00 ff ff ff ff
            00 7f ff fc 07 ff 1e 7f cf 9f 80 00 00 30 0e 00
            ff 80 ff f0 18 00 00 00 01 07 38 ff 00 3f f0 1b
            3f fe 00 00 00 00 1f ff fc 7f fe 07 ff c3 df f8
            1c 3f f8 00 ef 00 1f f7 0f ff 01 c0 fe c0 1f f8
            00 07 80 00 00 00 0f 00 00 ff fc ff ff ff ff f8
            1c 0f 03 8f c0 00 fe 3e 7f ff ff df ff ff f8 00
            7e 00 00 00 00 00 18 07 ff c0 e7 ff f0 3f f0 04
            1f c0 07 fe 00 10 fc 00 00 30 01 df 00 1f 01 ff
            ff c0 00 00 00 00 00 00 00 3f ff ff ff ff ff fc
            00 00 00 00 00 00 00 00 00 00 07 ff ff ff ff
        """
    ),
    "W": bytes.fromhex(
        """
            ff ff ff ff ff 9c 00 00 00 00 00 00 0f ff ff ff
            ff ff f0 00 00 00 00 00 00 00 00 00 00 0f ff ff
            ff ff ff ff ff ff ff ff e0 00 00 00 00 00 01 ff
            ff ff ff ff fc 00 00 00 00 00 00 00 00 00 00 0f
            ff ff ff ff ff fe ff ff ff ff fe 00 00 00 00 00
            00 ff ff ff ff ff 00 00 00 00 00 00 00 00 00 00
            1f ff ff ff ff fc 00 00 07 ff ff ff ff c0 00 00
            00 00 00 3f ff ff ff ff f0 00 00 00 00 00 00 00
            01 ff ff ff ff c0 00 00 00 01 ff ff ff ff ff f0
            00 00 00 00 00 1f ff ff ff ff f8 00 00 00 00 00
            1f ff ff ff ff ff e0 00 00 00 00 7f ff ff ff ff
            f8 00 00 00 00 00 00 00 1f ff ff ff fe 00 00 00
            00 3f ff ff ff ff ff ff f0 00 00 00 00 7f ff ff
            ff c0 00 00 01 ff ff f0 00 00 00 0f ff ff ff e0
            00 00 00 ff ff fe 00 00 0f ff ff f0 00 00 00 0f
            ff ff ff 00 00 00 0f ff ff ff ff c0 00 00 00 00
            00 7f ff ff fe 00 00 00 00 1f ff ff ff ff ff 00
            00 00 00 07 ff ff ff c0 00 00 00 1f ff ff ff ff
            ff fe 00 00 00 00 3f ff ff fc 00 00 00 00 3f ff
            ff ff ff ff 00 00 00 00 1f ff ff ff 00 00 00 00
            3f ff ff ff ff 00 00 00 3f ff ff 00 00 00 03 ff
            ff ff 80 00 00 07 80 f0 08 ff ff ff c0 00 00 00
            c7 ff ff c3 c0 00 00 40 00 00 3f ff ff fc 00 00
            00 7f ff ff ff ff 3f 00 00 00 0f ff ff fe 00 00
            00 0f 8f ff ff ff ff fc 00 00 00 3f ff ff f8 00
            00 00 00 00 33 ff ff ff 00 00 00 07 ff ff f8 00
            00 03 ff fe 0f ff ff ff e0 00 03 01 ff ff 9f 80
            00 0c 03 e0 01 ff ff ff 00 00 00 0f ff ff fe 00
            00 70 00 00 00 3f ff ff f0 00 00 07 ff ff c0 0c
            7f ff 00 00 00 1f ff ff c0 00 00 01 f8 30 00 0f
            ff f8 00 00 01 ff fe 00 00 0f ff f0 00 00 03 ff
            ff fe 00 00 03 ff e0 00 1f ff ff 00 00 00 7f ff
            fc 00 00 ff e0 00 00 00 ff ff c0 00 00 03 ff e0
            00 00 7f ff 00 00 00 3f fc 00 00 00 3f ff c0 00
            00 30 00 04 00 06 00 c7 80 00 00 00 00 f0 03 00
            c0 00 80 00 00 00 00 00 00 60 03 c7 fc 7f 00
        """
    ),
    "Y": bytes.fromhex(
        """
            fc 07 83 c0 7f f1 ff ff ff ff f0 fc 02 00 00 00
            00 00 00 00 3e 07 f7 ff ff f9 ff ff 87 f0 0c 00
            00 00 00 00 00 30 78 3f ff ff ff ff ff c3 f0 00
            00 00 00 00 00 00 01 f0 1f ef ff ff ff ff ff 7f
            c0 70 00 00 00 00 00 00 e1 f8 ff ff ff f8 7f 00
            c0 00 00 00 00 00 00 1f 01 fc ff 9f ff ff ff e1
            fe 00 f0 00 00 00 00 00 03 ff ff ff ff ff e0 fe
            03 c0 00 00 00 00 00 00 fc 03 f0 fc 3f ff ff ff
            c3 f8 01 f8 00 80 00 00 00 07 ff ff ff ff ef f0
            ff 00 00 00 00 00 00 00 00 1f 03 ff fe 1f ff ff
            ff e0 fc 03 e0 00 00 00 f0 1f f3 ff ff ff ff ff
            c0 fc 00 c0 00 00 00 1c 00 80 ff ff ff fc 3f ef
            ff ff 81 f0 01 00 00 00 00 f0 3f ff ff ff ff ff
            7f 01 f8 00 80 00 00 00 3c 00 03 ff ff ff fc 7f
            fc 3f fe 00 c0 00 00 00 00 0f f0 ff ff ff ff ff
            fc 00 0f 80 03 80 00 7c 01 ff ff ff ff ff ff c0
            ff c0 00 30 00 00 00 00 fc 00 ff f1 ff ff ff fe
            07 c0 00 0f 00 03 80 00 fc 07 ff ff ff ff fc 1f
            c0 00 00 00 1c 00 80 3f f0 7f fe 1f fc 1f ff 03
            ff 0f c0 00 1f 00 0f 00 01 fc 1f ff ff ff ff f8
            0f 80 00 00 00 3f 03 ff ff e0 ff 00 1f c0 07 f8
            1f ff ff ff ff e0 03 e0 00 78 00 3f 83 ff ff ff
            df ff 00 38 00 00 00 03 fc ff ff ff f0 01 c0 00
            00 00 3f ff ff ff ff ff fe 00 00 78 00 1f 00 1f
            ff ff ff ff c0 00 00 00 00 03 ff ff ff ff f8 00
            00 00 00 00 7f 03 ff e7 ff f0 7f 00 7f 00 ff ff
            ff 00 fc 00 1e 01 0f f0 ff f0 3f e0 20 00 03 e0
            03 ff ff ff c3 f8 00 00 00 00 00 ff ff ff ff f8
            00 00 00 7e 01 ff ff ff e1 ff 00 3c 03 ff fe 01
            f8 00 78 1f ff c0 ff 01 ff 00 fc 1e 0f e0 ff de
            ff 83 80 00 0e 00 03 f0 ff ff ff c0 00 00 00 10
            0f f0 f8 fe 07 f0 00 00 18 78 79 fe 0c 3f 06 00
            01 f0 f0 7f ff e1 81 e1 e0 00 07 ff f8 00 00 00
            c0 03 ff f0 fc 3f 1e 00 00 1c 1f 0f ff fe 3c ff
            f8 07 0f ff f0 00 00 01 f0 fe 3f 87 f3 ff fc 00
            00 1f ff 00 01 ff ff c0 00 01 f0 00 07 ff fe
        """
    ),
    "R": bytes.fromhex(
        """
            00 0f ff ff ff ff 00 00 00 3f ff f0 00 1f ff e0
            00 00 03 e1 ff ff 1f ff ff f8 00 00 3f ff 00 07
            ff ff 00 00 03 c0 00 1f ff ff 00 3f ff ff ff f8
            00 00 00 ff ff c0 00 ff ff 80 00 00 1f 87 f3 fc
            7f ff ff c0 00 00 3f fc 00 0f ff fe 00 00 07 80
            00 3f ff fe 00 7f ff ff ff f0 00 00 03 ff ff 00
            01 ff fe 00 00 00 7e 1f cf f1 fc ff ff 80 00 01
            ff f0 00 7f ff fc 00 00 7e 00 01 ff ff f8 00 ff
            ff ff ff e0 00 00 07 ff fe 00 07 ff fc 00 00 00
            f8 7f ff e7 f3 ff fe 00 00 01 ff c0 00 ff ff f0
            00 00 68 00 01 ff ff f8 03 ff ff ff ff e0 00 00
            0f ff fc 00 0f ff f8 00 00 00 f0 ff ff cf ff ff
            fc 00 00 03 ff e0 00 ff ff f0 00 00 f0 00 07 ff
            ff fc 07 ff ff e7 ff e0 00 00 07 ff fc 00 07 ff
            f8 00 00 00 f8 ff ff ff ff ff fe 00 00 01 ff c0
            00 ff ff f0 00 00 30 00 01 ff ff f8 01 ff ff bf
            ff e0 00 00 07 ff fc 00 07 ff fc 00 00 00 f8 7f
            ff c7 fb ff fe 00 00 01 ff c0 00 ff ff e0 00 00
            f8 00 03 ff ff c0 07 ff ff ff ff 00 00 00 3f ff
            f0 00 3f ff e0 00 00 03 e1 fe ff 1f ff ff f8 00
            00 1f fe 00 07 ff ff 00 00 03 c0 00 0f ff ff 80
            1f ff ff ff fe 00 00 00 7f ff c0 00 7f ff c0 00
            00 0f 83 f1 fe 3f 9f ff e0 00 00 ff fc 00 0f ff
            fe 00 00 0f 80 00 3f ff fe 00 3f ff ff ff fe 00
            00 00 7f ff c0 00 7f ff c0 00 00 0f 87 fb fe 7f
            ff ff e0 00 00 ff fc 00 0f ff ff 00 00 0f 00 00
            3f ff fc 00 0f ff ff ff fc 00 00 00 ff ff c0 00
            ff ff 80 00 00 1f 0f f7 fc 7f ff ff c0 00 00 ff
            f8 00 1f ff fc 00 00 1f 00 00 ff ff fc 00 ff ff
            ff ff f8 00 00 01 ff ff 00 01 ff ff 00 00 00 3f
            1f ef f8 ff ff ff 80 00 01 ff f8 00 07 ff ff 80
            00 00 0e 00 6f ff ff 80 00 ff ff ff f0 00 00 01
            ff ff 00 01 ff ff 00 00 00 7f 1f cf f1 ff ff ff
            00 00 00 ff f0 00 7f ff f0 00 00 3c 00 01 ff fe
            f0 00 00 00 f0 ff ff ff ff 06 00 00 00 1c 1f ff
            ff ff fc 00 00 00 00 02 07 ef ff ff ff ff f0
        """
    ),
    "L": bytes.fromhex(
        """
            00 00 00 00 03 8f ff ff ff ff e0 00 00 01 e1 ff
            ff ff fc 00 00 00 00 38 3f ff ff ff fc 00 00 00
            00 00 1f 9f ff ff ff ff c0 00 00 00 00 07 1f ff
            ff ff fc 80 00 00 03 83 ff ff ff f8 00 00 00 00
            70 7f ff ff ff f8 00 00 00 00 00 1f bf ff ff ff
            ff c0 00 00 00 00 00 ff ff ff ff ff 00 00 00 07
            9f ff ff ff f8 18 00 00 00 70 7f ff ff ff f0 00
            00 00 00 08 1f bf ff ff ff ff 80 00 00 00 00 00
            7f ff ff ff ff 00 00 00 03 07 ff ff ff fc 1c 00
            00 00 38 7f ff ff ff f8 00 00 00 00 08 1f cf ff
            ff ff ff c0 00 00 00 00 03 cf ff ff ff fe 00 00
            00 03 c1 ff ff ff fe 00 00 00 00 38 3f ff ff ff
            f8 00 00 00 00 04 0f df ff ff ff ff e0 00 00 00
            00 07 8f ff ff ff fe 00 00 00 01 c3 ff ff ff ff
            00 00 00 00 0e 1f ff ff ff fe 00 00 00 00 03 07
            ff ff ff ff f9 e0 00 00 00 00 00 3f ff ff ff fe
            00 00 00 00 ff ff ff ff ff 80 00 00 00 07 07 ff
            ff ff ff 00 00 00 00 01 83 ff ff ff ff ff f8 00
            00 00 00 00 3f ff ff ff ff 00 00 00 00 7d ff ff
            ff ff e0 00 00 00 01 c1 ff ff ff ff c0 00 00 00
            00 38 ff ff ff ff ff be 00 00 00 00 00 0f ff ff
            ff ff 80 00 00 00 0f ff ff ff ff f8 00 00 00 00
            38 7f ff ff ff f8 00 00 00 00 0e 1f ff ff ff ff
            ef 80 00 00 00 00 00 ff ff ff ff f0 00 00 00 03
            ff ff ff ff fe 00 00 00 00 07 1f ff ff ff fe 00
            00 00 00 01 87 ff ff ff ff fb e0 00 00 00 00 01
            ef ff ff ff fc 00 00 00 00 f1 ff ff ff ff 00 00
            00 00 07 0f ff ff ff ff 00 00 00 00 01 83 ff ff
            ff ff fc f0 00 00 00 00 01 ff ff ff ff ff 00 00
            00 00 fd ff ff ff fe 00 00 00 00 0c 1f ff ff ff
            ff 00 00 00 00 03 07 ff ff ff ff ff e0 00 00 00
            00 01 f7 ff ff ff ff 00 00 00 00 f0 ff ff ff fc
            00 00 00 00 38 3f ff ff ff fc 00 00 00 00 04 0f
            df ff ff ff ff c0 00 00 00 00 01 f3 ff ff ff ff
            ff ff ff ff ff ff ff ff ff f8 00 f8 0c 00 00 00
            3e 07 81 ff ff ff ff ff f0 1f ff 07 80 20 00
        """
    ),
    "M": bytes.fromhex(
        """
            00 00 00 0c 00 00 78 00 0c 0f ff ff ff ff ff ff
            ff ff ff ff f0 01 f0 18 00 00 00 7e 07 81 ff ff
            ff ff ff f0 3f ff 0f 80 00 00 00 00 00 00 00 06
            00 03 06 0f ff ff ff ff ff ff ff ff ff ff f0 01
            f0 18 00 00 00 7c 07 83 ff ff ff ff ff f0 3f fe
            0f 00 00 00 00 00 00 00 00 00 3c 00 00 0f ff ff
            ff ff ff ff ff ff ff ff c0 03 e0 60 00 00 00 f8
            1e 0f ff ff ff ff ff c0 ff fc 3e 00 00 00 20 00
            00 00 1c 3e 00 0e 00 7f ff ff ff ff ff ff ff ff
            ff ff 00 3f 03 00 00 00 0f 80 e0 ff ff ff ff ff
            fe 0f ff c3 e0 10 00 00 00 00 00 00 01 e0 00 00
            01 ff ff ff ff ff ff ff ff ff ff f8 01 f0 38 00
            00 00 7c 0f 03 ff ff ff ff ff f0 7f fe 0f 00 40
            00 00 00 00 00 00 1f f8 00 00 0f ff ff ff ff ff
            ff ff ff ff ff 80 1f 01 80 00 00 07 c0 f0 3f ff
            ff ff ff ff 03 ff e1 f0 00 00 00 80 00 00 00 c0
            f0 00 00 00 ff ff ff ff ff ff ff ff ff ff fc 00
            f8 0c 00 00 00 3e 07 81 ff ff ff ff ff f8 1f ff
            0f 80 00 00 00 00 00 00 00 0f fc 10 00 01 ff ff
            ff ff ff ff ff ff ff ff 80 1f 01 80 00 00 07 c0
            f0 3f ff ff ff ff ff 07 ff e1 f0 00 00 01 80 00
            00 00 01 00 00 00 00 3f ff ff ff ff ff ff ff ff
            ff fc 00 f8 1c 00 00 00 3e 07 81 ff ff ff ff ff
            f0 3b ff 0f 00 00 00 00 00 00 00 00 00 00 03 00
            07 ff ff ff ff ff ff ff ff ff ff c0 07 c0 c0 00
            00 01 f0 3c 1f ff ff ff ff ff 81 ff f8 fc 02 00
            00 c0 00 00 00 00 00 00 00 00 3f ff ff ff ff ff
            ff ff ff ff ff 00 3e 07 00 00 00 0f 81 e0 ff ff
            ff ff ff fe 0f ff c3 c0 00 00 00 00 00 00 00 00
            18 08 00 0f ff ff ff ff ff ff ff ff ff ff f8 01
            f0 18 00 00 00 7c 0f 03 ff ff ff ff ff f0 7f fe
            1f 00 80 00 10 00 00 00 00 7f c0 00 00 0f ff ff
            ff ff ff ff ff ff ff ff 00 7e 02 00 00 00 1f 81
            e0 ff ff ff ff ff fe 0f ff c3 c0 00 00 02 00 01
            ff ff 00 00 18 78 00 00 0e 00 00 01 ff f1 e0 ff
            ff ff ff ff ff ff ff ff ff 00 1f 80 00 00 00
        """
    ),
    "N": bytes.fromhex(
        """
            00 00 0f ff ff ff ff ff f8 0f ff fc 00 00 03 00
            00 00 1c 00 00 0f ff e7 07 ff ff ef ff ff ff ff
            ff ff f8 00 fe 00 00 00 00 00 00 3f ff ff ff ff
            ff e0 3f ff e0 00 00 06 00 00 00 e0 00 00 3f ff
            1c 3f ff ff ff ff ff ff ff ff ff e0 03 f8 00 00
            00 00 00 00 ff ff ff ff ff ff 00 ff ff 80 00 00
            38 00 00 07 80 00 00 ff fe 38 3f ff ff ff ff ff
            ff ff ff ff 80 0f c0 00 00 00 00 00 07 ff ff ff
            ff ff fc 07 ff fe 00 00 01 f0 00 00 00 00 00 03
            ff e0 40 ff ff ff ff ff ff ff ff ff ff 00 3f 00
            00 00 00 00 00 0f ff ff ff ff ff f0 0f ff fc 00
            00 01 00 00 00 00 00 00 0f ff e1 41 ff ff ff ff
            ff ff ff ff ff f8 00 fc 00 00 00 00 00 00 7f ff
            ff ff ff ff c0 7f ff e0 00 00 1e 00 00 00 00 1c
            00 1f ff 1f 1f ff ff ff ff ff ff ff ff ff 80 1f
            80 00 00 00 00 00 0f ff ff ff ff ff f8 07 f9 fe
            00 00 03 e0 00 00 0f 00 00 07 ff f9 f0 ff ff ff
            ff ff ff ff ff ff f8 00 fe 00 00 00 00 00 00 3f
            ff ff ff ff ff c0 3f ff f0 00 00 0f 80 00 00 70
            00 00 3f ff f8 03 ff ff ff ff ff ff ff ff ff 80
            0f c0 00 00 00 00 00 07 ff ff ff ff ff fc 07 ff
            ff 00 00 03 f0 00 00 1e 00 00 07 ff 0f 80 7f ff
            ff ff ff ff ff ff ff fc 00 7e 00 00 00 00 00 00
            3f ff ff 3f ff ff c0 1f ff f8 00 00 0f 80 00 00
            1e 00 00 3f fc 3c 00 ff ff ff ff ff ff ff ff ff
            f8 00 fc 00 00 00 00 00 00 7f ff ff 7f ff ff 80
            7f 9f f0 00 00 1f 00 00 00 7e 00 80 7f f8 7c 01
            ff ff fe ff ff ff ff ff ff f8 01 f8 00 00 00 00
            0c 00 ff ff fe ff ff ff 80 7f 9f f0 00 00 1f 00
            00 00 7c 00 80 7f f8 7b 43 ff ff ff ff ff ff ff
            ff ff e0 07 e0 00 00 00 00 00 01 ff ff f9 ff ff
            fe 01 fe 3f c0 00 00 7c 00 00 01 f8 06 01 ff c1
            f8 0f ff ff ff ff ff ff ff ff ff 00 1f 80 00 00
            00 01 80 0f ff ff cf ff ff f8 07 f8 ff 00 00 07
            81 f0 e0 f0 78 3e 38 f1 98 78 7e 1f 0f 0e 3c 70
            78 3c 1e 00 ce 3c 3f 0f 03 e1 e1 18 0e 01 e0
        """
    ),
    "S": bytes.fromhex(
        """
            f0 f8 7c 78 fe 3e 0f 0f 83 e0 e0 e0 f0 f0 7c 3c
            3c 3e 3e 1e 0f 07 78 fc 3c 3c 71 87 38 7c 1e 1f
            00 f0 f8 7c 63 f1 e0 f8 7e 1e 07 87 83 1e 1e 1f
            81 e1 e0 70 f0 f8 78 70 fe 07 0f 00 f0 f8 f8 3c
            3c 1f 0f 01 c0 e0 63 83 87 81 e0 f0 f8 3c 70 0e
            00 38 c6 1e 43 8c 70 78 3f 0f 87 e1 f8 7c 3b c3
            c0 e1 e1 e0 e1 e1 e0 f8 7c 03 87 18 f0 e0 61 c1
            e7 3c 38 c0 e0 3c 0f 38 fe 1f 83 e1 e0 78 f0 01
            c3 c1 e1 c0 f0 78 3e 1f 00 f0 f0 78 78 1e 39 c3
            c1 3e 1e 0f 1d c3 c1 e1 c0 1f 1f c3 c3 e0 f8 3e
            1f 07 87 c0 c7 07 07 c0 f8 f0 f0 07 07 80 f8 7e
            1e 3e 17 87 0f 03 c3 e3 e0 ff 07 80 38 0e 03 c1
            c1 e1 f0 f0 47 c0 f8 7c 3e 1e 19 87 80 f0 7c 1e
            0e f0 e0 f0 c7 07 e0 7c 3c 3f 03 c3 c1 e0 f8 7f
            0f 18 e0 e0 f0 78 3f 0f 80 f0 f8 0f 0f 1f 07 83
            e0 f1 9c 07 03 1c 70 c7 03 87 c1 f0 f0 fc 3e 0f
            87 83 c0 f8 78 79 c7 3c 70 7e 1c 71 87 1e 1e 3e
            1f 03 86 1e 1f 01 c3 c3 e0 f0 f0 f8 3c 1f 07 1e
            38 f8 70 3e 3f 83 c0 78 71 e0 f8 0f 0f 00 f0 1e
            1f 0f 1f 0f c1 f1 f8 e1 e0 e3 0e 1f c3 0f 07 1c
            70 f8 78 7c 3e 3c 1f c3 c0 f8 30 78 3f 1f 01 f0
            7c 3f 1e 3f 1c 1f 0f 07 83 c0 f0 78 3e 1e 78 71
            87 0f 7e 03 c3 70 e3 07 01 e1 e3 98 f8 77 01 0c
            1c 1c 27 0f 01 c1 c3 80 c1 f0 f0 7e 1f 0f 07 c3
            f0 78 0f 38 e1 c1 e1 f0 3e 0f 83 c3 87 80 f0 f0
            1f 01 e1 f0 c7 0f 11 c3 c0 f8 7c 3c 3e 0f 0e 70
            8e 3d 87 c7 18 f0 7c 3e 1f 07 8c f0 3f 8f 0e 1b
            c3 87 07 83 e0 f0 78 c7 18 e3 c3 e1 e0 7c 3c 71
            9c 70 78 f0 c6 3e 1f 0f 80 e0 1c 3e 3c 87 0e 71
            87 83 c2 3c 3e 1e 18 c7 83 c3 80 f0 f1 8e 19 c1
            c0 78 7c 3c 0f 87 73 8f 0f 0f 0e 3e 0f 0c f8 78
            78 c0 f0 e1 c0 f0 f0 1e 1e 10 f0 ff 83 f1 e3 c0
            3c 78 e0 f0 fc 3e 1e 18 f0 3e 1f 07 81 e1 e3 1c
            38 87 83 c1 ce 1e 0f 1f 0f 83 c1 c3 8f 1e 07 ff
            ff ff 39 e7 f9 e6 00 00 00 07 f0 06 07 73 bd ff
            cf ff e3 9c 00 03 e7 7f cf 3f fe 00 00 00 00
        """
    ),
    "V": bytes.fromhex(
        """
            00 00 00 00 01 ff ff ff ff ff ff ff 07 f3 f8 e7
            80 00 00 01 f0 00 00 87 e3 ff ff ff ff 87 3c 43
            9f ff ff ff e0 00 00 00 00 00 00 00 00 07 ff ff
            ff ff ff ff e7 1e ff 0f 00 00 00 00 81 00 31 0f
            3e 0f ff fe ff 9e 43 9c 39 e7 fc cf ff c0 00 00
            00 00 00 00 00 00 3f ff ff ff ff ff ff f3 ff 7f
            9e 70 00 00 00 3f 82 1c 71 00 f3 ff ff f0 e3 dc
            73 87 1f e7 ff ff 00 00 00 00 00 00 00 00 01 ff
            ff ff ff ff ff fe c1 f8 e3 00 00 00 00 8c 01 80
            40 87 f3 7f e7 1f ff 83 1c ff 8e ff cf bf f8 00
            00 00 00 00 00 00 00 01 ff ff ff ff ff ff ff 83
            ff cf 20 00 00 00 03 30 03 0c e7 1f ff bf de 7b
            c7 39 df 7f cf ff 9f f0 00 00 00 00 00 00 00 00
            07 ff ff ff ff ff ff ee 1f ff 00 0c 00 00 00 e3
            00 60 00 7f 7f ff fe e0 7c 78 61 fb ff 8f 7f ff
            c0 00 00 00 00 00 00 00 00 0f ff ff ff ff fe ff
            88 7f fe ec 00 00 00 70 03 30 80 07 de ff f8 7f
            f0 ec 09 fe f1 df 79 ff ff 80 00 00 00 00 00 00
            00 00 7f ff ff ff ff ff ff fe fb e4 30 c0 1c 40
            3b 00 20 00 47 e7 ff 9c f7 e0 c3 78 f7 ce 73 ff
            ff ff 80 00 00 00 00 00 00 00 00 7f ff ff ff ff
            ff ff e0 ff 80 61 00 1c 00 3c 21 80 18 f3 f3 ff
            e7 fc 67 1f 80 01 fc 3f ff 8f fe 00 00 00 00 00
            00 00 00 01 ff ff ff ff ff e7 fd df ff 80 42 00
            18 06 e0 07 81 18 e7 ff ef 79 9c 39 e6 30 ff 1c
            ff ff ff e0 00 00 00 00 00 00 00 00 0f ff ff ff
            ff ff ff f3 8f fc 00 60 00 70 0e f0 00 00 19 ef
            bd e7 ff c1 1f 81 87 ff 81 f0 0f ff 80 00 00 00
            00 00 00 00 00 7f ff ff ff ff ff ff f0 7e f8 00
            60 00 30 c0 00 c0 47 3e f3 3f f7 cf 0c e1 ef 31
            c3 8e 78 ff bc 00 00 00 00 00 00 00 00 01 ff ff
            ff ff ff f7 fc e7 ff e0 01 84 30 00 79 90 06 00
            3b ff fe 3f ce 31 8e 70 0f fd cf f8 ff c0 00 00
            00 00 00 00 00 00 1f ff ff ff ff ff ff 9e 7f 39
            cc f1 c1 9b 83 18 c7 1c 79 18 f1 81 f8 80 e6 86
            67 18 e4 8f ec 0e 73 b8 8e 32 31 81 cc 7c 7e
        """
    ),
    "F": bytes.fromhex(
        """
            30 37 78 03 9c cb 0c c1 ce 73 73 e2 67 63 70 8e
            70 1c 3f e0 c7 0c 71 c3 0f 8e 71 c6 01 c6 98 c6
            3e 6e 70 63 66 73 66 f2 6e 71 cc ce e7 73 07 39
            19 22 83 03 f1 81 e1 e0 e3 83 f9 8f 99 1c 30 1c
            f0 63 31 c6 63 7d 03 03 67 31 00 0e 73 e0 e1 f6
            e3 00 e8 f8 f9 9c 9f 19 8d 8e c7 38 39 83 83 81
            f8 38 e2 0f 31 f0 03 cf 03 c0 27 63 c3 63 86 7c
            7c 79 c3 31 f3 33 8f 0f 87 38 71 9c c1 ce e6 7c
            60 3e 11 f1 8c e6 1f 18 cc ec 79 3e 2f 1c 39 19
            e6 03 61 8f 04 1f 61 c3 33 fb 3c 66 47 cc e4 c0
            07 9f 00 e1 38 ff 3d 81 8e c0 f8 38 c7 39 83 1c
            f3 33 3b 36 3f c6 e7 06 e6 67 70 c1 cc 7c c4 64
            c3 11 b9 38 63 73 e3 e6 70 7e 60 bc e3 b0 63 36
            73 26 78 cc e0 9c f8 dc cc 9c c9 9c 19 1f 3c 01
            8f c7 80 d3 18 19 f1 10 e2 f0 f8 c9 99 99 98 f1
            bc 33 07 03 61 f0 62 38 e1 98 c1 98 ef 9c c7 1c
            c1 9c f3 31 b9 e3 98 63 72 33 07 03 8e 1f 0c 46
            37 3c e0 e4 f6 60 c6 38 dc 80 dd 8c c3 07 18 c6
            e1 c7 61 86 70 e6 30 67 3c 76 66 78 3f 0f 06 cf
            c8 cc 0e 39 c8 98 0e 76 ce 19 cc 8c c7 8c d8 c3
            30 ce 78 38 f0 e9 07 1d 19 98 38 72 33 33 91 04
            e3 23 9c e3 61 cc dc cc cc 9c d8 79 cc 01 cf 11
            8e 0f 87 20 63 3b 38 1c 11 f9 39 c3 07 1f 01 80
            5d 84 e5 84 71 c6 3c 07 0c c4 fe c7 8f 1d cc c7
            ee 63 3c 66 e4 60 c7 03 1c 8c ec 64 4c c6 66 e2
            ce d1 0e c0 3c dc ee 7c cc f3 71 9d 0c 8f 07 9c
            18 fc 83 18 39 98 71 fe 63 c7 66 c6 46 e6 46 cc
            c6 e4 c0 fc f1 30 3b 33 18 33 1e 33 0e 3f 0c 19
            37 01 b6 e0 f9 70 67 73 86 3b 00 1e 0e 0e c7 c6
            71 c4 c4 e6 60 66 70 ce ce 1f 9d 8c cf 0c 78 dc
            31 c7 11 0e 38 3e 0c 8e 0f 1f 1c 18 ce 79 c7 31
            88 78 70 9c ce 77 6c c6 6e ce 03 39 cc e8 e3 88
            e7 c0 cd 87 99 1c fc 13 18 99 9c f9 b8 98 31 b9
            c7 c1 83 81 8e 67 c1 1c c6 70 19 9c 67 1c 60 7f
            fe 7c 00 fc 7f f0 08 1e 0f ff 07 80 1f f8 3f 00
            30 1f 78 38 0f 80 fe 00 06 07 ff 0f c0 3f 9f
        """
    ),
    "H": bytes.fromhex(
        """
            c0 01 ef 83 e0 1f 0f c1 f0 40 1f c3 fe 03 ff f8
            fe 03 00 ff 07 c0 00 7f c0 e0 7e 00 01 ff 86 01
            fc 0f f2 03 c0 07 ff ff 00 c0 1f f9 98 00 0c 7f
            ff c0 1e 3f fc 00 0e 7c 1f 01 fe 00 ff c0 7e 03
            f8 00 70 fc f8 00 1f 80 f0 0c 07 fd f0 38 38 ff
            3f 80 ff 80 ff 00 ff 01 f8 07 f0 3e 00 03 e0 1f
            80 07 fc 07 e0 e7 f8 70 78 00 fe 03 f0 07 f8 0f
            00 7f e1 87 ff f8 01 ff 01 f0 07 f0 0f f0 00 00
            7f cf 80 00 ff c0 7c 00 7f 80 ff 00 3e 00 ff 00
            fe 00 7e 3f 0e 00 7f 07 fc ff 00 03 fe 3e 06 00
            3f 00 7c 00 23 c0 38 0f bc 1e 00 7f 98 7e 0f 78
            1f f8 00 08 fe 00 00 03 fc 07 c0 00 7e 07 f0 1e
            03 f0 00 0f e0 3c 1f c7 e0 3c 07 98 7f 0f 80 e1
            ff ce 00 8f e7 c0 03 c7 c3 c3 c1 c1 ef ff 80 01
            ff 87 c1 80 0f c7 81 f8 07 e0 ff c0 01 c0 fe 00
            00 78 f8 0f 80 78 01 fc 00 f8 01 f1 fb f0 07 f8
            03 ff 83 83 ff ff 80 3f 1f c0 00 31 fc 1e 00 1f
            80 1f 00 3f 00 fc 07 ff 80 3e 07 c0 e0 3c 78 38
            f8 7c 1f c0 1e 0f 1f 80 1f 1e 00 1f 1e 00 0e 00
            00 3f c0 00 07 0f c1 fc 03 ff ff e0 1f 0f ff fe
            00 03 f8 7f f0 01 f8 1f 80 f0 7f 83 81 00 01 e0
            e0 07 c1 fc 00 7f c0 7f 80 1f 81 ff f0 00 00 0f
            ff 00 02 07 e0 0f 00 03 f8 0f 83 0e 02 0f c0 7f
            0f 03 c0 7e 06 07 ff 1f 00 1f cf 1f 03 fc 0f ff
            1f 00 0f c7 fc 00 3f e0 7f 80 60 00 7f 03 e1 03
            c1 83 e0 03 00 fc 1f c0 00 fc 0f c1 f2 03 e1 07
            c0 0f 80 0f 03 87 00 00 0f 81 fc 07 ff f0 0e 07
            ff 87 8f 87 ff cf c7 e1 ff ff 01 f0 ff 80 01 80
            e3 00 e0 00 00 00 e0 0f f8 00 fe 0f 80 3e 0f ff
            c0 f8 03 fe 3f 1f 01 fc 00 3f 00 ff 00 06 03 fc
            01 fc 07 f0 0f e0 3e 00 3f 80 fe 01 f8 00 f8 0f
            e0 30 f1 f1 f8 00 f0 7f f0 3f 80 7e 07 e0 00 fe
            03 e0 0f fe 01 f8 0f f0 74 00 18 03 f8 00 e0 1f
            c0 00 c0 7e 03 fc 1c 00 3f 78 3e 00 7c 3f 00 fc
            7e 0f 83 f8 3b c1 f0 7c 1f 80 f0 8f 83 e1 c7 e0
            f0 7c 07 0f 0f 81 c0 63 c0 7c 07 83 c0 3e 03
        """
    ),
    "Z": bytes.fromhex(
        """
            80 00 00 03 00 00 7e 1f f0 f8 f8 7e 3b e1 f8 07
            83 c0 1c 00 c3 c1 c0 7c fc 7c 7f 1d 9e 1e 3e 1e
            1f 1e 30 3e 1f 07 00 f0 1f 00 00 38 07 00 40 fe
            1f 8f ff f8 f1 f0 f0 f8 61 e0 f8 7c 1f 03 f0 7e
            07 81 e6 1e 0f 87 e0 f0 87 c0 e0 78 3e 1f 03 81
            c0 3c 00 00 00 00 00 03 ff 8f e0 7f 8f e3 cf 8f
            c1 e1 c1 87 03 81 e0 7c 1f c1 f0 3c 3e 3f 3c e0
            0f 07 87 c3 f8 78 1e 78 c0 10 30 00 00 00 00 00
            01 9f 9f f1 fe fc ff 03 c7 83 c3 c0 3e 00 30 18
            7c 1f c3 e1 f8 e7 18 e1 e0 3f 0f 83 c0 73 87 e0
            7c 00 00 70 1c 00 00 c0 1c 00 f8 fc ff 3f ff e3
            c0 fc 3e 03 00 03 c1 c0 38 3e 0f 0f 1e 1f 07 f0
            fe 1f c0 78 7f 07 c1 f0 7e 0f 81 e0 78 0e 00 60
            00 00 00 7d 03 ff ff ff 0f e0 3f 81 f8 1c 0f 02
            78 3f 03 e0 fc 1f 83 c1 e1 fc e3 c1 f0 3e 1f 03
            c0 cf 07 c0 f0 00 00 00 00 00 00 1c 3f 01 f0 7f
            f0 ff 1f 0f 8f 07 81 c0 0f 03 b0 e0 3c 73 81 c7
            78 7f 83 c1 f0 f8 f8 3c 0f 01 e0 f8 70 03 00 38
            00 01 c0 f0 00 07 c3 ff ff f8 fe 1e 1f 83 87 07
            06 00 0f 0f 81 e0 fe 0f e1 e4 3e 1f 18 f0 1f 87
            81 e3 81 e1 f0 f0 0f 81 e0 00 00 00 00 00 1f 81
            f8 ff ff c0 f8 c7 c1 8f 0c 60 1e 1f 07 10 1e 1e
            1f 1f c7 ff c1 f0 3e 03 c3 e0 f0 78 e1 f8 7c 07
            c0 f0 00 03 00 00 01 ff c3 f3 ff f9 f8 7f 1f c0
            f0 3e 0f 81 e0 f0 78 1c f0 3e 0f 07 c3 81 e3 c0
            7e 0f 83 c7 1e 1f 00 f0 3e 07 00 00 08 00 00 00
            7f 0f f3 ff fc 0f 1e 7e 3c 07 e0 e1 e0 38 c0 dc
            1e 1e 3f c1 ce 3e 03 f0 cf 07 c3 c1 f0 f0 43 c1
            e0 00 00 00 00 00 00 00 00 7e cf f1 ff ff f0 fc
            3f e1 e0 30 40 e0 fc 1e 0f 0f 07 87 e1 fc 78 4f
            03 83 c3 c0 f0 1f 07 80 fc 02 03 80 1c 00 00 00
            20 00 3f 0f e7 e3 f7 f0 fc 1f c7 1c 00 e0 3c 3f
            0f 1f 0e 21 f0 f8 f0 fc 3e 1f 87 8e 71 1e 03 f0
            fc f1 80 38 00 60 00 00 00 80 00 ff 1f c7 ef 00
            01 ff fe 00 0e ff ff e0 00 00 ff ff ff c0 00 00
            3f ff ff fc 00 00 07 ff ff f8 3f ff fe 00 00
        """
    ),
    "AW": bytes.fromhex(
        """
            03 ff ff e0 00 00 1f ff e0 00 01 ff ff c0 00 8f
            ff fe 00 00 3f ff ff fc 00 00 03 ff ff ff c0 00
            00 7f ff ff 01 ff ff c0 00 00 7f ff fe 00 00 01
            ff fe 00 00 1f ff f8 00 04 ff ff c0 00 01 ff ff
            ff e0 00 00 1f ff ff ff 00 00 03 ff ff f8 3f ff
            ff 00 00 03 ff ff e0 00 00 0f ff c0 00 01 8f ff
            00 00 cf ff fe 00 00 07 ff ff ff 00 00 00 ff ff
            ff fc 00 00 0f ff ff e0 ff ff f0 00 00 0f ff ff
            80 00 00 7f ff 00 00 1d ff fc 00 00 7f ff f0 00
            00 3f ff ff f0 00 00 1f ff ff ff 00 00 01 ff fb
            fc 1f ff ff 00 00 03 ff ff f0 00 00 0f ff c0 00
            00 7f ef 80 00 07 ff ff 80 00 07 ff ff f8 00 00
            0f ff ff ff 00 00 01 ff ff fe 0f ff ff 00 00 03
            ff ff f0 00 00 07 ff c0 00 00 c7 ff 80 00 3f ff
            ff 00 00 01 ff ff ff 80 00 00 ff ff ff f8 00 00
            1f ff bf c0 ff ff f0 00 00 3f ff ff 80 00 00 ff
            ff 80 00 03 ff f8 00 00 7f ff e0 00 00 1f ff ff
            ff 00 00 03 f7 ff ff f0 00 00 3f ff ff 81 ff ff
            e0 00 00 3f ff ff 00 00 01 ff ff c0 00 21 ff e0
            00 03 ff ff c0 00 00 ff ff ff f8 00 00 0f ff ff
            ff 80 00 00 ff ff fe 0f ff ff 00 00 01 ff ff f8
            00 00 0f ff f0 00 00 ff ff c0 00 03 ff ff 80 00
            00 ff ff ff 80 00 00 1f ff ff ff 00 00 03 ff ff
            f8 3f ff fe 00 00 03 ff ff f0 00 00 1f ff c0 00
            01 ff ff 00 00 07 ff ff 00 00 07 ff ff fe 00 00
            00 ff ff ff f0 00 00 1f ff ff c1 ff ff f0 00 00
            1f ff ff 80 00 00 ff fe 00 00 1f ff fc 00 00 3f
            ff f8 00 00 3f ff ff e0 00 00 1f ff ff ff 00 00
            03 ff fb f8 3f ff fe 00 00 07 ff ff e0 00 00 1f
            ff 80 00 00 ff ff 80 00 07 ff ff 00 00 07 ff ff
            fc 00 00 01 ff ff ff e0 00 00 3f ff ff 83 ff ff
            c0 00 00 7f ff fe 00 00 03 ff fc 00 00 3f ff f0
            00 00 ff ff e0 00 00 ff ff ff 00 00 00 7f ff ff
            f8 00 00 07 ff ef e0 3f ff fc 00 00 07 ff ff 00
            00 ff fe 00 00 3f 00 0f ff ff 00 03 c7 ff 00 03
            f3 ff ff ff 00 1f 07 ff f0 0f 80 fc 00 0f ff
        """
    ),
    "AH": bytes.fromhex(
        """
            ff 00 03 f0 1f e0 1f f8 00 00 03 ff e0 00 00 78
            00 3f ff fe 00 0e 1f f8 00 1f ff ff ff fe 00 3e
            0f ff c0 1f 01 f8 00 1f ff ff 00 07 e0 7f c0 7f
            f0 00 00 0f ff c0 20 03 f0 00 ff ff f0 00 30 1f
            e0 00 7f c7 ff ff fc 00 7c 1f ff 80 3e 03 f0 00
            3f ff fe 00 0f c0 ff c0 7f f0 00 00 0f ff 00 00
            03 e0 00 ff ff f0 00 1c 1f f8 00 7f f7 ff ff f8
            00 f8 7f ff 00 7c 07 e0 00 7f ff fc 00 1f 80 7f
            00 ff c0 00 00 3f ff 00 80 03 e0 03 ff ff e0 01
            e0 ff c0 01 ff cf ff ff f0 01 e0 ff fe 00 f8 0f
            c0 00 ff ff f0 00 3f 83 ff 01 ff 80 00 00 7f fe
            00 00 0f 80 01 ff ff c0 00 61 ff 80 01 ff 7f ff
            ff e0 03 c0 ff fe 01 f0 1f 80 01 ff ff f0 00 7f
            03 ff 03 ff 80 00 00 ff fc 02 00 1f 00 07 ff ff
            c0 01 73 ff c0 07 fe ff ff ff c0 07 81 ff f8 03
            e0 3f 00 03 ff ff c0 00 fc 0f fc 07 ff 00 00 01
            ff f8 00 00 7c 00 1f ff ff 00 06 07 ff 00 07 f8
            7f df ff c0 07 81 ff f8 03 e0 7f 00 03 ff ff c0
            00 f8 07 fc 07 fe 00 00 01 ff f8 18 00 fe 00 1f
            ff fe 00 03 c7 ff 00 1f fb ff ff ff 80 0f 03 ff
            f0 07 c0 7e 00 07 ff ff c0 01 f8 1f f8 0f fc 00
            00 03 ff f0 10 00 fc 00 1f ff fe 00 07 07 fe 00
            0f f0 7f bf ff 80 0f 07 ff f0 0f 80 fc 00 0f ff
            ff 80 01 f0 0f f8 0f fc 00 00 03 ff e0 1c 00 7c
            00 3f ff ff 00 0e 1f fe 00 3f f7 ff ff fe 00 3c
            0f ff c0 1f 01 f8 00 1f ff ff 00 07 c0 3f e0 3f
            f0 00 00 07 ff c0 e0 00 f8 00 ff ff fc 00 1e 9f
            fc 00 3f e3 ff ff fe 00 3c 0f ff c0 1f 01 f8 00
            1f ff ff 00 07 e0 1f e0 3f f8 00 00 07 ff c0 70
            03 f0 00 7f ff fc 00 3c 7f f8 00 3f cf ff 9f ff
            80 1f 07 ff f0 0f 80 fe 00 07 ff ff 80 01 f0 1f
            f8 0f fc 00 00 01 ff e0 38 00 fc 00 1f ff ff 00
            07 cf fe 00 3f ef ff ff ff 00 3e 0f ff e0 1f 00
            fc 00 0f ff ff 00 03 f0 3f f0 3f f8 00 00 07 00
            7f ff ff c0 e0 0c 00 00 00 7f ff fe 00 00 00 1c
            7f 0f ff df c0 00 01 ff ff e0 00 1f ff fe 00
        """
    ),
    "UH": bytes.fromhex(
        """
            00 00 ff ff ff 83 f0 7c 00 00 07 ff ff f8 1c 01
            80 00 00 0f ff ff c0 00 00 00 87 e0 ff ff f8 00
            00 3f ff fe 00 03 ff ff 80 00 00 1f ff ff f8 7e
            07 80 00 00 ff ff ff 03 00 20 00 00 00 ff ff f8
            00 00 00 30 fe 3f ff ff 00 00 03 ff ff 80 00 ff
            ff f0 00 00 07 ff ff fe 1f 81 f0 00 00 1f ff ff
            e0 e0 06 00 00 00 0f ff ff 00 00 00 0f 1f c7 ff
            ff 38 00 00 7f ff e0 00 0f ff ff 00 00 00 fe ff
            ff 83 e0 7e 00 00 07 ff ff f8 18 01 80 00 00 01
            ff ff c0 00 00 03 c7 e0 ff ff f8 00 00 1f ff fe
            00 03 ff ff 80 00 00 1f ff ff f0 7e 0f 80 00 00
            ff ff ff 07 00 20 00 00 00 7f ff f8 00 00 00 e0
            fc 3f ff ff 00 00 07 ff ff 00 00 ff ff e0 00 00
            0f ff ff f8 1f 03 e0 00 00 7f ff ff 81 80 18 00
            00 00 3f ff fc 00 00 00 38 3f 0f ff ff 80 00 00
            ff ff e0 00 3f ff fc 00 00 03 ff ff fe 0f 81 f0
            00 00 1f ff ff e0 60 00 00 00 00 07 ff ff f0 00
            00 1f 1f c7 ff ff f0 00 00 7f ff f0 00 0f ff fe
            00 00 03 ff ff fe 0f 81 f8 00 00 1f ff ff e0 60
            00 00 00 00 07 ff ff e0 00 00 0f 0f c3 ff ff e0
            00 00 7f ff f8 00 07 ff ff 00 00 00 ff ff ff 03
            e0 7c 00 00 07 ff ff f0 18 00 00 00 00 01 ff ff
            e0 00 00 07 07 e1 ff ff fc 00 00 1f ff fe 00 07
            ff ff 00 00 00 fd ff ff 03 e0 fc 00 00 0f ff ff
            f0 70 00 00 00 00 03 ff ff fc 00 00 0f 0f c1 ff
            ff f8 00 00 3f ff f8 00 0f ff fe 00 00 01 ff ff
            ff 07 c0 f8 00 00 0f ff ff e0 00 00 00 00 00 07
            ff ff f8 00 00 0e 0f c3 ff ff e0 00 00 3f ff fc
            00 0f ff ff 00 00 00 ff ff ff 83 e0 7c 00 00 03
            ff ff f8 10 00 00 00 00 01 ff ff fe 00 00 03 07
            f3 ff ff f8 00 00 0f ff fe 00 03 ff ff 00 00 01
            f9 ff ff 07 c0 fc 00 00 07 7f ff f0 60 00 00 00
            00 03 ff ff fc 00 00 06 0f 87 ff ff f3 00 00 3f
            ff fc 00 07 ff ff 00 00 03 e3 ff fc 1f 03 f8 01
            ff ff 01 63 f0 03 f1 ff bf f0 03 f8 0f e0 fe 00
            ff e0 0f c1 fe 03 fc 00 01 01 fc 07 f0 00 03
        """
    ),
    "AE": bytes.fromhex(
        """
            c0 00 1f e0 07 c0 06 00 7f 00 7c 3e 00 01 f8 01
            ff ff ff f0 03 f8 0f e0 fe 00 fb e0 0f c0 fe 03
            fc 00 03 00 fc 07 f0 00 01 e0 00 1f e0 1c 00 00
            00 7f 80 ff ff 00 03 fc 00 fe ff 9f fc 01 fc 07
            f0 7f 00 7d f8 07 e0 ff 01 fe 00 03 80 fe 03 fc
            00 00 c0 00 07 f8 00 0f 80 00 3f e0 00 ff 80 00
            3f 00 3f ff 1f f8 01 fc 07 f0 7f 00 ff f0 07 e0
            ff 01 fe 00 03 80 fe 03 f8 00 00 60 08 0f f0 07
            f8 03 c0 7f 80 7f f7 80 08 f8 01 ff ff ff e0 0f
            e0 1f 83 fc 03 ef c0 3f 03 f8 0f f0 00 1e 07 f0
            3f c0 00 0f 03 c0 ff 01 e0 04 00 00 fc 03 e1 f8
            00 00 30 03 e7 ff ff 00 7f 80 fe 1f c0 1f 7f 00
            fc 1f c0 7f 80 01 f0 3f 80 ff 00 00 30 04 01 f8
            07 80 70 00 03 f0 1f 9f f0 06 08 00 1f ff ff f8
            01 fc 07 e0 ff 00 f3 f8 07 e0 fe 01 fe 00 07 80
            fe 07 f8 00 03 c0 78 1f e0 3e 03 00 00 7f 80 f0
            7f 80 02 80 00 79 ff f3 f0 07 f0 1f 83 fc 03 8f
            e0 1f 83 f8 0f f8 00 1f 07 f0 1f e0 00 0e 01 00
            7f 00 70 00 00 00 fe 01 f8 7f 00 08 70 07 ff ff
            ff 80 1f 80 7e 0f e0 0e 1f 00 fe 0f e0 3f f0 00
            f8 1f c0 ff 00 00 70 1e 01 fc 0f 00 f8 00 03 fc
            1e 0f e0 00 00 80 0f ff ff f0 01 fc 07 e0 ff 00
            e1 f8 07 e0 fe 03 ff 00 0f 80 fc 0f f8 00 03 c1
            e0 1f 80 f0 07 80 00 7f 80 20 7f 00 00 03 00 3f
            ff ff 00 3f 80 fe 1f e0 3f 3f 00 fc 3f c0 7f c0
            00 f0 3f 80 ff 00 00 70 07 00 ff c0 00 fc 00 03
            fc 38 3f f0 00 07 e0 03 ff fe 00 3f 80 fe 0f e0
            1f ff 00 fc 1f c0 3f c0 00 70 1f 80 ff 00 00 3c
            00 00 ff c0 0f fe 00 07 f8 03 ff f0 00 3b 00 0f
            ff fc 00 ff 01 f8 3f c0 7f fc 01 f8 7f 80 ff 00
            00 f0 7f 01 fe 00 00 78 00 01 ff 00 7f 8f 00 1f
            e0 0c ff e0 00 3f 00 7f ff f0 03 fc 07 e0 ff 00
            ff f0 07 c1 fe 03 fc 00 03 c1 fc 07 f8 00 03 e0
            00 0f 81 e0 0f d0 00 7e 03 f0 ff 00 00 ce 0f ff
            00 00 00 00 03 f0 00 01 ff ff ff f0 00 00 00 1f
            ff ff f8 00 03 ff fe 00 00 00 7f ff ff fc 00
        """
    ),
    "OH": bytes.fromhex(
        """
            00 00 ff e0 00 00 00 3f ff ff f8 00 00 00 00 7f
            00 00 1f ff ff ff 00 00 00 01 ff ff ff 02 00 1f
            fe 00 00 00 0f ff ff ff 80 00 00 7f fe 00 00 00
            03 ff ff ff 00 00 00 01 03 e0 00 03 ff ff ff e0
            00 00 00 3f ff ff f8 00 0f bf fc 00 00 00 7f ff
            ff f8 00 00 00 ff 80 00 00 00 ff ff ff e0 00 00
            00 00 fe 00 00 7f ff ff fc 00 00 00 03 ff ff fc
            00 00 7f fe 00 00 00 0f ff ff ff 00 00 00 3f f0
            00 00 00 1f ff ff f8 00 00 00 00 3f 80 00 0f ff
            ff ff 80 00 00 00 ff ff ff 80 00 07 ff c0 00 00
            03 ff ff ff c0 00 00 07 f8 02 00 00 0f ff ff fe
            00 00 00 00 1f c0 00 0f ff ff ff c0 00 00 00 7f
            ff ff c0 00 03 87 c8 00 00 00 ff ff ff f0 00 00
            00 fc 01 00 00 07 ff ff ff 00 00 00 00 07 e0 00
            03 ff ff ff e0 00 00 00 1f ff ff fe 00 07 07 fe
            00 00 00 7f ff ff fc 00 00 00 7f 00 c0 00 01 ff
            ff ff 80 00 00 00 03 f8 00 01 ff ff ff f8 00 00
            00 0f ff ff f8 00 00 7f f8 00 00 00 3f ff ff fc
            00 00 00 1f 00 00 00 00 ff ff ff c0 00 00 00 01
            fc 00 00 ff ff ff fc 00 00 00 07 ff ff f8 00 00
            ff fc 00 00 00 3f ff ff fc 00 00 00 1f 80 00 00
            00 ff ff ff c0 00 00 00 00 fc 00 01 ff ff ff fc
            00 00 00 07 ff ff fc 00 00 7f fc 00 00 00 3f ff
            ff fc 00 00 00 1f 00 00 00 00 ff ff ff c0 00 00
            00 01 fc 00 01 ff ff ff f8 00 00 00 07 ff ff ff
            00 01 c1 ff 00 00 00 1f ff ff fc 00 00 00 7c 01
            80 00 03 ff ff ff 02 00 00 00 07 f0 3c 0f ff ff
            ff e0 00 00 00 1f ff ff f0 00 00 ff f0 00 00 00
            ff ff ff f8 00 00 00 7c 01 00 00 07 ff ff ff 00
            00 00 00 0f e0 18 07 ff ff ff e0 00 00 00 3f ff
            ff f0 00 00 e3 e0 00 00 00 ff ff ff f0 00 00 00
            7e 00 80 00 03 ff ff ff 00 00 00 00 03 f0 08 03
            ff ff ff e0 00 00 00 1f ff ff e0 00 01 e0 ff 00
            00 00 ff ff ff fc 00 00 00 7c 01 00 00 03 ff ff
            80 00 00 c0 0f ff ff ff fe 00 00 00 00 3f ff ff
            c7 f0 00 06 03 ff ff ff ff c0 00 7c 07 03 f3
        """
    ),
    "EH": bytes.fromhex(
        """
            fc 1f c0 01 80 20 00 7f 81 ff e0 60 00 38 01 ff
            ff fd ff c0 00 00 00 07 ff df f8 7c 00 06 00 7f
            ff fe ff f8 00 1f 01 c1 fc ff 07 f0 00 60 00 00
            1f f0 7f f8 18 00 1e 00 ff ff ff 7f c0 00 00 00
            01 ff ff fc 07 c0 03 e0 7f ff ff 87 fc 00 07 c0
            78 7f 1f 81 fc 00 0c 00 00 03 fc 1f fe 00 00 03
            80 3f ff ff 9f fc 00 00 00 03 ff 87 ff ff 00 7e
            00 1d ff ff 3f f8 00 00 f8 0e 1f c7 f0 7f 80 07
            00 00 00 ff 07 ff 80 80 00 e0 0f ff df ff ff 00
            00 00 18 1f ff ff fc 1e 00 07 03 ff ff ff ff c0
            00 fc 0f 07 e3 f8 3f c0 03 00 00 00 7f 83 ff c0
            c0 00 f0 07 ff ff f9 ff 80 00 00 00 07 ff ff f0
            fe 00 01 40 ff ff fe 7f f8 00 1f 01 c1 fc ff 07
            f8 00 60 10 00 1f f0 ff f8 18 00 1e 00 ff fb ff
            ff f0 00 00 00 00 ff ff fe 0f c0 00 00 1f ff ff
            ff ff 80 01 f0 1c 1f 8f e0 ff 00 06 00 00 01 fe
            0f ff 00 00 00 c0 0f ff bf ff fc 00 00 00 00 3f
            ff ff e1 fc 00 00 03 ff 7f ff ff e0 00 0f 81 e0
            fc 7f 07 f8 00 60 00 00 0f f0 7f f8 18 00 0e 00
            ff ff ff 3f f0 00 00 00 00 ff ff fe 1f e0 00 18
            3f ff ff ff ff 00 01 f0 3c 1f 8f e0 ff 00 0e 00
            00 01 fe 0f ff 01 00 00 80 0f ff 9f ff fc 00 00
            00 00 1f ff ff 81 f8 00 00 07 ff ff ff ff f0 00
            1f 01 c1 fc ff 07 f8 00 60 00 00 1f e0 ff f8 18
            00 1e 00 ff ff ff ff c0 00 00 00 0f fe 0f ff fc
            00 fc 00 ff ff ff ff f0 00 07 c0 f0 fe 3f 83 fc
            00 38 00 00 07 f8 3f fe 04 00 06 00 7f fc ff ff
            f8 00 00 00 00 3f fb ff 03 f0 00 18 1f f8 ff ff
            ff 00 00 f8 1e 1f c7 f0 7f 80 07 00 00 00 ff 07
            ff 80 00 00 c0 07 ff ff ff ff 00 00 08 00 1f fe
            7f 87 f0 00 02 03 ff ff ef ff c0 00 3e 07 83 f1
            fc 1f e0 00 c0 00 00 3f c1 ff f0 30 00 1c 01 ff
            fb fd ff c0 00 00 00 3f 9c 7f ff f0 03 e0 01 ff
            ff ff ff c0 00 1f 01 c1 fc 7f 0f f0 00 e0 00 00
            00 fc 00 00 00 07 ff ff ff ff ff ff ff c0 00 00
            00 00 1f ff ff ff ff ff ff ff 80 00 00 00 00
        """
    ),
    "OO": bytes.fromhex(
        """
            00 00 00 3f ff ff ff 01 00 07 ff 80 00 00 0f ff
            ff ff ff c0 0f ff 80 00 00 00 00 1f ff ff ff ff
            ff ff ff 80 00 00 00 00 00 00 00 3f ff ff ff e0
            00 03 ff 00 00 00 03 ff ff ff ff ff ff ff c0 00
            00 00 00 07 ff ff ff ff ff ff ff c0 00 00 00 00
            00 00 00 0f ff ff ff f0 00 00 7f 00 00 00 01 ff
            ff ff ff ff ff ff f0 00 00 00 00 01 ff ff ff ff
            ff ff ff f8 00 00 00 00 00 00 00 03 ff ff ff ff
            40 1e 3f c0 00 00 01 ff ff ff ff ff ff ff c0 00
            00 00 00 00 ff ff ff ff ff ff ff fc 00 00 00 00
            00 00 00 03 ff ff ff ff 70 06 0f c0 00 00 00 7f
            ff ff ff ff ff ff f8 00 00 00 00 00 7f ff ff ff
            ff ff ff fc 00 00 00 00 00 00 00 01 ff ff ff ff
            e0 07 ff f0 00 00 00 ff ff ff ff fe 03 ff f0 00
            00 00 00 03 ff ff ff ff ff ff ff f0 00 00 00 00
            00 00 00 03 ff ff ff ff f8 73 ff e0 00 00 00 ff
            ff ff ff ff ff ff c0 00 00 00 00 01 ff ff ff ff
            ff ff ff e0 00 00 00 00 00 00 00 0f ff ff ff ff
            e1 ff ff c0 00 00 07 ff ff ff ff ff ff ff 00 00
            00 00 00 0f ff ff ff ff ff ff ff 80 00 00 00 00
            00 00 00 3f ff ff ff ff c7 ff fe 00 00 00 1f ff
            ff ff ff ff ff fc 00 00 00 00 00 3f ff ff ff ff
            ff ff ff 00 00 00 00 00 00 00 00 ff ff ff ff ff
            ff ff f8 00 00 00 3f ff ff ff ff ff ff e0 00 00
            00 00 00 ff ff ff ff ff ff ff f8 00 00 00 00 00
            00 00 03 ff ff ff ff ff f3 ff c0 00 00 01 ff ff
            ff ff ff ff ff 00 00 00 00 00 03 ff ff ff ff ff
            ff ff c0 00 00 00 00 00 00 00 1f ff ff ff ff ff
            ff ff 00 00 00 07 ff ff ff ff ff ff fc 00 00 00
            00 00 3f ff ff ff ff ff ff ff 00 00 00 00 00 00
            00 00 ff ff ff ff fc 7f ff d0 00 00 00 0f ff ff
            ff ff ff ff f0 00 00 00 00 00 7f ff ff ff ff ff
            ff fc 00 00 00 00 00 00 00 01 ff ff ff ff fc 79
            ff f8 00 00 00 1f ff ff ff ff ff ff f0 00 00 f8
            03 fc 01 c0 00 00 fc 00 ff c0 7f e0 03 fc 00 1f
            e0 0f fe 07 ff 80 3f 00 f8 3c 07 e1 fe 0f fc
        """
    ),
    "IH": bytes.fromhex(
        """
            03 fc 00 3e 01 c0 ff fc 1f f0 0f f0 06 00 00 00
            3f 00 ff 80 ff e0 0f 81 c0 0f e0 1f f8 07 fe 00
            fc 03 e0 60 3f 87 f0 7f e0 0f f0 01 f0 0f 01 ff
            e0 7f c0 3f c0 18 00 00 01 f8 03 fe 03 ff 00 3f
            80 00 7f 80 ff f0 3f fc 00 fc 07 c1 e0 7f 0f f0
            ff e0 1f e0 01 f0 0f 03 ff e0 ff 80 3f c0 00 00
            00 1f e0 0f fc 07 ff 00 3f e0 00 fe 00 ff c0 7f
            f8 01 f0 0f 83 c0 fe 1f c0 ff c0 3f c0 03 e0 3c
            0f ff 81 ff 00 7f 00 00 00 00 3f 80 1f f0 0f fc
            00 7f e0 03 fe 03 ff 81 ff 80 1f 80 fc 0c 07 e0
            fe 0f fc 03 fc 00 7e 01 e0 7f fc 1f f0 07 f0 06
            00 00 01 fc 01 ff 00 ff 00 0e 7f 00 1f c0 3f f8
            0f f8 01 f8 07 c0 c0 7f 0f e0 ff c0 3f 80 03 e0
            3e 07 ff c1 ff 00 ff 00 e0 00 00 0f c0 1f f8 0f
            f8 00 fe 00 01 fc 01 ff 80 7f e0 03 f0 0f 87 80
            fe 3f c1 ff 80 7f 80 07 c0 78 1f ff 83 fe 00 ff
            00 80 80 00 0f c0 1f f0 0f f8 01 f1 fc 03 fe 01
            ff 80 ff c0 07 c0 3e 07 01 f8 7f 03 ff 00 ff 00
            1f 00 f0 3f ff 07 f8 03 fc 03 80 00 00 1f 80 3f
            e0 3f f0 03 c1 f8 07 fc 03 fe 03 ff c0 1f 80 f8
            1c 07 e1 fe 0f fc 03 f8 00 7e 03 c0 ff f8 1f f0
            07 f0 0c 00 00 00 7f 00 ff c0 7f e0 1f c7 e0 0f
            f0 1f fe 07 fc 00 fc 07 c0 c0 7f 0f f0 7f e0 1f
            c0 03 f0 1f 07 ff c0 ff 00 7f 00 f0 00 00 01 f8
            03 fc 07 fe 03 f8 1f 80 ff 00 7f e0 7f c0 03 f0
            1f 03 80 fe 3f 81 ff 80 7f 00 07 c0 7c 0f ff 03
            fc 00 ff 00 c0 00 00 03 f0 0f f8 0f fc 03 f0 7f
            01 ff 00 ff c0 ff cc 01 f8 0f 83 c0 ff 1f c1 ff
            c0 3f 80 03 e0 3c 0f ff 83 fe 00 7f 00 80 00 00
            07 f0 0f fc 0f fe 01 f8 7e 01 ff 01 ff c0 ff e0
            01 f8 0f 81 c0 ff 1f c0 ff c0 3f 80 03 e0 1e 07
            ff 81 ff 00 ff 00 60 00 00 03 f8 07 fc 07 ff 01
            f8 3f 00 ff 00 ff c0 3f f8 00 fc 07 c1 e0 7f 0f
            e0 ff e0 1f c0 01 f0 0e 03 ff c0 ff 00 3f 80 00
            03 f0 1f 80 3f e0 0f e0 1f f0 7f ff 01 fe 00 07
            e0 0f e0 0f f0 07 fc 07 f8 01 ff 00 fe 00 7f
        """
    ),
    "EE": bytes.fromhex(
        """
            00 1f c0 7f c0 3f f8 0f fe 0c 03 f0 1f 80 3f c0
            0f e0 0f f0 3f ff 01 fe 00 07 e0 0f e0 0f f0 03
            fc 07 f8 01 ff 00 7f 00 3f 80 0f e0 3f e0 0f f8
            07 fc 0f c0 7e 03 f0 07 fc 01 fe 03 fe 0f ff f0
            3f 80 00 fc 00 fc 01 fe 00 7f 00 ff 00 7f c0 07
            e0 03 f8 01 fc 03 fe 03 ff 80 ff 03 f8 0f c0 7e
            00 ff 00 7f 80 7f 81 ff fe 07 f0 00 1f 80 3f 80
            7f 80 1f e0 1f e0 1f e3 00 fc 00 7e 00 7f 80 7f
            80 7f e0 3f e0 7e 01 f8 1f c0 3f e0 0f f0 0f f0
            3f ff 81 fe 00 03 f0 07 e0 0f f0 03 fc 07 fc 01
            ff 00 3f 00 0f c0 0f f0 0f f0 1f fc 07 fc 07 c0
            7e 03 f0 07 f8 01 fc 03 fc 0f ff e0 7f 80 00 fc
            01 fc 01 fc 00 ff 01 ff 00 7f 80 0f c0 07 f0 03
            fc 03 fc 03 ff 01 ff 80 00 7e 03 f0 07 fc 01 fe
            01 fe 07 ff e0 3f c0 00 fc 01 fc 01 fe 00 ff 80
            ff 80 7f e0 07 e0 03 f0 01 fc 03 fe 01 ff 01 ff
            81 f0 1f 00 fc 01 fe 00 ff 00 ff 03 ff f8 0f e0
            00 3f 00 7f 00 ff 00 3f c0 7f c0 1f e0 03 f0 01
            fc 00 ff 00 ff 80 ff c0 7f e0 00 3f 00 fc 01 ff
            00 7f 00 ff 01 ff f8 0f e0 00 3f 00 7f 00 ff 80
            3f c0 3f e0 0f f0 03 f0 01 fc 00 fe 01 ff 80 7f
            c0 ff e0 38 0f c0 7f 00 ff 00 3f 80 7f 80 ff fe
            07 f8 00 0f 80 3f 80 3f c0 0f f0 1f f0 0f f0 01
            f8 00 7e 00 3f 80 7f e0 3f f0 3f f8 38 07 e0 3f
            00 7f 80 1f c0 1f e0 7f ff 03 fc 00 07 c0 1f c0
            1f e0 07 f8 0f f8 03 fc 00 fc 00 3e 00 1f c0 3f
            e0 7f f0 1f f8 07 03 f0 1f 80 3f c0 0f e0 1f e0
            7f ff 81 fe 00 07 e0 0f e0 1f f0 03 fc 07 f8 03
            fc 00 7e 00 1f 00 0f e0 1f f0 0f f8 0f fe 0f 01
            f0 0f c0 1f e0 07 f0 0f f0 3f ff 80 fe 00 03 f0
            03 f0 0f f8 03 fe 03 fe 00 fc 00 3f 00 02 90 03
            f8 0f fe 0f fc 03 ff 00 03 f0 1f 80 3f e0 0f f0
            0f f0 3f ff 80 ff 00 07 e0 07 e0 0f f0 03 fc 07
            fc 01 fc 00 7e 00 1f 00 0f e0 1f f8 1f fc 0f 00
            00 00 00 00 00 00 00 00 07 ff ff ff c0 3f ff ff
            ff ff 00 00 00 00 00 00 07 ff ff ff ff ff ff
        """
    ),
    "WH": bytes.fromhex(
        """
            cc 00 00 00 00 00 00 00 00 07 ff ff f8 00 00 07
            c0 00 00 00 07 e3 8f ff e0 01 ff ff ff ff ff 1e
            00 00 00 01 ff ff c0 00 00 00 00 1f ff ff ff ff
            ff ff ff 80 00 00 00 00 00 00 00 00 01 ff ff ff
            ff 00 00 00 00 00 00 00 00 00 ff ff ff ff fe 84
            00 00 00 00 00 00 00 07 ff ff ff ff 80 00 00 00
            07 ff ff ff ff b1 e3 ff ff ff ff c6 90 00 00 00
            00 00 01 ff ff ff ff 80 00 00 00 01 ff ff ff e7
            00 01 e7 ff fe bf 39 ff f7 e0 00 00 00 00 1f ff
            ff ff f0 00 00 00 00 ff ff ff f0 00 00 00 1e 8f
            81 ff ff ff ff f8 00 00 00 00 7f ff ff ff 80 00
            00 00 3f ff ff ff f0 00 00 00 00 00 01 ff ff ff
            ff c0 00 00 00 00 00 ff ff ff ff c0 00 00 00 07
            ff ff ff fc 00 00 00 00 00 03 ff ff ff e0 00 00
            0f ff e0 00 00 00 ff ff ff fc 00 00 00 3f ff ff
            f8 00 00 03 ff f8 00 00 03 ff ff ff c0 00 00 3f
            ff ff c0 00 00 03 ff ff ff 00 00 00 03 ff ff e0
            00 00 3f ff e0 00 00 00 7f ff ff 80 00 00 07 ff
            ff fe e0 00 00 00 18 07 ff ff ff f0 00 00 00 7f
            ff ff fc 60 00 00 00 00 07 ff ff ff f0 00 00 03
            ff ff fd e0 ef ff ff 00 00 00 03 ff ff ff 00 00
            00 0f ff ff e0 30 07 83 f0 00 00 01 ff ff f8 00
            00 00 ff ff ff 00 00 03 ff ff ff 80 00 00 00 1e
            0f ff ff fc 00 00 00 1f ff ff e1 f0 04 00 00 00
            0f ff ff fe 00 00 00 27 ff ff f8 00 00 07 d9 ff
            60 08 00 00 01 e7 ff ff c0 30 07 80 ff ff f0 00
            00 07 cf ff c1 f0 3f 83 e0 00 00 07 ff ff 80 00
            00 01 ff ff 80 00 23 07 c0 00 00 7f ff e0 00 00
            00 ff ff e0 00 00 03 ff f7 80 00 00 31 40 00 00
            07 ff ef 80 00 00 07 ff ff dc 00 00 00 10 00 00
            39 ff e0 00 00 00 38 77 c0 00 00 00 73 e6 08 00
            08 22 00 00 08 33 ff 00 00 00 03 ff ff c0 00 00
            01 78 00 00 07 ff f8 00 00 03 ff fc 00 00 00 9e
            fe 18 00 00 00 60 00 00 04 10 44 00 00 00 02 0f
            c0 3f 07 c3 9f 07 e0 07 80 7e 1f 78 7e 00 f8 1f
            c3 f8 7f 0e 3f 07 0f 03 f0 00 f0 e3 83 e0 78
        """
    ),
    "CH": bytes.fromhex(
        """
            f0 f8 03 c0 f8 e1 ff 07 87 87 c3 c3 0f e0 f1 c0
            fe 60 0f 80 f8 f8 7c 78 7c 70 f8 77 f0 c7 e0 7c
            7c 00 f8 83 f0 3f f0 c3 86 38 7e 1f 1e 7c 07 8e
            0f e0 fc 0f 0f 81 c7 c3 f1 c3 c7 e1 8f 03 ce 07
            ce 3c 78 3e 3c 71 c7 1e 38 7f 0f 3c 03 e0 f8 1e
            70 3e 1e 0f c3 c3 83 c1 cf 0f c0 fb 0c 78 1f 08
            ef 83 c0 ff 07 c0 f0 f8 3e 3c 3f 03 e0 f0 f8 78
            f3 87 e1 8f 38 7e 3f c3 98 78 78 1e 0f 00 78 60
            7c 31 cc 3f 9e 07 c6 03 e0 ff 03 fc 70 f8 78 fc
            1f e3 00 fc 3f 00 78 83 f0 3f e1 07 8e 38 ff 03
            e0 07 c3 80 1f 87 f8 f8 70 e0 3e 1e 1c 78 7c 0f
            83 3f 81 f0 7c 03 f0 fc 78 78 1e 31 f0 f1 e0 f8
            3f e0 3c 1f 0f 1f 0f 80 c7 80 fc 1e 1f 86 0f 87
            c3 81 e1 87 f8 78 31 e0 3c f0 7c 0e 03 fc 1f 87
            e1 c7 30 f3 1f e3 c7 8f 00 f8 07 ce 3c 7f 1c f1
            e0 fe 3c 3c 43 c1 e0 f0 e3 0f c0 fe 30 e3 81 c3
            c1 e0 3c 78 78 8e 1c 38 fe 1c 7c 78 78 7c 03 ff
            1f 07 80 3b e0 c7 f0 07 ce 03 c3 0f 80 0f c0 70
            8e 1f c1 9f 00 3c e0 1f f0 ff 03 f8 e1 9e 01 f0
            83 c7 01 ef 07 3e 1c 1f c2 1f c3 39 ef 1c f0 1f
            83 00 f0 5f 0e 01 c3 c0 3f 98 3f 83 1f 00 39 e0
            0f 1e 1f 8e 1c 67 80 c7 06 f0 f0 c3 98 70 e1 c2
            1c 71 c1 8f 01 f0 f3 f0 7e f0 f8 1f c3 83 f0 18
            f8 3f 03 8f 07 e0 e1 e2 01 f1 c1 f3 00 7e 00 f8
            01 f1 81 ff 03 07 8f 80 e1 e3 e1 83 f8 01 f7 81
            f1 83 ff 0f 0e 1e 38 1f 9c 03 8f 80 7c fc c0 7e
            0f 1c 1e 3f 00 30 1f 80 f0 01 f0 3c 78 20 07 e3
            83 0f 1e 00 ce 60 3e 3e 07 c0 03 c0 fc 70 01 fc
            00 7c 00 0f 07 0f 00 00 f1 81 e0 1c e1 00 73 e0
            01 f0 71 e0 3d f0 61 fc 00 3f e0 00 78 f8 f0 3f
            c0 0e 60 0f 80 00 70 00 00 78 e0 38 f0 ff 06 1f
            01 0f 07 18 73 0c 38 3e 0f 01 fc 00 3f 00 00 00
            0c 00 03 80 e0 e0 1e 70 00 20 c2 00 ff c0 03 fe
            10 04 c3 80 00 ff 00 0f 19 00 0f c0 03 f0 00 07
            81 e0 0e 0f 02 1e 3c 1f f0 c1 f0 71 fe 07 c0 f8
            1e 1f 00 1f 83 df 07 87 00 cf 0f 1c 3e 07 03
        """
    ),
    "SH": bytes.fromhex(
        """
            c4 3e 1e 3c 3f 03 e0 0f e0 f8 7c 1f 03 f0 3f 07
            fc 0f fe 07 f0 7c 00 7c 1f c1 f0 f8 1f 83 c1 c3
            c0 cf e0 c3 e0 fe 0e 3c 03 c7 80 f0 03 c3 80 3e
            08 7e 0f c1 c0 fe 0f f0 3c 78 1f 83 ff 03 fe 01
            f7 03 f0 e3 f0 01 f0 7f 00 fe 00 fe 01 fe 18 3c
            70 fc 0e 7c 3f 38 3c 7c 03 f0 01 f0 03 f0 07 f0
            3f f0 3e e0 0f 80 ff 80 fe 07 3c 3c 3e 03 e1 ce
            1f 03 e0 cf 38 3f 83 8f 83 0f 80 7e 10 f0 f0 71
            c3 e0 3e 1c 07 87 80 1e 1e 38 e0 e1 e0 cf 0f c1
            ff 07 81 f8 3f 07 07 fe 0f ce 0f 07 30 e1 e0 e1
            e1 1f 07 07 83 fc 3c 3c 38 7c 1f 83 c0 00 f8 1f
            07 07 87 1e 07 c0 1e 1f 01 ff 80 c1 e0 fe 03 3e
            60 7f 00 e1 f0 7e 0f 1f 07 9e 00 ff 0e 1f 00 f8
            3c 3f 03 f0 1f c3 83 f8 0f c0 0f e0 1f 8f 0f 80
            70 e0 f8 10 f8 11 f8 0f c0 1e 3c 0f 0f 0f 81 f8
            c0 ff 80 3e 1e 01 f8 11 f0 1f 03 c7 0e 0f f0 7c
            40 fe 0f 0f 07 1f 0f c1 e0 f1 c0 fc 07 c6 0c 7c
            30 fc 03 f0 78 7c 1c 7c 1f 00 78 f8 1f f8 61 e1
            c0 7e 07 c0 03 f0 31 f8 3f 80 ff 87 87 e0 7c 3c
            0f c0 fc 07 8f 03 f0 03 fc 0f 83 83 e1 e1 f8 3f
            1c 01 f0 7e 07 0f c0 7f 01 f8 01 f0 78 f0 41 f0
            70 f0 3c 78 38 e3 07 1e 1c 1f 01 e1 83 f0 c3 e0
            7f e0 f8 f8 07 e0 f0 e1 c3 c1 f3 c0 f8 3f 0f 07
            83 c3 c0 ff 03 e0 07 e0 7f 00 3c 78 78 3d e0 f0
            f8 0f f0 07 e0 78 7c 1f 80 1f 07 0f 80 7f 81 e1
            e0 0f c1 07 c0 ff 00 f8 3c 03 e0 f8 7c 03 8f 07
            83 f0 ff 0c 70 3f 0f 0f 80 78 e1 c0 f0 70 fc 1c
            1f 1e 38 f8 78 7c 3c 1e 70 e1 f0 f3 83 8e 38 60
            f0 79 e0 fc 1e 3c 61 f0 73 c0 1e 3c 1f 01 f0 f1
            c3 c1 f0 00 7f c1 ff 80 3c 3c 7f 03 e0 f8 78 3f
            81 e0 f0 7f c0 fe 00 f0 e0 07 81 fc 03 e0 f0 7c
            0e 3c 3e 07 c0 73 c3 fc 0f f8 78 7c 1f 80 f8 07
            0f 83 f0 78 0f e0 fc 03 8f 07 87 c0 f8 e0 1f 07
            f0 f8 7e 38 3f 00 3f 81 9f 81 fe 00 fc 03 f0 fe
            ef 79 cf 73 9c f0 00 00 00 00 00 00 00 00 00 38
            e1 ff 9e ff bf ff fb ff ff ff 1c f3 80 0e 30
        """
    ),
    "TZ": bytes.fromhex(
        """
            8e 40 64 20 87 19 ff f8 ff 7c ef 9e f3 9f ff 3c
            e3 00 00 00 00 00 00 00 00 00 0f 0c 7d f7 ef f7
            ff df ef f7 ff c7 fc c0 1e 00 3e 18 80 20 03 84
            e7 3f be e7 ff e3 7f 9c ff 39 ee 00 00 00 00 00
            00 00 01 00 01 80 3f ff ff f3 ff dd ff bd ff e7
            3f e0 03 06 1c c4 61 00 18 c8 77 f3 1e f1 fc e7
            73 fc fe e3 9e 00 00 00 00 00 00 00 00 80 02 3e
            1f ff ff fe f3 ff ff f7 3f f9 e7 f8 80 82 03 73
            00 00 08 fc 61 ff 9e fc e7 b8 ef fe f3 cf cf e0
            00 00 00 00 00 00 00 00 00 0f c7 ff 3f ff ff ff
            cf 7f df 9c e7 fc 00 70 83 e3 10 86 00 7e 38 fc
            7e f3 9f cf 1f bf 1f fe ff 78 00 00 00 00 00 00
            00 00 00 46 78 ff f3 df 8f ff f7 ff bf ef 73 cf
            20 06 00 7c 20 31 80 c7 30 c7 ee e7 3c ff f1 fe
            f3 fc fe fc c0 00 00 00 00 00 00 00 20 00 c1 8f
            ff 7f ff 9c ff bf ff ff f9 99 e0 c0 61 80 ee 02
            38 30 7e 33 dc c7 ff 3f 9c e7 7f 33 c3 8f e6 00
            00 00 00 00 00 00 01 00 07 07 1f bf ff fd f7 de
            ff ff ff 79 fc e0 01 81 07 00 04 00 61 f3 79 8f
            9c f0 fd f6 dc e6 e7 1f 7e fc 00 00 00 00 00 00
            00 00 01 01 ec ff fb ff cf ff 9c e7 f9 ff fc c1
            80 03 00 1f 00 00 c2 03 e3 1f f1 ff fc f3 8e 7f
            73 b9 cf 3e e0 00 00 00 00 00 00 00 00 10 70 ed
            ff ff ff ff ff fc ef ff e3 8f 8c 80 0e 30 f9 c0
            00 00 0f 63 0f 38 df 1c ff f7 3f cf 7e f3 7e 00
            00 00 00 00 00 00 01 c0 03 e0 1e f3 ff ff ff f8
            fe f3 9c ec 7b 8c 02 00 07 20 03 00 00 f1 87 f7
            3b be ff f7 3f fc ce 7b 9e fc 00 10 00 00 00 00
            00 03 00 0e 30 ff f3 ff cf ff ff fe 7c f3 b9 79
            80 07 00 33 00 71 8c 60 c3 cf 73 bc ce 79 fe 3f
            f7 1e fc e7 20 00 00 00 00 00 00 00 60 61 01 bf
            df 7f ff ff ff cf fb 9f ef 77 63 00 18 01 c7 00
            30 18 de 73 7d 8f 9e fe ff 8f 9f 0f f3 87 fc 00
            00 00 00 00 00 00 01 80 03 0e 7f ff ff ff ff c7
            37 b3 9c 73 98 e3 86 40 c6 80 38 30 8e 70 e7 1d
            87 39 bc c6 71 e3 11 c7 1c f3 01 ce 64 31 ce
        """
    ),
    "TH": bytes.fromhex(
        """
            60 e2 31 c6 18 e7 87 00 80 0c 63 1c e7 79 c3 e0
            c0 00 0c 70 c3 e7 8e 60 0e 78 38 70 e1 30 c1 c3
            39 9c 3e 78 f1 ce c7 1c 1c 0f 1c 7e 78 d1 c7 07
            ce 3e 39 99 f8 e3 b1 cd 8e 39 ce 66 18 f8 c7 38
            ce 18 e3 8c e1 c3 81 c7 18 c3 38 1c 71 c0 f0 c7
            38 ce 38 70 0c c6 33 88 0e 70 30 c7 67 18 c3 39
            9c e3 1c ce 71 88 0c 3c 61 f1 8f ff 8e 70 3c 70
            c1 81 0e 23 1c 4e 70 61 81 86 03 00 00 38 03 c3
            87 c7 87 1e 0e 7c f1 f1 8e 73 9f cf 1e 3b 9c f0
            c1 f3 1c e3 1c cc 78 70 f1 8e 0c 87 30 18 e1 88
            7c 33 ce 38 38 61 83 0e 01 98 00 ce 31 cc 8f 07
            0f 38 37 1c e1 c3 78 f1 8c 38 70 c1 c3 9c 8e 4d
            1c 60 38 ce 72 1c 70 01 c7 c3 03 c7 0f 51 f1 98
            e3 e0 dc 71 8e 70 38 c6 30 c7 0c 03 82 00 c7 1c
            39 9f 82 01 06 70 38 00 00 01 b9 c7 fc f3 9e 67
            ff ff bd fc e7 c7 cf 79 9e 33 38 c4 63 0c e3 1c
            c6 7d e6 0f 70 78 e6 6f 38 e3 00 02 08 73 9c e7
            f3 7f 8f 1c 61 80 e1 08 e3 1e fc 33 8e 7e 70 e7
            10 8c 00 0e 3c 62 00 c7 01 c6 38 cc 71 80 f1 c6
            10 66 38 c7 3c c6 73 18 3c 30 f8 63 91 30 c7 39
            8c 67 39 cf e3 99 8e 71 c8 e3 18 c3 03 00 0e 70
            02 1c 1c c3 c3 1c 78 71 c1 e7 39 c7 f0 78 7c 79
            19 c6 39 c7 1e 23 06 33 38 f1 cf 71 8c 71 38 3c
            e7 38 07 31 84 03 8c 18 60 e1 c6 7f 87 39 8e 06
            18 e3 81 c7 78 f4 78 f0 c8 87 1c 0e 38 1c 71 18
            c3 08 03 0f 3f f9 c7 39 c6 73 9c e4 38 7e 38 8e
            63 1e 06 71 86 e3 80 c3 11 8c 00 0e 07 04 06 30
            c1 e7 3d e1 c6 77 38 38 78 30 dc 61 ce 33 1c e2
            38 ec e3 1c e3 30 e0 c3 01 c7 38 39 99 39 87 c1
            c7 18 c6 63 9c e7 3e 38 71 ce 23 0f 1e 79 01 99
            c1 c7 83 8c 78 f0 e0 38 78 0e 0f 8e 38 c7 c7 0e
            e6 33 8e c0 e3 1c 70 0e 39 8f 0e 1c c3 e7 81 e3
            82 30 20 7c 78 71 63 87 0e 63 1e 3c 71 f8 e7 38
            c2 e3 19 8e 71 8c c7 39 3f c7 39 8e 30 ce 70 00
            f8 3f e1 ff f7 8f ff c1 fc 0f 01 e3 c0 ff 01 c1
            e6 0f f0 03 f8 3f 00 3f 00 ff 80 7f f0 3f c0
        """
    ),
    "ZH": bytes.fromhex(
        """
            7f 81 ff 06 1f 00 7c 00 0e 01 e0 03 c7 f8 3f fe
            3f fc 3f 07 de 1e 06 3c 07 83 80 fc 00 ff 87 1e
            3c 7c 7c 3f 07 80 7c 38 3c 20 f8 3f 00 18 07 c0
            01 c0 f0 03 e0 07 e0 3f c1 ff e0 7f e0 fc 7c 1c
            c0 1f c0 3f 80 0c 3e 1e 0f c0 fc 3f c0 1e 38 03
            f0 3f f0 78 f8 e0 fe 07 80 f8 00 3c 0f 00 07 80
            1f 88 1f fe 7f fc 7f f0 1f 87 03 e0 c0 f0 c3 c0
            83 e0 fe 07 c7 0f c0 7c 7c 38 ff 03 fe 07 80 7c
            1f 00 1c 00 f0 03 c0 00 00 40 01 fc 0f c1 ff 0f
            ff 07 fe 03 f8 0f f8 03 f0 00 fc 07 1e 01 e3 c0
            ff 00 ff c0 f8 3c 7c 80 1f 07 80 f8 f0 03 e0 00
            f0 03 00 07 00 0f f0 7c 7f f3 ff 1f e0 3f 87 80
            3f c0 0f c0 71 f8 18 f0 1f e0 fc 70 f0 7c 1c e7
            87 1f 07 8f 81 ff e0 78 01 80 20 00 00 03 e0 07
            fe 3c 0f fc 7e 3f e0 1f 80 f8 03 f8 01 ff 80 7f
            07 83 f0 f8 fe 1f 00 39 f0 0f 80 3f 03 e3 c0 7f
            e0 0f 80 f0 00 86 00 00 78 00 fc 07 f1 ff c0 ff
            0f fc 3f c0 f3 83 c0 e1 c0 03 e1 c1 8f 83 e0 fc
            1f e3 07 87 1e 3e 0c 3e 07 e0 e1 c0 0f c0 3f 00
            00 00 c0 00 03 e0 07 ff e3 ff 0f cf c1 f8 07 e0
            7f c0 e3 c0 7f 0c 3f 00 fc 0f 8e 1f 3c c1 ff 03
            e7 c0 ff 00 ff 00 3f 80 3f 80 3f 00 ff 01 ff 01
            ff fe 1f fe 70 f8 3f 81 f8 70 03 fe 07 f0 00 7c
            38 78 f8 3f e0 f0 f9 c0 fe 07 ff 03 f0 1f 83 00
            fc 00 fe 01 c0 07 c0 3f 00 fc 3f e3 ff fb f0 7f
            c0 0f e0 00 01 fc 07 ff c0 0f fc 03 f8 0f f0 07
            e0 f7 c1 e1 ff 80 fe 01 f0 1f c0 00 00 00 3f 80
            1f c0 3f 07 ff 1f bf c0 3f 8f e0 07 f0 60 7f 00
            ff e0 1f 0f 07 0f 9c 3e f0 7e 03 c3 e0 86 fc 07
            e0 f8 00 7e 00 38 00 00 c0 00 00 ff 01 ff fe 0f
            ff 03 fe f0 7c fc 1e 00 7e 00 fe 00 3f 00 f8 7e
            3e f0 f0 70 f3 83 c0 f8 78 03 f0 e0 07 f0 07 f0
            00 e0 00 00 01 ff 80 ff 81 ff f0 ff e7 e0 3f f0
            03 8f 01 c1 ef 00 7f f0 3f c1 ff c0 ff 00 3f 53
            70 65 65 63 68 20 62 79 20 41 6e 64 79 20 43 2e
            20 4d 63 47 75 69 72 65 20 43 6f 70 79 72 69
        """
    ),
}


def _validate_phoneme_data() -> None:
    if tuple(PHONEME_DATA) != PHONEME_NAMES:
        raise ValueError("The phoneme inventory is out of order")

    invalid_lengths = {
        name: len(data)
        for name, data in PHONEME_DATA.items()
        if len(data) != PHONEME_BYTES
    }
    if invalid_lengths:
        raise ValueError(f"Unexpected phoneme data lengths: {invalid_lengths}")


_validate_phoneme_data()

phonemes_dictionary: dict[str, bytes] = {
    "space": bytes(PHONEME_BYTES),
    **PHONEME_DATA,
}
