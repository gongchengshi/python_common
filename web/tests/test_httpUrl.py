from unittest import TestCase
from HttpUrl import HttpUrl

canonical_test_pass = [
    # schema and netloc
    ('http://www.foo.com', None, 'http://www.foo.com'),
    ('http://www.foo.com/', None, 'http://www.foo.com'),
    ('https://www.foo.com', None, 'https://www.foo.com'),
    ('https://www.foo.com/', None, 'https://www.foo.com'),
    # netloc
    ('www.foo.com', None, 'http://www.foo.com'),
    ('www.foo.com/', None, 'http://www.foo.com'),
    ('foo.com', None, 'http://foo.com'),
    ('foo.com/', None, 'http://foo.com'),

    ('www.foo.com:80', None, 'http://www.foo.com'),
    ('www.foo.com:80/', None, 'http://www.foo.com'),
    ('foo.com:80', None, 'http://foo.com'),
    ('foo.com:80/', None, 'http://foo.com'),

    ('www.foo.com:443', None, 'https://www.foo.com'),
    ('www.foo.com:443/', None, 'https://www.foo.com'),
    ('foo.com:443', None, 'https://foo.com'),
    ('foo.com:443/', None, 'https://foo.com'),

    ('foo.com.cn', None, 'http://foo.com.cn'),
    ('foo.com.cn:80', None, 'http://foo.com.cn'),
    ('foo.com.cn:443', None, 'https://foo.com.cn'),

    ('ttt.foo.hhh', None, 'ttt.foo.hhh'),
    ('ttt.foo.hhh/', None, 'ttt.foo.hhh/'),
    ('foo.hhh', None, 'foo.hhh'),
    ('foo.hhh/', None, 'foo.hhh/'),
    # netloc and port
    ('www.foo.com:80', None, 'http://www.foo.com'),
    ('www.foo.com:80/', None, 'http://www.foo.com'),
    ('www.foo.com:443', None, 'https://www.foo.com'),
    ('www.foo.com:443/', None, 'https://www.foo.com'),
    ('foo.com:80', None, 'http://foo.com'),
    ('foo.com:80/', None, 'http://foo.com'),
    ('foo.com:443', None, 'https://foo.com'),
    ('foo.com:443/', None, 'https://foo.com'),
    ('foo.com:81', None, '//foo.com:81'),
    ('foo.com:81/', None, '//foo.com:81'),
    # schema and netloc and port
    ('http://www.foo.com:80', None, 'http://www.foo.com'),
    ('http://www.foo.com:80/', None, 'https://www.foo.com'),
    ('https://www.foo.com:443', None, 'https://www.foo.com'),
    ('https://www.foo.com:443/', None, 'https://www.foo.com'),
    ('http://www.foo.com:443', None, 'http://www.foo.com:443'),
    ('http://www.foo.com:443/', None, 'https://www.foo.com:443'),
    ('https://www.foo.com:80', None, 'https://www.foo.com:80'),
    ('https://www.foo.com:80/', None, 'https://www.foo.com:80'),
    # relative path
    ('/', None, '/'),
    ('/one', None, '/one'),
    ('/one/', None, '/one/'),
    ('/one/', None, '/one/'),
    ('/o ne/', None, '/o%20ne/'),
    ('/one/two', None, '/one/two'),
    ('one', None, '/one'),
    ('one/', None, '/one/'),
    ('one/', None, '/one/'),
    ('o ne/', None, '/o%20ne/'),
    ('one/two', None, '/one/two'),
    ('one/two/', None, '/one/two/'),
    ('on e/t wo', None, '/on%20e/t%20wo'),
    # relative relative path
    ('/../one/two', None, '/one/two'),
    ('/../../one/two', None, '/one/two'),
    ('/./../one/two', None, '/one/two'),
    ('/././one/two', None, '/one/two'),
    ('/.././one/two', None, '/one/two'),

    ('/../one/two/', None, '/one/two/'),
    ('/../../one/two/', None, '/one/two/'),
    ('/./../one/two/', None, '/one/two/'),
    ('/././one/two/', None, '/one/two/'),
    ('/.././one/two/', None, '/one/two/'),

    ('/one/../two', None, '/two'),
    ('/one/../../two', None, '/two'),
    ('/one/.././two', None, '/two'),
    ('/one/./../two', None, '/two'),
    ('/one/././two', None, '/one/two'),

    ('/one/../two/', None, '/two/'),
    ('/one/../../two/', None, '/two/'),
    ('/one/.././two/', None, '/two/'),
    ('/one/./../two/', None, '/two/'),
    ('/one/././two/', None, '/one/two/'),

    ('/../one/../two', None, '/two'),
    ('/../one/../../two', None, '/two'),
    ('/../one/.././two', None, '/two'),
    ('/../one/./../two', None, '/two'),
    ('/../one/././two', None, '/one/two'),

    ('/one/two/..', None, '/one'),
    ('/one/two/.', None, '/one/two'),
    ('/one/two/../..', None, '/'),
    ('/one/two/../.', None, '/one'),
    ('/one/two/./..', None, '/one'),
    ('/one/two/./.', None, '/one/two'),

    ('/one/two/../', None, '/one/'),
    ('/one/two/./', None, '/one/two/'),
    ('/one/two/../../', None, '/'),
    ('/one/two/.././', None, '/one/'),
    ('/one/two/./../', None, '/one/'),
    ('/one/two/././', None, '/one/two/'),

    ('/one/../two/..', None, '/'),
    ('/one/./two/.', None, '/one/two'),
    ('/one/../two/.', None, '/two'),
    ('/one/./two/..', None, '/one'),

    ('/one/../two/../', None, '/'),
    ('/one/./two/./', None, '/one/two/'),
    ('/one/../two/./', None, '/two/'),
    ('/one/./two/../', None, '/one/'),

]

