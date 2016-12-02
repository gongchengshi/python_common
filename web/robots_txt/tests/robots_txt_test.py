import unittest
import time

from python_common.web.robots_txt.rerp_wrapper import RerpWrapper as RobotsTxtParser
# from python_common.web.robots_txt.reppy_wrapper import ReppyWrapper as RobotsTxtParser


class TestParserWrapper(unittest.TestCase):
    def setUp(self):
        self.url = 'https://www.selinc.com/myaccount/login.aspx'
        self.agent = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'

    def test_disallow_all(self):
        content = """
User-agent: *
Disallow: /
"""
        parser = RobotsTxtParser(content)
        self.assertFalse(parser.allowed(self.agent, self.url))

    def test_disallow_rules_split(self):
        content = """
User-agent: *
Disallow: /workarea/
User-agent: *
Disallow: /
        """
        parser = RobotsTxtParser(content)
        self.assertFalse(parser.allowed(self.agent, self.url))

    def test_disallow_some(self):
        content = """
User-agent: *
Disallow: /myaccount/
        """
        parser = RobotsTxtParser(content)
        self.assertFalse(parser.allowed(self.agent, self.url))

    def test_empty_content(self):
        parser = RobotsTxtParser('')
        self.assertTrue(parser.allowed(self.agent, self.url))

        parser = RobotsTxtParser()
        self.assertTrue(parser.allowed(self.agent, self.url))

    def test_capitalization(self):
        content = """
User-agent: *
Disallow: /workarea/
        """

        parser = RobotsTxtParser(content)
        self.assertFalse(parser.allowed(self.agent, "https://www.selinc.com/workarea/FrameworkUI/"))

        self.assertFalse(parser.allowed(self.agent, "https://www.selinc.com/WorkArea/FrameworkUI/"))

    def test_expired(self):
        content = "#robots.txt"
        parser = RobotsTxtParser(content, time.time() + 2)
        self.assertFalse(parser.expired)
        time.sleep(3)
        self.assertTrue(parser.expired)
