#!/usr/bin/env python3
# from typing import *


# def solve(R: int, C: int, K: int, N: int, r: List[int], c: List[int]) -> int:
def solve(R, C, K, N, r, c):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    R, C, K = map(int, input().split())
    N = int(input())
    r = [None for _ in range(N)]
    c = [None for _ in range(N)]
    for i in range(N):
        r[i], c[i] = map(int, input().split())
    a = solve(R, C, K, N, r, c)
    print(a)


if __name__ == '__main__':
    main()