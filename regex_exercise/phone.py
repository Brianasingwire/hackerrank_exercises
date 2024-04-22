'''Validating phone number'''

import re


def valid_phone_number(phone_number):
    '''regex function'''
    regex = r'^[7-9]\d{9}$'

    return bool(re.match(regex, phone_number))


if __name__ == '__main__':
    N = int(input().strip())

    for _ in range(N):
        digit = input().strip()
        print(valid_phone_number(digit))
    print('')


# READING FROM .TXT FILE


def validate_phone_number(file_name):
    '''regex function'''
    pattern = r'^[7-9]\d{9}$'

    with open(file_name, 'r', encoding='utf-8') as file:
        phone_numbers = file.readlines()

        for number in phone_numbers:
            number = number.strip()
            print(number)

            if re.match(pattern, number):
                print('YES')
            else:
                print('NO')


if __name__ == '__main__':
    validate_phone_number('numbers.txt')
