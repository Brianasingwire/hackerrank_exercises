'''Validating HEX code'''

import re


def validate_hex_code(code):

    # This still incomplete
    '''regex function'''
    regex = r'^#[0-9a-fA-F]{3,6}$'
    hex_code = re.findall(regex, code)
    unique_hex = list(set(hex_code))
    return unique_hex


if __name__ == '__main__':
    N = int(input().strip())

    s = [input() for _ in range(N)]

    hex_color = validate_hex_code(s)

    for css_code in hex_color:
        print(css_code)
