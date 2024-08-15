#!/usr/bin/env python3
# from typing import *


# def solve(N: int, S: str, Q: int, c: List[str], d: List[str]) -> str:
def solve(N, S, Q, c, d):
    to = "abcdefghijklmnopqrstuvwxyz"
    for i in range(Q):
        to = to.replace(c[i], d[i])
    ans = ""
    for s in S:
        ans += to[ord(s)-97]
    return ans

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    S = input()
    Q = int(input())
    c = [None for _ in range(Q)]
    d = [None for _ in range(Q)]
    for i in range(Q):
        c[i], d[i] = input().split()
    a = solve(N, S, Q, c, d)
    print(a)


if __name__ == '__main__':
    main()