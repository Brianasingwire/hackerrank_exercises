'''Vowel substring'''

import re


def find_substrings_with_vowels(s):
    '''regex function'''

    pattern = r'(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])[aeiouAEIOU]{2,}(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])'

    # pattern = r'[aeiouAEIOU]{3,}'
    substrings = re.findall(pattern, s)

    print('substrings:', substrings)

    if substrings:
        for substring in substrings:
            print(substring)
    else:
        print(-1)


if __name__ == '__main__':
    string = input().strip()

    find_substrings_with_vowels(string)