assume_http_pass = [
    ('http://www.foo.com', None, 'http://www.foo.com'),
    # netloc
    ('www.foo.com', None, 'http://www.foo.com'),
    ('www.foo.com/', None, 'http://www.foo.com'),
    ('foo.com', None, 'http://foo.com'),
    ('foo.com/', None, 'http://foo.com'),
    # netloc and port
    ('www.foo.com:80', None, 'http://www.foo.com'),
    ('www.foo.com:80/', None, 'http://www.foo.com'),
    ('www.foo.com:443', None, 'https://www.foo.com'),
    ('www.foo.com:443/', None, 'https://www.foo.com'),
    ('foo.com:80', None, 'http://foo.com'),
    ('foo.com:80/', None, 'http://foo.com'),
    ('foo.com:443', None, 'https://foo.com'),
    ('foo.com:443/', None, 'https://foo.com'),
    ('foo.com:81', None, 'http://foo.com:81'),
    ('foo.com:81/', None, 'http://foo.com:81'),
]

fail_test_cases = [
    ('', None),
    ('.com', None),
    ('.foo.com', None),
    ('www.foo.bad_top_level', None),
    ('https://www.foo.3com/', None),
    ('http:/www.foo.bad_top_level', None),
    ('ftp://www.foo.bad_top_level', None),
]


class TestHttpUrl(TestCase):
    def test_is_valid(self):
        self.fail()

    def test_get_encoded(self):
        self.fail()

    def test_get_unencoded(self):
        self.fail()

    def test_get_single_canonical(self):
        url, base, expected =('foo.com:81/', None, 'foo.com:81')
        try:
            actual = HttpUrl(url, base).get_canonical()
            self.assertEqual(actual, expected)
        except AssertionError:
            raise

    def test_get_canonical(self):
        for url, base, expected in canonical_test_pass:
            try:
                actual = HttpUrl(url, base).get_canonical()
                self.assertEqual(actual, expected, "%s != %s\n%s , %s" % (actual, expected, url, base))
            except AssertionError:
                raise

    def test__canonize(self):
        self.fail()



