# python3

def solve(A):
    res = 0
    n = len(A)
    previous_less = [-1]*n
    s1 = []
    for i in range(n):
        while len(s1) != 0 and A[s1[-1]] >= A[i]:
            _ = s1.pop()
        previous_less[i] = i+1 if len(s1) == 0 else i-s1[-1]
        s1.append(i)
    next_less = [-1]*n
    s2 = []
    for i in range(n-1, -1, -1):
        while len(s2) != 0 and A[s2[-1]] > A[i]:
            _ = s2.pop()
        next_less[i] = n-i if len(s2) == 0 else s2[-1]-i
        s2.append(i)
    for i in range(n):
        res += A[i]*previous_less[i]*next_less[i]
    return res


if __name__ == '__main__':
    n = int(input())
    A = [int(i) for i in input().split()]
    print(solve(A))
