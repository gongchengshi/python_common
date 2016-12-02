import unittest

from python_common.web.sitemap_parser import SitemapParser


def read_all(path):
    with open(path, 'r') as f:
        return f.read()


def sitemap_index_fetcher(url):
    content = ''
    if url.endswith('sitemap.xml'):
        content = read_all('input/sitemap_parser/sitemap_index_0.xml')
    elif url.endswith('txt'):
        content = read_all('input/sitemap_parser/sitemap_0.txt')
    elif url.endswith('_0.xml'):
        content = read_all('input/sitemap_parser/sitemap_0.xml')
    return content


def sitemap_fetcher(url):
    content = ''
    if url.endswith('txt'):
        content = read_all('input/sitemap_parser/sitemap_0.txt')
    elif url.endswith('xml'):
        content = read_all('input/sitemap_parser/sitemap_0.xml')
    return content


class TestSitemapParser(unittest.TestCase):
    def evaluate(self, target):
        target.process()

        for url in [
            'http://www.example.com/file1.html',
            'http://www.example.com/file2.html',
            'http://www.example.com/foo.html',
            'http://example.com/image.jpg',
            'http://www.example.com/video123.flv',
            'http://www.example.com/videoplayer.swf?video=123',
            'http://www.example.com/thumbs/123.jpg'
        ]:
            self.assertIn(url, target.urls)

    def test_process_sitemap(self):
        target = SitemapParser('http://www.example.com', sitemap_fetcher)

        self.evaluate(target)

        for sitemap_url in ['http://www.example.com/sitemap.xml', 'http://www.example.com/sitemap.txt']:
            self.assertIn(sitemap_url, target.sitemap_urls)

    def test_process_sitemap_index(self):
        target = SitemapParser('http://www.example.com', sitemap_index_fetcher)
        self.evaluate(target)

        for sitemap_url in ['http://www.example.com/sitemap_0.xml', 'http://www.example.com/sitemap_0.txt']:
            self.assertIn(sitemap_url, target.sitemap_urls)
