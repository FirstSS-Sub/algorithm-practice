#!/usr/bin/env python3
# from typing import *


# def solve(H: int, W: int, c: List[List[int]], A: List[List[int]]) -> int:
def solve(H, W, cost, A):
    cost_to_one = [float('inf') for _ in range(10)]
    for k in range(10):
        for start in range(10):
            for goal in range(10):
                if cost[start][k] + cost[k][goal] < cost[start][goal]:
                    cost[start][goal] = cost[start][k] + cost[k][goal]

    ans = 0
    for i in range(H):
        for j in range(W):
            if A[i][j] != -1:
                ans += cost[A[i][j]][1]
    return ans


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    c = [[None for _ in range(10)] for _ in range(10)]
    import sys
    tokens = iter(sys.stdin.read().split())
    H = int(next(tokens))
    W = int(next(tokens))
    A = [[None for _ in range(W)] for _ in range(H)]
    for j in range(10):
        for i in range(10):
            c[j][i] = int(next(tokens))
    for j in range(H):
        for i in range(W):
            A[j][i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(H, W, c, A)
    print(a)


if __name__ == '__main__':
    main()
