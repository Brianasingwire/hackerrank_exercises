'''Permutations in itertools'''

from itertools import permutations


def return_permutations(string, size):
    '''Function to return permutations'''
    perms = permutations(sorted(string), size)

    for perm in perms:
        print(''.join(perm))


if __name__ == '__main__':
    S, k = input().split()
    k = int(k)

    return_permutations(S, k)
