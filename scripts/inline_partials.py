#!/usr/bin/env python3
"""Inline the shared header/footer into every page as static HTML.

Google often reads a page's raw HTML before (or without) running JavaScript.
When the nav and footer were injected by components.js, the raw HTML of every
page had no links to the home page, the hubs, or the trust pages. This script
writes assets/partials/header.html and footer.html directly into each page
between marker comments, so the links are present without JS.

Re-run after editing either partial:  python3 scripts/inline_partials.py
It is idempotent: it replaces whatever sits between the markers.
"""
import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

HEADER = open('assets/partials/header.html').read().strip().replace('{{BASE}}', '/')
FOOTER = open('assets/partials/footer.html').read().strip().replace('{{BASE}}', '/')

H_START, H_END = '<!-- HEADER:START -->', '<!-- HEADER:END -->'
F_START, F_END = '<!-- FOOTER:START -->', '<!-- FOOTER:END -->'
H_BLOCK = '%s\n%s\n%s' % (H_START, HEADER, H_END)
F_BLOCK = '%s\n%s\n%s' % (F_START, FOOTER, F_END)

changed = 0
for f in glob.glob('**/*.html', recursive=True):
    if f.startswith(('assets/', '.git')):
        continue
    s = open(f).read()
    o = s
    if H_START in s:
        s = re.sub(re.escape(H_START) + r'.*?' + re.escape(H_END), lambda m: H_BLOCK, s, flags=re.S)
    else:
        s = s.replace('<div id="header-placeholder"></div>', H_BLOCK, 1)
    if F_START in s:
        s = re.sub(re.escape(F_START) + r'.*?' + re.escape(F_END), lambda m: F_BLOCK, s, flags=re.S)
    else:
        s = s.replace('<div id="footer-placeholder"></div>', F_BLOCK, 1)
    if s != o:
        open(f, 'w').write(s)
        changed += 1
print('pages updated:', changed)
