#!/usr/bin/env python3
# from typing import *
from collections import defaultdict, deque

# def solve(N: int, t: List[int], x: List[int]) -> int:
def solve(N, t, x):
    deq = deque()
    d = defaultdict(int)
    min_p = 0
    temp_p = 0
    for i in range(N-1, -1, -1):
        if t[i] == 1:
            if x[i] in d:
                if temp_p < min_p:
                    min_p = temp_p
                temp_p += 1
                d[x[i]] -= 1
                if d[x[i]] == 0:
                    d.pop(x[i])
                deq.appendleft(1)
            else:
                deq.appendleft(0)
        else:
            temp_p -= 1
            d[x[i]] += 1
    if len(d):
        print(-1)
        return
    print(-min_p)
    print(*deq)


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    t = [None for _ in range(N)]
    x = [None for _ in range(N)]
    for i in range(N):
        t[i], x[i] = map(int, input().split())
    solve(N, t, x)


if __name__ == '__main__':
    main()
