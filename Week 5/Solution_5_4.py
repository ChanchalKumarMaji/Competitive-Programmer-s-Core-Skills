# python3

def solve(A):
    n = len(A)
    C = max(A)
    dp = [[0]*(C+1) for _ in range(n)]
    prefixMin = [[0]*(C+1) for _ in range(n)]
    for x in range(1, C+1):
        dp[0][x] = abs(x-A[0])
    for i in range(n-1):
        prefixMin[i][1] = dp[i][1]
        for x in range(1, C):
            prefixMin[i][x+1] = min(prefixMin[i][x], dp[i][x+1])
        for y in range(1, C+1):
            dp[i+1][y] = prefixMin[i][y] + abs(y-A[i+1])
    #print(dp)
    return min(dp[n-1][1:])


if __name__ == '__main__':
    n = int(input())
    A = [int(i) for i in input().split()]
    print(solve(A))
