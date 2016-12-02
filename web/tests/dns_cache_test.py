import time
import unittest
import timeit
import socket

import python_common.web.dns_cache
from python_common.web.dns_cache import DnsCache
import requests
import dns.resolver


class TestDnsCache(unittest.TestCase):
    def basic_test(self):
        domain1 = 'www.baidu.com'
        domain2 = 'www.zdnet.com'
        domain1 = 'www.google.com'

        dns_cache = DnsCache()

        # This one puts it into the local DNS server cache
        start_time = timeit.default_timer()
        a = socket.getaddrinfo(domain1, 80)
        print timeit.default_timer() - start_time
        self.assertEquals(len(dns_cache.cache), 0)

        # This one should be shorter than the first one if it wasn't already in the local DNS server cache
        start_time = timeit.default_timer()
        a = socket.getaddrinfo(domain1, 80)
        print timeit.default_timer() - start_time
        self.assertEquals(len(dns_cache.cache), 0)

        # The next three should take about the same amount of time as the second using socket.getaddrinfo
        start_time = timeit.default_timer()
        answer = dns.resolver.query(domain1, 'A')
        print timeit.default_timer() - start_time
        self.assertEquals(len(dns_cache.cache), 0)

        start_time = timeit.default_timer()
        answer = dns.resolver.query(domain1, 'A')
        print timeit.default_timer() - start_time
        self.assertEquals(len(dns_cache.cache), 0)

        # This one puts it into the local in-memory cache.
        # It should take about the same amount of time as using dns.resolver.
        start_time = timeit.default_timer()
        a = dns_cache.resolve(domain1)
        print timeit.default_timer() - start_time
        self.assertIsNotNone(a)
        self.assertEquals(len(dns_cache.cache), 1)

        # The next two should be significantly faster because they are just doing an in memory dict lookup
        start_time = timeit.default_timer()
        a = dns_cache.resolve(domain1)
        print timeit.default_timer() - start_time
        self.assertIsNotNone(a)
        self.assertEquals(len(dns_cache.cache), 1)

        start_time = timeit.default_timer()
        a = dns_cache.resolve(domain1)
        print timeit.default_timer() - start_time
        self.assertIsNotNone(a)
        self.assertEquals(len(dns_cache.cache), 1)

        dns_cache.reset(domain1)
        self.assertEquals(len(dns_cache.cache), 0)

        # This one should be slower
        start_time = timeit.default_timer()
        a = dns_cache.resolve(domain1)
        print timeit.default_timer() - start_time
        self.assertIsNotNone(a)
        self.assertEquals(len(dns_cache.cache), 1)

        # This one should be faster
        start_time = timeit.default_timer()
        a = dns_cache.resolve(domain1)
        print timeit.default_timer() - start_time
        self.assertIsNotNone(a)
        self.assertEquals(len(dns_cache.cache), 1)

        dns_cache.cache[domain1].expires = time.time() + 5
        time.sleep(dns_cache.cache[domain1].expires - time.time())

        # This one should be about the same as all the other non-in-memory cached ones
        start_time = timeit.default_timer()
        a = dns_cache.resolve(domain1)
        print timeit.default_timer() - start_time
        self.assertIsNotNone(a)
        self.assertEquals(len(dns_cache.cache), 1)


global_dns_cache = python_common.web.dns_cache.global_dns_cache.cache


class TestGlobalDnsCache(unittest.TestCase):
    def basic_test(self):
        url1 = 'http://www.baidu.com'
        url2 = 'http://www.zdnet.com'

        start_time = timeit.default_timer()
        r = requests.get(url1)
        print timeit.default_timer() - start_time
        # self.assertEquals(len(global_dns_cache.cache), 1)

        start_time = timeit.default_timer()
        r = requests.get(url1)
        print timeit.default_timer() - start_time
        # self.assertEquals(len(global_dns_cache.cache), 1)

        start_time = timeit.default_timer()
        r = requests.get(url1)
        print timeit.default_timer() - start_time
        # self.assertEquals(len(global_dns_cache.cache), 1)
