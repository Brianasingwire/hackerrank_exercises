'''Regex to detect float number'''

import re


def is_float(float_num):
    '''regex function'''
    pattern = r'^[+-]?[0-9]+\.[0-9]+$'
    return bool(re.match(pattern, float_num))


if __name__ == '__main__':
    N = int(input().strip())

    for _ in range(N):
        num = input().strip()
        print(is_float(num))
