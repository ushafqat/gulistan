#!/usr/bin/env python3
"""
epub_packager.py
A standalone, zero-dependency Python module for packaging EPUB 3 (.epub) files.
Compliant with IDPF EPUB 3.2 specifications, with backwards-compatible EPUB 2 NCX toc.
"""

import os
import zipfile
import uuid
from datetime import datetime
import xml.sax.saxutils as saxutils

def escape_xml(text):
    return saxutils.escape(str(text)) if text else ""

class EpubBook:
    def __init__(self, title, identifier=None, language="ur", author="شیخ سعدی شیرازی", direction="rtl"):
        self.title = title
        self.identifier = identifier or f"urn:uuid:{uuid.uuid4()}"
        self.language = language
        self.author = author
        self.direction = direction
        self.chapters = [] # list of dicts: {'id', 'title', 'filename', 'content_xhtml'}
        self.fonts = [] # list of dicts: {'id', 'filename', 'filepath', 'media_type'}
        self.images = [] # list of dicts: {'id', 'filename', 'filepath', 'media_type'}
        self.css_content = ""
        self.cover_image = None

    def set_cover(self, image_filepath):
        self.cover_image = image_filepath

    def add_image(self, image_filepath, filename=None, media_type="image/png"):
        if not filename:
            filename = os.path.basename(image_filepath)
        image_id = f"img_{len(self.images) + 1}"
        self.images.append({
            "id": image_id,
            "filename": filename,
            "filepath": image_filepath,
            "media_type": media_type
        })

    def add_font(self, font_filepath, filename=None, media_type="font/woff"):
        if not filename:
            filename = os.path.basename(font_filepath)
        font_id = f"font_{len(self.fonts) + 1}"
        self.fonts.append({
            "id": font_id,
            "filename": filename,
            "filepath": font_filepath,
            "media_type": media_type
        })

    def add_chapter(self, title, filename, content_body_xhtml):
        chapter_id = f"chap_{len(self.chapters) + 1}"
        self.chapters.append({
            "id": chapter_id,
            "title": title,
            "filename": filename,
            "body": content_body_xhtml
        })

    def set_css(self, css_text):
        self.css_content = css_text

    def write_epub(self, output_filepath):
        os.makedirs(os.path.dirname(os.path.abspath(output_filepath)), exist_ok=True)
        
        # Build EPUB archive
        with zipfile.ZipFile(output_filepath, "w") as zf:
            # 1. mimetype (MUST be first, uncompressed)
            mimetype_info = zipfile.ZipInfo("mimetype")
            mimetype_info.compress_type = zipfile.ZIP_STORED
            zf.writestr(mimetype_info, b"application/epub+zip")

            # 2. META-INF/container.xml
            container_xml = """<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>"""
            zf.writestr("META-INF/container.xml", container_xml)

            # 3. OEBPS/style.css
            default_css = self.css_content or """
body {
    direction: rtl;
    text-align: right;
    font-family: 'Noto Naskh Arabic', serif;
    margin: 1em;
    line-height: 2.0;
}
"""
            zf.writestr("OEBPS/style.css", default_css)

            has_cover = bool(self.cover_image and os.path.exists(self.cover_image))

            # 4. Chapters XHTML
            for chap in self.chapters:
                doc = f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="{self.language}" lang="{self.language}" dir="{self.direction}">
<head>
  <meta charset="utf-8"/>
  <title>{escape_xml(chap['title'])}</title>
  <link rel="stylesheet" type="text/css" href="style.css"/>
</head>
<body dir="{self.direction}">
{chap['body']}
</body>
</html>"""
                zf.writestr(f"OEBPS/{chap['filename']}", doc.encode("utf-8"))

            # 5. OEBPS/nav.xhtml (EPUB 3 navigation document)
            nav_items = "\n".join([
                f'        <li><a href="{c["filename"]}">{escape_xml(c["title"])}</a></li>'
                for c in self.chapters
            ])
            first_chap = self.chapters[0]["filename"] if self.chapters else "cover_metadata.xhtml"
            landmarks_xhtml = ""
            if has_cover:
                landmarks_xhtml = f"""
    <nav epub:type="landmarks" id="landmarks" hidden="">
      <h2>Landmarks</h2>
      <ol>
        <li><a epub:type="cover" href="cover.xhtml">سرورق</a></li>
        <li><a epub:type="toc" href="nav.xhtml">فہرست مضامین</a></li>
        <li><a epub:type="bodymatter" href="{first_chap}">آغاز کتاب</a></li>
      </ol>
    </nav>"""

            nav_xhtml = f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="{self.language}" lang="{self.language}" dir="{self.direction}">
<head>
  <meta charset="utf-8"/>
  <title>Table of Contents</title>
  <link rel="stylesheet" type="text/css" href="style.css"/>
</head>
<body dir="{self.direction}">
  <nav epub:type="toc" id="toc">
    <h1>فہرست مضامین</h1>
    <ol>
{nav_items}
    </ol>
  </nav>{landmarks_xhtml}
</body>
</html>"""
            zf.writestr("OEBPS/nav.xhtml", nav_xhtml.encode("utf-8"))

            # 6. OEBPS/toc.ncx (EPUB 2 backwards compatibility)
            ncx_points = []
            for idx, c in enumerate(self.chapters, start=1):
                ncx_points.append(f"""    <navPoint id="navPoint-{idx}" playOrder="{idx}">
      <navLabel><text>{escape_xml(c['title'])}</text></navLabel>
      <content src="{c['filename']}"/>
    </navPoint>""")
            ncx_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
  <head>
    <meta name="dtb:uid" content="{self.identifier}"/>
    <meta name="dtb:depth" content="1"/>
    <meta name="dtb:totalPageCount" content="0"/>
    <meta name="dtb:maxPageNumber" content="0"/>
  </head>
  <docTitle><text>{escape_xml(self.title)}</text></docTitle>
  <navMap>
{chr(10).join(ncx_points)}
  </navMap>
