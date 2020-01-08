# python3

def solve(A):
    n = len(A)
    m = max(A)
    if A.count(m) == 1:
        for i in range(n):
            if A[i] == m:
                return A[:i]+A[i+1:]
    else:
        count = 0
        for i in range(n):
            if A[i] == m:
                count += 1
                if count == 3:
                    return A[:i]+A[i+1:]


if __name__ == '__main__':
    n = int(input())
    A = [int(i) for i in input().split()]
    print(' '.join([str(e) for e in solve(A)]))
