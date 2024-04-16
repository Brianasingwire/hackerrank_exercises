'''Find indices'''

import re


def find_spices(main_string, sub_string):
    '''regex function'''
    matches = re.search(sub_string, main_string)

    if matches:
        return (matches.start(), matches.end() - 1)
    return (-1, -1)


if __name__ == '__main__':
    main = input()
    sub = input()

    result = find_spices(main, sub)
    print(result)
