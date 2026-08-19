#!/usr/bin/env python3
"""Render every lab Markdown file to PDF, beside the source.

labs/lab-NN-*/README.md    -> labs/lab-NN-*/README.pdf
labs/lab-NN-*/worksheet.md -> labs/lab-NN-*/worksheet.pdf
labs/README.md, labs/tools.md -> the same, beside them

Markdown is converted to HTML in the Tertiary house style (Arial 11pt, blue
headings, real tables, monospace code blocks) and then rendered by LibreOffice,
which is the same engine that produces the deck/LG/LP PDFs — so a lab PDF looks
like the rest of the courseware rather than like a browser print.

Images are inlined as data URIs. A relative <img src> would resolve against the
temp directory LibreOffice renders in, not the repo, and would silently come out
blank.

Usage:
  python3 build_lab_pdfs.py            # convert all, skipping up-to-date PDFs
  python3 build_lab_pdfs.py --force    # reconvert everything
"""
import base64
import mimetypes
import os
import re
import shutil
import subprocess
import sys
import tempfile

import markdown

HERE = os.path.dirname(os.path.abspath(__file__))


def _find_repo(start):
    env = os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env):
        return env
    d = start
    for _ in range(8):
        d = os.path.dirname(d)
        if os.path.isdir(os.path.join(d, "courseware")) and os.path.isdir(os.path.join(d, "labs")):
            return d
    return os.path.dirname(os.path.dirname(HERE))


REPO = _find_repo(HERE)
LABS = os.path.join(REPO, "labs")
SOFFICE = os.environ.get("SOFFICE", "soffice")

CSS = """
@page { size: A4; margin: 18mm 16mm 16mm 16mm; }
body { font-family: Arial, Helvetica, sans-serif; font-size: 11pt; color: #161B26;
       line-height: 1.45; }
h1 { font-size: 20pt; color: #1F6FEB; margin: 0 0 4pt 0; }
h2 { font-size: 14pt; color: #1F6FEB; margin: 16pt 0 4pt 0;
     border-bottom: 1px solid #E2E8F0; padding-bottom: 3pt; }
h3 { font-size: 12pt; color: #10B981; margin: 12pt 0 3pt 0; }
p  { margin: 0 0 6pt 0; }
ul, ol { margin: 0 0 8pt 0; padding-left: 18pt; }
li { margin: 0 0 3pt 0; }
blockquote { margin: 6pt 0; padding: 6pt 10pt; background: #F5F8FC;
             border-left: 3px solid #1F6FEB; color: #5B6372; }
blockquote p { margin: 0 0 3pt 0; }
code { font-family: "Courier New", monospace; font-size: 9.5pt;
       background: #F5F8FC; padding: 1pt 3pt; }
pre { font-family: "Courier New", monospace; font-size: 9pt; background: #0B1220;
      color: #9CDCFE; padding: 8pt 10pt; margin: 4pt 0 8pt 0;
      white-space: pre-wrap; word-wrap: break-word; }
pre code { background: transparent; color: inherit; padding: 0; font-size: 9pt; }
table { border-collapse: collapse; width: 100%; margin: 4pt 0 10pt 0; font-size: 10pt; }
th { background: #1F6FEB; color: #FFFFFF; text-align: left; padding: 5pt 6pt;
     border: 1px solid #C9D4E3; font-size: 9.5pt; }
td { padding: 5pt 6pt; border: 1px solid #C9D4E3; vertical-align: top;
     word-wrap: break-word; }
tr:nth-child(even) td { background: #F7FAFD; }
/* Worksheet "Record as you go": the learner writes in the last column, so it must
   be the widest and every row needs vertical room. Without a fixed layout the
   step text takes the whole width and leaves no space to write in. */
table.worksheet .writein { min-height: 30pt; height: 30pt; }
img { max-width: 100%; }
hr { border: none; border-top: 1px solid #E2E8F0; margin: 12pt 0; }
a { color: #1F6FEB; text-decoration: none; }
.footer { margin-top: 14pt; padding-top: 6pt; border-top: 1px solid #E2E8F0;
          font-size: 8.5pt; color: #5B6372; }
/* A written-on line, in place of a run of underscores. */
.rule { display: inline-block; width: 62%; border-bottom: 1px solid #8A93A0;
        height: 11pt; vertical-align: bottom; }
/* Tick box for "[ ]" list items. */
li.check { list-style: none; margin-left: -12pt; }
li.check:before { content: ""; display: inline-block; width: 9pt; height: 9pt;
                  border: 1px solid #5B6372; margin-right: 6pt;
                  vertical-align: middle; }
"""


