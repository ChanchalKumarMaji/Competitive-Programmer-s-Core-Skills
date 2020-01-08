# python3

import heapq

def solve(X):
    n = len(X)
    min_heap = []
    max_heap = []
    for i in range(n):
        x = X[i]
        heapq.heappush(min_heap, (x, i+1))
        heapq.heappush(max_heap, (-x, i+1))
        print(str(min_heap[0][1]) + " " + str(max_heap[0][1]))


if __name__ == '__main__':
    n = int(input())
    X = []
    for _ in range(n):
        x = int(input())
        X.append(x)
    solve(X)
