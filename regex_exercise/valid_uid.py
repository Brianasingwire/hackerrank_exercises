'''Validating UID'''

import re


def validate_uids(uid):
    '''regex function'''
    if len(re.findall(r'[A-Z]', uid)) < 2:
        return 'Invalid'

    if len(re.findall(r'[0-9]', uid)) < 3:
        return 'Invalid'

    if not re.match(r'^[0-9a-zA-Z]+$', uid):
        return 'Invalid'

    if len(uid) != 10:
        return 'Invalid'

    if len(set(uid)) != len(uid):
        return 'Invalid'

    return 'Valid'


if __name__ == '__main__':
    T = int(input().strip())

    uid_number = []
    for _ in range(T):
        uid_number.append(input().strip())

    for uids in uid_number:
        print(validate_uids(uids))
