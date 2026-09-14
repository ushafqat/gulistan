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
    --font-system: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    --font-ui-urdu: 'Noto Naskh Arabic', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
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
    padding: 0.6rem 2rem;
    position: sticky;
    top: 0;
    z-index: 100;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 2px 12px rgba(0,0,0,0.04);
    transition: background-color 0.25s ease, border-color 0.25s ease;
}

.header-branding {
    display: flex;
    align-items: center;
    gap: 1.1rem;
    text-decoration: none;
}

.header-logo-img {
    height: 52px;
    width: auto;
    object-fit: contain;
    display: block;
    transition: transform 0.2s ease, filter 0.25s ease;
}

.header-branding:hover .header-logo-img {
    transform: scale(1.03);
}

body[data-theme="dark"] .header-logo-img {
    filter: invert(0.92) hue-rotate(180deg) brightness(1.2);
}

.header-title {
    font-family: var(--font-urdu);
    font-size: 1.6rem;
    color: var(--accent-emerald);
    line-height: 1.4;
    font-weight: 700;
}

.header-subtitle {
    font-size: 1.02rem;
    color: var(--accent-gold);
    background: var(--quote-bg);
    border: 1px solid var(--quote-border);
    padding: 4px 12px;
    border-radius: 6px;
    font-weight: 700;
    font-family: var(--font-urdu);
    line-height: 1.6;
}

.header-controls {
    display: flex;
    align-items: center;
    gap: 0.8rem;
}

/* Header Action Buttons (ToC & Settings) */
.header-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    background: var(--ctrl-bg);
    color: var(--text-primary);
    border: 1px solid var(--border-color);
    padding: 0.45rem 0.95rem;
    border-radius: 8px;
    font-family: var(--font-ui-urdu);
    font-size: 0.95rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s ease;
    line-height: 1.25;
    white-space: nowrap;
}

.header-btn:hover {
    background: var(--ctrl-bg-hover);
    border-color: var(--accent-emerald);
}

.header-btn svg {
    width: 17px;
    height: 17px;
    flex-shrink: 0;
    color: var(--accent-emerald);
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
    font-size: 0.78rem;
    padding: 2px 8px;
    border-radius: 6px;
    border: 1px solid var(--tag-border);
    margin-right: 0.4rem;
    font-family: var(--font-ui-urdu);
    line-height: 1.35;
    vertical-align: middle;
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
    font-family: var(--font-ui-urdu);
    line-height: 1.35;
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
    font-size: calc(2.3rem * var(--font-scale));
    text-align: center;
    margin-bottom: 1.5rem;
    line-height: 1.9;
    padding-bottom: 1rem;
    border-bottom: 1px dashed var(--border-color);
    font-weight: 700;
}

.chapter-main-title {
    font-family: var(--font-urdu);
    color: var(--accent-emerald);
    font-size: calc(2.35rem * var(--font-scale));
    text-align: center;
    margin: 2.2rem 0 1.5rem 0;
    line-height: 1.9;
    font-weight: 700;
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
    font-size: calc(1.85rem * var(--font-scale));
    line-height: 2.2;
    color: var(--accent-emerald);
    font-weight: 700;
    direction: rtl;
}

