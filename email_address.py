import re
email_address_pattern = re.compile(r'((?P<desc>.+)\s<)?(?P<user>[^@]+)@(?P<domain>[^>]+)>?')


class EmailAddress:
    def __init__(self, address):
        self.original = address

        m = email_address_pattern.match(self.original)
        if not m:
            raise Exception('%s is not a valid email address' % str(address))
        self.desc = m.group('desc')
        self.user = m.group('user')
        self.domain = m.group('domain')
        self.address = "%s@%s" % (self.user, self.domain)
