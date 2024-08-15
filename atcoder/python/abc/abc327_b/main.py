#!/usr/bin/env python3
# from typing import *

# def solve(B: int) -> int:
def solve(B):
    n = 1
    while n**n <= B:
        if n**n == B: return n
        n += 1
    return -1


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    B = int(input())
    a = solve(B)
    print(a)


if __name__ == '__main__':
    main()
