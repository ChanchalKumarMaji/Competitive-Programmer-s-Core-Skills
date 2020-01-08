# python3

def solve(L, R):
    n = len(L)
    N = 10**5 + 1
    start = [0]*N
    end = [0]*N
    for i in range(n):
        l, r = L[i], R[i]
        start[l] += 1
        end[r] += 1
    for i in range(1, N):
        start[i] += start[i-1]
        end[i] += end[i-1]
    ans = [0]*N
    for i in range(1, N):
        ans[i] = start[i] - end[i-1]
    for i in range(1, N):
        if ans[i] != 0:
            print(str(i) + " " + str(ans[i]))


if __name__ == '__main__':
    n = int(input())
    L, R = [], []
    for _ in range(n):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    solve(L, R)
