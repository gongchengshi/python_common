from robotexclusionrulesparser import RobotExclusionRulesParser

import python_common.web.robots_txt.parser_base


class RerpWrapper(python_common.web.robots_txt.parser_base.RobotsTxtParser):
    def __init__(self, content=None, expires=None):
        super(RerpWrapper, self).__init__(content, expires)
        if content:
            self.parser = RobotExclusionRulesParser()
            self.parser.use_local_time = False
            self.parser.expiration_date = self.expires
            self.parser.parse(content)
        else:
            self.parser = None
            self.my_super = super(RerpWrapper, self)

    def allowed(self, user_agent, url):
        return self.parser.is_allowed(user_agent, url) if self.parser else self.my_super.allowed(user_agent, url)

    def delay(self, user_agent):
        return self.parser.get_crawl_delay(user_agent) if self.parser else self.my_super.delay(user_agent)

    @property
    def expired(self):
        return self.parser.is_expired if self.parser else self.my_super.expired

    @property
    def sitemaps(self):
        return self.parser.sitemaps if self.parser else self.my_super.sitemaps
