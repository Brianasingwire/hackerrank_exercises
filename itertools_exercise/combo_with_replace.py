'''Combination with replacement in itertools'''

from itertools import combinations_with_replacement


def return_combination_with_replacement(string, size):
    '''Function'''
    string = sorted(string)

    combs = combinations_with_replacement(string, size)

    for comb in combs:
        print(''.join(comb))


if __name__ == '__main__':
    S, k = input().split()
    k = int(k)

    return_combination_with_replacement(S, k)
