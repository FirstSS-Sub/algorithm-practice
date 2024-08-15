#!/usr/bin/env python3
# from typing import *

YES = 'Yes'
NO = 'No'


# def solve(S: str) -> str:
def solve(S):
    now = ord(S[0])-1
    for s in S:
        if not (ord(s) == now or ord(s) == now+1 or ord(s) == now+2): return NO
        now = ord(s)
    return YES


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    S = input()
    a = solve(S)
    print(a)


if __name__ == '__main__':
    main()