import calendar
from datetime import datetime
import unittest

from python_common.web.http_utils import parse_http_datetime, parse_http_timestamp


class Test_parse_http_datetime(unittest.TestCase):
    def test_parse_http_datetime(self):
        actual = parse_http_datetime(u'Fri, 20 Sep 2013 22:38:58 GMT')
        expected = datetime(2013, 9, 20, 22, 38, 58)

        print actual
        print expected
        self.assertEqual(actual, expected)

    def test_parse_http_timestamp(self):
        actual = parse_http_timestamp(u'Fri, 20 Sep 2013 22:38:58 GMT')
        expected = calendar.timegm(datetime(2013, 9, 20, 22, 38, 58).timetuple())

        print actual
        print expected
        self.assertEqual(actual, expected)
