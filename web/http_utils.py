from urllib2 import urlopen, URLError
from urlparse import urljoin

def download_robots_txt(url):
    try:
        resp = urlopen(urljoin(url, '/robots.txt'))
        return resp.read()
    except URLError:
        pass  # There is no robots.txt file


import re


ContentTypeHeaderPattern = re.compile(r"(?P<type>.*?)(;|$)(\s?charset=(?P<charset>.*?)(;|$))?", re.IGNORECASE)


def split_content_type_header(content_type_header):
    m = ContentTypeHeaderPattern.search(content_type_header)
    content_type = m.group('type')
    charset = m.group('charset')
    return content_type.lower() if content_type else None, charset.lower() if charset else None


# See robotexclusionrulesparser.py for explanation of this.
try:
    import email.utils as email_utils
except ImportError:
    import rfc822 as email_utils
from datetime import datetime
import calendar


def parse_http_datetime(text):
    time_tuple = email_utils.parsedate_tz(text)
    return None if time_tuple is None else datetime(*time_tuple[:7])


def parse_http_timestamp(text):
    time_tuple = email_utils.parsedate_tz(text)
    return None if time_tuple is None else calendar.timegm(time_tuple)


# datetime parsing and formatting
weekdayname = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
monthname = [None,
             'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
             'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
weekdayname_lower = [name.lower() for name in weekdayname]
monthname_lower = [name and name.lower() for name in monthname]


import time


def sec_since_epoch_to_http_date(sec_since_epoch=None):
    """
    Convert seconds since epoch to HTTP datetime string.
    Example: Tue, 15 Nov 1994 08:12:31 GMT

    @rtype: C{bytes}
    """
    if sec_since_epoch is None:
        ms_since_epoch = time.time()
    year, month, day, hh, mm, ss, wd, y, z = time.gmtime(sec_since_epoch)
    s = "%s, %02d %3s %4d %02d:%02d:%02d GMT" % (weekdayname[wd], day, monthname[month], year, hh, mm, ss)
    return s
