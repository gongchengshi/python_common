from urlparse import urljoin
from StringIO import StringIO
from lxml import etree


class SitemapParser:
    def __init__(self, root_url, fetch):
        self.base_url = root_url
        self.fetch = fetch
        self.urls = set()
        self.sitemap_urls = set()
        self._sitemap_index_urls = set()

    def process(self, known_sitemaps_urls=None):
        if known_sitemaps_urls:
            self.urls.update(self._process_sitemap_url_list(known_sitemaps_urls))
        self.urls.update(self._process_sitemap_url_list([urljoin(self.base_url, 'sitemap.xml'),
                                                         urljoin(self.base_url, 'sitemap.txt')]))

    def _process_sitemap_url_list(self, sitemap_urls):
        urls = set()
        for sitemap_url in sitemap_urls:
            content = self.fetch(sitemap_url)
            if content:
                self.sitemap_urls.add(sitemap_url)
                if sitemap_url.endswith('txt'):
                    urls.update(self.parse_txt(content))
                elif sitemap_url.endswith('xml'):
                    urls.update(self.process_xml(content, sitemap_url))
        return urls

    def process_xml(self, content, sitemap_url):
        tree = etree.parse(StringIO(content))
        if tree.docinfo.root_name == 'sitemapindex':
            if sitemap_url in self._sitemap_index_urls:  # This protects against infinite recursive looping
                return []
            else:
                self._sitemap_index_urls.add(sitemap_url)
            locs = tree.xpath('//*[name()="loc"]/text()')

            sitemap_urls = [loc for loc in [text.strip() for text in locs] if loc.startswith('http')]
            return self._process_sitemap_url_list(sitemap_urls)
        elif tree.docinfo.root_name == 'urlset':
            return self.parse_xml(content)
        else:
            return []

    @staticmethod
    def parse_xml(content):
        tree = etree.parse(StringIO(content))
        locs = tree.xpath('//*[substring(name(), string-length(name())-2)="loc"]/text()')
        return [loc for loc in [text.strip() for text in locs] if loc.startswith('http')]

    @staticmethod
    def parse_txt(content):
        return [line for line in content.splitlines() if line.startswith('http')]
