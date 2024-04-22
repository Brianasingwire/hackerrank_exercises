'''Regex groups for repeated characters'''

import re


def repeated_characters(string):
    '''regex function'''
    matches = re.search(r'(\w)\1', string)

    if matches:
        return matches.group(1)
    return -1


if __name__ == '__main__':
    n = input()

    result = repeated_characters(n)
    print(result)
