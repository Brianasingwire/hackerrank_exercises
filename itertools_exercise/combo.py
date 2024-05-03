'''Combinations in itertools'''

from itertools import combinations


def return_combinations(string, size):
    '''Function to return combinations of a string'''
    string = sorted(string)

    for r in range(1, size+1):
        combs = combinations(string, r)
        for comb in combs:
            print(''.join(comb))


if __name__ == "__main__":
    S, k = input().split()
    k = int(k)

    return_combinations(S, k)
