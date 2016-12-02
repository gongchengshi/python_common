import unittest

from python_common.web.url_utils import url_norm, InvalidUrl
from python_common.web.tests.canonize_url_test_cases import TestCases


class TestUrlCanonization(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            TestCases.canonical_urls,
            TestCases.case_sensitivity,
            TestCases.slashes,
            TestCases.scheme,
            TestCases.add_scheme,
            TestCases.fix_scheme,
            TestCases.port,
            TestCases.relative_paths,
            TestCases.back_slashes,
            TestCases.query,
            TestCases.authentication,
            TestCases.fragment,
            TestCases.tld_dot,
            TestCases.ends_with,
            ##TestCases.idna
        ]

    def get_msg(self, input, actual, expected):
        return "\nInput   : %s\nActual  : %s\nExpected: %s" % (input, actual, expected)


    # def test_CanonizeUrl_single(self):
    #     input = 'http://.com/'
    #     expected = ''
    #
    #     actual = url_norm(input, strip=True, remove_fragment=True)[0]
    #     self.assertEqual(expected, actual, self.get_msg(input, actual, expected))


    def test_CanonizeUrl(self):
        for case_set in self.test_cases:
            if type(case_set) is list:
                for input in case_set:
                    #actual = CanonizeUrl(input)
                    actual = url_norm(input, strip=True, remove_fragment=True)[0]
                    self.assertEqual(input, actual)
            elif type(case_set) is dict:
                for input, expected in case_set.iteritems():
                    #actual = CanonizeUrl(input)
                    actual = url_norm(input, strip=True, remove_fragment=True)[0]
                    self.assertEqual(expected, actual, self.get_msg(input, actual, expected))
            else:
                raise Exception()

    def test_invalid_urls(self):
        for input in TestCases.invalid_urls:
            try:
                # actual = url_norm(input, strip=True, remove_fragment=True)[0]
                self.assertRaises(InvalidUrl, url_norm, input, strip=True, remove_fragment=True)
            except AssertionError:
                print 'Input   : %s' % input
