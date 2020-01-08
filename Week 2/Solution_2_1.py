# python3

from itertools import permutations

def cost(perm, A):
    c = 0
    for i in range(len(perm)-1):
        c += A[perm[i]][perm[i+1]]
    return c

def solve(A):
    res = []
    m = 2**32
    n = len(A)
    perms = list(permutations([i for i in range(n)]))
    for perm in perms:
        if cost(perm, A) < m:
            m = cost(perm, A)
            res = perm[:]
    print(' '.join([str(e+1) for e in res]))


if __name__ == '__main__':
    n = int(input())
    A = []
    for _ in range(n):
        l = [int(i) for i in input().split()]
        A.append(l)
    solve(A)
