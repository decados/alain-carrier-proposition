"""Static contract checks for the three self-contained site versions."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import re
import unittest

SITE = Path(__file__).resolve().parents[1] / 'site'
VERSIONS = (SITE / 'index.html', SITE / 'v1/index.html', SITE / 'v2/index.html')


class Inventory(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []
        self.assets = []
        self.meta = []
        self.images = []
        self.headings = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            self.ids.add(a['id'])
        if tag == 'a':
            self.links.append(a.get('href', ''))
        if tag in ('script', 'link', 'img'):
            self.assets.append(a.get('src', a.get('href', '')))
        if tag == 'img':
            self.images.append(a)
        if tag == 'meta':
            self.meta.append(a)
        if tag == 'h1':
            self.headings.append(a)


def parse(text):
    page = Inventory()
    page.feed(text)
    return page


class SiteChecks(unittest.TestCase):
    def test_links_anchors_assets_and_indexing_for_every_version(self):
        for path in VERSIONS:
            with self.subTest(path=path):
                page = parse(path.read_text())
                for href in page.links:
                    if href.startswith('#'):
                        self.assertIn(href[1:], page.ids, (path, href))
                    elif not href.startswith(('mailto:', 'http://', 'https://')):
                        self.assertTrue((path.parent / urlsplit(href).path).is_file(), (path, href))
                for asset in page.assets:
                    if asset.startswith(('./', '../')):
                        self.assertTrue((path.parent / urlsplit(asset).path).is_file(), (path, asset))
                self.assertTrue(all('alt' in image for image in page.images))
                self.assertTrue(any(m.get('name') == 'robots' and m.get('content') == 'noindex,nofollow' for m in page.meta))
                self.assertTrue(any(h.startswith('mailto:alaincarrier.cla@gmail.com') for h in page.links))
                self.assertEqual(len(page.headings), 1)
                self.assertIn('Disallow: /', (path.parent / 'robots.txt').read_text())

    def test_identity_and_brand_at_top(self):
        html = VERSIONS[0].read_text()
        hero = html.split('id="ceremonies"')[0]
        for text in ('Alain Carrier', 'Célébrant laïc agréé', 'Grand-Montréal', 'célébrations funéraires', 'Écrire à Alain', 'logo-acr.png', 'alain-carrier.jpg'):
            self.assertIn(text, hero)
        for target in ('#ceremonies', '#approche', '#alain', '#contact'):
            self.assertIn(f'href="{target}"', html)
        css = (SITE / 'styles.css').read_text()
        self.assertIn('width:236px', css)  # ACR must not revert to a 64px badge.
        for font in ('dm-sans.ttf', 'newsreader.ttf'):
            self.assertIn(font, css)
            self.assertTrue((SITE / 'assets/fonts' / font).is_file())

    def test_contact_fallback_and_no_collection(self):
        html = VERSIONS[0].read_text()
        script = (SITE / 'script.js').read_text()
        page = parse(html)
        self.assertIn('href="#contenu"', html)
        self.assertEqual(len(re.findall('type="radio"', html)), 2)
        self.assertIn('mailto:alaincarrier.cla@gmail.com?subject=', html)
        self.assertIn('mailto:alaincarrier.cla@gmail.com"', html)
        self.assertIn('encodeURIComponent(subject)', script)
        self.assertIn('encodeURIComponent(body)', script)
        self.assertIn("addEventListener('change', updateEmail)", script)
        self.assertIn('prefers-reduced-motion:reduce', (SITE / 'styles.css').read_text())
        for forbidden in ('fetch(', 'localStorage', 'sessionStorage', 'sendBeacon', 'XMLHttpRequest', '<form', 'navigator.send'):
            self.assertNotIn(forbidden, html + script)
        self.assertTrue(page.ids.issuperset({'contact', 'contenu'}))

    def test_versions_are_presented_as_finished_sites(self):
        for path in VERSIONS:
            html = path.read_text().lower()
            for term in ('proposition de site', 'pour validation', 'brouillon de site', 'class="preview"'):
                self.assertNotIn(term, html, (path, term))
        current = VERSIONS[0].read_text().lower()
        for term in ('514-', '438-', 'tarif de', 'années d’expérience', 'mariage', 'crémation personnalisée'):
            self.assertNotIn(term, current)

if __name__ == '__main__':
    unittest.main()