.essay-subheading {
    font-family: var(--font-urdu);
    font-size: calc(1.6rem * var(--font-scale));
    color: var(--accent-emerald);
    line-height: 1.9;
    margin: 2.4rem 0 1rem;
    padding-right: 0.9rem;
    border-right: 4px solid var(--accent-crimson);
    display: flex;
    align-items: center;
    gap: 0.6rem;
    font-weight: 700;
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

/* ============================================================
   AUTHENTIC LITHOGRAPH BOOK-PAGE LEAF LAYOUT
   ============================================================ */
.book-page-leaf {
    scroll-margin-top: 85px;
    background: var(--bg-card);
    border: 2px solid var(--border-jadwal);
    border-radius: 6px;
    margin: 3rem auto;
    max-width: 860px;
    box-shadow: 0 4px 24px rgba(22, 92, 50, 0.08), 0 1px 3px rgba(0,0,0,0.05);
    position: relative;
    overflow: hidden;
    transition: background-color 0.25s ease, border-color 0.25s ease;
}

/* 3-Part Running Header Strip (دیباچہ | صفحہ ۶ | گلستان مترجم) */
.page-header-strip {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid var(--border-jadwal);
    padding: 0.5rem 1.4rem;
    background: var(--banner-bg);
    font-family: var(--font-urdu);
    font-size: 1.15rem;
    font-weight: 700;
    color: var(--accent-emerald);
}

.page-header-right {
    flex: 1;
    text-align: right;
    font-size: 1.15rem;
}

.page-header-center {
    flex: 1;
    text-align: center;
    font-size: 1.4rem;
    color: var(--accent-crimson);
}

.page-header-left {
    flex: 1;
    text-align: left;
    font-size: 1.15rem;
    color: var(--accent-gold);
}

/* Inner Double Jadwal Frame */
.page-jadwal-inner {
    border: 1px solid var(--border-jadwal);
    margin: 6px;
    padding: 1.6rem 2rem;
    position: relative;
}

.page-content-flow {
    display: flex;
    flex-direction: column;
    gap: 0.8rem;
}

/* Page In-line Section Title Cartouche */
.page-section-cartouche {
    margin: 1.6rem 0 1.2rem 0;
    padding: 0.8rem 1.2rem;
    background: var(--banner-bg);
    border: 2px double var(--border-jadwal);
    border-radius: 6px;
    text-align: center;
    position: relative;
    box-shadow: 0 2px 8px rgba(0,0,0,0.03);
}

.cartouche-title-persian {
    font-family: var(--font-urdu);
    font-size: calc(1.4rem * var(--font-scale));
    font-weight: 700;
    color: var(--accent-emerald);
    line-height: 2.1;
}

.cartouche-title-urdu {
    font-family: var(--font-urdu);
    font-size: calc(1.02rem * var(--font-scale));
    color: var(--text-secondary);
    line-height: 1.85;
    margin-top: 0.25rem;
}

/* Centered Calligraphic Verse Ornament (بیت / قطعہ) */
.verse-ornament {
    text-align: center;
    font-family: var(--font-urdu);
    font-size: 1.4rem;
    font-weight: 700;
    color: var(--accent-emerald);
    margin: 1.2rem auto 0.4rem;
    display: table;
    padding: 0 1rem;
}

.verse-ornament::before, .verse-ornament::after {
    content: "✤";
    color: var(--accent-gold);
    padding: 0 0.5rem;
    font-size: 1.05rem;
}

/* Side-by-Side Couplets & Stanzas Grid with Central Divider */
.couplet-block {
    margin: 0.8rem 0;
}

.verse-couplet-grid {
    display: flex;
    align-items: stretch;
    justify-content: space-between;
    margin: 0.5rem 0;
    border: 1px solid var(--border-color);
    border-radius: 4px;
    background: var(--verse-bg);
}

.verse-col {
    flex: 1;
    padding: 0.8rem 1.2rem;
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.verse-col-divider {
    width: 1px;
    background-color: var(--border-jadwal);
    margin: 6px 0;
    flex-shrink: 0;
}

.persian-verse {
    font-family: var(--font-urdu);
    font-size: calc(1.5rem * var(--font-scale));
    font-weight: 700;
    color: var(--persian-color);
    line-height: var(--line-height-urdu);
    margin-bottom: 0.25rem;
    direction: rtl;
}

.urdu-interlinear-verse {
    font-family: var(--font-urdu);
    font-size: calc(1.08rem * var(--font-scale) * var(--urdu-size-offset));
    color: var(--urdu-color);
    line-height: var(--line-height-urdu);
    direction: rtl;
}

/* Continuous Interlinear Prose Block */
.prose-interlinear-block {
    margin: 0.8rem 0;
    padding: 0.4rem 0;
}

.persian-prose {
    font-family: var(--font-urdu);
    font-size: calc(1.5rem * var(--font-scale));
    font-weight: 700;
    color: var(--persian-color);
    line-height: var(--line-height-urdu);
    direction: rtl;
    text-align: justify;
    text-justify: inter-word;
    margin-bottom: 0.25rem;
}

.urdu-interlinear-prose {
    font-family: var(--font-urdu);
    font-size: calc(1.1rem * var(--font-scale) * var(--urdu-size-offset));
    color: var(--urdu-color);
    line-height: var(--line-height-urdu);
    direction: rtl;
    text-align: justify;
    text-justify: inter-word;
    padding-right: 0.8rem;
    border-right: 3px solid var(--accent-crimson);
    margin-bottom: 0.5rem;
}

/* Quranic verse block */
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
    margin-bottom: 0.4rem;
    font-weight: 700;
}

.urdu-interlinear-quran {
    font-family: var(--font-urdu);
    font-size: calc(1.15rem * var(--font-scale) * var(--urdu-size-offset));
    color: var(--urdu-color);
    line-height: var(--line-height-urdu);
    direction: rtl;
    text-align: center;
}

/* Grouped Bottom Footnotes */
.page-footnotes-container {
    margin-top: 2rem;
    padding-top: 1rem;
    border-top: 1.5px solid var(--border-jadwal);
    direction: rtl;
    text-align: right;
}

.footnote-mark-ref {
    font-family: var(--font-urdu);
    font-size: 0.85em;
    color: var(--accent-emerald);
    text-decoration: none;
    margin: 0 3px;
    font-weight: bold;
    vertical-align: super;
    line-height: 1;
    transition: color 0.15s ease;
}

.footnote-mark-ref:hover {
    color: var(--accent-crimson);
}

.page-footnotes-container {
    margin-top: 1.8rem;
    padding-top: 1.1rem;
    border-top: 1.5px solid var(--border-color);
    position: relative;
}

.page-footnotes-container::before {
    content: "✤  حواشیِ کتاب  ✤";
    position: absolute;
    top: -12px;
    left: 50%;
    transform: translateX(-50%);
    background: var(--bg-card);
    padding: 0 14px;
    font-family: var(--font-urdu);
    font-size: 0.92rem;
    color: var(--accent-emerald);
    letter-spacing: 0.05em;
}

.page-footnotes-title {
    display: none;
}

.footnote-entry {
    font-family: var(--font-urdu);
    font-size: calc(1.04rem * var(--font-scale) * var(--urdu-size-offset));
    color: var(--text-primary);
    line-height: var(--line-height-urdu);
    margin-bottom: 0.5rem;
    padding-right: 0.3rem;
    text-align: justify;
    text-justify: inter-word;
}

.fn-num {
    color: var(--accent-crimson);
    font-weight: bold;
    margin-left: 6px;
}

/* ============================================================
   COLLAPSIBLE ENGLISH STUDY DRAWER (Study Edition)
   Hidden by default so original book page remains completely visible
   ============================================================ */
.en-study-collapse {
    margin: 0.3rem 0 0.6rem 0;
    border: 1px solid transparent;
    border-radius: 8px;
    background: transparent;
    transition: all 0.2s ease;
}

.en-study-collapse[open] {
    border-color: var(--border-color);
    background: var(--study-bg);
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.04);
    padding-bottom: 0.4rem;
}

.en-study-summary {
    list-style: none;
    cursor: pointer;
    padding: 0.2rem 0;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    user-select: none;
    outline: none;
}

.en-study-summary::-webkit-details-marker {
    display: none;
}

.en-study-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    font-size: 0.8rem;
    font-weight: 500;
    color: var(--text-secondary);
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    padding: 3px 11px;
    border-radius: 14px;
    transition: all 0.18s ease;
    box-shadow: 0 1px 3px rgba(0,0,0,0.02);
}

.en-study-summary:hover .en-study-badge {
    background: var(--ctrl-bg-hover);
    color: var(--accent-emerald);
    border-color: var(--accent-emerald);
}

.en-study-collapse[open] .en-study-badge {
    background: var(--accent-emerald);
    color: #ffffff;
    border-color: var(--accent-emerald);
}

.en-badge-arrow {
    font-size: 0.72rem;
    transition: transform 0.2s ease;
}

.en-study-collapse[open] .en-badge-arrow {
    transform: rotate(180deg);
}

.en-study-drawer {
    padding: 0.9rem 1.1rem;
    border-top: 1px solid var(--border-color);
    direction: ltr;
    text-align: left;
}

.en-trans-card {
    background: var(--bg-card);
    border-left: 3.5px solid var(--accent-gold);
    border-radius: 4px;
    padding: 0.65rem 0.9rem;
    margin-bottom: 0.75rem;
}

.en-card-label {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    font-size: 0.73rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: var(--accent-gold);
    margin-bottom: 0.25rem;
}

.en-trans-quote {
    font-family: Georgia, "Times New Roman", serif;
    font-size: calc(1rem * var(--font-scale));
    font-style: italic;
    color: var(--text-primary);
    line-height: 1.6;
}

.en-notes-card {
    background: var(--bg-card);
    border-left: 3.5px solid var(--accent-emerald);
    border-radius: 4px;
    padding: 0.65rem 0.9rem;
    margin-bottom: 0.75rem;
}

.en-notes-card .en-card-label {
    color: var(--accent-emerald);
}

.en-notes-text {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    font-size: calc(0.9rem * var(--font-scale));
    color: var(--text-primary);
    line-height: 1.6;
}

