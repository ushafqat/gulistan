#!/usr/bin/env python3
"""
src/build.py
Compiler script for Gulistan editions:
- Ingests data/*.json
- Compiles dist/html/original.html (Faithful Edition web reader)
- Compiles dist/html/study.html (Extended Study Edition web reader)
- Compiles dist/html/style.css
- Compiles dist/Gulistan_Original.epub (EPUB 3 with embedded cover & font)
- Compiles dist/Gulistan_Study_Edition.epub (EPUB 3 with embedded cover & font)
- Syncs complete static site to docs/ for instant GitHub Pages deployment
"""

import os
import glob
import json
import re
import shutil
from epub_packager import EpubBook, escape_xml

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
DIST_DIR = os.path.join(PROJECT_ROOT, "dist")
HTML_DIR = os.path.join(DIST_DIR, "html")
DOCS_DIR = os.path.join(PROJECT_ROOT, "docs")
FONTS_DIR = os.path.join(PROJECT_ROOT, "fonts")
ASSETS_DIR = os.path.join(PROJECT_ROOT, "assets/processed")

HTML_FONTS_DIR = os.path.join(HTML_DIR, "fonts")
HTML_IMAGES_DIR = os.path.join(HTML_DIR, "images")

os.makedirs(HTML_DIR, exist_ok=True)
os.makedirs(HTML_FONTS_DIR, exist_ok=True)
os.makedirs(HTML_IMAGES_DIR, exist_ok=True)
os.makedirs(DOCS_DIR, exist_ok=True)

def copy_assets():
    """Copy fonts, processed cover art, and scripts to dist/html/"""
    # 1. Fonts
    if os.path.exists(FONTS_DIR):
        for fname in os.listdir(FONTS_DIR):
            src_f = os.path.join(FONTS_DIR, fname)
            if os.path.isfile(src_f):
                shutil.copy2(src_f, os.path.join(HTML_FONTS_DIR, fname))
    
    # 2. Images (Cover art & calligraphy)
    if os.path.exists(ASSETS_DIR):
        for fname in os.listdir(ASSETS_DIR):
            src_f = os.path.join(ASSETS_DIR, fname)
            if os.path.isfile(src_f):
                shutil.copy2(src_f, os.path.join(HTML_IMAGES_DIR, fname))

    # 3. Settings script
    settings_src = os.path.join(os.path.dirname(__file__), "settings.js")
    if os.path.exists(settings_src):
        shutil.copy2(settings_src, os.path.join(HTML_DIR, "settings.js"))

