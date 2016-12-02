from urlparse import urljoin


def create_absolute_url(url, base=''):
    return urljoin(base, url)


from python_common.web.url_utils import url_norm


def canonize_url(absolute_url, lowercase_path=False):
    return url_norm(absolute_url, strip=True, lowercase_path=lowercase_path, remove_fragment=True)[0]