.ur-notes-card {
    background: var(--bg-card);
    border-right: 3.5px solid var(--accent-emerald);
    border-left: none;
    border-radius: 4px;
    padding: 0.65rem 0.9rem;
    margin-bottom: 0.75rem;
    direction: rtl;
    text-align: right;
}

.ur-notes-card .ur-card-label {
    font-family: var(--font-urdu);
    font-size: 0.95rem;
    font-weight: bold;
    color: var(--accent-emerald);
    margin-bottom: 0.25rem;
}

.ur-notes-card .ur-notes-text {
    font-family: var(--font-urdu);
    font-size: calc(1.08rem * var(--font-scale) * var(--urdu-size-offset));
    line-height: var(--line-height-urdu);
    color: var(--text-primary);
}

.en-vocab-card {
    margin-top: 0.75rem;
}

.en-vocab-card .en-card-label {
    color: var(--persian-color);
}

/* Vocabulary Table */
.vocab-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 0.5rem;
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

/* Global Study Reading Toolbar */
.study-reading-toolbar {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    margin: 1.5rem auto 1rem;
    max-width: 860px;
    padding: 0 0.5rem;
}

.btn-toggle-notes {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: var(--bg-card);
    color: var(--accent-emerald);
    border: 1.5px solid var(--accent-emerald);
    padding: 0.45rem 1.2rem;
    border-radius: 20px;
    font-family: var(--font-ui-urdu);
    font-size: 0.88rem;
    font-weight: 600;
    cursor: pointer;
    box-shadow: 0 2px 6px rgba(0,0,0,0.04);
    transition: all 0.2s ease;
    line-height: 1.35;
}

.btn-toggle-notes:hover {
    background: var(--accent-emerald);
    color: #ffffff;
}

footer.site-footer {
    text-align: center;
    padding: 2rem 1rem;
    color: var(--text-secondary);
    font-family: var(--font-ui-urdu);
    font-size: 0.88rem;
    border-top: 1px solid var(--border-color);
    margin-top: 3.5rem;
    line-height: 1.6;
}

/* ============================================================
   SETTINGS DRAWER & MODAL STYLES (System UI Typography)
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
    font-family: var(--font-ui-urdu);
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
    font-family: var(--font-ui-urdu);
}

.settings-header h3 {
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--accent-emerald);
    font-family: var(--font-ui-urdu);
    margin: 0;
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
    font-family: var(--font-ui-urdu);
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
    font-family: var(--font-ui-urdu);
}

.label-title {
    font-size: 0.92rem;
    font-weight: 700;
    color: var(--text-primary);
    font-family: var(--font-ui-urdu);
}

.label-desc {
    font-size: 0.77rem;
    color: var(--text-secondary);
    font-family: var(--font-ui-urdu);
}

/* Edition Switcher in Settings */
.edition-switcher {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 0.65rem;
    margin-top: 0.25rem;
}

.edition-btn {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    padding: 0.75rem 0.85rem;
    border-radius: 10px;
    border: 1.5px solid var(--border-color);
    background: var(--ctrl-bg);
    color: var(--text-primary);
    text-decoration: none;
    transition: all 0.2s ease;
    direction: ltr;
    text-align: left;
    gap: 0.2rem;
}

.edition-btn:hover {
    border-color: var(--accent-emerald);
    background: var(--ctrl-bg-hover);
    transform: translateY(-1px);
}

.edition-btn.active {
    border-color: var(--accent-emerald);
    background: var(--bg-card);
    box-shadow: 0 2px 10px rgba(22, 92, 50, 0.12);
    outline: 2px solid var(--accent-emerald);
}

.edition-btn .edition-title {
    font-family: var(--font-system);
    font-size: 0.92rem;
    font-weight: 700;
    color: var(--accent-emerald);
    line-height: 1.25;
}

.edition-btn .edition-title-ur {
    font-family: var(--font-ui-urdu);
    font-size: 0.82rem;
    font-weight: 600;
    color: var(--text-primary);
    direction: rtl;
    line-height: 1.35;
}

.edition-btn .edition-desc {
    font-family: var(--font-system);
    font-size: 0.72rem;
    color: var(--text-secondary);
    line-height: 1.3;
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
    font-family: var(--font-ui-urdu);
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
    font-family: var(--font-ui-urdu);
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
    font-family: var(--font-ui-urdu);
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
    font-family: var(--font-ui-urdu);
    transition: all 0.2s;
}

.reset-btn:hover {
    border-color: var(--accent-emerald);
    color: var(--accent-emerald);
}

/* ============================================================
   TABLE OF CONTENTS (ToC) MODAL DRAWER
   ============================================================ */
.toc-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.52);
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

.toc-overlay.open {
    opacity: 1;
    pointer-events: auto;
}

.toc-modal {
    background: var(--bg-card);
    color: var(--text-primary);
    border: 1px solid var(--border-color);
    border-radius: 16px;
    width: 100%;
    max-width: 580px;
    max-height: 90vh;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    box-shadow: 0 14px 44px rgba(0,0,0,0.25);
    transform: translateY(20px) scale(0.97);
    transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    direction: rtl;
    font-family: var(--font-ui-urdu);
}

.toc-overlay.open .toc-modal {
    transform: translateY(0) scale(1);
}

.toc-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.1rem 1.35rem;
    border-bottom: 1px solid var(--border-color);
    background: var(--bg-card);
    font-family: var(--font-ui-urdu);
}

.toc-header-title-wrap {
    display: flex;
    align-items: center;
    gap: 0.6rem;
}

.toc-header-title-wrap svg {
    color: var(--accent-emerald);
}

.toc-header h3 {
    font-size: 1.15rem;
    font-weight: 700;
    color: var(--accent-emerald);
    font-family: var(--font-ui-urdu);
    margin: 0;
}

.toc-close-btn {
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

.toc-close-btn:hover {
    background: rgba(0,0,0,0.06);
    color: var(--text-primary);
}

/* Resume Reading Banner in ToC */
.toc-resume-banner {
    background: var(--banner-bg);
    border-bottom: 1px solid var(--banner-border);
    padding: 0.75rem 1.35rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 0.8rem;
    font-family: var(--font-ui-urdu);
}

.toc-resume-info {
    display: flex;
    flex-direction: column;
    gap: 0.15rem;
}

.toc-resume-badge {
    font-size: 0.72rem;
    color: var(--accent-emerald);
    font-weight: 700;
    font-family: var(--font-ui-urdu);
}

.toc-resume-title {
    font-size: 0.95rem;
    font-weight: 700;
    color: var(--text-primary);
    font-family: var(--font-ui-urdu);
}

.toc-resume-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    background: var(--accent-emerald);
    color: #ffffff;
    border: none;
    padding: 0.45rem 0.9rem;
    border-radius: 8px;
    font-family: var(--font-ui-urdu);
    font-size: 0.84rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s ease;
    white-space: nowrap;
}

