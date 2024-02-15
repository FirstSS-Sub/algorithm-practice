#!/usr/bin/env python3
# from typing import *


# def solve(N: int, W: int, w: List[int], v: List[int]) -> int:
def solve(N, W, w, v):
    MAX_SUM_VALUE = N * 10**3
    dp = [[W+1 for _ in range(MAX_SUM_VALUE+1)] for _ in range(N+1)]
    for i in range(N+1):
        dp[i][0] = 0
    for i in range(1, N+1):
        for j in range(1, MAX_SUM_VALUE+1):
            if j - v[i-1] < 0:
                dp[i][j] = dp[i-1][j]
            else:
                if dp[i-1][j] <= dp[i-1][j-v[i-1]] + w[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j-v[i-1]] + w[i-1]
    ans = 0
    for i in range(1, N+1):
        for j in range(MAX_SUM_VALUE+1):
            if dp[i][j] <= W and j > ans:
                ans = j
    return ans


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, W = map(int, input().split())
    w = [None for _ in range(N)]
    v = [None for _ in range(N)]
    for i in range(N):
        w[i], v[i] = map(int, input().split())
    a = solve(N, W, w, v)
    print(a)


if __name__ == '__main__':
    main()