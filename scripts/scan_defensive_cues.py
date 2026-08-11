#!/usr/bin/env python3
"""Create a candidate register from a DOCX without making editorial decisions.

The output is a cue list, not a diagnosis. Review every row in paragraph and
source context before assigning KEEP, TIGHTEN, REFRAME, RELOCATE, CUT, or QUERY.
"""

from __future__ import annotations

import argparse
import csv
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


W_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

CUE_PATTERNS = {
    "D1_self_deprecation": re.compile(
        r"\b(?:regrettably|unfortunately|sadly|merely|falls?\s+short|fails?\s+to|"
        r"lags?\s+behind|unable\s+to|cannot\s+(?:match|support|show|demonstrate))\b",
        re.IGNORECASE,
    ),
    "D2_preemptive_defence": re.compile(
        r"\b(?:we\s+do\s+not\s+claim|this\s+(?:article|paper|study)\s+does\s+not|"
        r"it\s+should\s+be\s+noted|this\s+is\s+not\s+to\s+say|one\s+might\s+object|"
        r"not\s+intended\s+to|not\s+designed\s+to)\b",
        re.IGNORECASE,
    ),
    "D3_hedge_cluster": re.compile(
        r"\b(?:may|might|could|perhaps|possibly|potentially|appears?\s+to|tends?\s+to|"
        r"suggest(?:s|ed)?)\b(?:[\w,;:\-\s]{0,72})\b(?:may|might|could|perhaps|possibly|"
        r"potentially|appears?\s+to|tends?\s+to|suggest(?:s|ed)?)\b",
        re.IGNORECASE,
    ),
    "D4_work_log": re.compile(
        r"\b(?:we\s+first|initially|then\s+tried|later\s+tried|eventually\s+found|"
        r"after\s+several\s+attempts|经过多次尝试|我们先|后来|最终)\b",
        re.IGNORECASE,
    ),
    "D6_comparison_concession": re.compile(
        r"\b(?:does\s+not\s+outperform|weaker\s+than|outperformed\s+by|"
        r"cannot\s+compete|performs?\s+worse|明显落后|效果有限|未能超过)\b",
        re.IGNORECASE,
    ),
}


def paragraph_text(paragraph: ET.Element) -> str:
    """Return visible Word text, excluding deletion text in tracked documents."""
    return "".join(node.text or "" for node in paragraph.iter(W_NS + "t")).strip()


def paragraph_style(paragraph: ET.Element) -> str:
    ppr = paragraph.find(W_NS + "pPr")
    if ppr is None:
        return ""
    style = ppr.find(W_NS + "pStyle")
    return "" if style is None else style.get(W_NS + "val", "")


def reference_like(text: str) -> str:
    """Flag a likely bibliography entry without suppressing it automatically."""
    compact = " ".join(text.split())
    looks_like_entry = bool(
        re.match(r"^[A-Z][A-Za-z'’\-]+, .{0,180}\b(?:18|19|20)\d{2}\. ", compact)
    )
    return "yes" if looks_like_entry else "no"


def iter_paragraphs(docx_path: Path):
    with zipfile.ZipFile(docx_path) as archive:
        xml = archive.read("word/document.xml")
    root = ET.fromstring(xml)
    for index, paragraph in enumerate(root.iter(W_NS + "p"), start=1):
        text = paragraph_text(paragraph)
        if text:
            yield index, paragraph_style(paragraph), text


def snippet(text: str, start: int, end: int, width: int = 280) -> str:
    left = max(0, start - width // 2)
    right = min(len(text), end + width // 2)
    prefix = "…" if left else ""
    suffix = "…" if right < len(text) else ""
    return prefix + text[left:right].strip() + suffix


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Export defensive-writing cue candidates from a DOCX; no candidate is an edit decision."
    )
    parser.add_argument("docx", type=Path, help="Clean DOCX preferred; tracked DOCX may contain both baseline and insertion text.")
    parser.add_argument("--out", required=True, type=Path, help="Destination CSV path.")
    args = parser.parse_args()

    if args.docx.suffix.lower() != ".docx" or not args.docx.is_file():
        parser.error("docx must name an existing .docx file")
    args.out.parent.mkdir(parents=True, exist_ok=True)

    fields = [
        "issue_id",
        "paragraph_id",
        "word_style",
        "reference_like",
        "pattern_code",
        "matched_cue",
        "candidate_text",
        "provisional_disposition",
        "integrity_note",
        "reviewer_decision",
    ]
    rows = []
    for index, style, text in iter_paragraphs(args.docx):
        for pattern_code, pattern in CUE_PATTERNS.items():
            for match in pattern.finditer(text):
                rows.append(
                    {
                        "issue_id": f"C{len(rows) + 1:03d}",
                        "paragraph_id": f"P{index:03d}",
                        "word_style": style,
                        "reference_like": reference_like(text),
                        "pattern_code": pattern_code,
                        "matched_cue": match.group(0),
                        "candidate_text": snippet(text, match.start(), match.end()),
                        "provisional_disposition": "REVIEW_REQUIRED",
                        "integrity_note": "Cue only; test evidence status, scope, rival role, and claim ceiling.",
                        "reviewer_decision": "",
                    }
                )

    with args.out.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} cue candidates to {args.out}")
    print("No editorial decision was made. Review every candidate in context.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
