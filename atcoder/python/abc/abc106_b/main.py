#!/usr/bin/env python3
# from typing import *


# def solve(N: int) -> int:
def solve(N):
    ans = 0
    for i in range(1, N+1, 2):
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
        if count == 8:
            ans += 1
    return ans

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    a = solve(N)
    print(a)


if __name__ == '__main__':
    main()