.toc-resume-btn:hover {
    filter: brightness(1.1);
    transform: translateY(-1px);
}

.toc-resume-btn svg {
    transform: scaleX(-1);
}

/* ToC Navigation Tabs */
.toc-tabs {
    display: flex;
    border-bottom: 1px solid var(--border-color);
    background: var(--ctrl-bg);
    padding: 0.35rem 0.6rem 0 0.6rem;
    gap: 0.4rem;
    font-family: var(--font-ui-urdu);
}

.toc-tab-btn {
    flex: 1;
    background: transparent;
    border: none;
    border-bottom: 3px solid transparent;
    padding: 0.65rem 0.8rem;
    cursor: pointer;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.15rem;
    color: var(--text-secondary);
    font-family: var(--font-ui-urdu);
    font-size: 0.92rem;
    font-weight: 600;
    transition: all 0.2s;
    border-radius: 6px 6px 0 0;
}

.toc-tab-btn small {
    font-size: 0.72rem;
    opacity: 0.8;
    font-family: var(--font-system);
}

.toc-tab-btn:hover {
    color: var(--text-primary);
    background: rgba(0,0,0,0.03);
}

.toc-tab-btn.active {
    background: var(--bg-card);
    color: var(--accent-emerald);
    border-bottom-color: var(--accent-emerald);
}

/* ToC Modal Body */
.toc-body {
    padding: 1.1rem 1.35rem;
    overflow-y: auto;
    flex: 1;
    max-height: calc(90vh - 160px);
    font-family: var(--font-ui-urdu);
}

.toc-tab-pane {
    display: none;
}

.toc-tab-pane.active {
    display: block;
}

/* Sections List */
.toc-section-list {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 0.6rem;
}

.toc-section-item {
    border: 1px solid var(--border-color);
    border-radius: 9px;
    background: var(--bg-card);
    transition: all 0.2s ease;
}

.toc-section-item:hover {
    border-color: var(--accent-emerald);
    background: var(--quote-bg);
}

.toc-section-link {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.75rem 1rem;
    text-decoration: none;
    color: var(--text-primary);
    gap: 0.8rem;
    font-family: var(--font-ui-urdu);
}

.toc-sec-title-wrap {
    display: flex;
    flex-direction: column;
    gap: 0.15rem;
}

.toc-sec-title-ur {
    font-size: 0.96rem;
    font-weight: 700;
    color: var(--text-primary);
    line-height: 1.45;
    font-family: var(--font-ui-urdu);
}

.toc-sec-title-en {
    font-size: 0.76rem;
    color: var(--text-secondary);
    font-family: var(--font-system);
}

.toc-sec-page {
    font-size: 0.82rem;
    font-weight: 600;
    color: var(--accent-emerald);
    background: var(--tag-bg);
    border: 1px solid var(--tag-border);
    padding: 3px 9px;
    border-radius: 6px;
    white-space: nowrap;
    font-family: var(--font-ui-urdu);
}

/* Page Jump Grid */
.toc-page-intro {
    font-size: 0.84rem;
    color: var(--text-secondary);
    margin-bottom: 0.9rem;
    line-height: 1.4;
    font-family: var(--font-ui-urdu);
}

.toc-page-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(68px, 1fr));
    gap: 0.55rem;
}

.page-chip {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 0.55rem 0.35rem;
    border: 1px solid var(--border-color);
    border-radius: 8px;
    background: var(--ctrl-bg);
    color: var(--text-primary);
    text-decoration: none;
    transition: all 0.2s ease;
    gap: 0.1rem;
    font-family: var(--font-ui-urdu);
}

.page-chip:hover {
    border-color: var(--accent-emerald);
    background: var(--ctrl-bg-hover);
    transform: translateY(-2px);
    box-shadow: 0 3px 8px rgba(0,0,0,0.06);
}

.chip-ur {
    font-size: 1.05rem;
    font-weight: 700;
    color: var(--accent-emerald);
    line-height: 1.2;
    font-family: var(--font-ui-urdu);
}

.chip-en {
    font-size: 0.68rem;
    color: var(--text-secondary);
    font-family: var(--font-system);
}

/* ============================================================
   FLOATING RESUME READING TOAST
   ============================================================ */
.resume-toast {
    position: fixed;
    bottom: 24px;
    right: 24px;
    z-index: 900;
    background: var(--bg-card);
    border: 1.5px solid var(--accent-emerald);
    border-radius: 12px;
    padding: 0.65rem 1rem;
    box-shadow: 0 8px 24px rgba(0,0,0,0.16);
    display: flex;
    align-items: center;
    gap: 0.9rem;
    direction: rtl;
    font-family: var(--font-ui-urdu);
    transform: translateY(120px);
    opacity: 0;
    pointer-events: none;
    transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.3s ease;
    max-width: calc(100vw - 48px);
}

.resume-toast.show {
    transform: translateY(0);
    opacity: 1;
    pointer-events: auto;
}

.resume-toast-content {
    display: flex;
    align-items: center;
    gap: 0.55rem;
}

.resume-toast-icon svg {
    color: var(--accent-emerald);
    display: block;
}

.resume-toast-text {
    font-size: 0.88rem;
    font-weight: 600;
    color: var(--text-primary);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    max-width: 200px;
    font-family: var(--font-ui-urdu);
}

.resume-toast-actions {
    display: flex;
    align-items: center;
    gap: 0.4rem;
}

.resume-toast-btn {
    background: var(--accent-emerald);
    color: #ffffff;
    border: none;
    padding: 0.35rem 0.75rem;
    border-radius: 6px;
    font-size: 0.82rem;
    font-weight: 600;
    cursor: pointer;
    font-family: var(--font-ui-urdu);
    transition: all 0.2s;
}

.resume-toast-btn:hover {
    filter: brightness(1.1);
}

.resume-toast-dismiss {
    background: transparent;
    border: none;
    color: var(--text-secondary);
    font-size: 1.3rem;
    line-height: 1;
    cursor: pointer;
    padding: 0 0.3rem;
    border-radius: 4px;
    transition: all 0.2s;
}

.resume-toast-dismiss:hover {
    color: var(--text-primary);
    background: rgba(0,0,0,0.06);
}

/* ============================================================
   MOBILE RESPONSIVENESS (< 640px)
   ============================================================ */
