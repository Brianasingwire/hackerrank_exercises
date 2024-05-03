'''Cartesian Product'''

from itertools import product


def cartesian_product(set_A, set_B):
    '''Function to get cartesian product of two sets'''
    prod = list(product(set_A, set_B))

    for item in prod:
        print(item, end=' ')


if __name__ == '__main__':
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    cartesian_product(A, B)
