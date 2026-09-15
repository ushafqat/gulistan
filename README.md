# گُلِسْتَانِ سَعْدِیْ (The Rose Garden of Saadi)
### Dual-Edition Digital Transcription & Study System (فارسی مع اردو ترجمہ و تسہیل)

🌐 **Live Web Reader on GitHub Pages:** **[https://ushafqat.github.io/gulistan/](https://ushafqat.github.io/gulistan/)**

This repository contains the complete digitized, transcribed, and annotated edition of **Sheikh Saadi Shirazi's *Gulistan*** based on the celebrated subcontinent edition translated and annotated by **Maulana Qazi Sajjad Husain** (formerly Head Teacher, Madrasah Aliya Fatehpuri, Delhi).

---

## 📊 Transcription Progress Dashboard (Front & Center)

| Metric | Current Progress | Details |
| :--- | :---: | :--- |
| **PDF Pages** | **`40 / 284` (14.1%)** | PDF pages 1–40 rendered and verified |
| **Book Pages** | **`38 / ~280`** | Book Pages 1–38 transcribed with complete Persian *i'rāb* |
| **Active Landmark** | **بَابِ اَوَّلْ: دَرْ سِیْرَتِ پَادْشَاہَاں** | Chapter 1 Hikayats 1 to 7 complete (Pages 25–38) |
| **Preceding Milestone** | **دِیْبَاجَہ (Author's Preface)** | **100% COMPLETE** (Pages 5–24, 8 Chapters Catalog & 656 AH Date) |
| **Historical Footnotes** | **`60` footnotes** | Fully collated against the 1967 Fatehpuri Delhi lithograph |
| **Vocabulary Database** | **`300` terms** | Grammatical analysis, English, Urdu meanings & Urdu cognates |
| **Batch Verification** | **4 / 4 Batches (100%)** | Validated via `scripts/verify_batch.py` with **0 errors** |

### 🧭 Chapter-by-Chapter Status

| # | Chapter / Section | Book Pages | Status | Contents Completed |
| :-: | :--- | :---: | :---: | :--- |
| — | **سرورق و تعارفِ کتاب** (Frontispiece & Title) | Page 1 | ✅ **100% Complete** | Monumental title calligraphy & publication cartouche |
| — | **پیش لفظ — سوانح حیات حضرت شیخ سعدیؒ** (Foreword) | Pages 1–4 | ✅ **100% Complete** | Complete biography of Saadi by Maulana Qazi Sajjad Husain |
| ۰ | **دِیْبَاجَہ** (Author's Preface) | Pages 5–24 | ✅ **100% Complete** | Hamd, Na'at, Genesis of Gulistan, 8 Chapters Index, 656 AH Date |
| ۱ | **باب اول: در سیرتِ پادشاہاں** (Manners of Kings) | Pages 25–38+ | 🔄 **In Progress (Pages 25–38)** | **Hikayats 1 through 7 complete** (14 book pages transcribed) |
| ۲ | **باب دوم: در اخلاقِ درویشاں** (Morals of Dervishes) | — | ⏳ *Planned* | Next upcoming milestone |
| ۳ | **باب سوم: در فضیلتِ قناعت** (Excellence of Contentment) | — | ⏳ *Planned* | Planned |
| ۴ | **باب چہارم: در فوائدِ خاموشی** (Benefits of Silence) | — | ⏳ *Planned* | Planned |
| ۵ | **باب پنجم: در عشق و جوانی** (Love & Youth) | — | ⏳ *Planned* | Planned |
| ۶ | **باب ششم: در ضعف و پیری** (Weakness & Old Age) | — | ⏳ *Planned* | Planned |
| ۷ | **باب ہفتم: در تاثیرِ تربیت** (Effects of Education) | — | ⏳ *Planned* | Planned |
| ۸ | **باب ہشتم: در آدابِ صحبت** (Rules of Conduct) | — | ⏳ *Planned* | Planned |
| — | **خاتمہ کتاب** (Epilogue & Concluding Verses) | — | ⏳ *Planned* | Planned |

### 📦 Completed Batches

* ✅ **Batch 1 (PDF 1–10 / Book 1–8)**: Frontispiece, Foreword (Saadi's biography), and Opening of *Dībācha* (Hamd, Na'at, Divine Mercy).
* ✅ **Batch 2 (PDF 11–20 / Book 9–18)**: *Dībācha* continuation (Mystical ecstasy, Praise of Atabak Abu Bakr ibn Sa'd, The Garden metaphor, and Genesis of the work).
* ✅ **Batch 3 (PDF 21–30 / Book 19–28)**: *Dībācha* conclusion (Dedication to Fakhr al-Din, Eight Chapters catalog, 656 AH date) + **Chapter 1 Inception** (Hikayats 1, 2, and start of 3).
* ✅ **Batch 4 (PDF 31–40 / Book 29–38)**: **Chapter 1 Continuation** (Hikayat 3 conclusion, Hikayat 4 young brigand, Hikayat 5 profligate heir, Hikayat 6 tyrannical king, and Hikayat 7 panicked slave).

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
├── data/                           # Master source of truth (validated JSON batches)
│   ├── batch_01_pages_001_010.json # Book pages 1–8 (Frontispiece, Foreword, Hamd, Na'at)
│   ├── batch_02_pages_011_020.json # Book pages 9–18 (Dibacha, Atabak, Genesis)
│   ├── batch_03_pages_021_030.json # Book pages 19–28 (Dibacha end, Chapter 1 Hikayats 1-3)
│   └── batch_04_pages_031_040.json # Book pages 29–38 (Chapter 1 Hikayats 3-7)
├── docs/                           # GitHub Pages static site root (auto-synced)
│   ├── index.html
│   ├── original.html
│   ├── study.html
│   ├── style.css
│   ├── settings.js
│   ├── fonts/
│   └── images/
├── fonts/                          # Noto Naskh Arabic & Mehr Nastaliq fonts
├── pages/                          # Reference PDF page renders (PNG) & OCR cache
├── scripts/
│   ├── verify_batch.py             # Schema validator & collation checker
│   ├── snapshot_pages.swift        # Headless WebKit visual collation tester
│   └── build_batch_*.py            # Automated extraction scripts
├── src/
│   ├── build.py                    # Dual-edition compiler & docs syncer
│   ├── epub_packager.py            # EPUB3 generator with font/cover embedding
│   └── settings.js                 # Reader settings controller
├── render_page.swift               # Native PDF renderer
└── README.md
```

### Verification & Schema Validation
All batch JSON datasets are rigorously validated against the project schema:
```bash
python3 scripts/verify_batch.py
```

### Recompiling & Syncing
To compile changes into HTML, EPUBs, and sync to `docs/` for GitHub Pages:
```bash
python3 src/build.py
```
