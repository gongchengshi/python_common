from abc import abstractmethod, abstractproperty, ABCMeta
import time


class RobotsTxtParser:
    __metaclass__ = ABCMeta

    DEFAULT_TTL = 86400 * 10  # 10 days
    MIN_TTL = 86400 * 1  # 1 day

    def __init__(self, content, expires=None):
        if expires is None:
            self.expires = time.time() + RobotsTxtParser.DEFAULT_TTL
        else:
            min_expires = time.time() + RobotsTxtParser.MIN_TTL
            self.expires = min_expires if expires < min_expires else expires

    @abstractmethod
    def allowed(self, user_agent, url):
        return True

    @abstractmethod
    def delay(self, user_agent):
        return 0.0

    @abstractproperty
    def expired(self):
        return self.expires < time.time()

    @abstractproperty
    def sitemaps(self):
        return []
