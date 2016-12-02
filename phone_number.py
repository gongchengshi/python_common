import re


class PhoneNumber:
    phone_ext_pattern = re.compile(r"\s+e?xt?\.?:?\s*", flags=re.IGNORECASE)
    phone_sub_pattern = re.compile(r'(\)-?\s*)|(\s+)')

    def __init__(self, phone_number, line=None):
        self.line = line
        if 'x' in phone_number:
            main, self.ext = self.phone_ext_pattern.split(phone_number)
        else:
            main = phone_number
            self.ext = None

        self.main = self.phone_sub_pattern.sub('-', main.replace('(', '').strip())

    def __str__(self):
        return ("%s x%s" % (self.main, self.ext)) if self.ext else self.main

    def __hash__(self):
        return hash(self.__str__() + (self.line or ''))
