"""Checks sans dépendances pour la version statique publiée."""
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

SITE = Path(__file__).resolve().parents[1] / 'site'
HTML = (SITE / 'index.html').read_text()
CSS = (SITE / 'styles.css').read_text()
JS = (SITE / 'script.js').read_text()


class Inventory(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []
        self.images = []
        self.meta = []
        self.inputs = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            self.ids.add(a['id'])
        if tag == 'a':
            self.links.append(a.get('href', ''))
        if tag == 'img':
            self.images.append(a)
        if tag == 'meta':
            self.meta.append(a)
        if tag == 'input':
            self.inputs.append(a)


class SiteChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.page = Inventory()
        cls.page.feed(HTML)

    def test_local_links_and_assets(self):
        for href in self.page.links:
            if href.startswith('#'):
                self.assertIn(href[1:], self.page.ids)
            elif not href.startswith('mailto:'):
                self.assertTrue((SITE / href).exists(), href)
        for image in self.page.images:
            self.assertTrue((SITE / image['src']).is_file(), image)
            self.assertIn('alt', image)

    def test_no_index_and_contact(self):
        self.assertTrue(any(m.get('name') == 'robots' and m.get('content') == 'noindex,nofollow' for m in self.page.meta))
        self.assertIn('Disallow: /', (SITE / 'robots.txt').read_text())
        self.assertTrue(any(h.startswith('mailto:alaincarrier.cla@gmail.com') for h in self.page.links))
        self.assertNotIn('<form', HTML)
        self.assertNotIn('localStorage', HTML + JS)
        self.assertNotIn('sendBeacon', HTML + JS)
        self.assertNotIn('analytics', HTML + JS)

    def test_keyboard_and_mobile_contract(self):
        self.assertIn('href="#contenu"', HTML)
        self.assertIn('<summary>', HTML)
        self.assertEqual([i.get('value') for i in self.page.inputs], ['souvenirs', 'valeurs', 'musique'])
        self.assertTrue(all(i.get('type') == 'checkbox' for i in self.page.inputs))
        self.assertIn(':focus-visible', CSS)
        self.assertIn('prefers-reduced-motion:reduce', CSS)
        self.assertIn('@media(max-width:550px)', CSS)
        self.assertIn('compose.addEventListener(\'click\'', JS)
        self.assertIn('encodeURIComponent(body)', JS)
        self.assertNotIn('fetch(', JS)

    def test_only_relative_assets(self):
        for path in re.findall(r'''(?:src|href)=["'](\.[^"']+)["']''', HTML):
            self.assertTrue((SITE / path).exists(), path)


if __name__ == '__main__':
    unittest.main()
