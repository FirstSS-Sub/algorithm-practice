#!/usr/bin/env python3
# from typing import *


# def solve(n: int, a: List[int]) -> Any:
def solve(N, A):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    A = []
    for _ in range(N):
        a = []
        for _ in range(N):
            a.append(int(next(tokens)))
        A.append(a)
    assert next(tokens, None) is None
    ans = solve(N, A)
    print(ans)


if __name__ == '__main__':
    main()
