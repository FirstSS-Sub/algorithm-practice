#!/usr/bin/env python3
# from typing import *


# def solve(n: int, a: List[int]) -> Any:
def solve(l):
    for i in range(9):
        flag = [False]*9
        for j in range(9):
            if not flag[l[i][j]-1]:
                flag[l[i][j]-1] = True
            else:
                return "No"
    for j in range(9):
        flag = [False]*9
        for i in range(9):
            if not flag[l[i][j]-1]:
                flag[l[i][j]-1] = True
            else:
                return "No"
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            flag = [False]*9
            for ii in range(i, i+3):
                for jj in range(j, j+3):
                    if not flag[l[ii][jj]-1]:
                        flag[l[ii][jj]-1] = True
                    else:
                        return "No"
    return "Yes"


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    # failed to analyze input format
    l = []
    for _ in range(9):
        l.append(list(map(int, input().split())))
    ans = solve(l)
    print(ans)


if __name__ == '__main__':
    main()
