'''Regex substitution'''

import re


def modify_symbols(text):
    '''Regex function'''
    text = re.sub(r'\s+&&\s+', ' and ', text)
    text = re.sub(r'\s+\|\|\s+', ' or ', text)

    return text


if __name__ == "__main__":
    N = int(input().strip())

    lines = []
    for _ in range(N):
        lines.append(input())

    modify_lines = []
    for line in lines:
        modify_lines.append(modify_symbols(line))

    for line in modify_lines:
        print(line)


# text = re.sub(r'(?<= )&&(?= )', 'and', text)
# text = re.sub(r'(?<= )\|\|(?= )', 'or', text)
