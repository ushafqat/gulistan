# گُلِسْتَانِ سَعْدِیْ (The Rose Garden of Saadi)
### Dual-Edition Digital Transcription & Study System (فارسی مع اردو ترجمہ و تسہیل)

This repository contains the complete digitized, transcribed, and annotated edition of **Sheikh Saadi Shirazi's *Gulistan*** based on the celebrated subcontinent edition translated and annotated by **Maulana Qazi Sajjad Husain** (formerly Head Teacher, Madrasah Aliya Fatehpuri, Delhi).

---

## 📖 Editions Produced

This pipeline automatically compiles two complementary editions:

1. **Faithful Original Edition (`dist/html/original.html` & `dist/Gulistan_Original.epub`)**:
   - 100% faithful reproduction of the original printed scan.
   - Vocalized Persian text (*i'rāb* preserved).
   - Qazi Sajjad Husain's word-for-word and idiomatic Urdu interlinear translation.
   - Original footnotes (*ḥawāshī*).

2. **Extended Study Edition (`dist/html/study.html` & `dist/Gulistan_Study_Edition.epub`)**:
   - Designed specifically for readers who know Urdu and want to learn/understand classical Persian literature.
   - **Vocabulary Tables:** Every Persian word parsed with its grammatical category, English meaning, Urdu meaning, and **Urdu Cognates (*mushtarak alfāẓ*)** so you can leverage your Urdu vocabulary.
   - **Grammar & Syntax:** Explanations of classical Persian constructions (*mar ... rā*, archaic prepositions, subjunctive verbs, contractions like *kaz* and *kardast*).
   - **Literary & Contextual Notes:** In both English and modern Urdu.

---

## 🚀 How to View the Output

### 1. View in Browser (HTML Readers)
Both HTML editions feature beautiful RTL typography (Google Fonts *Noto Nastaliq Urdu* and *Amiri*):
- **Original Edition:** Open `dist/html/original.html` in Safari or Chrome.
- **Study Edition:** Open `dist/html/study.html` in Safari or Chrome.

### 2. View on E-Readers (Apple Books, Kindle, Kobo, Calibre)
The EPUB3 files are located in `dist/`:
- `dist/Gulistan_Original.epub`
- `dist/Gulistan_Study_Edition.epub`

On macOS, you can double-click either `.epub` file to immediately open it in **Apple Books**.

---

## 🛠️ Architecture & How It Works

```
Gulistan/
├── Gulistan-ur.pdf                 # Scanned source PDF (284 pages)
├── render_page.swift               # Native Swift tool to render any PDF page to PNG
├── pages/                          # Reference page scans (page_001.png ... page_010.png)
├── data/                           # Master source of truth
│   └── batch_01_pages_001_010.json # Batch 1 structured data
├── src/
│   ├── build.py                    # Main compiler script
│   └── epub_packager.py            # Self-contained zero-dependency EPUB3 generator
├── dist/                           # Generated publication outputs
│   ├── html/
│   │   ├── original.html
│   │   ├── study.html
│   │   └── style.css
│   ├── Gulistan_Original.epub
│   └── Gulistan_Study_Edition.epub
└── README.md
```

### Recompiling After Adding Pages
To recompile the entire project after adding or editing data batches:
```bash
python3 src/build.py
```

### Rendering Additional PDF Pages for Transcription
To render any range of pages from the PDF:
```bash
swift -module-cache-path .cache render_page.swift <start_page> [end_page]
```
For example, to render pages 11 through 20:
```bash
swift -module-cache-path .cache render_page.swift 11 20
```

---

## 📊 Progress & Milestones

- [x] **Batch 1 (Pages 1–10 / Book pages 1–8)**:
  - Page 1: Title page and publication metadata.
  - Page 2: Front matter endleaf.
  - Pages 3–6 (Book 1–4): Maulana Qazi Sajjad Husain's *Pesh Lafẓ* (Foreword and Saadi's complete biography).
  - Pages 7–10 (Book 5–8): Opening of Saadi's *Dībādīchah* (Doxology, Inhalation/Exhalation reflection, Providence, Allegory of Spring, Prophetic Praise, and Divine Grace toward penitents).
- [ ] **Batch 2 (Pages 11–20)**: Continuation of Saadi's *Dībādīchah* and the reason for composing *Gulistan*.
