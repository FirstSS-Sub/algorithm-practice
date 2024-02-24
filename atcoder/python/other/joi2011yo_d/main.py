#!/usr/bin/env python3
# from typing import *


# def solve(n: int, a: List[int]) -> int:
def solve(n, a):
    # f(k,B) := 『左からk個の穴に「+」or「-」を入れて「a0からakまでの部分の和」をBにする方法の数』（0≦k≦n-2, 0≦B≦20）
    f = [[0 for _ in range(20+1)] for _ in range(n-1)] # 最後の符号はイコールになるので、+か-が入るのはn-1個
    # +や-を1つも挟まない（最初の数のみ）場合、その合計数がBになるのは「最初の数=B」のときだけなので、それ以外の場合は全て0
    f[0][a[0]] = 1
    for k in range(1, n-1):
        for B in range(20+1):
            minus = 0
            plus = 0
            if B - a[k] >= 0:
                minus = f[k-1][B-a[k]]
            if B + a[k] <= 20:
                plus = f[k-1][B+a[k]]
            f[k][B] = minus + plus
    return f[n-2][a[n-1]]


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    n = int(next(tokens))
    a = [None for _ in range(n)]
    for i in range(n):
        a[i] = int(next(tokens))
    assert next(tokens, None) is None
    a1 = solve(n, a)
    print(a1)


if __name__ == '__main__':
    main()
