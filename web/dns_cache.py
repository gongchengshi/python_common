import socket
from threading import RLock
import time
import dns.resolver


class DnsCache:
    """
    Todo: If the authoritative name server is doing round robin for the domain then DnsCache should do round robin too.
    """
    class Record:
        def __init__(self, ip_address, expires):
            self.ip_address = ip_address
            self.expires = expires

    @staticmethod
    def get_new_record(domain):
        try:
            answer = dns.resolver.query(domain, 'A')
            if len(answer) > 0:
                return DnsCache.Record(str(answer[0]), answer.expiration)
        except dns.resolver.NXDOMAIN:
            return None
        return None

    def __init__(self):
        self.cache = {}
        self.cache_lock = RLock()

    def resolve(self, domain):
        with self.cache_lock:
            try:
                record = self.cache[domain]
                if record.expires < time.time():
                    record = None
            except KeyError:
                record = None

            if record is None:
                record = DnsCache.get_new_record(domain)
                if record is None:
                    raise socket.gaierror(socket.EAI_NONAME)
                else:
                    self.cache[domain] = record

        return record.ip_address

    def reset(self, domain):
        with self.cache_lock:
            del self.cache[domain]


global_dns_cache = DnsCache()

# Monkey patch HTTPConnection.new_conn to use a DNS caching DNS resolver

import requests.packages.urllib3.connection


def patched_new_conn(self):
    """ Establish a socket connection and set nodelay settings on it

    :return: a new socket connection
    """
    hostname = global_dns_cache.resolve(self.host)
    try:
        conn = socket.create_connection((hostname, self.port), self.timeout, self.source_address)
    except AttributeError:  # Python 2.6
        conn = socket.create_connection((hostname, self.port), self.timeout)
    # conn.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, self.tcp_nodelay)
    return conn


requests.packages.urllib3.connection.HTTPConnection._new_conn = patched_new_conn
