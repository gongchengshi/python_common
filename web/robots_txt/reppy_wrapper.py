from reppy.parser import Rules
import time

import python_common.web.robots_txt.parser_base


class ReppyWrapper(python_common.web.robots_txt.parser_base.RobotsTxtParser):
    def __init__(self, content=None, expires=None):
        super(ReppyWrapper, self).__init__(content, expires)
        if content:
            self.parser = Rules('robots.txt', 200, content, self.expires)
        else:
            self.parser = None
            self.my_super = super(ReppyWrapper, self)

    def allowed(self, user_agent, url):
        return self.parser.allowed(url, user_agent) if self.parser else self.my_super.allowed(user_agent, url)

    def delay(self, user_agent):
        return self.parser.delay(user_agent) if self.parser else self.my_super.delay(user_agent)

    @property
    def expired(self):
        return self.parser.expired if self.parser else self.my_super.expired

    @property
    def sitemaps(self):
        return self.parser.sitemaps if self.parser else self.my_super.sitemaps
