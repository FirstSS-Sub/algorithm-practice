#!/usr/bin/env python3
# from typing import *


# def solve(a: int, b: int, c: List[int], d: List[int], e: List[int]) -> int:
def solve(n, l):
    for k in range(n):
        for start in range(n):
            for goal in range(n):
                if start == goal:
                    continue
                if l[start][k] + l[k][goal] < l[start][goal]:
                    l[start][goal] = l[start][k] + l[k][goal]
    worst_l = []
    for i in range(n):
        max_t = 0
        for j in range(n):
            if l[i][j] != float('inf') and l[i][j] > max_t:
                max_t = l[i][j]
        worst_l.append(max_t)
    return min(worst_l)


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    n, m = map(int, input().split())
    l = [[float('inf') for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        a, b, t = map(int, input().split())
        l[a-1][b-1] = t
        l[b-1][a-1] = t
    a1 = solve(n, l)
    print(a1)


if __name__ == '__main__':
    main()
