#!/usr/bin/env python3
# from typing import *


# def solve(n: int, a: List[int]) -> Tuple[int, int]:
def solve(n, a):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    n = int(input())
    a = [None for _ in range(n)]
    for i in range(n):
        a[i] = int(input())
    d, e = solve(n, a)
    print(d)
    print(e)


if __name__ == '__main__':
    main()
