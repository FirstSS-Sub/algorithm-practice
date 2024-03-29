#!/usr/bin/env python3
# from typing import *

YES = 'Yes'
NO = 'No'


# def solve(N: str) -> str:
def solve(N):
    ans = 0
    for c in str(N):
        ans += int(c)
    if ans % 9 == 0: return YES
    return NO


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = input()
    a = solve(N)
    print(a)


if __name__ == '__main__':
    main()
