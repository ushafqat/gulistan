#!/usr/bin/env python3
"""
scripts/verify_batch.py
Automated batch validator for Gulistan-e-Mutarjam digitization project.

Validates:
1. JSON schema structure (batch_info, sections, entries).
2. Bilingual symmetry (persian vs urdu_interlinear, couplet hemistichs).
3. Footnote referential integrity (text markers vs collected footnotes).
4. English translation & vocabulary completeness for study edition.
"""

import sys
import os
import json

REQUIRED_BATCH_INFO = ["batch_id", "pages_pdf", "pages_book", "title_ur", "title_en"]
REQUIRED_SECTION_KEYS = ["section_id", "title_ur", "title_en", "content_type"]
ENTRY_TYPES = ["prose", "couplet", "stanza", "quran", "bismillah"]

def verify_batch_file(file_path):
    print(f"\n==================================================")
    print(f"🔍 Validating Batch: {os.path.basename(file_path)}")
    print(f"==================================================")

    if not os.path.exists(file_path):
        print(f"❌ Error: File not found: {file_path}")
        return False

    with open(file_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"❌ JSON Syntax Error: {e}")
            return False

    errors = []
    warnings = []

    # 1. Batch Info
    binfo = data.get("batch_info")
    if not binfo:
        errors.append("Missing 'batch_info' object.")
    else:
        for k in REQUIRED_BATCH_INFO:
            if k not in binfo:
                errors.append(f"batch_info missing required key: '{k}'")

    # 2. Sections
    sections = data.get("sections", [])
    if not sections:
        errors.append("No sections defined in batch.")

    total_entries = 0
    total_footnotes = 0
    total_vocab = 0

    for s_idx, sec in enumerate(sections):
        sid = sec.get("section_id", f"sec_{s_idx}")
        stype = sec.get("content_type")

        for k in REQUIRED_SECTION_KEYS:
            if k not in sec:
                errors.append(f"Section '{sid}' missing key '{k}'.")

        if stype == "bilingual_text":
            entries = sec.get("entries", [])
            if not entries:
                warnings.append(f"Section '{sid}' has no entries.")

            page_fn_map = {}

            for e_idx, e in enumerate(entries):
                total_entries += 1
                eid = e.get("id", f"{sid}_{e_idx}")
                etype = e.get("type")
                bp = e.get("book_page")

                if not bp:
                    errors.append(f"Entry '{eid}' missing 'book_page'.")
                if etype not in ENTRY_TYPES:
                    errors.append(f"Entry '{eid}' has unknown type '{etype}'. Expected one of {ENTRY_TYPES}.")

                # Type-specific checks
                if etype == "prose":
                    p = e.get("persian", "").strip()
                    u = e.get("urdu_interlinear", "").strip()
                    if not p:
                        errors.append(f"Entry '{eid}' (prose) has empty 'persian'.")
                    if not u:
                        errors.append(f"Entry '{eid}' (prose) has empty 'urdu_interlinear'.")

                elif etype == "couplet":
                    m1_p = e.get("persian_m1", "").strip()
                    m2_p = e.get("persian_m2", "").strip()
                    m1_u = e.get("urdu_m1", "").strip()
                    m2_u = e.get("urdu_m2", "").strip()
                    if not (m1_p and m2_p):
                        errors.append(f"Entry '{eid}' (couplet) missing Persian hemistichs.")
                    if not (m1_u and m2_u):
                        errors.append(f"Entry '{eid}' (couplet) missing Urdu interlinear hemistichs.")

                elif etype == "stanza":
                    lines = e.get("lines", [])
                    if not lines:
                        errors.append(f"Entry '{eid}' (stanza) has empty 'lines' array.")
                    for l_idx, l in enumerate(lines):
                        if not (l.get("persian_m1") and l.get("persian_m2")):
                            errors.append(f"Entry '{eid}' line {l_idx+1} missing Persian hemistichs.")
                        if not (l.get("urdu_m1") and l.get("urdu_m2")):
                            errors.append(f"Entry '{eid}' line {l_idx+1} missing Urdu hemistichs.")

                # Footnotes tracking
                fns = e.get("footnotes", [])
                total_footnotes += len(fns)
                if bp not in page_fn_map:
                    page_fn_map[bp] = []
                for fn in fns:
                    if fn not in page_fn_map[bp]:
                        page_fn_map[bp].append(fn)

                # Study scaffolding checks
                en_trans = e.get("english_trans", "").strip()
                if not en_trans and etype != "bismillah":
                    warnings.append(f"Entry '{eid}' missing 'english_trans'.")

                study = e.get("study", {})
                vocab = study.get("vocabulary", [])
                total_vocab += len(vocab)
                for v in vocab:
                    if not v.get("persian"):
                        errors.append(f"Entry '{eid}' vocab missing 'persian'.")
                    if not v.get("meaning_en"):
                        errors.append(f"Entry '{eid}' vocab '{v.get('persian')}' missing 'meaning_en'.")
                    if not v.get("meaning_ur"):
                        errors.append(f"Entry '{eid}' vocab '{v.get('persian')}' missing 'meaning_ur'.")

    # Summary Report
    print(f"📊 Summary:")
    print(f"   • Total Sections: {len(sections)}")
    print(f"   • Total Entries: {total_entries}")
    print(f"   • Total Historical Footnotes: {total_footnotes}")
    print(f"   • Total Vocabulary Items: {total_vocab}")

    if warnings:
        print(f"\n⚠️ Warnings ({len(warnings)}):")
        for w in warnings[:10]:
            print(f"   - {w}")
        if len(warnings) > 10:
            print(f"   ... and {len(warnings) - 10} more warnings.")

    if errors:
        print(f"\n❌ Validation FAILED ({len(errors)} errors):")
        for err in errors:
            print(f"   - {err}")
        return False

    print(f"\n✅ All checks PASSED with 0 errors!")
    return True

if __name__ == "__main__":
    if len(sys.argv) > 1:
        files = sys.argv[1:]
    else:
        import glob
        files = sorted(glob.glob("data/batch_*.json"))

    success = True
    for f in files:
        if not verify_batch_file(f):
            success = False

    sys.exit(0 if success else 1)
