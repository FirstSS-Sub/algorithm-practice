#!/usr/bin/env python3
# from typing import *
from collections import defaultdict

# def solve(S: str) -> str:
def solve(S):
    d = defaultdict(int)
    dd = defaultdict(list)
    mx = 0
    for s in S:
        d[s] += 1
        dd[d[s]].append(s)
        if d[s] > mx:
            mx = d[s]
    return sorted(dd[mx])[0]


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    S = input()
    a = solve(S)
    print(a)


if __name__ == '__main__':
    main()