def inline_images(html, base_dir):
    """Embed <img src="..."> as data URIs — a relative path would render blank."""
    def repl(m):
        pre, src, post = m.group(1), m.group(2), m.group(3)
        if src.startswith(("http://", "https://", "data:")):
            return m.group(0)
        path = os.path.normpath(os.path.join(base_dir, src))
        if not os.path.isfile(path):
            return m.group(0)
        mime = mimetypes.guess_type(path)[0] or "image/png"
        with open(path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("ascii")
        return f'{pre}data:{mime};base64,{b64}{post}'
    return re.sub(r'(<img[^>]*\ssrc=")([^"]+)(")', repl, html)


def md_to_html(md_path):
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    # The PDF is a standalone handout: links back to sibling .md files are noise.
    text = re.sub(r"\[([^\]]+)\]\((?:\.\./)*[^)]*\.md(?:#[^)]*)?\)", r"\1", text)
    body = markdown.markdown(
        text, extensions=["tables", "fenced_code", "sane_lists", "attr_list"])
    body = inline_images(body, os.path.dirname(md_path))

    # A run of underscores is a fill-in rule in the source. Markdown renders it as
    # literal underscores that wrap badly; draw it as a real ruled line instead.
    body = re.sub(r"_{6,}", '<span class="rule"></span>', body)
    # Checkbox items are for ticking on paper, so give them a real box.
    body = re.sub(r"<li>\s*\[\s*\]\s*", '<li class="check">', body)

    # The worksheet's evidence table is written on by hand, so the observation column
    # must be wide and every row tall. LibreOffice's HTML import ignores CSS
    # `table-layout: fixed` and cell `height`, so the geometry goes in the markup as
    # <col width> plus a spacer div — CSS alone silently produces a squashed column.
    if os.path.basename(md_path) == "worksheet.md":
        body = body.replace(
            "<table>",
            '<table class="worksheet" width="100%" cellspacing="0" cellpadding="4">'
            '<colgroup><col width="42"><col width="330"><col width="300"></colgroup>',
            1)
        body = re.sub(r'(<table class="worksheet">.*?</table>)',
                      lambda m: m.group(1).replace(
                          "<td></td>", '<td><div class="writein"></div></td>'),
                      body, flags=re.S)
    title = os.path.splitext(os.path.basename(md_path))[0]
    m = re.search(r"<h1[^>]*>(.*?)</h1>", body, re.S)
    if m:
        title = re.sub(r"<[^>]+>", "", m.group(1)).strip()
    return (f"<!DOCTYPE html><html><head><meta charset='utf-8'>"
            f"<title>{title}</title><style>{CSS}</style></head><body>{body}"
            f"<div class='footer'>CompTIA Certified A+ Training (Core 1 and Core 2)"
            f"  ·  TGS-2024048317  ·  © 2026 Tertiary Infotech Academy Pte Ltd</div>"
            f"</body></html>")


def main():
    force = "--force" in sys.argv
    targets = sorted(
        [os.path.join(LABS, d, n)
         for d in os.listdir(LABS) if d.startswith("lab-")
         for n in ("README.md", "worksheet.md")
         if os.path.isfile(os.path.join(LABS, d, n))]
        + [p for p in (os.path.join(LABS, "README.md"), os.path.join(LABS, "tools.md"))
           if os.path.isfile(p)])

    todo = []
    for md in targets:
        pdf = md[:-3] + ".pdf"
        if force or not os.path.exists(pdf) or os.path.getmtime(pdf) < os.path.getmtime(md):
            todo.append(md)
    print(f"{len(targets)} markdown file(s); {len(todo)} to convert"
          f"{' (--force)' if force else ''}")
    if not todo:
        return 0

    ok = fail = 0
    with tempfile.TemporaryDirectory() as tmp:
        # One soffice invocation per batch: starting it per file dominates the runtime.
        BATCH = 12
        for i in range(0, len(todo), BATCH):
            chunk = todo[i:i + BATCH]
            names = {}
            for j, md in enumerate(chunk):
                stem = f"{i + j:04d}_{os.path.basename(os.path.dirname(md))}_" \
                       f"{os.path.splitext(os.path.basename(md))[0]}"
                html = os.path.join(tmp, stem + ".html")
                with open(html, "w", encoding="utf-8") as f:
                    f.write(md_to_html(md))
                names[stem] = md
            subprocess.run(
                [SOFFICE, "--headless", "--convert-to", "pdf", "--outdir", tmp]
                + [os.path.join(tmp, s + ".html") for s in names],
                capture_output=True, text=True, timeout=900)
            for stem, md in names.items():
                out = os.path.join(tmp, stem + ".pdf")
                dest = md[:-3] + ".pdf"
                if os.path.exists(out) and os.path.getsize(out) > 800:
                    shutil.move(out, dest)
                    ok += 1
                else:
                    print(f"  ! failed: {os.path.relpath(md, REPO)}")
                    fail += 1
            print(f"  {min(i + BATCH, len(todo))}/{len(todo)}")

    print(f"Done — {ok} PDF(s) written, {fail} failed.")
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
