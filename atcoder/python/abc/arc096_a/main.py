#!/usr/bin/env python3
# from typing import *


# def solve(A: int, B: int, C: int, X: int, Y: int) -> int:
def solve(A, B, C, X, Y):
    ans = 0
    ab_count = 0
    surplus = 0

    if A + B > C * 2:
        if X > Y:
            ans += Y * C * 2
            if A > C * 2:
                ans += (X - Y) * C * 2
            else:
                ans += (X - Y) * A
        else:
            ans += X * C * 2
            if B > C * 2:
                ans += (Y - X) * C * 2
            else:
                ans += (Y - X) * B
        return ans
    else: return A*X + B*Y
    

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    A, B, C, X, Y = map(int, input().split())
    a = solve(A, B, C, X, Y)
    print(a)


if __name__ == '__main__':
    main()
