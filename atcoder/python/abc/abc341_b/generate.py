#!/usr/bin/env python3
# usage: $ oj generate-input 'python3 generate.py'
# usage: $ oj generate-input --hack-actual=./a.out --hack-expected=./naive 'python3 generate.py'
import random


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = random.randint(1, 1000)  # TODO: edit here
    A = [None for _ in range(N)]
    S = [None for _ in range(N - 1)]
    T = [None for _ in range(N - 1)]
    for i in range(N):
        A[i] = random.randint(1, 10**9)  # TODO: edit here
    for i in range(N - 1):
        S[i] = random.randint(1, 10**9)  # TODO: edit here
        T[i] = random.randint(1, 10**9)  # TODO: edit here
    print(N)
    print(*[A[i] for i in range(N)])
    for i in range(N - 1):
        print(S[i], T[i])


if __name__ == "__main__":
    main()