</ncx>"""
            zf.writestr("OEBPS/toc.ncx", ncx_content.encode("utf-8"))

            # 7. OEBPS/fonts
            for font in self.fonts:
                if os.path.exists(font["filepath"]):
                    with open(font["filepath"], "rb") as ff:
                        zf.writestr(f"OEBPS/fonts/{font['filename']}", ff.read())

            # 8. Cover Image and Cover Page
            has_cover = self.cover_image and os.path.exists(self.cover_image)
            if has_cover:
                with open(self.cover_image, "rb") as cf:
                    zf.writestr("OEBPS/images/cover.jpg", cf.read())
                cover_xhtml = f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="{self.language}" lang="{self.language}" dir="{self.direction}">
<head>
  <meta charset="utf-8"/>
  <title>سرورق</title>
  <style type="text/css">
    body {{ margin: 0; padding: 0; text-align: center; background: #ffffff; }}
    img.cover {{ max-width: 100%; max-height: 100vh; height: auto; object-fit: contain; }}
  </style>
</head>
<body dir="{self.direction}">
  <div style="text-align:center; padding: 0; margin: 0;">
    <img class="cover" src="images/cover.jpg" alt="{escape_xml(self.title)} — سرورق"/>
  </div>
</body>
</html>"""
                zf.writestr("OEBPS/cover.xhtml", cover_xhtml.encode("utf-8"))

            # 9. OEBPS/content.opf
            manifest_items = [
                '    <item id="style" href="style.css" media-type="text/css"/>',
                '    <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
                '    <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>'
            ]
            if has_cover:
                manifest_items.append('    <item id="cover-image" href="images/cover.jpg" media-type="image/jpeg" properties="cover-image"/>')
                manifest_items.append('    <item id="cover-page" href="cover.xhtml" media-type="application/xhtml+xml"/>')

            for font in self.fonts:
                if os.path.exists(font["filepath"]):
                    manifest_items.append(f'    <item id="{font["id"]}" href="fonts/{font["filename"]}" media-type="{font["media_type"]}"/>')

            for img in self.images:
                if os.path.exists(img["filepath"]):
                    with open(img["filepath"], "rb") as imf:
                        zf.writestr(f"OEBPS/images/{img['filename']}", imf.read())
                    manifest_items.append(f'    <item id="{img["id"]}" href="images/{img["filename"]}" media-type="{img["media_type"]}"/>')

            spine_items = []
            if has_cover:
                spine_items.append('    <itemref idref="cover-page"/>')

            for c in self.chapters:
                manifest_items.append(f'    <item id="{c["id"]}" href="{c["filename"]}" media-type="application/xhtml+xml"/>')
                spine_items.append(f'    <itemref idref="{c["id"]}"/>')

            manifest_str = "\n".join(manifest_items)
            spine_str = "\n".join(spine_items)
            date_str = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
            cover_meta = '    <meta name="cover" content="cover-image"/>\n' if has_cover else ''

            content_opf = f"""<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="pub-id" version="3.0" prefix="rendition: http://www.idpf.org/vocab/rendition/#" dir="{self.direction}">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="pub-id">{self.identifier}</dc:identifier>
    <dc:title>{escape_xml(self.title)}</dc:title>
    <dc:language>{self.language}</dc:language>
    <dc:creator>{escape_xml(self.author)}</dc:creator>
    <dc:date>{date_str}</dc:date>
    <meta property="dcterms:modified">{date_str}</meta>
{cover_meta}  </metadata>
  <manifest>
{manifest_str}
  </manifest>
  <spine toc="ncx" page-progression-direction="{self.direction}">
{spine_str}
  </spine>
</package>"""
            zf.writestr("OEBPS/content.opf", content_opf.encode("utf-8"))

        print(f"Successfully created EPUB: {output_filepath}")
        return output_filepath
