from urlparse import urlsplit, urlunsplit, parse_qsl, urljoin

import re
import urlnorm
from string_utils import rstrip_string


class HttpUrl:
    # BASE_PATTERN = r'https?://([a-z]\.[a-z]{2,3}|\d{1,3}(\.\d{1,3}){3})'

    def __init__(self, raw, base=None, repair=True):
        try:
            self.raw = raw
            self.canonical = None
            self.encoded = None
            self.unencoded = None

            self.raw_subdomain = ''
            self.raw_sldomain = ''
            self.raw_tld = ''
            self.raw_port = ''
            self.is_absolute = None

            self._parse_raw()

            if repair:
                self._handle_missing_netloc()

            if (not self.is_absolute) and base:
                self.raw = urljoin(base, self.raw)
                self._parse_raw()

            if not self.is_valid():
                raise Exception()
        except Exception, ex:
            raise Exception(self.raw + " is not a valid HTTP URL")


    netloc_port_pattern = re.compile(r":\d{1,5}?$")
    common_netloc_pattern = re.compile(r"\.(com|net|org|info|biz)(\.[a-z]{2})?(:(80|443))?$")

    def _handle_missing_netloc(self):
        if self.is_absolute:
            return

        parts = self.raw.split('/', 2)
        possible_netloc = parts[0].lower()

        m = HttpUrl.netloc_port_pattern.search(possible_netloc)
        if m:
            if m.group(0) == ':80':
                self.raw = 'https://' + self.raw
            elif m.group(0) == ':443':
                self.raw = 'http://' + self.raw

        colon_pos = possible_netloc.find(':')

        if possible_netloc.startswith('www') or HttpUrl.common_netloc_pattern.match(possible_netloc):
            if possible_netloc.endswith('443'):
                self.raw = 'https://' + self.raw
            else:
                self.raw = 'http://' + self.raw
            self._parse_raw()
        elif colon_pos != -1:
            self.raw_scheme = ''
            self.raw_netloc = possible_netloc
            self.raw_path = '/'

    def _parse_raw(self):
        self.raw_scheme, self.raw_netloc, self.raw_path, self.raw_query, self.raw_fragment = urlsplit(self.raw)
        self._parse_netloc()
        self.is_absolute = bool(self.raw_scheme and self.raw_netloc)

    def _parse_netloc(self):
        if not self.raw_netloc:
            return

        parts = self.raw_netloc.split('.')
        self.raw_tld = parts[-1]
        if ':' in self.raw_tld:
            self.raw_tld, self.raw_port = self.raw_tld.split(':')
        else:
            self.raw_port = ''
        self.raw_domain = parts[-2]
        self.raw_subdomain = '.'.join(parts[:-2])

    def is_valid(self):
        if self.is_absolute:
            if (self.raw_scheme != 'http' and self.raw_scheme != 'https') or self.raw_tld[0] in [0, 1, 2, 3, 4, 5, 6, 7,
                                                                                                 8, 9]:
                return False

        return True

    def get_encoded(self):

        pass

    def get_unencoded(self):
        pass

    def get_canonical(self, include_fragment=False):
        if not self.canonical:
            self._canonize()

        if include_fragment and self.canonical_fragment:
            return self.canonical + '#' + self.canonical_fragment
        else:
            return self.canonical

    def _canonize(self):
        if self.is_absolute:
            self.canonical_scheme, self.canonical_netloc, self.canonical_path, self.canonical_query, self.canonical_fragment \
                = urlsplit(urlnorm.norm(self.raw))
        else:
            self.canonical_scheme, self.canonical_netloc, self.canonical_path, self.canonical_query, self.canonical_fragment \
                = self.raw_scheme, self.raw_netloc, self.raw_path, self.raw_query, self.raw_fragment

        self.canonical_scheme = self.canonical_scheme.lower()

        if self.raw_scheme.endswith('s'):
            self.canonical_netloc, _ = rstrip_string(self.canonical_netloc, ':443')
        else:
            self.canonical_netloc, _ = rstrip_string(self.canonical_netloc, ':80')

        self.canonical_netloc = self.canonical_netloc.lower()

        self.canonical_path = '' if self.canonical_path == '/' else self.canonical_path

        params = parse_qsl(self.canonical_query, True)
        self.canonical_query_params = [(k, v) for (k, v) in sorted(params)]

        self.canonical = urlunsplit((self.canonical_scheme, self.canonical_netloc, self.canonical_path,
                                     self.canonical_query, ''))


class StrictHttpUrl(HttpUrl):
    pass
