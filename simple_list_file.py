import re


class SimpleListFile:
    sectionPattern = re.compile('^\[(?P<section>.*)\]$')

    def __init__(self, path):
        self.path = path
        self.lists = {}
        current_list = []  # this one will be thrown away

        with open(self.path, 'r') as file:
            for line in file:
                text = line.strip()
                if (not text) or text.startswith('<>'):
                    continue

                match = self.sectionPattern.search(text)
                if match:
                    current_list = []
                    self.lists[match.group('section')] = current_list
                    continue

                current_list.append(text)

    def colon_delimited_tuples(self, section_name):
        return self.delimited_tuples(':', section_name)

    def delimited_tuples(self, delimiter, section_name):
        if section_name not in self.lists:
            return []
        tuples = []
        for item in self.lists[section_name]:
            split = item.split(delimiter, 1)
            tuples.append((split[0].strip(), split[1].strip()))
        return tuples

    def colon_delimited_dict(self, section_name):
        return dict(self.colon_delimited_tuples(section_name))
