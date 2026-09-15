# گُلِسْتَانِ سَعْدِیْ (The Rose Garden of Saadi)
### Dual-Edition Digital Transcription & Study System (فارسی مع اردو ترجمہ و تسہیل)

🌐 **Live Web Reader on GitHub Pages:** **[https://ushafqat.github.io/gulistan/](https://ushafqat.github.io/gulistan/)**

This repository contains the complete digitized, transcribed, and annotated edition of **Sheikh Saadi Shirazi's *Gulistan*** based on the celebrated subcontinent edition translated and annotated by **Maulana Qazi Sajjad Husain** (formerly Head Teacher, Madrasah Aliya Fatehpuri, Delhi).

---

## 🌟 Features & Visual Design

* **Authentic Historical Calligraphy & Artwork:** Directly incorporates the authentic calligraphic title (*گُلِسْتَانِ مُتَرْجَمْ*), frontispiece plate, and repeating rosette mosaic border from the original 1967 Fatehpuri Delhi lithograph edition.
* **Interactive Typography & Settings Drawer (`⚙️ ترتیبات`):**
  * **Urdu Fonts:** Choose between **مہر نستعلیق (Mehr Nastaliq)** (authentic compact calligraphy), **نوٹو نستعلیق (Noto Nastaliq)**, and **نوٹو نسخ (Noto Naskh)**.
  * **Persian Fonts:** Choose between **عمیری نسخ (Amiri)**, **نوٹو نسخ (Noto Naskh)**, and **ہم آہنگ خط (Match Urdu)**.
  * **Font Scaling:** One-click sizing (`A-`, `100%`, `A+`, `A++`).
  * **4 Reading Themes:** **سبز سرورق (Cover Emerald - Default)**, **کاغذی (Parchment Light)**, **کتابی (Classic Sepia)**, and **شبینہ (Night Dark)**.
  * **Instant Persistence:** Settings remember your preference across reloads and across pages via `localStorage`.

---

## 📖 Editions Produced

This publishing pipeline automatically compiles two complementary editions:

1. **Faithful Original Edition ([Web Reader](https://ushafqat.github.io/gulistan/original.html) | [Download EPUB](https://ushafqat.github.io/gulistan/Gulistan_Original.epub))**:
   - 100% faithful reproduction of the original printed scan.
   - Fully vocalized Persian text (*i'rāb* preserved).
   - Qazi Sajjad Husain's word-for-word and idiomatic Urdu interlinear translation.
   - Original footnotes (*ḥawāshī*).

2. **Extended Study Edition ([Web Reader](https://ushafqat.github.io/gulistan/study.html) | [Download EPUB](https://ushafqat.github.io/gulistan/Gulistan_Study_Edition.epub))**:
   - Designed specifically for readers who know Urdu and want to learn/understand classical Persian literature.
   - **Vocabulary Tables:** Every Persian word parsed with its grammatical category, English meaning, Urdu meaning, and **Urdu Cognates (*mushtarak alfāẓ*)** so you can leverage your Urdu vocabulary.
   - **Grammar & Syntax:** Explanations of classical Persian constructions (*mar ... rā*, archaic prepositions, subjunctive verbs, contractions like *kaz* and *kardast*).
   - **Literary & Contextual Notes:** In both English and modern Urdu.

---

## 📱 E-Reader & Apple Books Support

Both EPUB3 editions (`dist/Gulistan_Original.epub` and `dist/Gulistan_Study_Edition.epub`) feature:
* **Embedded Authentic Cover Art:** Appears automatically in the Apple Books shelf and on the title page.
* **Embedded Noto Naskh Arabic Font (Regular & Bold):** Displays crisp, perfectly rendered Arabic/Persian/Urdu text offline natively across Apple Books, Kindle, Kobo, and e-readers without baseline clipping or distortion.
* **RTL Reading Order:** Full IDPF EPUB3 compliance with RTL page progression and EPUB2 NCX fallback.

---

## 🛠️ Architecture & Build System

```
Gulistan/
├── assets/                         # Source cover scan and extracted calligraphic assets
│   ├── cover.jpg
│   └── processed/
│       ├── border_ribbon.png       # Authentic illuminated rosette ribbon
│       ├── cover_full.jpg          # Full cover art
│       ├── frontispiece_plate.png  # Inner frontispiece plate
│       ├── publisher_cartouche.png # Original publisher box
│       └── title_calligraphy.png   # Transparent monumental title calligraphy
├── data/                           # Master source of truth (JSON batches)
│   └── batch_01_pages_001_010.json
├── docs/                           # GitHub Pages static site root (auto-synced)
│   ├── index.html
│   ├── original.html
│   ├── study.html
│   ├── style.css
│   ├── settings.js
│   ├── fonts/
│   └── images/
├── fonts/                          # Mehr Nastaliq web fonts (WOFF & TTF)
├── pages/                          # Reference PDF page renders (PNG)
├── src/
│   ├── build.py                    # Dual-edition compiler & docs syncer
│   ├── epub_packager.py            # Standalone EPUB3 generator with font/cover embedding
│   └── settings.js                 # Reader settings controller
├── render_page.swift               # Native PDF renderer
└── README.md
```

### Recompiling & Syncing
To compile changes into HTML, EPUB, and sync to `docs/` for GitHub Pages:
```bash
python3 src/build.py
```

---

## 📊 Progress & Milestones

- [x] **Batch 1 (Pages 1–10 / Book pages 1–8)**:
  - Page 1: Title page and authentic frontispiece.
  - Page 2: Front matter endleaf.
  - Pages 3–6 (Book 1–4): Maulana Qazi Sajjad Husain's *Pesh Lafẓ* (Foreword and Saadi's complete biography).
  - Pages 7–10 (Book 5–8): Opening of Saadi's *Dībādīchah* (Doxology, Inhalation/Exhalation reflection, Providence, Allegory of Spring, Prophetic Praise, and Divine Grace toward penitents).
- [ ] **Batch 2 (Pages 11–20)**: Continuation of Saadi's *Dībādīchah* and the reason for composing *Gulistan*.
