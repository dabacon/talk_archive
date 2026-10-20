#!/usr/bin/env python3
"""
Repair legacy PowerPoint (.ppt) files (Office 97-2004):
1. Repairs Symbol font Private Use Area (U+F020..U+F0FF) characters in UTF-16LE
   TextCharsAtom (0x0FA0) records so modern macOS QuickLook renders math symbols
   (|0⟩, |1⟩, ⊗, →, ⇒, ≡, α, β, ψ, φ, σ, etc.) instead of missing-glyph boxes (□).
2. Repairs embedded Equation Editor 3.0 WMF metafiles (OfficeArtBlipWMF 0xF01A / 0xF01B)
   that reference the missing 'MT Extra' font, mapping 'MT Extra' -> 'Symbol' and
   translating MT Extra glyph codes (\cdots 'K', \hbar 'h'/'g', underbrace '14243',
   \mapsto ';', \vec 'r') into standard Symbol font codes so no [?] boxes appear.
"""

import re
import struct
import sys
import zlib
from pathlib import Path

# Adobe Symbol encoding (0x20..0xFF) mapped from Microsoft PUA (0xF020..U+F0FF) to standard BMP Unicode
SYMBOL_PUA_MAP = {
    0xF022: "\u2200",  # forall
    0xF024: "\u2203",  # exists
    0xF027: "\u220B",  # suchthat
    0xF02A: "\u2217",  # asteriskmath
    0xF02D: "\u2212",  # minus
    0xF040: "\u2245",  # congruent
    0xF044: "\u0394",  # Delta
    0xF046: "\u03A6",  # Phi
    0xF047: "\u0393",  # Gamma
    0xF04C: "\u039B",  # Lambda
    0xF050: "\u03A0",  # Pi
    0xF051: "\u0398",  # Theta
    0xF053: "\u03A3",  # Sigma
    0xF055: "\u03A5",  # Upsilon
    0xF057: "\u03A9",  # Omega
    0xF058: "\u039E",  # Xi
    0xF059: "\u03A8",  # Psi
    0xF061: "\u03B1",  # alpha
    0xF062: "\u03B2",  # beta
    0xF063: "\u03C7",  # chi
    0xF064: "\u03B4",  # delta
    0xF065: "\u03B5",  # epsilon
    0xF066: "\u03C6",  # phi
    0xF067: "\u03B3",  # gamma
    0xF068: "\u03B7",  # eta
    0xF069: "\u03B9",  # iota
    0xF06A: "\u03D5",  # phi1
    0xF06B: "\u03BA",  # kappa
    0xF06C: "\u03BB",  # lambda
    0xF06D: "\u03BC",  # mu
    0xF06E: "\u03BD",  # nu
    0xF06F: "\u03BF",  # omicron
    0xF070: "\u03C0",  # pi
    0xF071: "\u03B8",  # theta
    0xF072: "\u03C1",  # rho
    0xF073: "\u03C3",  # sigma
    0xF074: "\u03C4",  # tau
    0xF075: "\u03C5",  # upsilon
    0xF076: "\u03D6",  # omega1
    0xF077: "\u03C9",  # omega
    0xF078: "\u03BE",  # xi
    0xF079: "\u03C8",  # psi
    0xF07A: "\u03B6",  # zeta
    0xF07E: "\u223C",  # similar
    0xF0A3: "\u2264",  # lessequal
    0xF0A5: "\u221E",  # infinity
    0xF0AA: "\u2660",  # spade
    0xF0A7: "\u2663",  # club
    0xF0A8: "\u2666",  # diamond
    0xF0A9: "\u2665",  # heart
    0xF0AB: "\u2194",  # arrowboth
    0xF0AC: "\u2190",  # arrowleft
    0xF0AD: "\u2191",  # arrowup
    0xF0AE: "\u2192",  # arrowright
    0xF0AF: "\u2193",  # arrowdown
    0xF0B0: "\u00B0",  # degree
    0xF0B1: "\u00B1",  # plusminus
    0xF0B3: "\u2265",  # greaterequal
    0xF0B4: "\u00D7",  # multiply
    0xF0B5: "\u221D",  # proportional
    0xF0B6: "\u2202",  # partialdiff
    0xF0B7: "\u2022",  # bullet
    0xF0B8: "\u00F7",  # divide
    0xF0B9: "\u2260",  # notequal
    0xF0BA: "\u2261",  # equivalence
    0xF0BB: "\u2248",  # approxequal
    0xF0BC: "\u2026",  # ellipsis
    0xF0C4: "\u2297",  # circlemultiply (tensor)
    0xF0C5: "\u2295",  # circleplus (direct sum)
    0xF0C6: "\u2205",  # emptyset
    0xF0C7: "\u2229",  # intersection
    0xF0C8: "\u222A",  # union
    0xF0CC: "\u2282",  # propersubset
    0xF0CD: "\u2286",  # reflexsubset
    0xF0CE: "\u2208",  # element
    0xF0CF: "\u2209",  # notelement
    0xF0D0: "\u2220",  # angle
    0xF0D1: "\u2207",  # gradient / nabla
    0xF0D5: "\u220F",  # product
    0xF0D6: "\u221A",  # radical
    0xF0D7: "\u22C5",  # dotmath
    0xF0D9: "\u2227",  # logicaland
    0xF0DA: "\u2228",  # logicalor
    0xF0DB: "\u21D4",  # arrowdblboth
    0xF0DC: "\u21D0",  # arrowdblleft
    0xF0DD: "\u21D1",  # arrowdblup
    0xF0DE: "\u21D2",  # arrowdblright
    0xF020: " ",       # space
    0xF04A: "\u263A",  # Wingdings J smiley
    0xF04B: "\u263A",  # Wingdings K neutral/smiley
    0xF05A: "Z",       # Z (integers)
    0xF094: "\u21D4",  # arrowdblboth
    0xF099: "\u2297",  # tensor product
    0xF0DF: "\u21D3",  # arrowdbldown
    0xF0E0: "\u2192",  # Wingdings rightarrow (0 -> 000, 1 -> 111)
    0xF0E1: "\u3008",  # angleleft / bra (〈)
    0xF0E5: "\u2211",  # summation
    0xF0E9: "\u2308",  # left ceiling (⌈)
    0xF0EA: "\u2192",  # Wingdings arrow
    0xF0EB: "\u230A",  # left floor (⌊)
    0xF0F1: "\u3009",  # angleright / ket (〉)
    0xF0F2: "\u222B",  # integral
    0xF0F9: "\u2309",  # right ceiling (⌉)
    0xF0FB: "\u230B",  # right floor (⌋)
}

