# Gulistan Digitization & Publishing Pipeline

This specification documents the complete, reproducible process for digitizing Sheikh Saadi Shirazi's *Gulistan* from Maulana Qazi Sajjad Husain's 1967 Fatehpuri Delhi lithograph edition (*Gulistan-e-Mutarjam*, Maktaba Rahmaniya, Lahore) into dual web editions (`study.html` & `original.html`) and EPUB 3 e-books.

---

## 🎯 Core Principles

1. **Authenticity First:** The original book page layout (running header with book page number in Urdu numerals, double *jadwal* frame, side-by-side couplets with emerald divider, interlinear Urdu translation, and collected bottom footnotes with `[۱؎]`, `[۲؎]`) must be **100% visible by default**.
2. **Unobtrusive Scaffolding:** Modern pedagogical additions (English translation, English grammar notes, Urdu linguistic commentary, and vocabulary analysis tables) must be **tucked into collapsible drawers** (`▾ English Notes & Translation 🇬🇧`), never cluttering the classical reading experience.
3. **Visual Collation as Ground Truth:** High-resolution scans from `Gulistan-ur.pdf` serve as the immutable ground truth for all text, diacritics (*i'rāb*), and footnote markings.

---

## 🔁 Step-by-Step Batch Workflow

### Step 1: High-Resolution Page Rasterization
Extract and render PDF pages at 2x scale (~144 DPI) for optical collation:
```bash
swift render_page.swift <start_pdf_page> <end_pdf_page>
```
Images will be saved to `pages/page_XXX.png`.

### Step 2: Transcription & Annotation (`data/batch_XX_*.json`)
Create the structured JSON for the 10-page batch adhering to the schema:
* `batch_info`: `batch_id`, `pages_pdf`, `pages_book`, `title_ur`, `title_en`.
* `sections`: Array of sections containing:
  * `section_id`, `title_ur`, `title_en`, `content_type` (`"bilingual_text"` or `"urdu_essay"` or `"metadata"`).
  * `entries`:
    * `id`: Unique identifier (e.g. `entry_p11_01`).
    * `book_page`: Printed lithograph page number (integer).
    * `pdf_page`: PDF page number (integer).
    * `type`: `"prose"`, `"couplet"`, `"stanza"`, `"quran"`, or `"bismillah"`.
    * `persian` / `persian_m1` / `persian_m2`: Full Persian Nastaliq with complete diacritics/erab matching the lithograph.
    * `urdu_interlinear` / `urdu_m1` / `urdu_m2`: Word-for-word interlinear Urdu matching the lithograph.
    * `footnotes`: Array of verbatim Urdu footnotes from the bottom of the page frame.
    * `english_trans`: Scholarly, elegant literary English translation.
    * `study`:
      * `notes_en`: Morphological, syntactical, and historical commentary in English.
      * `notes_ur`: Linguistic commentary on Persian idioms and rhetoric in Urdu.
      * `vocabulary`: Array of `{ persian, grammar, meaning_en, meaning_ur, urdu_cognates }`.

### Step 3: Automated Validation
Run the validator to assert schema conformance, bilingual symmetry, and footnote referential integrity:
```bash
python3 scripts/verify_batch.py data/batch_XX_*.json
```

### Step 4: Visual Collation (Ground Truth Audit)
Cross-examine each transcribed line against the rasterized page scan (`pages/page_XXX.png`):
* Confirm vocalization diacritics match the lithograph.
* Confirm interlinear Urdu matches line by line.
* Confirm footnote markers in the text correspond to the numbered footnotes at the foot of the page.

### Step 5: Dual-Edition Build & Synchronization
Compile both HTML editions and EPUB 3 archives:
```bash
python3 src/build.py
```
This updates:
* `dist/html/original.html` & `docs/original.html`
* `dist/html/study.html` & `docs/study.html`
* `dist/Gulistan_Original.epub` & `docs/Gulistan_Original.epub`
* `dist/Gulistan_Study_Edition.epub` & `docs/Gulistan_Study_Edition.epub`

### Step 6: WebKit Visual Verification
Render headless browser snapshots of newly compiled pages using `scripts/snapshot_pages.swift` and inspect with `view_file` to verify font metrics, couplet balance, and drawer behavior:
```bash
swift scripts/snapshot_pages.swift dist/html/study.html page_11 page_18
```

### Step 7: Git Commit & GitHub Pages Deployment
```bash
git add -A
git commit -m "feat: digitize batch XX (pages XX-XX)"
git push origin main
```
Verify live deployment at `https://ushafqat.github.io/gulistan/`.
