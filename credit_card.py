'''Validating credit card'''

import re


def validate_credit_card(credit_card):
    '''regex function'''
    regex = r'^[4-6]\d{3}(-?\d{4}){3}$'

    if re.match(regex, credit_card):
        if not re.search(r'(\d)\1{3}', credit_card.replace('-', '')):
            return 'Valid'
    return 'Invalid'


if __name__ == '__main__':
    N = int(input().strip())

    for _ in range(N):
        card_number = input().strip()
        print(validate_credit_card(card_number))