# Map single-byte MT Extra character codes to single-byte Symbol font character codes
MT_EXTRA_TO_SYMBOL = {
    ord("K"): 0xBC,  # \cdots -> ellipsis (…)
    ord("L"): 0xBD,  # \vdots -> vertical bar
    ord("M"): 0xBC,  # \ddots -> ellipsis
    ord("O"): 0xBC,  # dots
    ord(";"): 0xAE,  # \mapsto -> \rightarrow (→)
    ord("h"): ord("h"),  # \hbar -> h
    ord("g"): ord("h"),  # \hbar -> h
    ord("f"): ord("h"),  # \hbar -> h
    ord("r"): 0x20,  # combining \vec arrow above char -> space (avoids box overlapping char)
    ord("s"): 0x20,  # combining \vec
    ord("t"): 0x20,  # combining \tilde
    ord("u"): 0x20,  # combining \hat
    ord("1"): 0xBE,  # underbrace left tip -> horizontal extender (⎯)
    ord("2"): 0xBE,  # underbrace middle cusp -> horizontal extender (⎯)
    ord("3"): 0xBE,  # underbrace right tip -> horizontal extender (⎯)
    ord("4"): 0xBE,  # underbrace bar -> horizontal extender (⎯)
    ord("5"): 0xBE,  # overbrace left tip -> horizontal extender
    ord("6"): 0xBE,  # overbrace middle -> horizontal extender
    ord("7"): 0xBE,  # overbrace right -> horizontal extender
    ord("8"): 0xBE,  # overbrace bar -> horizontal extender
    ord("{"): ord("{"),
    ord("}"): ord("}"),
    ord("("): ord("("),
    ord(")"): ord(")"),
    ord("["): ord("["),
    ord("]"): ord("]"),
}


