"""Static checks for both published proposals, without build dependencies."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import unittest

SITE = Path(__file__).resolve().parents[1] / 'site'
V2 = (SITE / 'index.html').read_text()
CSS = (SITE / 'v2.css').read_text()
JS = (SITE / 'v2.js').read_text()


class Inventory(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []
        self.assets = []
        self.meta = []
        self.images = []
        self.inputs = []
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
        if tag == 'input':
            self.inputs.append(a)
        if tag in ('h1', 'h2', 'h3'):
            self.headings.append(tag)


def parse(text):
    page = Inventory()
    page.feed(text)
    return page


class SiteChecks(unittest.TestCase):
    def test_links_and_assets_in_both_versions(self):
        for path in (SITE / 'index.html', SITE / 'v1/index.html'):
            page = parse(path.read_text())
            for href in page.links:
                if href.startswith('#'):
                    self.assertIn(href[1:], page.ids, (path, href))
                elif not href.startswith(('mailto:', 'http://', 'https://')):
                    self.assertTrue((path.parent / urlsplit(href).path).exists(), (path, href))
            for asset in page.assets:
                if asset.startswith(('./', '../')):
                    self.assertTrue((path.parent / urlsplit(asset).path).is_file(), (path, asset))
            self.assertTrue(all('alt' in image for image in page.images))
            self.assertTrue(any(m.get('name') == 'robots' and m.get('content') == 'noindex,nofollow' for m in page.meta))
            self.assertTrue(any(h.startswith('mailto:alaincarrier.cla@gmail.com') for h in page.links))
            self.assertEqual(page.headings.count('h1'), 1)
        self.assertIn('Disallow: /', (SITE / 'robots.txt').read_text())
        self.assertIn('Disallow: /', (SITE / 'v1/robots.txt').read_text())

    def test_first_screen_identity_and_clear_navigation(self):
        hero = V2.split('</section>', 1)[0]
        for text in ('Alain Carrier', 'Célébrant laïc agréé', 'Grand-Montréal', 'cérémonies funéraires', 'Écrire à Alain'):
            self.assertIn(text, hero)
        for target in ('#alain', '#ceremonies', '#accompagnement', '#contact'):
            self.assertIn(f'href="{target}"', V2)
        self.assertIn('src="./assets/alain-carrier.jpg"', hero)
        self.assertIn('src="./assets/logo-acr.png"', hero)


    def test_privacy_and_mail_choices(self):
        self.assertEqual({i.get('value') for i in parse(V2).inputs}, {'hommage', 'question'})
        self.assertTrue(all(i.get('type') == 'radio' for i in parse(V2).inputs))
        self.assertIn('href="#contenu"', V2)
        self.assertIn(':focus-visible', CSS)
        self.assertRegex(CSS, r'prefers-reduced-motion\s*:\s*reduce')
        self.assertRegex(CSS, r'@media\s*\(max-width:\s*700px\)')
        self.assertIn('encodeURIComponent(subject)', JS)
        self.assertIn('encodeURIComponent(body)', JS)
        for forbidden in ('fetch(', 'localStorage', 'sessionStorage', 'sendBeacon', 'XMLHttpRequest', '<form', 'navigator.send'):
            self.assertNotIn(forbidden, V2 + JS)
        for subject in ('Premier contact - célébration hommage', 'Question sur les célébrations'):
            self.assertIn(subject, JS)
        self.assertRegex(JS, r'addEventListener\([\'\"]change[\'\"],\s*updateEmail\)')

    def test_finished_site_copy(self):
        for path in (SITE / 'index.html', SITE / 'v1/index.html'):
            html = path.read_text().lower()
            for term in ('proposition', 'pour validation', 'brouillon', 'class="preview"'):
                self.assertNotIn(term, html, (path, term))

    def test_no_unconfirmed_offers(self):
        for term in ('514-', '438-', 'tarif de', 'années d’expérience', 'mariage', 'crémation personnalisée'):
            self.assertNotIn(term, V2.lower())


if __name__ == '__main__':
    unittest.main()
