'''Validate Roman numeral'''

import re


def validate_roman_numeral(num):
    '''Regex function'''
    pattern = r'M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'

    return bool(re.match(pattern, num))


if __name__ == '__main__':
    NUM = 'CDXXI'
    print(validate_roman_numeral(NUM))
