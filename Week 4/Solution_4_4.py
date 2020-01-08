# python3

def solve(A):
    res = []
    n = len(A)
    prefixSum = 0
    prefixMin = [0]*n
    for i in range(1, n):
        prefixSum += A[i-1]
        prefixMin[i] = min(prefixMin[i-1], prefixSum)
    suffixSum = 0
    suffixMin = [0]*n
    for i in range(n-2, -1, -1):
        suffixSum += A[i+1]
        suffixMin[i] = min(suffixMin[i+1], suffixSum)
    s = sum(A)
    for i in range(n):
        res.append(s-prefixMin[i]-suffixMin[i])
    return " ".join(map(str, res))


if __name__ == '__main__':
    n = int(input())
    A = [int(i) for i in input().split()]
    print(solve(A))