@media screen and (max-width: 640px) {
    header.site-header {
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        gap: 0.5rem;
        padding: 0.6rem 0.85rem;
    }

    .header-branding {
        gap: 0.6rem;
    }

    .header-logo-img {
        height: 38px;
    }

    .header-subtitle {
        font-size: 0.82rem;
        padding: 2px 6px;
    }

    .header-controls {
        gap: 0.4rem;
    }

    .header-btn {
        padding: 0.38rem 0.65rem;
        font-size: 0.85rem;
        gap: 0.3rem;
    }

    .header-btn svg {
        width: 15px;
        height: 15px;
    }

    .resume-toast {
        bottom: 16px;
        right: 16px;
        left: 16px;
        max-width: none;
        justify-content: space-between;
    }

    .resume-toast-text {
        max-width: 150px;
    }

    .edition-switcher {
        grid-template-columns: 1fr;
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

    .book-page-leaf {
        margin: 1.5rem auto;
        border-radius: 4px;
    }

    .page-header-strip {
        padding: 0.45rem 0.8rem;
        font-size: 0.98rem;
    }

    .page-header-center {
        font-size: 1.2rem;
    }

    .page-jadwal-inner {
        margin: 4px;
        padding: 1rem 0.8rem;
    }

    .verse-couplet-grid {
        flex-direction: column;
    }

    .verse-col-divider {
        width: 100%;
        height: 1px;
        margin: 0;
    }

    .verse-col {
        padding: 0.6rem 0.5rem;
    }

    .persian-verse {
        font-size: calc(1.35rem * var(--font-scale));
    }

    .persian-prose {
        font-size: calc(1.35rem * var(--font-scale));
    }

    .urdu-interlinear-verse, .urdu-interlinear-prose {
        font-size: calc(1.02rem * var(--font-scale) * var(--urdu-size-offset));
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

def to_urdu_numerals(n):
    digits = {'0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴', '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹'}
    return ''.join(digits.get(c, c) for c in str(n))

def render_study_accordion(entry):
    study = entry.get("study", {})
    vocab = study.get("vocabulary", [])
    notes_en = study.get("notes_en", "")
    notes_ur = study.get("notes_ur", "")
    english_trans = entry.get("english_trans", "")

    if not (vocab or notes_en or notes_ur or english_trans):
        return ""

    eid = entry.get("id", "")
    s_html = f"""          <details class="en-study-collapse" id="study_{eid}">
            <summary class="en-study-summary" title="Click to view English translation, notes, and vocabulary">
              <span class="en-study-badge">
                <span class="en-flag">🇬🇧</span>
                <span class="en-badge-text">English Notes &amp; Translation</span>
                <span class="en-badge-arrow">▾</span>
              </span>
            </summary>
            <div class="en-study-drawer">
"""
    if english_trans:
        s_html += f"""              <div class="en-trans-card">
                <div class="en-card-label">English Translation</div>
                <div class="en-trans-quote">“{escape_xml(english_trans)}”</div>
              </div>
"""
    if notes_en:
        s_html += f"""              <div class="en-notes-card">
                <div class="en-card-label">Grammar &amp; Commentary (English)</div>
                <div class="en-notes-text">{escape_xml(notes_en)}</div>
              </div>
"""
    if notes_ur:
        s_html += f"""              <div class="ur-notes-card">
                <div class="ur-card-label">وضاحت و نکات (اضافی)</div>
                <div class="ur-notes-text">{escape_xml(notes_ur)}</div>
              </div>
"""
    if vocab:
        s_html += """              <div class="en-vocab-card">
                <div class="en-card-label">Vocabulary &amp; Root Analysis</div>
                <table class="vocab-table">
                  <thead>
                    <tr>
                      <th>لفظ (Word)</th>
                      <th>صرفی حیثیت (Grammar)</th>
                      <th>English Meaning</th>
                      <th>اردو معنی</th>
                      <th>Urdu Cognates (مشترک الفاظ)</th>
                    </tr>
                  </thead>
                  <tbody>
"""
        for v in vocab:
            cognates_html = "".join([f'<span class="cognate-tag">{escape_xml(c.strip())}</span>' for c in v.get("urdu_cognates", "").split("،")])
            s_html += f"""                    <tr>
                      <td class="vocab-persian" data-label="لفظ">{escape_xml(v["persian"])}</td>
                      <td data-label="Grammar">{escape_xml(v.get("grammar", ""))}</td>
                      <td data-label="English">{escape_xml(v.get("meaning_en", ""))}</td>
                      <td style="direction:rtl;font-family:var(--font-urdu);" data-label="Urdu">{escape_xml(v.get("meaning_ur", ""))}</td>
                      <td data-label="مشترک الفاظ">{cognates_html}</td>
                    </tr>
"""
        s_html += """                  </tbody>
                </table>
              </div>
"""
    s_html += "            </div>\n          </details>\n"
    return s_html

def render_book_page(section_title, book_page, page_entries, is_study=False):
    urdu_page = to_urdu_numerals(book_page) if str(book_page).isdigit() else str(book_page)

    page_footnotes = []
    fn_map = {}
    for e in page_entries:
        for fn in e.get("footnotes", []):
            if fn not in fn_map:
                page_footnotes.append(fn)
                fn_map[fn] = len(page_footnotes)

    html = f"""<section class="book-page-leaf" id="page_{book_page}">
  <!-- 3-Part Lithograph Running Header -->
  <div class="page-header-strip">
    <div class="page-header-right">{escape_xml(section_title)}</div>
    <div class="page-header-center">صفحہ {urdu_page}</div>
    <div class="page-header-left">گُلِسْتَانِ مُتَرْجَمْ</div>
  </div>

  <!-- Inner Double Jadwal Frame -->
  <div class="page-jadwal-inner">
    <div class="page-content-flow">
"""
    for e in page_entries:
        if e.get("section_banner"):
            sb = e["section_banner"]
            html += f"""      <div class="page-section-cartouche">
        <div class="cartouche-title-persian">{escape_xml(sb.get("persian", ""))}</div>
        <div class="cartouche-title-urdu">{escape_xml(sb.get("urdu", ""))}</div>
      </div>\n"""

        etype = e.get("type", "prose")
        eid = e.get("id", "")

        # Generate footnote callouts if this entry has footnotes
        fn_callouts = []
        for fn in e.get("footnotes", []):
            fn_idx = fn_map[fn]
            urdu_sym = f"{to_urdu_numerals(fn_idx)}؎"
            fn_callouts.append(f'<sup class="fn-callout"><a href="#fn_p{book_page}_{fn_idx}" class="footnote-mark-ref" title="حاشیہ نمبر {urdu_sym}">[{urdu_sym}]</a></sup>')
        fn_callouts_html = "".join(fn_callouts)

        if etype in ["bismillah", "quran"]:
            arabic_txt = e.get("arabic") or e.get("persian", "")
            html += f"""      <div class="quran-block" id="{eid}">
        <div class="quran-arabic">{escape_xml(arabic_txt)}{fn_callouts_html}</div>
        <div class="urdu-interlinear-quran">{escape_xml(e.get("urdu_interlinear", ""))}</div>
"""
            if is_study:
                html += render_study_accordion(e)
            html += "      </div>\n"

        elif etype == "prose":
            html += f"""      <div class="prose-interlinear-block" id="{eid}">
        <div class="persian-prose">{escape_xml(e.get("persian", ""))}{fn_callouts_html}</div>
        <div class="urdu-interlinear-prose">{escape_xml(e.get("urdu_interlinear", ""))}</div>
"""
            if is_study:
                html += render_study_accordion(e)
            html += "      </div>\n"

        elif etype == "couplet":
            header_txt = e.get("header_persian")
            ornament_html = f'        <div class="verse-ornament">{escape_xml(header_txt)}</div>\n' if header_txt else ""
            html += f"""      <div class="couplet-block" id="{eid}">
{ornament_html}        <div class="verse-couplet-grid">
          <div class="verse-col verse-col-right">
            <div class="persian-verse">{escape_xml(e.get("persian_m1", ""))}</div>
            <div class="urdu-interlinear-verse">{escape_xml(e.get("urdu_m1", ""))}</div>
          </div>
          <div class="verse-col-divider"></div>
          <div class="verse-col verse-col-left">
            <div class="persian-verse">{escape_xml(e.get("persian_m2", ""))}{fn_callouts_html}</div>
            <div class="urdu-interlinear-verse">{escape_xml(e.get("urdu_m2", ""))}</div>
          </div>
        </div>
"""
            if is_study:
                html += render_study_accordion(e)
            html += "      </div>\n"

        elif etype == "stanza":
            header_txt = e.get("header_persian")
            ornament_html = f'        <div class="verse-ornament">{escape_xml(header_txt)}</div>\n' if header_txt else ""
            lines = e.get("lines", [])
            html += f"""      <div class="couplet-block" id="{eid}">
{ornament_html}"""
            for l_idx, line in enumerate(lines):
                is_last_line = (l_idx == len(lines) - 1)
                line_fn_html = fn_callouts_html if is_last_line else ""
                html += f"""        <div class="verse-couplet-grid">
          <div class="verse-col verse-col-right">
            <div class="persian-verse">{escape_xml(line.get("persian_m1", ""))}</div>
            <div class="urdu-interlinear-verse">{escape_xml(line.get("urdu_m1", ""))}</div>
          </div>
          <div class="verse-col-divider"></div>
          <div class="verse-col verse-col-left">
            <div class="persian-verse">{escape_xml(line.get("persian_m2", ""))}{line_fn_html}</div>
            <div class="urdu-interlinear-verse">{escape_xml(line.get("urdu_m2", ""))}</div>
          </div>
        </div>
"""
            if is_study:
                html += render_study_accordion(e)
            html += "      </div>\n"

    html += "    </div>\n"

    if page_footnotes:
        html += f"""    <div class="page-footnotes-container">
      <div class="page-footnotes-title">حواشی و تشریحاتِ صفحہ:</div>
"""
        for idx, fn in enumerate(page_footnotes, 1):
            urdu_sym = f"{to_urdu_numerals(idx)}؎"
            html += f'      <div class="footnote-entry" id="fn_p{book_page}_{idx}"><span class="fn-num">[{urdu_sym}]</span> {escape_xml(fn)}</div>\n'
        html += "    </div>\n"

    html += "  </div>\n</section>\n"
    return html

    html += "  </div>\n</section>\n"
    return html

def render_toc_html(batches, bilingual_pages):
    # 1. Sections list
    sections = [
        {
            "id": "frontispiece",
            "title_ur": "سرورق و تعارفِ کتاب",
            "title_en": "Title Page & Frontispiece",
            "page_num": "۱"
        },
        {
            "id": "pesh_lafz",
            "title_ur": "پیش لفظ — سوانح حیات حضرت شیخ سعدی شیرازیؒ",
            "title_en": "Foreword — Biography of Sheikh Saadi",
            "page_num": "۱–۴"
        }
    ]

    for b in batches:
        for sec in b.get("sections", []):
            if sec.get("content_type") == "bilingual_text":
                entries = sec.get("entries", [])
                if entries:
                    bps = [e.get("book_page") for e in entries if e.get("book_page")]
                    if bps:
                        first_bp = bps[0]
                        last_bp = bps[-1]
                        prange = f"{first_bp}–{last_bp}" if first_bp != last_bp else f"{first_bp}"
                    else:
                        first_bp = 1
                        prange = "۱"
                    tur = sec.get("title_ur") or sec.get("title") or "فصل"
                    ten = sec.get("title_en") or ""
                    sections.append({
                        "id": f"page_{first_bp}",
                        "title_ur": tur,
                        "title_en": ten,
                        "page_num": prange
                    })

    sec_items_html = []
    for s in sections:
        ur_p = to_urdu_numerals(s["page_num"])
        en_sub = f'<span class="toc-sec-title-en">{escape_xml(s["title_en"])}</span>' if s.get("title_en") else ''
        sec_items_html.append(f"""          <li class="toc-section-item">
            <a href="#{s['id']}" class="toc-section-link">
              <div class="toc-sec-title-wrap">
                <span class="toc-sec-title-ur">{escape_xml(s['title_ur'])}</span>
                {en_sub}
              </div>
              <span class="toc-sec-page">صفحہ {ur_p}</span>
            </a>
          </li>""")
    sections_list_html = "\n".join(sec_items_html)

    # 2. Pages tab chips
    page_chips_html = []
    # Foreword pages 1 to 4
    for p in range(1, 5):
        ur_num = to_urdu_numerals(p)
        page_chips_html.append(f"""          <a href="#pesh_lafz" class="page-chip" title="پیش لفظ صفحہ {ur_num}">
            <span class="chip-ur">{ur_num}</span>
            <span class="chip-en">p.{p}</span>
          </a>""")
    # Bilingual book pages
    sorted_pages = sorted(bilingual_pages.keys(), key=lambda x: int(x) if x.isdigit() else 999)
    for bp in sorted_pages:
        ur_num = to_urdu_numerals(bp)
        page_chips_html.append(f"""          <a href="#page_{bp}" class="page-chip" title="صفحہ {ur_num}">
            <span class="chip-ur">{ur_num}</span>
            <span class="chip-en">p.{bp}</span>
          </a>""")
    pages_grid_html = "\n".join(page_chips_html)

    return f"""  <!-- Table of Contents (ToC) Modal Drawer -->
  <div id="tocOverlay" class="toc-overlay" aria-hidden="true">
    <div class="toc-modal" role="dialog" aria-modal="true" aria-labelledby="tocModalTitle">
      <div class="toc-header">
        <div class="toc-header-title-wrap">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="8" y1="6" x2="21" y2="6"></line>
            <line x1="8" y1="12" x2="21" y2="12"></line>
            <line x1="8" y1="18" x2="21" y2="18"></line>
            <line x1="3" y1="6" x2="3.01" y2="6"></line>
            <line x1="3" y1="12" x2="3.01" y2="12"></line>
            <line x1="3" y1="18" x2="3.01" y2="18"></line>
          </svg>
          <h3 id="tocModalTitle">فہرستِ مضامین (Table of Contents)</h3>
        </div>
        <button type="button" id="tocClose" class="toc-close-btn" aria-label="بند کریں">&times;</button>
      </div>

      <!-- Reading Resume Banner in ToC -->
      <div id="tocResumeBanner" class="toc-resume-banner" style="display:none;">
        <div class="toc-resume-info">
          <span class="toc-resume-badge">آخری مطالعہ (Last Read)</span>
          <span id="tocResumeTitle" class="toc-resume-title">صفحہ ۱</span>
        </div>
        <button type="button" id="tocResumeBtn" class="toc-resume-btn">
          <span>یہیں سے جاری رکھیں</span>
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
        </button>
      </div>

      <!-- Navigation Tabs -->
      <div class="toc-tabs">
        <button type="button" class="toc-tab-btn active" data-toc-tab="sections">
          <span>ابواب و مضامین</span>
          <small>Sections</small>
        </button>
        <button type="button" class="toc-tab-btn" data-toc-tab="pages">
          <span>صفحات کا انتخاب</span>
          <small>Page Jump (1–18)</small>
        </button>
      </div>

      <div class="toc-body">
        <!-- Sections Tab Content -->
        <div id="tocTabSections" class="toc-tab-pane active">
          <ul class="toc-section-list">
{sections_list_html}
          </ul>
        </div>

        <!-- Pages Tab Content -->
        <div id="tocTabPages" class="toc-tab-pane">
          <div class="toc-page-intro">
            <span>کتاب کے اصل صفحات پر براہِ راست جائیں (Jump directly to any book page):</span>
          </div>
          <div class="toc-page-grid">
{pages_grid_html}
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Floating Resume Reading Toast -->
  <div id="resumeToast" class="resume-toast" aria-hidden="true">
    <div class="resume-toast-content">
      <div class="resume-toast-icon">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
      </div>
      <span id="resumeToastText" class="resume-toast-text">آخری مطالعہ: صفحہ ۱</span>
    </div>
    <div class="resume-toast-actions">
      <button type="button" id="resumeToastBtn" class="resume-toast-btn">پڑھیں</button>
      <button type="button" id="resumeToastDismiss" class="resume-toast-dismiss" aria-label="Dismiss">&times;</button>
    </div>
  </div>"""

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
    <a href="index.html" class="header-branding" title="گُلِسْتَانِ سَعْدِیْ — صفحۂ اول">
      <img src="images/header_logo.png" alt="گُلِسْتَانِ مُتَرْجَمْ" class="header-logo-img"/>
      <span class="header-subtitle">{subtitle}</span>
    </a>
    <div class="header-controls">
      <button type="button" id="tocToggle" class="header-btn" aria-label="فہرستِ مضامین / Table of Contents" title="فہرستِ مضامین (Table of Contents)">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <line x1="8" y1="6" x2="21" y2="6"></line>
          <line x1="8" y1="12" x2="21" y2="12"></line>
          <line x1="8" y1="18" x2="21" y2="18"></line>
          <line x1="3" y1="6" x2="3.01" y2="6"></line>
          <line x1="3" y1="12" x2="3.01" y2="12"></line>
          <line x1="3" y1="18" x2="3.01" y2="18"></line>
        </svg>
        <span>فہرست</span>
      </button>
      <button type="button" id="settingsToggle" class="header-btn" aria-label="ترتیبات / Reader Settings" title="ترتیبات (Settings)">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
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
        <!-- Edition Mode Switcher -->
        <div class="setting-group">
          <div class="setting-label">
            <span class="label-title">Edition Mode (ورژن کا انتخاب)</span>
            <span class="label-desc">Switch between Faithful Original and English Study Edition</span>
          </div>
          <div class="edition-switcher">
            <a href="original.html" class="edition-btn {orig_active}">
              <span class="edition-title">Faithful Original</span>
              <span class="edition-title-ur">اصل متن مع ترجمہ</span>
              <span class="edition-desc">Persian text, Urdu interlinear &amp; footnotes only</span>
            </a>
            <a href="study.html" class="edition-btn {study_active}">
              <span class="edition-title">Study Edition 🇬🇧</span>
              <span class="edition-title-ur">ایڈیشن مطالعہ و فرہنگ</span>
              <span class="edition-desc">Bilingual explanations, vocabulary &amp; English notes</span>
            </a>
          </div>
        </div>

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

{toc_html}

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
                m_html = """<div class="frontispiece-card" id="frontispiece">
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

    # Gather all bilingual entries across batches by book page
    bilingual_pages = {}
    for b in batches:
        for sec in b["sections"]:
            if sec.get("content_type") == "bilingual_text":
                for e in sec.get("entries", []):
                    bp = str(e.get("book_page") or "1")
                    if bp not in bilingual_pages:
                        bilingual_pages[bp] = []
                    bilingual_pages[bp].append(e)

    if bilingual_pages:
        d_header = '<h2 class="chapter-main-title">دِیْبَاجَہ (مقدمۂ کتاب)</h2>'
        body_orig.append(d_header)
        body_study.append(d_header)

        # Reading toolbar with Expand/Collapse All English Notes button (Study Edition only)
        study_toolbar = """<div class="study-reading-toolbar">
  <button type="button" id="toggleAllNotesBtn" class="btn-toggle-notes" title="تمام انگریزی نوٹس اور ترجمہ کھولیں یا چھپائیں">
    <span style="font-size:1.15rem;line-height:1;">🇬🇧</span>
    <span id="toggleAllNotesText">انگریزی نوٹس و ترجمہ کھولیں (Show English Notes &amp; Translation)</span>
  </button>
</div>"""
        body_study.append(study_toolbar)

        sorted_pages = sorted(bilingual_pages.keys(), key=lambda x: int(x) if x.isdigit() else 999)
        for bp in sorted_pages:
            bp_num = int(bp) if bp.isdigit() else 1
            if bp_num >= 25:
                sec_title = "باب ۱"
            else:
                sec_title = "دیباچہ"

            if bp_num == 25:
                c1_header = '<h2 class="chapter-main-title" id="chapter_1">بَابِ اَوَّلْ: دَرْ سِیْرَتِ پَادْشَاہَاں</h2>'
                body_orig.append(c1_header)
                body_study.append(c1_header)

            page_entries = bilingual_pages[bp]
            orig_page_html = render_book_page(sec_title, bp, page_entries, is_study=False)
            study_page_html = render_book_page(sec_title, bp, page_entries, is_study=True)
            body_orig.append(orig_page_html)
            body_study.append(study_page_html)

    toc_html = render_toc_html(batches, bilingual_pages)

    with open(os.path.join(HTML_DIR, "original.html"), "w", encoding="utf-8") as f:
        f.write(header_template.format(
            title="گلستان سعدی — اصل متن مع ترجمہ",
            subtitle="اصل متن مع ترجمہ"
        ) + "\n".join(body_orig) + footer_template.format(
            orig_active="active",
            study_active="",
            toc_html=toc_html
        ))

    with open(os.path.join(HTML_DIR, "study.html"), "w", encoding="utf-8") as f:
        f.write(header_template.format(
            title="گلستان سعدی — ایڈیشن مطالعہ و فرہنگ",
            subtitle="ایڈیشن مطالعہ و فرہنگ"
        ) + "\n".join(body_study) + footer_template.format(
            orig_active="",
            study_active="active",
            toc_html=toc_html
        ))

    # Also write index.html in HTML_DIR
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
    with open(os.path.join(HTML_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)

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
table.verse-table {
    width: 100%;
    margin: 1em 0;
    border-collapse: collapse;
    border: 1px solid #c4ded0;
    background-color: #f7fbf8;
}
table.verse-table td {
    width: 50%;
    text-align: center;
    vertical-align: top;
    padding: 0.6em 0.8em;
}
table.verse-table td.col-divider {
    border-left: 1px solid #165c32;
}
.verse-ornament {
    text-align: center;
    font-size: 1.15em;
    font-weight: bold;
    color: #165c32;
    margin: 1.2em 0 0.3em 0;
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
                    entry_o = ""
                    if e.get("section_banner"):
                        sb = e["section_banner"]
                        entry_o += f"""<div style="margin:22px 0 16px 0;padding:12px 16px;background:#e2f0e6;border:2px solid #165c32;border-radius:6px;text-align:center;">
  <div style="font-size:1.35em;font-weight:bold;color:#165c32;line-height:2.0;">{escape_xml(sb.get("persian",""))}</div>
  <div style="font-size:0.95em;color:#4a5c52;margin-top:4px;line-height:1.8;">{escape_xml(sb.get("urdu",""))}</div>
</div>"""
                    entry_o += f'<div id="{e["id"]}">'
                    if e["type"] in ["bismillah", "quran"]:
                        entry_o += f'<div class="quran">{escape_xml(e.get("persian") or e.get("arabic"))}</div>'
                        entry_o += f'<div class="urdu-interlinear" style="text-align:center;">{escape_xml(e["urdu_interlinear"])}</div>'
                    elif e["type"] == "prose":
                        entry_o += f'<div class="persian-text">{escape_xml(e["persian"])}</div>'
                        entry_o += f'<div class="urdu-interlinear">{escape_xml(e["urdu_interlinear"])}</div>'
                    elif e["type"] == "couplet":
                        if e.get("header_persian"):
                            entry_o += f'<div class="verse-ornament">✤ {escape_xml(e["header_persian"])} ✤</div>'
                        entry_o += f"""<table class="verse-table">
  <tr>
    <td>
      <div class="persian-text" style="font-size:1.15em;margin:0;">{escape_xml(e["persian_m1"])}</div>
      <div class="urdu-interlinear" style="border:none;margin:0.2em 0 0 0;padding:0;">{escape_xml(e["urdu_m1"])}</div>
    </td>
    <td class="col-divider">
      <div class="persian-text" style="font-size:1.15em;margin:0;">{escape_xml(e["persian_m2"])}</div>
      <div class="urdu-interlinear" style="border:none;margin:0.2em 0 0 0;padding:0;">{escape_xml(e["urdu_m2"])}</div>
    </td>
  </tr>
</table>"""
                    elif e["type"] == "stanza":
                        if e.get("header_persian"):
                            entry_o += f'<div class="verse-ornament">✤ {escape_xml(e["header_persian"])} ✤</div>'
                        for l in e.get("lines", []):
                            entry_o += f"""<table class="verse-table">
  <tr>
    <td>
      <div class="persian-text" style="font-size:1.15em;margin:0;">{escape_xml(l["persian_m1"])}</div>
      <div class="urdu-interlinear" style="border:none;margin:0.2em 0 0 0;padding:0;">{escape_xml(l["urdu_m1"])}</div>
    </td>
    <td class="col-divider">
      <div class="persian-text" style="font-size:1.15em;margin:0;">{escape_xml(l["persian_m2"])}</div>
      <div class="urdu-interlinear" style="border:none;margin:0.2em 0 0 0;padding:0;">{escape_xml(l["urdu_m2"])}</div>
    </td>
  </tr>
</table>"""

                    if e.get("footnotes"):
                        entry_o += '<div class="footnotes"><strong>حواشی:</strong><br/>'
                        for fn in e["footnotes"]:
                            entry_o += f'• {escape_xml(fn)}<br/>'
                        entry_o += '</div>'
                    entry_o += '</div>'

                    body_o += entry_o + '<hr/>'
                    body_s += entry_o

                    # Study rendering
                    english_trans = e.get("english_trans", "")
                    study = e.get("study", {})
                    if english_trans or study.get("vocabulary") or study.get("notes_en") or study.get("notes_ur"):
                        body_s += '<div class="study-box">'
                        if english_trans:
                            body_s += f'<div style="font-style:italic;margin-bottom:0.7em;color:#1a221e;background:#faf7f0;padding:8px 12px;border-left:3px solid #996515;"><strong>English Translation:</strong> “{escape_xml(english_trans)}”</div>'
                        if study.get("notes_en"):
                            body_s += f'<p><strong>Study Note (English):</strong> {escape_xml(study["notes_en"])}</p>'
                        if study.get("notes_ur"):
                            body_s += f'<p><strong>وضاحت (اردو):</strong> {escape_xml(study["notes_ur"])}</p>'
                        if study.get("vocabulary"):
                            body_s += '<table class="vocab"><tr><th>لفظ</th><th>English</th><th>معنی (اردو)</th><th>اردو مشترک الفاظ</th></tr>'
                            for v in study["vocabulary"]:
                                body_s += f'<tr><td><strong>{escape_xml(v["persian"])}</strong></td><td>{escape_xml(v.get("meaning_en",""))}</td><td>{escape_xml(v.get("meaning_ur",""))}</td><td>{escape_xml(v.get("urdu_cognates",""))}</td></tr>'
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
