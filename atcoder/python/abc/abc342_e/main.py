#!/usr/bin/env python3
# from typing import *


# def solve(N: int, M: int, l: List[int], d: List[int], k: List[int], c: List[int], A: List[int], B: List[int]) -> List[str]:
def solve(N, M, l, d, k, c, A, B):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, M = map(int, input().split())
    l = [None for _ in range(M)]
    d = [None for _ in range(M)]
    k = [None for _ in range(M)]
    c = [None for _ in range(M)]
    A = [None for _ in range(M)]
    B = [None for _ in range(M)]
    for i in range(M):
        l[i], d[i], k[i], c[i], A[i], B[i] = map(int, input().split())
    a = solve(N, M, l, d, k, c, A, B)
    for i in range(N):
        print(a[i])


if __name__ == '__main__':
    main()
