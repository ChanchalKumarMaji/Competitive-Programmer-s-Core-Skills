# python3

import heapq

def solve(X, Y):
    n = len(X)
    min_heap1 = []
    max_heap1 = []
    min_heap2 = []
    max_heap2 = []
    for i in range(n):
        x, y = X[i], Y[i]
        heapq.heappush(min_heap1, (x+y, i+1))
        heapq.heappush(max_heap1, (-(x+y), i+1))
        heapq.heappush(min_heap2, (x-y, i+1))
        heapq.heappush(max_heap2, (-(x-y), i+1))
        if abs(min_heap1[0][0] + max_heap1[0][0]) >= abs(min_heap2[0][0] + max_heap2[0][0]):
            print(str(min_heap1[0][1]) + " " + str(max_heap1[0][1]))
        else:
            print(str(min_heap2[0][1]) + " " + str(max_heap2[0][1]))


if __name__ == '__main__':
    n = int(input())
    X, Y = [], []
    for _ in range(n):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    solve(X, Y)


# |X| + |Y| = max(|X+Y|, |X-Y|)
# |x1-x2| + |y1-y2| = max(|(x1+y1)-(x2+y2)|, |(x1-y1)-(x2-y2)|)
