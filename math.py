def percent_diff(v1, v2):
    return abs(v1 - v2) / ((v1 + v2) / 2.0)


def is_power2(num):
    return num != 0 and ((num & (num - 1)) == 0)

