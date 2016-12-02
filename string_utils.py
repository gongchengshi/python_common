def lstrip_string(string, unwanted_string):
    if string.startswith(unwanted_string):
        string = string[len(unwanted_string):]
        return string, True
    return string, False


def lstrip_strings(string, unwanted_strings):
    removed = True
    while removed:
        removed = False
        for unwanted_string in unwanted_strings:
            string, removed = lstrip_string(string, unwanted_string)
    return string


def rstrip_string(string, unwanted_string):
    if string.endswith(unwanted_string):
        string = string[:-len(unwanted_string)]
        return string, True
    return string, False


def rstrip_strings(string, unwanted_strings):
    removed = True
    while removed:
        removed = False
        for unwanted_string in unwanted_strings:
            string, removed = rstrip_string(string, unwanted_string)
    return string


def longest_common_substring(s1, s2):
    """
    Taken from http://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Longest_common_substring
    :param s1:
    :param s2:
    :return:
    """
    m = [[0] * (1 + len(s2)) for i in xrange(1 + len(s1))]
    longest, x_longest = 0, 0
    for x in xrange(1, 1 + len(s1)):
        for y in xrange(1, 1 + len(s2)):
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x
            else:
                m[x][y] = 0
    return s1[x_longest - longest: x_longest]


def lcs_pairwise_similarity(s1, s2):
    return (2 * len(longest_common_substring(s1, s2))) / (len(s1) + len(s2))