def repair_wmf_bytes(raw: bytes) -> tuple:
    """
    In-place repair of uncompressed WMF metafile bytes that use 'MT Extra' font.
    Returns (repaired_wmf_bytes, count_fixed).
    """
    if b"MT Extra" not in raw:
        return raw, 0
    wh = raw.find(b"\x01\x00\x09\x00\x00\x03")
    if wh < 0:
        return raw, 0

    buf = bytearray(raw)
    p = wh + 18
    slots = {}
    cur_font = ""
    fixes = 0

    while p + 6 <= len(buf):
        sz_words, func = struct.unpack_from("<IH", buf, p)
        if sz_words < 3 or p + sz_words * 2 > len(buf):
            break
        rec_end = p + sz_words * 2
        if func in (0x02FB, 0x02FA, 0x02FC, 0x06FE, 0x0142):
            slot = 0
            while slot in slots:
                slot += 1
            if func == 0x02FB and p + 24 < rec_end:  # META_CREATEFONTINDIRECT
                name_off = p + 6 + 18
                fname_bytes = bytes(buf[name_off:rec_end]).split(b"\x00")[0]
                fname = fname_bytes.decode("latin1", errors="ignore")
                slots[slot] = fname
                if fname == "MT Extra" and name_off + 9 <= rec_end:
                    # Set lfCharSet (offset p + 6 + 13) to SYMBOL_CHARSET (2)
                    buf[p + 6 + 13] = 2
                    # Replace "MT Extra\x00" with "Symbol\x00\x00\x00"
                    buf[name_off : name_off + 9] = b"Symbol\x00\x00\x00"
                    fixes += 1
            else:
                slots[slot] = "other"
        elif func == 0x01F0 and p + 8 <= rec_end:  # META_DELETEOBJECT
            slot = struct.unpack_from("<H", buf, p + 6)[0]
            slots.pop(slot, None)
        elif func == 0x012D and p + 8 <= rec_end:  # META_SELECTOBJECT
            slot = struct.unpack_from("<H", buf, p + 6)[0]
            if slots.get(slot) not in (None, "other"):
                cur_font = slots[slot]
        elif func == 0x0A32 and cur_font == "MT Extra" and p + 14 <= rec_end:  # META_EXTTEXTOUT
            y, x, count, opts = struct.unpack_from("<hhHH", buf, p + 6)
            off = p + 14 + (8 if (opts & 0x06) else 0)
            if off + count <= rec_end:
                for i in range(count):
                    bval = buf[off + i]
                    buf[off + i] = MT_EXTRA_TO_SYMBOL.get(bval, 0xBC)
                fixes += 1
        elif func == 0x0521 and cur_font == "MT Extra" and p + 8 <= rec_end:  # META_TEXTOUT
            count = struct.unpack_from("<H", buf, p + 6)[0]
            off = p + 8
            if off + count <= rec_end:
                for i in range(count):
                    bval = buf[off + i]
                    buf[off + i] = MT_EXTRA_TO_SYMBOL.get(bval, 0xBC)
                fixes += 1
        p = rec_end

    return bytes(buf), fixes


def repair_ppt_bytes(data: bytes) -> tuple:
    """
    In-place byte-length-preserving repair of:
    1. UTF-16LE TextCharsAtom (0x0FA0) records (Symbol PUA U+F0xx -> standard Unicode)
    2. OfficeArtBlipWMF (0xF01A / 0xF01B) compressed WMF equation streams ('MT Extra' -> 'Symbol')
    Returns (repaired_bytes, num_replacements).
    """
    buf = bytearray(data)
    n = len(buf)
    replacements = 0

    # 1. Repair TextCharsAtom (0x0FA0)
    for m in re.finditer(b"[\x00-\xff][\x00-\xff]\xa0\x0f", data):
        idx = m.start()
        if idx + 8 > n:
            continue
        ver_inst, rec_type, rec_len = struct.unpack_from("<HHI", data, idx)
        if (ver_inst & 0x0F) != 0:
            continue
        if rec_len == 0 or rec_len > 32000 or rec_len % 2 != 0 or idx + 8 + rec_len > n:
            continue
        start = idx + 8
        end = start + rec_len
        for pos in range(start, end, 2):
            code = buf[pos] | (buf[pos + 1] << 8)
            if code in SYMBOL_PUA_MAP:
                new_ch = SYMBOL_PUA_MAP[code]
                new_code = ord(new_ch)
                buf[pos] = new_code & 0xFF
                buf[pos + 1] = (new_code >> 8) & 0xFF
                replacements += 1

    # 2. Repair OfficeArtBlipWMF (0xF01A / 0xF01B) equation metafiles
    for m in re.finditer(b"[\x1a\x1b]\xf0", data):
        idx = m.start() - 2
        if idx < 0 or idx + 8 + 50 > n:
            continue
        ver_inst, rec_type, rec_len = struct.unpack_from("<HHI", data, idx)
        if rec_type not in (0xF01A, 0xF01B):
            continue
        inst = ver_inst >> 4
        uid_len = 32 if (inst in (0x217, 0x3D5)) else 16
        hdr_off = idx + 8 + uid_len
        if hdr_off + 34 > n:
            continue
        cbSize, l, t, r, b, w, h, cbSave, comp, filt = struct.unpack_from("<IiiiiiiIBB", data, hdr_off)
        z_off = hdr_off + 34
        if comp == 0 and 0 < cbSave <= 500000 and z_off + cbSave <= n:
            z_bytes = bytes(buf[z_off : z_off + cbSave])
            try:
                raw = zlib.decompress(z_bytes)
                if b"MT Extra" in raw:
                    fixed_raw, wmf_fixes = repair_wmf_bytes(raw)
                    if wmf_fixes > 0:
                        recomp = zlib.compress(fixed_raw, 9)
                        if len(recomp) <= cbSave:
                            padded = recomp + b"\x00" * (cbSave - len(recomp))
                            buf[z_off : z_off + cbSave] = padded
                            replacements += wmf_fixes
            except Exception:
                pass

    return bytes(buf), replacements


if __name__ == "__main__":
    src = Path(sys.argv[1])
    dst = Path(sys.argv[2])
    repaired, count = repair_ppt_bytes(src.read_bytes())
    dst.write_bytes(repaired)
    print(f"Repaired {count} Symbol/WMF items in {src} -> {dst}")
