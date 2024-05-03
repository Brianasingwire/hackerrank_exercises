'''groupby in itertools'''

from itertools import groupby


def compress_strings(string):
    '''Function to compress a string using groupby'''
    grouped = groupby(string)

    result = []

    for key, group in grouped:
        count = len(list(group))
        result.append(f'({count},{key})')

    return ' '.join(result)


if __name__ == '__main__':
    S = input().strip()

    print(compress_strings(S))
