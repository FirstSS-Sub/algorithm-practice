#!/usr/bin/env python3
# from typing import *
import sys
sys.setrecursionlimit(10**8)
import copy

# def solve(n: int, a: List[int]) -> Any:
def solve(H, W, A):
    ans = []
    dfs(0, 0, H, W, A, [], ans)
    ans_count = 0
    for result in ans:
        if not has_duplicates(result):
            ans_count += 1
    return ans_count

def dfs(x, y, H, W, A, l, ans):
    if H <= x or W <= y: return
    l.append(A[x][y])
    if x == H-1 and y == W-1:
        ans.append(l)
        return
    dfs(x+1, y, H, W, A, copy.copy(l), ans)
    dfs(x, y+1, H, W, A, copy.copy(l), ans)
    
def has_duplicates(seq):
    return len(seq) != len(set(seq))

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    # failed to analyze input format
    H, W = map(int, input().split())
    A = []
    for _ in range(H):
        tmp = []
        for x in input().split():
            tmp.append(int(x))
        A.append(tmp)
    ans = solve(H, W, A)
    print(ans)


if __name__ == '__main__':
    main()
