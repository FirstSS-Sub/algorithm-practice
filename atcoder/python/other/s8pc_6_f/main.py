#!/usr/bin/env python3
# from typing import *


# def solve(N: str, D: str, L: str, S: List[str]) -> Any:
def solve(N, D, L, S):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = next(tokens)
    D = next(tokens)
    L = next(tokens)
    S = [None for _ in range(N)]
    for i in range(N):
        S[i] = next(tokens)
    assert next(tokens, None) is None
    ans = solve(N, D, L, S)
    print(ans)  # TODO: edit here


if __name__ == '__main__':
    main()