def sync_to_docs():
    """Sync built web reader and epubs to docs/ for GitHub Pages"""
    os.makedirs(DOCS_DIR, exist_ok=True)
    # Copy html dist contents
    for item in os.listdir(HTML_DIR):
        s = os.path.join(HTML_DIR, item)
        d = os.path.join(DOCS_DIR, item)
        if os.path.isdir(s):
            if os.path.exists(d):
                shutil.rmtree(d)
            shutil.copytree(s, d)
        else:
            shutil.copy2(s, d)
    
    # Copy EPUB files to docs so they are downloadable on GitHub Pages
    for epub_file in glob.glob(os.path.join(DIST_DIR, "*.epub")):
        shutil.copy2(epub_file, os.path.join(DOCS_DIR, os.path.basename(epub_file)))

    # Create index.html in docs that points to study.html
    index_html = """<!DOCTYPE html>
<html lang="ur" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0; url=study.html" />
  <title>گُلِسْتَانِ سَعْدِیْ</title>
</head>
<body>
  <p>صفحہ منتقل ہو رہا ہے... <a href="study.html">یہاں کلک کریں</a></p>
</body>
</html>"""
    with open(os.path.join(DOCS_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)
    
    # Add .nojekyll to prevent GitHub Pages from ignoring folders
    with open(os.path.join(DOCS_DIR, ".nojekyll"), "w") as f:
        f.write("")

def load_batches():
    batch_files = sorted(glob.glob(os.path.join(DATA_DIR, "batch_*.json")))
    batches = []
    for f in batch_files:
        with open(f, "r", encoding="utf-8") as fp:
            batches.append(json.load(fp))
    return batches

def generate_css():
    css = """/* Gulistan Dual-Edition Stylesheet */
@import url('https://fonts.googleapis.com/css2?family=Amiri:ital,wght@0,400;0,700;1,400&family=Noto+Nastaliq+Urdu:wght@400;700&family=Noto+Naskh+Arabic:wght@400;500;600;700&family=Noto+Sans+Arabic:wght@400;600;700&family=Inter:wght@400;500;600;700&display=swap');

@font-face {
    font-family: 'Mehr Nastaliq';
    src: url('fonts/Mehr_Nastaliq.woff') format('woff'),
         url('fonts/Mehr_Nastaliq.ttf') format('truetype');
    font-weight: normal;
    font-style: normal;
    font-display: swap;
}

:root {
    /* 1. Default Theme: سبز سرورق (Cover Emerald) */
    --bg-main: #edf5ef;
    --bg-card: #ffffff;
    --border-color: #c4ded0;
    --border-jadwal: #165c32;
    --text-primary: #121815;
    --text-secondary: #4a5c52;
    --accent-emerald: #165c32;
    --accent-gold: #9e6b18;
    --accent-crimson: #ad2020;
    --persian-color: #0b3c5d;
    --urdu-color: #1a221e;
    --shadow-soft: 0 4px 20px rgba(22, 92, 50, 0.07);
    --banner-bg: #e2f0e6;
    --banner-border: #9ec8ab;
    --quote-bg: #f5faf6;
    --quote-border: #c8e2d2;
    --verse-bg: #f2f8f4;
    --interlinear-bg: #eaf4ed;
    --study-bg: #f8fbf9;
    --study-border: #cde4d6;
    --tag-bg: #e4f2e7;
    --tag-color: #185c31;
    --tag-border: #b8dec4;
    --ctrl-bg: #dcece1;
    --ctrl-bg-hover: #cde3d4;

    /* Typography settings */
    --font-urdu: 'Mehr Nastaliq', 'Noto Nastaliq Urdu', serif;
    --font-persian: 'Amiri', serif;
    --font-scale: 1.0;
    --line-height-urdu: 2.3;
    --urdu-size-offset: 1.05;
}

/* ============================================================
   DYNAMIC THEME & FONT ATTRIBUTES (Controlled by settings.js)
   ============================================================ */

/* Urdu Font Choices */
html[data-font-urdu="mehr"], body[data-font-urdu="mehr"] {
    --font-urdu: 'Mehr Nastaliq', 'Noto Nastaliq Urdu', serif;
    --line-height-urdu: 2.3;
    --urdu-size-offset: 1.05;
}
html[data-font-urdu="noto-nastaliq"], body[data-font-urdu="noto-nastaliq"] {
    --font-urdu: 'Noto Nastaliq Urdu', serif;
    --line-height-urdu: 2.5;
    --urdu-size-offset: 1.0;
}
html[data-font-urdu="noto-naskh"], body[data-font-urdu="noto-naskh"] {
    --font-urdu: 'Noto Naskh Arabic', serif;
    --line-height-urdu: 1.95;
    --urdu-size-offset: 0.95;
}

/* Persian Font Choices */
html[data-font-persian="amiri"], body[data-font-persian="amiri"] {
    --font-persian: 'Amiri', serif;
}
html[data-font-persian="noto-naskh"], body[data-font-persian="noto-naskh"] {
    --font-persian: 'Noto Naskh Arabic', serif;
}
html[data-font-persian="match-urdu"], body[data-font-persian="match-urdu"] {
    --font-persian: var(--font-urdu);
}

/* Font Size Scales */
html[data-size="sm"], body[data-size="sm"] { --font-scale: 0.88; }
html[data-size="md"], body[data-size="md"] { --font-scale: 1.0; }
html[data-size="lg"], body[data-size="lg"] { --font-scale: 1.16; }
html[data-size="xl"], body[data-size="xl"] { --font-scale: 1.32; }

/* 4 Themes */
html[data-theme="emerald"], body[data-theme="emerald"] {
    --bg-main: #edf5ef;
    --bg-card: #ffffff;
    --border-color: #c4ded0;
    --border-jadwal: #165c32;
    --text-primary: #121815;
    --text-secondary: #4a5c52;
    --accent-emerald: #165c32;
    --accent-gold: #9e6b18;
    --accent-crimson: #ad2020;
    --persian-color: #0b3c5d;
    --urdu-color: #1a221e;
    --shadow-soft: 0 4px 20px rgba(22, 92, 50, 0.07);
    --banner-bg: #e2f0e6;
    --banner-border: #9ec8ab;
    --quote-bg: #f5faf6;
    --quote-border: #c8e2d2;
    --verse-bg: #f2f8f4;
    --interlinear-bg: #eaf4ed;
    --study-bg: #f8fbf9;
    --study-border: #cde4d6;
    --tag-bg: #e4f2e7;
    --tag-color: #185c31;
    --tag-border: #b8dec4;
    --ctrl-bg: #dcece1;
    --ctrl-bg-hover: #cde3d4;
}

html[data-theme="light"], body[data-theme="light"] {
    --bg-main: #fbfaf6;
    --bg-card: #ffffff;
    --border-color: #e8e3d8;
    --border-jadwal: #145a32;
    --text-primary: #1d211f;
    --text-secondary: #59615d;
    --accent-emerald: #145a32;
    --accent-gold: #996515;
    --accent-crimson: #ad2020;
    --persian-color: #0b3c5d;
    --urdu-color: #212529;
    --shadow-soft: 0 4px 18px rgba(0,0,0,0.04);
    --banner-bg: #f1f8f3;
    --banner-border: #cce5d4;
    --quote-bg: #fbf9f4;
    --quote-border: #ebdcc5;
    --verse-bg: #f7f3ea;
    --interlinear-bg: #f8f6f0;
    --study-bg: #fdfbf7;
    --study-border: #ebdcc5;
    --tag-bg: #eef6ee;
    --tag-color: #256029;
    --tag-border: #d4ebd5;
    --ctrl-bg: #ece7db;
    --ctrl-bg-hover: #dfd9cb;
}

html[data-theme="sepia"], body[data-theme="sepia"] {
    --bg-main: #f5eedb;
    --bg-card: #fcf7e9;
    --border-color: #ded1b8;
    --border-jadwal: #195229;
    --text-primary: #2d261e;
    --text-secondary: #635748;
    --accent-emerald: #195229;
    --accent-gold: #8d5b12;
    --accent-crimson: #a61c1c;
    --persian-color: #173b52;
    --urdu-color: #2b251d;
    --shadow-soft: 0 4px 18px rgba(90, 70, 30, 0.05);
    --banner-bg: #eaf1e7;
    --banner-border: #bfd4be;
    --quote-bg: #efe8d5;
    --quote-border: #dfd4be;
    --verse-bg: #efe7d3;
    --interlinear-bg: #eee5cf;
    --study-bg: #f9f4e5;
    --study-border: #dfd4be;
    --tag-bg: #e2ede0;
    --tag-color: #215424;
    --tag-border: #c8dec4;
    --ctrl-bg: #e4dac3;
    --ctrl-bg-hover: #d7cbaf;
}

html[data-theme="dark"], body[data-theme="dark"] {
    --bg-main: #131615;
    --bg-card: #1c211f;
    --border-color: #2c3530;
    --border-jadwal: #254433;
    --text-primary: #e6e8e6;
    --text-secondary: #9ea8a2;
    --accent-emerald: #48a86c;
    --accent-gold: #d4a34b;
    --accent-crimson: #e06060;
    --persian-color: #6fb2e2;
    --urdu-color: #dcdedc;
    --shadow-soft: 0 4px 18px rgba(0, 0, 0, 0.35);
    --banner-bg: #18281f;
    --banner-border: #254433;
    --quote-bg: #202723;
    --quote-border: #3b453e;
    --verse-bg: #222925;
    --interlinear-bg: #232a26;
    --study-bg: #181d1b;
    --study-border: #2c3530;
    --tag-bg: #1a3222;
    --tag-color: #8edaa8;
    --tag-border: #2a4c35;
    --ctrl-bg: #262d29;
    --ctrl-bg-hover: #323b36;
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    -webkit-tap-highlight-color: transparent;
}

body {
    background-color: var(--bg-main);
    color: var(--text-primary);
    font-family: 'Inter', system-ui, -apple-system, sans-serif;
    line-height: 1.7;
    padding: 0;
    text-rendering: optimizeLegibility;
    -webkit-font-smoothing: antialiased;
    transition: background-color 0.25s ease, color 0.25s ease;
}

/* Site Header */
header.site-header {
    background: var(--bg-card);
    border-bottom: 1px solid var(--border-color);
    padding: 0.75rem 1.5rem;
    position: sticky;
    top: 0;
    z-index: 100;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 2px 10px rgba(0,0,0,0.03);
    transition: background-color 0.25s ease, border-color 0.25s ease;
}

.header-branding {
    display: flex;
    align-items: center;
    gap: 0.8rem;
}

.header-title {
    font-family: var(--font-urdu);
    font-size: 1.4rem;
    color: var(--accent-emerald);
    line-height: 1.4;
}

.header-subtitle {
    font-size: 0.8rem;
    color: var(--accent-gold);
    background: var(--quote-bg);
    border: 1px solid var(--quote-border);
    padding: 2px 8px;
    border-radius: 6px;
    font-weight: 600;
}

.header-controls {
    display: flex;
    align-items: center;
    gap: 0.6rem;
}

/* Nav Links - Segmented Pill Control */
.nav-links {
    display: flex;
    background: var(--ctrl-bg);
    padding: 3px;
    border-radius: 9px;
    gap: 3px;
    transition: background-color 0.25s ease;
}

.nav-links a {
    text-decoration: none;
    color: var(--text-secondary);
    font-size: 0.84rem;
    font-weight: 600;
    padding: 0.4rem 0.9rem;
    border-radius: 7px;
    transition: all 0.2s ease;
    white-space: nowrap;
}

.nav-links a.active {
    color: var(--accent-emerald);
    background: var(--bg-card);
    box-shadow: 0 1px 4px rgba(0,0,0,0.1);
}

.nav-links a:hover:not(.active) {
    color: var(--text-primary);
}

/* Settings Toggle Button */
.settings-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    background: var(--ctrl-bg);
    color: var(--text-primary);
    border: 1px solid var(--border-color);
    padding: 0.42rem 0.85rem;
    border-radius: 8px;
    font-size: 0.84rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s ease;
    font-family: inherit;
}

.settings-btn:hover {
    background: var(--ctrl-bg-hover);
    color: var(--accent-emerald);
}

.settings-btn svg {
    flex-shrink: 0;
}

.container {
    max-width: 860px;
    margin: 1.8rem auto;
    padding: 0 1.2rem;
}

/* ============================================================
   AUTHENTIC FRONTISPIECE & COVER PRESENTATION
   ============================================================ */
.frontispiece-card {
    background: var(--bg-card);
    border: 2px solid var(--border-jadwal);
    border-radius: 12px;
    padding: 1.2rem;
    margin-bottom: 2.2rem;
    box-shadow: var(--shadow-soft);
    position: relative;
    overflow: hidden;
    transition: background-color 0.25s ease, border-color 0.25s ease;
}

.frontispiece-jadwal {
    border: 1px solid var(--accent-gold);
    outline: 2px solid var(--border-jadwal);
    outline-offset: 3px;
    border-radius: 8px;
    padding: 1.4rem 1.6rem;
    background: var(--bg-card);
    text-align: center;
}

.frontispiece-ribbon-top, .frontispiece-ribbon-bottom {
    height: 22px;
    background-image: url('images/border_ribbon.png');
    background-repeat: repeat-x;
    background-size: auto 22px;
    border-radius: 4px;
    margin: 0 -0.5rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}

.frontispiece-ribbon-top {
    margin-bottom: 1.5rem;
}

.frontispiece-ribbon-bottom {
    margin-top: 1.8rem;
}

.calligraphy-hero {
    margin: 0.5rem 0 1.2rem;
}

.frontispiece-title-img {
    display: block;
    max-width: 440px;
    width: 92%;
    height: auto;
    margin: 0 auto;
    filter: drop-shadow(0 2px 5px rgba(0,0,0,0.06));
    transition: filter 0.25s ease;
}

body[data-theme="dark"] .frontispiece-title-img {
    filter: invert(0.92) hue-rotate(170deg) contrast(1.1) drop-shadow(0 2px 6px rgba(255,255,255,0.05));
}

.frontispiece-meta {
    margin-top: 1.2rem;
}

.fp-line {
    margin: 0.6rem 0;
    font-family: var(--font-urdu);
    line-height: 2.0;
}

.fp-role-label {
    font-size: 0.95rem;
    color: var(--text-secondary);
    margin-left: 0.4rem;
}

.fp-name {
    font-size: 1.4rem;
    font-weight: 700;
}

.fp-author-name {
    color: var(--accent-crimson);
}

.fp-trans-name {
    color: var(--accent-crimson);
}

.fp-badge {
    background: var(--tag-bg);
    color: var(--tag-color);
    font-size: 0.8rem;
    padding: 2px 8px;
    border-radius: 6px;
    border: 1px solid var(--tag-border);
    margin-right: 0.4rem;
}

.fp-inst {
    font-family: var(--font-urdu);
    font-size: 1.05rem;
    color: var(--text-secondary);
    margin: 0.3rem 0 1.2rem;
}

.frontispiece-cartouche {
    display: inline-block;
    background: var(--bg-card);
    border: 1.5px solid var(--accent-crimson);
    outline: 2px solid var(--accent-emerald);
    outline-offset: 2px;
    border-radius: 6px;
    padding: 0.5rem 1.6rem;
    margin: 0.8rem auto;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}

.cartouche-pub {
    font-family: var(--font-urdu);
    font-size: 1.35rem;
    font-weight: 700;
    color: var(--accent-crimson);
    line-height: 1.5;
}

.cartouche-detail {
    font-family: var(--font-urdu);
    font-size: 0.85rem;
    color: var(--text-primary);
    direction: rtl;
}

.frontispiece-actions {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 0.8rem;
    margin-top: 1.4rem;
}

.view-cover-btn, .download-epub-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: var(--ctrl-bg);
    color: var(--accent-emerald);
    border: 1px solid var(--border-color);
    padding: 0.55rem 1.1rem;
    border-radius: 8px;
    font-size: 0.86rem;
    font-weight: 600;
    cursor: pointer;
    text-decoration: none;
    transition: all 0.2s ease;
    font-family: inherit;
}

.view-cover-btn:hover, .download-epub-btn:hover {
    background: var(--ctrl-bg-hover);
    border-color: var(--accent-emerald);
    box-shadow: 0 2px 6px rgba(0,0,0,0.06);
}

/* Lightbox Modal for Scanned Cover */
.cover-lightbox {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0, 0.78);
    backdrop-filter: blur(6px);
    -webkit-backdrop-filter: blur(6px);
    z-index: 2000;
    display: flex;
    justify-content: center;
    align-items: center;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.25s ease;
    padding: 1.2rem;
}

.cover-lightbox.open {
    opacity: 1;
    pointer-events: auto;
}

.lightbox-content {
    position: relative;
    max-width: 580px;
    max-height: 92vh;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.lightbox-img {
    max-width: 100%;
    max-height: 82vh;
    border-radius: 10px;
    box-shadow: 0 12px 45px rgba(0,0,0,0.6);
    border: 2px solid #ffffff;
    object-fit: contain;
}

.lightbox-caption {
    color: #f1f8f3;
    margin-top: 0.7rem;
    font-family: var(--font-urdu);
    font-size: 1.05rem;
    text-align: center;
    direction: rtl;
}

.lightbox-close {
    position: absolute;
    top: -38px;
    right: 0;
    background: none;
    border: none;
    color: #ffffff;
    font-size: 2.2rem;
    cursor: pointer;
    line-height: 1;
}

/* Page Marker */
.page-marker {
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 2.5rem 0 1.5rem;
    color: var(--accent-gold);
    font-size: 0.85rem;
    font-weight: 600;
    letter-spacing: 0.5px;
}

.page-marker::before, .page-marker::after {
    content: "";
    flex: 1;
    border-bottom: 1px dashed var(--border-color);
    margin: 0 1rem;
}

/* Foreword / Urdu prose */
.foreword-article {
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 12px;
    padding: 2.2rem;
    margin-bottom: 2rem;
    box-shadow: var(--shadow-soft);
    transition: background-color 0.25s ease, border-color 0.25s ease;
}

.foreword-article h2 {
    font-family: var(--font-urdu);
    color: var(--accent-emerald);
    font-size: calc(1.85rem * var(--font-scale));
    text-align: center;
    margin-bottom: 1.5rem;
    line-height: 2.0;
    padding-bottom: 1rem;
    border-bottom: 1px dashed var(--border-color);
}

.khutbah-banner {
    text-align: center;
    background: var(--banner-bg);
    border: 1px solid var(--banner-border);
    border-radius: 10px;
    padding: 1.2rem 1rem;
    margin-bottom: 2rem;
    box-shadow: 0 1px 4px rgba(20,90,50,0.05);
}

.khutbah-arabic {
    font-family: var(--font-persian);
    font-size: calc(1.65rem * var(--font-scale));
    line-height: 2.2;
    color: var(--accent-emerald);
    font-weight: 700;
    direction: rtl;
}

.essay-subheading {
    font-family: var(--font-urdu);
    font-size: calc(1.45rem * var(--font-scale));
    color: var(--accent-emerald);
    line-height: 1.9;
    margin: 2.4rem 0 1rem;
    padding-right: 0.9rem;
    border-right: 4px solid var(--accent-crimson);
    display: flex;
    align-items: center;
    gap: 0.6rem;
}

.subheading-bullet {
    color: var(--accent-crimson);
    font-size: 1.1rem;
}

.urdu-prose {
    font-family: var(--font-urdu);
    font-size: calc(1.22rem * var(--font-scale) * var(--urdu-size-offset));
    line-height: var(--line-height-urdu);
    text-align: right;
    direction: rtl;
    color: var(--text-primary);
    margin-bottom: 1.3rem;
    word-spacing: 1px;
}

.essay-quote-box {
    background: var(--quote-bg);
    border: 1px solid var(--quote-border);
    border-right: 4px solid var(--accent-gold);
    border-radius: 8px;
    padding: 1.1rem 1.3rem;
    margin: 1.4rem 0;
}

.essay-quote-box .quote-text {
    font-family: var(--font-urdu);
    font-size: calc(1.18rem * var(--font-scale) * var(--urdu-size-offset));
    line-height: var(--line-height-urdu);
    color: var(--text-primary);
    text-align: right;
    direction: rtl;
}

.essay-verse-box {
    text-align: center;
    background: var(--verse-bg);
    border: 1px dashed var(--border-color);
    border-radius: 8px;
    padding: 1rem;
    margin: 1.4rem 0;
    font-family: var(--font-persian);
    font-size: calc(1.35rem * var(--font-scale));
    line-height: 2.2;
    color: var(--persian-color);
    direction: rtl;
}

.essay-persian-quote {
    text-align: center;
    background: var(--banner-bg);
    border: 1px solid var(--banner-border);
    border-radius: 8px;
    padding: 1.1rem;
    margin: 1.4rem 0;
    font-family: var(--font-persian);
    font-size: calc(1.6rem * var(--font-scale));
    line-height: 2.2;
    color: var(--persian-color);
    font-weight: 700;
    direction: rtl;
}

.essay-signature {
    margin-top: 3rem;
    padding-top: 1.5rem;
    border-top: 1px dashed var(--border-color);
    text-align: left;
    direction: rtl;
}

.sig-author {
    font-family: var(--font-urdu);
    font-size: calc(1.45rem * var(--font-scale));
    color: var(--accent-crimson);
    font-weight: 700;
    line-height: 1.8;
}

.sig-role {
    font-family: var(--font-urdu);
    font-size: calc(0.95rem * var(--font-scale));
    color: var(--text-secondary);
    line-height: 1.6;
    margin-top: 0.2rem;
}

.sig-date {
    font-size: 0.9rem;
    color: var(--accent-gold);
    font-weight: 600;
    margin-top: 0.4rem;
}

/* Bilingual Segment Blocks */
.segment-card {
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 12px;
    margin-bottom: 1.8rem;
    padding: 1.8rem;
    box-shadow: var(--shadow-soft);
    position: relative;
    transition: background-color 0.25s ease, border-color 0.25s ease;
}

.segment-badge {
    position: absolute;
    top: -11px;
    right: 18px;
    background: var(--accent-emerald);
    color: #fff;
    padding: 2px 10px;
    border-radius: 10px;
    font-size: 0.75rem;
    font-weight: 600;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

/* Persian typography */
.persian-text {
    font-family: var(--font-persian);
    font-size: calc(1.75rem * var(--font-scale));
    line-height: 2.3;
    color: var(--persian-color);
    direction: rtl;
    text-align: right;
    margin-bottom: 0.6rem;
    font-weight: 600;
}

/* Urdu interlinear */
.urdu-interlinear {
    font-family: var(--font-urdu);
    font-size: calc(1.2rem * var(--font-scale) * var(--urdu-size-offset));
    line-height: var(--line-height-urdu);
    color: var(--urdu-color);
    direction: rtl;
    text-align: right;
    padding: 0.55rem 0.9rem;
    background: var(--interlinear-bg);
    border-right: 3px solid var(--accent-gold);
    border-radius: 4px;
    margin-bottom: 1rem;
}

/* Verses / Couplets */
.couplet-container {
    text-align: center;
    margin: 1.2rem 0;
}

.couplet-header {
    display: inline-block;
    background: var(--ctrl-bg);
    color: var(--accent-emerald);
    border: 1px solid var(--border-color);
    font-weight: 700;
    padding: 2px 14px;
    border-radius: 10px;
    font-size: 0.8rem;
    margin-bottom: 0.6rem;
}

.verse-line {
    display: flex;
    justify-content: center;
    gap: 1.5rem;
    direction: rtl;
    margin-bottom: 0.5rem;
}

.verse-hemistich {
    flex: 1;
    min-width: 220px;
}

/* Quranic verse */
.quran-block {
    text-align: center;
    background: var(--banner-bg);
    border: 1px solid var(--banner-border);
    border-radius: 8px;
    padding: 1.2rem;
    margin: 1.2rem 0;
}

.quran-arabic {
    font-family: 'Amiri', serif;
    font-size: calc(1.7rem * var(--font-scale));
    line-height: 2.2;
    color: var(--accent-emerald);
    direction: rtl;
    margin-bottom: 0.5rem;
}

/* Footnotes */
.footnotes-box {
    margin-top: 1.2rem;
    padding-top: 0.9rem;
    border-top: 1px dashed var(--border-color);
    direction: rtl;
    text-align: right;
}

.footnote-title {
    font-size: 0.85rem;
    font-weight: 700;
    color: var(--accent-gold);
    margin-bottom: 0.4rem;
}

.footnote-item {
    font-family: var(--font-urdu);
    font-size: calc(1.05rem * var(--font-scale) * var(--urdu-size-offset));
    line-height: var(--line-height-urdu);
    color: var(--text-secondary);
    margin-bottom: 0.4rem;
    padding-right: 0.4rem;
}

/* Study layer (Interactive / Extended) */
.study-layer {
    margin-top: 1.3rem;
    padding: 1.1rem;
    background: var(--study-bg);
    border: 1px solid var(--study-border);
    border-radius: 8px;
    transition: background-color 0.25s ease;
}

.study-title {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-weight: 700;
    color: var(--accent-emerald);
    margin-bottom: 0.8rem;
    font-size: 0.9rem;
}

.study-notes-en {
    font-size: calc(0.92rem * var(--font-scale));
    color: var(--text-primary);
    margin-bottom: 0.8rem;
    line-height: 1.6;
}

.study-notes-ur {
    font-family: var(--font-urdu);
    font-size: calc(1.12rem * var(--font-scale) * var(--urdu-size-offset));
    line-height: var(--line-height-urdu);
    direction: rtl;
    text-align: right;
    color: var(--text-primary);
    margin-bottom: 1rem;
    background: var(--bg-card);
    padding: 0.75rem 0.9rem;
    border-radius: 6px;
    border-right: 3px solid var(--accent-emerald);
}

/* Vocabulary Table */
.vocab-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 0.8rem;
    font-size: calc(0.88rem * var(--font-scale));
}

.vocab-table th, .vocab-table td {
    padding: 8px 10px;
    border: 1px solid var(--border-color);
}

.vocab-table th {
    background: var(--ctrl-bg);
    color: var(--accent-emerald);
    font-weight: 600;
    text-align: left;
}

.vocab-persian {
    font-family: var(--font-persian);
    font-size: calc(1.25rem * var(--font-scale));
    font-weight: 700;
    color: var(--persian-color);
    direction: rtl;
    text-align: right;
}

.cognate-tag {
    display: inline-block;
    background: var(--tag-bg);
    color: var(--tag-color);
    padding: 2px 7px;
    border-radius: 4px;
    font-size: calc(0.78rem * var(--font-scale));
    font-weight: 600;
    margin: 2px;
    font-family: var(--font-urdu);
    border: 1px solid var(--tag-border);
}

footer.site-footer {
    text-align: center;
    padding: 2rem 1rem;
    color: var(--text-secondary);
    font-size: 0.85rem;
    border-top: 1px solid var(--border-color);
    margin-top: 3.5rem;
}

/* ============================================================
   SETTINGS DRAWER & MODAL STYLES
   ============================================================ */
.settings-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0, 0.48);
    backdrop-filter: blur(5px);
    -webkit-backdrop-filter: blur(5px);
    z-index: 1000;
    display: flex;
    justify-content: center;
    align-items: center;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.25s ease;
    padding: 1rem;
}

.settings-overlay.open {
    opacity: 1;
    pointer-events: auto;
}

.settings-modal {
    background: var(--bg-card);
    color: var(--text-primary);
    border: 1px solid var(--border-color);
    border-radius: 16px;
    width: 100%;
    max-width: 530px;
    max-height: 90vh;
    overflow-y: auto;
    box-shadow: 0 12px 40px rgba(0,0,0,0.22);
    transform: translateY(20px) scale(0.97);
    transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    direction: rtl;
}

.settings-overlay.open .settings-modal {
    transform: translateY(0) scale(1);
}

.settings-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.1rem 1.35rem;
    border-bottom: 1px solid var(--border-color);
}

.settings-header h3 {
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--accent-emerald);
    font-family: system-ui, -apple-system, sans-serif;
}

.settings-close-btn {
    background: none;
    border: none;
    font-size: 1.6rem;
    line-height: 1;
    color: var(--text-secondary);
    cursor: pointer;
    padding: 0.2rem 0.5rem;
    border-radius: 6px;
    transition: all 0.2s;
}

.settings-close-btn:hover {
    background: rgba(0,0,0,0.06);
    color: var(--text-primary);
}

.settings-body {
    padding: 1.25rem 1.35rem;
    display: flex;
    flex-direction: column;
    gap: 1.4rem;
}

.setting-group {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.setting-label {
    display: flex;
    flex-direction: column;
    gap: 0.15rem;
}

.label-title {
    font-size: 0.92rem;
    font-weight: 700;
    color: var(--text-primary);
}

.label-desc {
    font-size: 0.77rem;
    color: var(--text-secondary);
}

.segmented-options {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(110px, 1fr));
    gap: 0.5rem;
    background: var(--ctrl-bg);
    padding: 4px;
    border-radius: 10px;
    border: 1px solid var(--border-color);
}

.opt-btn {
    background: transparent;
    border: 1px solid transparent;
    border-radius: 8px;
    padding: 0.65rem 0.5rem;
    cursor: pointer;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 0.2rem;
    transition: all 0.2s ease;
    color: var(--text-secondary);
    font-family: inherit;
}

.opt-btn:hover {
    background: var(--ctrl-bg-hover);
    color: var(--text-primary);
}

.opt-btn.active {
    background: var(--bg-card);
    border-color: var(--accent-emerald);
    color: var(--accent-emerald);
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    font-weight: 600;
}

.font-sample {
    font-size: 1.15rem;
    line-height: 1.5;
}

.sample-mehr { font-family: 'Mehr Nastaliq', 'Noto Nastaliq Urdu', serif; }
.sample-noto-nastaliq { font-family: 'Noto Nastaliq Urdu', serif; }
.sample-noto-naskh { font-family: 'Noto Naskh Arabic', serif; }
.sample-amiri { font-family: 'Amiri', serif; }

.opt-btn small {
    font-size: 0.7rem;
    opacity: 0.85;
}

.theme-options {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 0.6rem;
}

.theme-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    padding: 0.7rem 0.5rem;
    border-radius: 9px;
    border: 1px solid var(--border-color);
    background: var(--bg-card);
    color: var(--text-primary);
    font-size: 0.82rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s;
    font-family: inherit;
}

.theme-btn:hover {
    border-color: var(--accent-emerald);
}

.theme-btn.active {
    border-color: var(--accent-emerald);
    outline: 2px solid var(--accent-emerald);
}

.theme-swatch {
    width: 15px;
    height: 15px;
    border-radius: 50%;
    border: 1px solid rgba(0,0,0,0.2);
}

.swatch-emerald { background: #edf5ef; border-color: #165c32; }
.swatch-light { background: #fbfaf6; border-color: #d6cfc4; }
.swatch-sepia { background: #f5eedb; border-color: #c9bc9e; }
.swatch-dark { background: #131615; border-color: #333; }

.settings-footer {
    padding: 0.85rem 1.35rem;
    border-top: 1px solid var(--border-color);
    display: flex;
    justify-content: flex-end;
}

.reset-btn {
    background: transparent;
    border: 1px dashed var(--border-color);
    color: var(--text-secondary);
    padding: 0.35rem 0.75rem;
    border-radius: 6px;
    font-size: 0.76rem;
    cursor: pointer;
    font-family: inherit;
    transition: all 0.2s;
}

.reset-btn:hover {
    border-color: var(--accent-emerald);
    color: var(--accent-emerald);
}

/* ============================================================
   MOBILE RESPONSIVENESS (< 640px)
   ============================================================ */
@media screen and (max-width: 640px) {
    header.site-header {
        flex-direction: column;
        align-items: stretch;
        gap: 0.7rem;
        padding: 0.75rem 0.9rem;
    }

    .header-branding {
        justify-content: space-between;
        width: 100%;
    }

    .header-title {
        font-size: 1.25rem;
    }

    .header-controls {
        width: 100%;
        justify-content: space-between;
    }

    .nav-links {
        flex: 1;
    }

    .nav-links a {
        flex: 1;
        text-align: center;
        padding: 0.42rem 0.5rem;
        font-size: 0.8rem;
    }

    .settings-btn {
        padding: 0.42rem 0.65rem;
        font-size: 0.8rem;
    }

    .container {
        margin: 1rem auto;
        padding: 0 0.75rem;
    }

    .frontispiece-card {
        padding: 0.75rem;
    }

    .frontispiece-jadwal {
        padding: 1rem 0.75rem;
    }

    .frontispiece-title-img {
        width: 95%;
        margin-bottom: 1rem;
    }

    .fp-name {
        font-size: 1.2rem;
    }

    .frontispiece-cartouche {
        padding: 0.4rem 1rem;
    }

    .cartouche-pub {
        font-size: 1.15rem;
    }

    .view-cover-btn, .download-epub-btn {
        width: 100%;
        justify-content: center;
        font-size: 0.82rem;
        padding: 0.5rem 0.75rem;
    }

    .foreword-article {
        padding: 1.25rem 0.95rem;
        border-radius: 10px;
        margin-bottom: 1.25rem;
    }

    .foreword-article h2 {
        font-size: calc(1.35rem * var(--font-scale));
        line-height: 1.8;
        margin-bottom: 1.2rem;
    }

    .khutbah-banner {
        padding: 0.85rem 0.6rem;
        margin-bottom: 1.3rem;
    }

    .khutbah-arabic {
        font-size: calc(1.35rem * var(--font-scale));
        line-height: 1.9;
    }

    .essay-subheading {
        font-size: calc(1.25rem * var(--font-scale));
        line-height: 1.7;
        margin: 1.8rem 0 0.8rem;
    }

    .urdu-prose {
        font-size: calc(1.15rem * var(--font-scale) * var(--urdu-size-offset));
        line-height: var(--line-height-urdu);
        margin-bottom: 1.1rem;
    }

    .essay-quote-box {
        padding: 0.8rem 0.9rem;
        margin: 1rem 0;
    }

    .essay-quote-box .quote-text {
        font-size: calc(1.08rem * var(--font-scale) * var(--urdu-size-offset));
        line-height: var(--line-height-urdu);
    }

    .essay-verse-box, .essay-persian-quote {
        font-size: calc(1.2rem * var(--font-scale));
        line-height: 2.0;
        padding: 0.8rem 0.6rem;
    }

    .segment-card {
        padding: 1.25rem 0.9rem;
        border-radius: 10px;
        margin-bottom: 1.25rem;
    }

    .segment-badge {
        top: -10px;
        right: 12px;
        font-size: 0.7rem;
        padding: 1px 8px;
    }

    .persian-text {
        font-size: calc(1.5rem * var(--font-scale));
        line-height: 2.1;
        margin-bottom: 0.5rem;
    }

    .urdu-interlinear {
        font-size: calc(1.1rem * var(--font-scale) * var(--urdu-size-offset));
        line-height: var(--line-height-urdu);
        padding: 0.5rem 0.75rem;
        margin-bottom: 0.8rem;
    }

    .verse-line {
        flex-direction: column;
        gap: 0.6rem;
    }

    .verse-hemistich {
        width: 100%;
        min-width: unset;
    }

    .verse-hemistich:last-child {
        padding-right: 0.5rem;
    }

    .quran-block {
        padding: 0.9rem;
    }

    .quran-arabic {
        font-size: calc(1.35rem * var(--font-scale));
        line-height: 1.9;
    }

    .study-layer {
        padding: 0.9rem 0.75rem;
    }

    .study-notes-ur {
        font-size: calc(1.05rem * var(--font-scale) * var(--urdu-size-offset));
        line-height: var(--line-height-urdu);
        padding: 0.6rem 0.75rem;
    }

    /* Transform Table to Cards on Small Mobile */
    .vocab-table thead {
        display: none;
    }

    .vocab-table, .vocab-table tbody {
        display: block;
        width: 100%;
    }

    .vocab-table tr {
        display: block;
        background: var(--bg-card);
        border: 1px solid var(--border-color);
        border-radius: 8px;
        padding: 0.75rem 0.85rem;
        margin-bottom: 0.75rem;
        box-shadow: 0 1px 4px rgba(0,0,0,0.02);
    }

    .vocab-table td {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 5px 0;
        border: none;
        border-bottom: 1px dashed var(--border-color);
        text-align: left;
    }

    .vocab-table td:last-child {
        border-bottom: none;
    }

    .vocab-table td::before {
        content: attr(data-label);
        font-size: 0.75rem;
        font-weight: 600;
        color: var(--accent-gold);
        margin-right: 0.5rem;
    }

    .vocab-table td.vocab-persian {
        font-size: calc(1.35rem * var(--font-scale));
        color: var(--persian-color);
        border-bottom: 1px solid var(--border-color);
        padding-bottom: 6px;
        margin-bottom: 4px;
        display: block;
        text-align: right;
    }

    .vocab-table td.vocab-persian::before {
        display: none;
    }

    .settings-modal {
        max-height: 85vh;
    }

    .segmented-options {
        grid-template-columns: repeat(2, 1fr);
    }
}
"""
    with open(os.path.join(HTML_DIR, "style.css"), "w", encoding="utf-8") as f:
        f.write(css)
    return css

def render_entry_original(entry):
    etype = entry.get("type", "prose")
    html = f'<div class="segment-card" id="{entry["id"]}">'
    html += f'<span class="segment-badge">ص {entry.get("book_page", "")}</span>'
    
    if etype == "bismillah":
        html += f'<div class="quran-block"><div class="quran-arabic">{escape_xml(entry["persian"])}</div>'
        html += f'<div class="urdu-interlinear" style="text-align:center;">{escape_xml(entry["urdu_interlinear"])}</div></div>'
    elif etype == "quran":
        html += f'<div class="quran-block"><div class="quran-arabic">{escape_xml(entry["arabic"])}</div>'
        html += f'<div class="urdu-interlinear" style="text-align:center;">{escape_xml(entry["urdu_interlinear"])}</div></div>'
    elif etype == "prose":
        html += f'<div class="persian-text">{escape_xml(entry["persian"])}</div>'
        html += f'<div class="urdu-interlinear">{escape_xml(entry["urdu_interlinear"])}</div>'
    elif etype == "couplet":
        html += f'<div class="couplet-container"><span class="couplet-header">{escape_xml(entry.get("header_persian", "بیت"))}</span>'
        html += f'<div class="verse-line"><div class="verse-hemistich"><div class="persian-text">{escape_xml(entry["persian_m1"])}</div><div class="urdu-interlinear">{escape_xml(entry["urdu_m1"])}</div></div>'
        html += f'<div class="verse-hemistich"><div class="persian-text">{escape_xml(entry["persian_m2"])}</div><div class="urdu-interlinear">{escape_xml(entry["urdu_m2"])}</div></div></div></div>'
    elif etype == "stanza":
        html += f'<div class="couplet-container"><span class="couplet-header">{escape_xml(entry.get("header_persian", "قطعہ"))}</span>'
        for line in entry.get("lines", []):
            html += f'<div class="verse-line"><div class="verse-hemistich"><div class="persian-text">{escape_xml(line["persian_m1"])}</div><div class="urdu-interlinear">{escape_xml(line["urdu_m1"])}</div></div>'
            html += f'<div class="verse-hemistich"><div class="persian-text">{escape_xml(line["persian_m2"])}</div><div class="urdu-interlinear">{escape_xml(line["urdu_m2"])}</div></div></div>'
        html += '</div>'

    # Footnotes
    if entry.get("footnotes"):
        html += '<div class="footnotes-box"><div class="footnote-title">حواشیِ صفحہ:</div>'
        for fn in entry["footnotes"]:
            html += f'<div class="footnote-item">• {escape_xml(fn)}</div>'
        html += '</div>'

    html += '</div>'
    return html

def render_entry_study(entry):
    html = render_entry_original(entry)
    study = entry.get("study", {})
    vocab = study.get("vocabulary", [])
    notes_en = study.get("notes_en", "")
    notes_ur = study.get("notes_ur", "")

    if vocab or notes_en or notes_ur:
        study_html = '<div class="study-layer">'
        study_html += '<div class="study-title">📖 مطالعہ و تجزیہ (Linguistic & Study Scaffolding)</div>'
        
        if notes_en:
            study_html += f'<div class="study-notes-en"><strong>Context & Grammar (English):</strong> {escape_xml(notes_en)}</div>'
        if notes_ur:
            study_html += f'<div class="study-notes-ur"><strong>وضاحت و نکات (اردو):</strong> {escape_xml(notes_ur)}</div>'
        
        if vocab:
            study_html += '<table class="vocab-table"><thead><tr><th>لفظ (Word)</th><th>صرفی حیثیت (Grammar)</th><th>Urdu Meaning</th><th>English Meaning</th><th>Urdu Cognates (مشترک الفاظ)</th></tr></thead><tbody>'
            for v in vocab:
                cognates_html = "".join([f'<span class="cognate-tag">{escape_xml(c.strip())}</span>' for c in v.get("urdu_cognates", "").split("،")])
                study_html += f'<tr><td class="vocab-persian" data-label="لفظ">{escape_xml(v["persian"])}</td><td data-label="صرفی حیثیت">{escape_xml(v.get("grammar", ""))}</td><td style="direction:rtl;font-family:var(--font-urdu);" data-label="Urdu">{escape_xml(v.get("meaning_ur", ""))}</td><td data-label="English">{escape_xml(v.get("meaning_en", ""))}</td><td data-label="مشترک الفاظ">{cognates_html}</td></tr>'
            study_html += '</tbody></table>'

        study_html += '</div>'
        html = html[:-6] + study_html + '</div>'

    return html

def build_html_editions(batches):
    copy_assets()
    generate_css()

    header_template = """<!DOCTYPE html>
<html lang="ur" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
  <title>{title}</title>
  <link rel="stylesheet" href="style.css">
  <script>
    (function() {{
      try {{
        var s = JSON.parse(localStorage.getItem('gulistan_reader_settings') || '{{}}');
        var doc = document.documentElement;
        if (s.urduFont) doc.setAttribute('data-font-urdu', s.urduFont);
        if (s.persianFont) doc.setAttribute('data-font-persian', s.persianFont);
        if (s.textSize) doc.setAttribute('data-size', s.textSize);
        doc.setAttribute('data-theme', s.theme || 'emerald');
      }} catch(e) {{}}
    }})();
  </script>
</head>
<body>
  <header class="site-header">
    <div class="header-branding">
      <div class="header-title">گُلِسْتَانِ سَعْدِیْ</div>
      <div class="header-subtitle">{subtitle}</div>
    </div>
    <div class="header-controls">
      <nav class="nav-links">
        <a href="original.html" class="{orig_active}">اصل متن مع ترجمہ</a>
        <a href="study.html" class="{study_active}">مطالعہ و فرہنگ</a>
      </nav>
      <button type="button" id="settingsToggle" class="settings-btn" aria-label="ترتیبات / Reader Settings" title="ترتیبات (Settings)">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="3"></circle>
          <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path>
        </svg>
        <span>ترتیبات</span>
      </button>
    </div>
  </header>
  <main class="container">
"""

    footer_template = """
  </main>
  <footer class="site-footer">
    <p>گُلِسْتَانِ سَعْدِیْ (شیخ مصلح الدین سعدی شیرازیؒ) | مترجم: مولانا قاضی سجاد حسین مدظلہ</p>
    <p>Digitally transcribed and prepared for dual-edition publication.</p>
  </footer>

  <!-- Reader Settings Modal Drawer -->
  <div id="settingsOverlay" class="settings-overlay" aria-hidden="true">
    <div class="settings-modal" role="dialog" aria-modal="true" aria-labelledby="settingsModalTitle">
      <div class="settings-header">
        <h3 id="settingsModalTitle">ترتیباتِ مطالعہ (Reader Settings)</h3>
        <button type="button" id="settingsClose" class="settings-close-btn" aria-label="بند کریں">&times;</button>
      </div>
      <div class="settings-body">
        <!-- Urdu Font -->
        <div class="setting-group">
          <div class="setting-label">
            <span class="label-title">خطِ اردو (Urdu Font)</span>
            <span class="label-desc">اردو ترجمہ، حواشی اور تفہیم کے لئے خط</span>
          </div>
          <div class="segmented-options" data-setting="urdu-font">
            <button type="button" class="opt-btn" data-val="mehr">
              <span class="font-sample sample-mehr">مہر نستعلیق</span>
              <small>خوشخط روایتی</small>
            </button>
            <button type="button" class="opt-btn" data-val="noto-nastaliq">
              <span class="font-sample sample-noto-nastaliq">نوٹو نستعلیق</span>
              <small>گوگل نستعلیق</small>
            </button>
            <button type="button" class="opt-btn" data-val="noto-naskh">
              <span class="font-sample sample-noto-naskh">نوٹو نسخ</span>
              <small>کتابی واضح</small>
            </button>
          </div>
        </div>

        <!-- Persian Font -->
        <div class="setting-group">
          <div class="setting-label">
            <span class="label-title">خطِ فارسی (Persian Font)</span>
            <span class="label-desc">فارسی اصل متن و اشعار کے لئے</span>
          </div>
          <div class="segmented-options" data-setting="persian-font">
            <button type="button" class="opt-btn" data-val="amiri">
              <span class="font-sample sample-amiri">عمیری نسخ</span>
              <small>کلاسیکی عربی/فارسی</small>
            </button>
            <button type="button" class="opt-btn" data-val="noto-naskh">
              <span class="font-sample sample-noto-naskh">نوٹو نسخ</span>
              <small>صاف جدید نسخ</small>
            </button>
            <button type="button" class="opt-btn" data-val="match-urdu">
              <span class="font-sample sample-mehr">ہم آہنگ خط</span>
              <small>اردو جیسا خط</small>
            </button>
          </div>
        </div>

        <!-- Text Size -->
        <div class="setting-group">
          <div class="setting-label">
            <span class="label-title">حجمِ الفاظ (Text Size)</span>
            <span class="label-desc">مطالعہ کے لئے سائز منتخب کریں</span>
          </div>
          <div class="segmented-options" data-setting="text-size">
            <button type="button" class="opt-btn" data-val="sm">چھوٹا (A-)</button>
            <button type="button" class="opt-btn" data-val="md">معمول (100%)</button>
            <button type="button" class="opt-btn" data-val="lg">بڑا (A+)</button>
            <button type="button" class="opt-btn" data-val="xl">بہت بڑا (A++)</button>
          </div>
        </div>

        <!-- Theme -->
        <div class="setting-group">
          <div class="setting-label">
            <span class="label-title">رنگت و پس منظر (Theme)</span>
            <span class="label-desc">روز و شب کے مطابق پس منظر تبدیل کریں</span>
          </div>
          <div class="theme-options" data-setting="theme">
            <button type="button" class="theme-btn theme-emerald" data-val="emerald">
              <span class="theme-swatch swatch-emerald"></span>
              <span>سبز سرورق (Cover)</span>
            </button>
            <button type="button" class="theme-btn theme-light" data-val="light">
              <span class="theme-swatch swatch-light"></span>
              <span>کاغذی (Light)</span>
            </button>
            <button type="button" class="theme-btn theme-sepia" data-val="sepia">
              <span class="theme-swatch swatch-sepia"></span>
              <span>کتابی (Sepia)</span>
            </button>
            <button type="button" class="theme-btn theme-dark" data-val="dark">
              <span class="theme-swatch swatch-dark"></span>
              <span>شبینہ (Dark)</span>
            </button>
          </div>
        </div>
      </div>
      <div class="settings-footer">
        <button type="button" id="settingsReset" class="reset-btn">پہلے جیسی حالت (Reset Defaults)</button>
      </div>
    </div>
  </div>

  <script src="settings.js"></script>
</body>
</html>
"""

    # 1. Original HTML
    body_orig = []
    body_study = []

    for b in batches:
        for sec in b["sections"]:
            stype = sec.get("content_type")
            if stype == "metadata":
                m_html = """<div class="frontispiece-card">
  <div class="frontispiece-jadwal">
    <div class="frontispiece-ribbon-top"></div>
    <div class="frontispiece-inner">
      <div class="calligraphy-hero">
        <img src="images/title_calligraphy.png" alt="گُلِسْتَانِ مُتَرْجَمْ" class="frontispiece-title-img"/>
      </div>
      <div class="frontispiece-meta">
        <div class="fp-line fp-author">
          <span class="fp-role-label">تالیف:</span>
          <span class="fp-name fp-author-name">حضرت شیخ شرف الدین مصلح سعدی شیرازیؒ</span>
        </div>
        <div class="fp-line fp-translator">
          <span class="fp-role-label">ترجمہ و حواشی:</span>
          <span class="fp-name fp-trans-name">مولانا قاضی سجاد حسین مدظلہ</span>
          <span class="fp-badge">مترجم و محشی</span>
        </div>
        <div class="fp-inst">صدر مدرس، مدرسہ عالیہ فتحپوری دہلی</div>

        <div class="frontispiece-cartouche">
          <div class="cartouche-pub">مکتبہ رحمانیہ</div>
          <div class="cartouche-detail">غزنی سٹریٹ، اردو بازار، لاہور</div>
        </div>
      </div>

      <div class="frontispiece-actions">
        <button type="button" id="viewCoverModalBtn" class="view-cover-btn">
          <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>
          <span>اصل تاریخی سرورق مع حاشیہ دیکھیں (View Scanned Cover)</span>
        </button>
        <a href="Gulistan_Study_Edition.epub" class="download-epub-btn" download>
          <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
          <span>ای پب ڈاؤنلوڈ (Apple Books)</span>
        </a>
      </div>
    </div>
    <div class="frontispiece-ribbon-bottom"></div>
  </div>
</div>

<!-- Cover Lightbox Modal -->
<div id="coverLightbox" class="cover-lightbox" aria-hidden="true">
  <div class="lightbox-content">
    <button type="button" id="closeLightbox" class="lightbox-close">&times;</button>
    <img src="images/cover_full.jpg" alt="گُلِسْتَانِ مُتَرْجَمْ — اصل کتابی سرورق" class="lightbox-img"/>
    <div class="lightbox-caption">اصل تاریخی سرورق — مکتبہ رحمانیہ، اردو بازار، لاہور (۱۹۶۷ء)</div>
  </div>
</div>"""
                body_orig.append(m_html)
                body_study.append(m_html)

            elif stype == "urdu_essay":
                fw_html = f'<article class="foreword-article" id="{sec["section_id"]}">'
                fw_html += f'<h2>{escape_xml(sec["title_ur"])}</h2>'
                if sec.get("khutbah"):
                    fw_html += f'<div class="khutbah-banner"><div class="khutbah-arabic">{escape_xml(sec["khutbah"])}</div></div>'
                for s in sec.get("sections", []):
                    if s.get("heading"):
                        fw_html += f'<h3 class="essay-subheading"><span class="subheading-bullet">✤</span> {escape_xml(s["heading"])}</h3>'
                    for p in s.get("paragraphs", []):
                        fw_html += f'<p class="urdu-prose">{escape_xml(p)}</p>'
                    if s.get("quote"):
                        fw_html += f'<div class="essay-quote-box"><p class="quote-text">{escape_xml(s["quote"])}</p></div>'
                    if s.get("verse"):
                        v = s["verse"]
                        fw_html += f'<div class="essay-verse-box"><span class="verse-m1">{escape_xml(v["m1"])}</span> <span style="color:var(--accent-gold);padding:0 8px;">|</span> <span class="verse-m2">{escape_xml(v["m2"])}</span></div>'
                    if s.get("after_verse"):
                        fw_html += f'<p class="urdu-prose">{escape_xml(s["after_verse"])}</p>'
                    if s.get("persian_quote"):
                        fw_html += f'<div class="essay-persian-quote">{escape_xml(s["persian_quote"])}</div>'
                    for ap in s.get("after_quote_paragraphs", []):
                        fw_html += f'<p class="urdu-prose">{escape_xml(ap)}</p>'
                sig = sec.get("signature")
                if sig:
                    fw_html += f'<div class="essay-signature"><div class="sig-author">{escape_xml(sig.get("author"))}</div><div class="sig-role">{escape_xml(sig.get("role"))}</div><div class="sig-date">{escape_xml(sig.get("date"))}</div></div>'
                fw_html += '</article>'
                body_orig.append(fw_html)
                body_study.append(fw_html)

            elif stype == "bilingual_text":
                d_header = f'<div class="page-marker">صفحات {b["batch_info"]["pages_pdf"][0]} تا {b["batch_info"]["pages_pdf"][1]} (کتابی صفحہ {b["batch_info"]["pages_book"][0]} تا {b["batch_info"]["pages_book"][1]})</div>'
                d_header += f'<h2 style="font-family:var(--font-urdu);color:var(--accent-emerald);text-align:center;margin:2rem 0;">{escape_xml(sec["title_ur"])}</h2>'
                body_orig.append(d_header)
                body_study.append(d_header)

                for e in sec.get("entries", []):
                    body_orig.append(render_entry_original(e))
                    body_study.append(render_entry_study(e))

    with open(os.path.join(HTML_DIR, "original.html"), "w", encoding="utf-8") as f:
        f.write(header_template.format(
            title="گلستان سعدی — اصل متن مع ترجمہ",
            subtitle="اصل متن مع ترجمہ",
            orig_active="active",
            study_active=""
        ) + "\n".join(body_orig) + footer_template)

    with open(os.path.join(HTML_DIR, "study.html"), "w", encoding="utf-8") as f:
        f.write(header_template.format(
            title="گلستان سعدی — ایڈیشن مطالعہ و فرہنگ",
            subtitle="ایڈیشن مطالعہ و فرہنگ",
            orig_active="",
            study_active="active"
        ) + "\n".join(body_study) + footer_template)

    print("Successfully built HTML editions in dist/html/")

def build_epubs(batches):
    epub_css = """
@font-face {
    font-family: 'Mehr Nastaliq';
    src: url('fonts/Mehr_Nastaliq.woff') format('woff'),
         url('fonts/Mehr_Nastaliq.ttf') format('truetype');
    font-weight: normal;
    font-style: normal;
}
body {
    direction: rtl;
    text-align: right;
    font-family: 'Mehr Nastaliq', 'Noto Nastaliq Urdu', serif;
    margin: 1.2em;
    line-height: 2.3;
    color: #111;
}
h1, h2, h3 {
    text-align: center;
    color: #165c32;
    margin: 1em 0;
}
.persian-text {
    font-size: 1.35em;
    color: #0b3c5d;
    font-weight: bold;
    margin-top: 1em;
    line-height: 2.1;
}
.urdu-interlinear {
    font-size: 1.05em;
    color: #222;
    margin-bottom: 1em;
    padding-right: 0.8em;
    border-right: 3px solid #ad2020;
    line-height: 2.3;
}
.couplet {
    text-align: center;
    margin: 1.2em 0;
    padding: 0.8em;
    background: #f7fbf8;
    border: 1px solid #c4ded0;
    border-radius: 6px;
}
.verse-m1, .verse-m2 {
    display: block;
    margin: 0.3em 0;
}
.quran {
    text-align: center;
    color: #165c32;
    font-size: 1.3em;
    margin: 1em 0;
}
.footnotes {
    margin-top: 1.5em;
    border-top: 1px dashed #ccc;
    padding-top: 0.8em;
    font-size: 0.85em;
    color: #555;
}
.study-box {
    background-color: #f7fbf8;
    border: 1px solid #c4ded0;
    border-radius: 6px;
    padding: 1em;
    margin: 1.2em 0;
    font-size: 0.9em;
}
table.vocab {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.85em;
    margin-top: 0.8em;
}
table.vocab th {
    background-color: #e4f2e7;
    color: #185c31;
    border: 1px solid #c4ded0;
    padding: 6px 8px;
    text-align: right;
}
table.vocab td {
    border: 1px solid #c4ded0;
    padding: 6px 8px;
    text-align: right;
}
.frontispiece-meta-box {
    background: #fdfefe;
    border: 2px solid #165c32;
    border-radius: 8px;
    padding: 1.5em;
    margin: 1.5em auto;
    text-align: center;
}
"""

    # 1. Original EPUB
    epub_orig = EpubBook(
        title="گلستان سعدی (مترجم)",
        author="شیخ مصلح الدین سعدی شیرازی",
        language="ur",
        direction="rtl"
    )
    epub_orig.set_css(epub_css)

    # 2. Study EPUB
    epub_study = EpubBook(
        title="گلستان سعدی (ایڈیشن مطالعہ و فرہنگ)",
        author="شیخ مصلح الدین سعدی شیرازی",
        language="ur",
        direction="rtl"
    )
    epub_study.set_css(epub_css)

    # Embed Cover Image into EPUB packages
    cover_full_path = os.path.join(ASSETS_DIR, "cover_full.jpg")
    if os.path.exists(cover_full_path):
        epub_orig.set_cover(cover_full_path)
        epub_study.set_cover(cover_full_path)

    # Embed Mehr Nastaliq fonts (both WOFF and TTF for universal e-reader support)
    for font_file, mime in [("Mehr_Nastaliq.woff", "font/woff"), ("Mehr_Nastaliq.ttf", "font/ttf")]:
        font_path = os.path.join(FONTS_DIR, font_file)
        if os.path.exists(font_path):
            epub_orig.add_font(font_path, font_file, mime)
            epub_study.add_font(font_path, font_file, mime)

    # Embed authentic calligraphy and publisher cartouche
    for img_file in ["title_calligraphy.png", "publisher_cartouche.png"]:
        img_path = os.path.join(ASSETS_DIR, img_file)
        if os.path.exists(img_path):
            epub_orig.add_image(img_path, img_file, "image/png")
            epub_study.add_image(img_path, img_file, "image/png")

    for b in batches:
        for sec in b["sections"]:
            stype = sec.get("content_type")
            sid = sec["section_id"]
            title = sec["title_ur"]

            if stype == "metadata":
                body = """<div style="text-align:center;margin:1.5em 0;">
  <img src="images/title_calligraphy.png" alt="گُلِسْتَانِ مُتَرْجَمْ" style="max-width:85%;height:auto;"/>
</div>
<div class="frontispiece-meta-box">
  <p style="text-align:center;font-size:1.15em;margin:0.5em 0;"><strong style="color:#165c32;">تالیف:</strong> شیخ مصلح الدین سعدی شیرازیؒ</p>
  <p style="text-align:center;font-size:1.15em;margin:0.5em 0;"><strong style="color:#165c32;">ترجمہ و حواشی:</strong> مولانا قاضی سجاد حسین مدظلہ (صدر مدرس مدرسہ عالیہ فتحپوری دہلی)</p>
  <div style="margin-top:1.5em;text-align:center;">
    <img src="images/publisher_cartouche.png" alt="مکتبہ رحمانیہ لاہور" style="max-width:55%;height:auto;"/>
  </div>
</div>"""
                epub_orig.add_chapter(title, f"{sid}.xhtml", body)
                epub_study.add_chapter(title, f"{sid}.xhtml", body)

            elif stype == "urdu_essay":
                body = f"<h2>{escape_xml(title)}</h2>"
                if sec.get("khutbah"):
                    body += f'<p style="text-align:center;font-weight:bold;color:#165c32;margin:1.5em 0;font-size:1.3em;">{escape_xml(sec["khutbah"])}</p>'
                for s in sec.get("sections", []):
                    if s.get("heading"):
                        body += f'<h3 style="color:#165c32;margin-top:1.5em;border-right:3px solid #ad2020;padding-right:0.5em;">{escape_xml(s["heading"])}</h3>'
                    for p in s.get("paragraphs", []):
                        body += f"<p>{escape_xml(p)}</p>"
                    if s.get("quote"):
                        body += f'<blockquote style="background:#f5faf6;border-right:3px solid #9e6b18;padding:0.8em;margin:1em 0;"><p>{escape_xml(s["quote"])}</p></blockquote>'
                    if s.get("verse"):
                        v = s["verse"]
                        body += f'<p style="text-align:center;color:#0b3c5d;font-weight:bold;margin:1em 0;">{escape_xml(v["m1"])} | {escape_xml(v["m2"])}</p>'
                    if s.get("after_verse"):
                        body += f"<p>{escape_xml(s['after_verse'])}</p>"
                    if s.get("persian_quote"):
                        body += f'<p style="text-align:center;color:#0b3c5d;font-weight:bold;font-size:1.15em;margin:1em 0;">{escape_xml(s["persian_quote"])}</p>'
                    for ap in s.get("after_quote_paragraphs", []):
                        body += f"<p>{escape_xml(ap)}</p>"
                sig = sec.get("signature")
                if sig:
                    body += f'<div style="margin-top:2em;text-align:left;border-top:1px solid #ccc;padding-top:1em;"><p><strong style="color:#ad2020;">{escape_xml(sig.get("author"))}</strong><br/>{escape_xml(sig.get("role"))}<br/><small>{escape_xml(sig.get("date"))}</small></p></div>'
                epub_orig.add_chapter(title, f"{sid}.xhtml", body)
                epub_study.add_chapter(title, f"{sid}.xhtml", body)

            elif stype == "bilingual_text":
                body_o = f"<h2>{escape_xml(title)}</h2>"
                body_s = f"<h2>{escape_xml(title)}</h2>"

                for e in sec.get("entries", []):
                    # Original rendering
                    body_o += f'<div id="{e["id"]}">'
                    if e["type"] in ["bismillah", "quran"]:
                        body_o += f'<div class="quran">{escape_xml(e.get("persian") or e.get("arabic"))}</div>'
                        body_o += f'<div class="urdu-interlinear" style="text-align:center;">{escape_xml(e["urdu_interlinear"])}</div>'
                    elif e["type"] == "prose":
                        body_o += f'<div class="persian-text">{escape_xml(e["persian"])}</div>'
                        body_o += f'<div class="urdu-interlinear">{escape_xml(e["urdu_interlinear"])}</div>'
                    elif e["type"] == "couplet":
                        body_o += f'<div class="couplet"><strong>{escape_xml(e.get("header_persian", "بیت"))}</strong>'
                        body_o += f'<div class="persian-text"><span class="verse-m1">{escape_xml(e["persian_m1"])}</span><span class="verse-m2">{escape_xml(e["persian_m2"])}</span></div>'
                        body_o += f'<div class="urdu-interlinear"><span class="verse-m1">{escape_xml(e["urdu_m1"])}</span><span class="verse-m2">{escape_xml(e["urdu_m2"])}</span></div></div>'
                    elif e["type"] == "stanza":
                        body_o += f'<div class="couplet"><strong>{escape_xml(e.get("header_persian", "قطعہ"))}</strong>'
                        for l in e.get("lines", []):
                            body_o += f'<div class="persian-text"><span class="verse-m1">{escape_xml(l["persian_m1"])}</span><span class="verse-m2">{escape_xml(l["persian_m2"])}</span></div>'
                            body_o += f'<div class="urdu-interlinear"><span class="verse-m1">{escape_xml(l["urdu_m1"])}</span><span class="verse-m2">{escape_xml(l["urdu_m2"])}</span></div>'
                        body_o += '</div>'

                    if e.get("footnotes"):
                        body_o += '<div class="footnotes"><strong>حواشی:</strong><br/>'
                        for fn in e["footnotes"]:
                            body_o += f'• {escape_xml(fn)}<br/>'
                        body_o += '</div>'
                    body_o += '</div><hr/>'

                    # Study rendering
                    body_s += body_o.split("<hr/>")[-2] # take current entry snippet
                    study = e.get("study", {})
                    if study.get("vocabulary") or study.get("notes_en") or study.get("notes_ur"):
                        body_s += '<div class="study-box">'
                        if study.get("notes_en"):
                            body_s += f'<p><strong>Study Note (English):</strong> {escape_xml(study["notes_en"])}</p>'
                        if study.get("notes_ur"):
                            body_s += f'<p><strong>وضاحت (اردو):</strong> {escape_xml(study["notes_ur"])}</p>'
                        if study.get("vocabulary"):
                            body_s += '<table class="vocab"><tr><th>لفظ</th><th>معنی (اردو)</th><th>English</th><th>اردو مشترک الفاظ</th></tr>'
                            for v in study["vocabulary"]:
                                body_s += f'<tr><td><strong>{escape_xml(v["persian"])}</strong></td><td>{escape_xml(v.get("meaning_ur",""))}</td><td>{escape_xml(v.get("meaning_en",""))}</td><td>{escape_xml(v.get("urdu_cognates",""))}</td></tr>'
                            body_s += '</table>'
                        body_s += '</div>'
                    body_s += '<hr/>'

                epub_orig.add_chapter(title, f"{sid}.xhtml", body_o)
                epub_study.add_chapter(title, f"{sid}.xhtml", body_s)

    orig_epub_path = os.path.join(DIST_DIR, "Gulistan_Original.epub")
    study_epub_path = os.path.join(DIST_DIR, "Gulistan_Study_Edition.epub")
    epub_orig.write_epub(orig_epub_path)
    epub_study.write_epub(study_epub_path)

if __name__ == "__main__":
    batches = load_batches()
    print(f"Loaded {len(batches)} batch file(s).")
    build_html_editions(batches)
    build_epubs(batches)
    sync_to_docs()
    print("Compilation and docs/ sync complete!")
