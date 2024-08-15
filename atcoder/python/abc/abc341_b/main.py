#!/usr/bin/env python3
# from typing import *


# def solve(N: int, A: List[int], S: List[int], T: List[int]) -> int:
def solve(N, A, S, T):
    for i in range(N-1):
        A[i+1] += (A[i]//S[i])*T[i]
    return A[N-1]

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    A = [None for _ in range(N)]
    S = [None for _ in range(N - 1)]
    T = [None for _ in range(N - 1)]
    for i in range(N):
        A[i] = int(next(tokens))
    for i in range(N - 1):
        S[i] = int(next(tokens))
        T[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, A, S, T)
    print(a)


if __name__ == '__main__':
    main()