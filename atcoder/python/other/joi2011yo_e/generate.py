#!/usr/bin/env python3
# usage: $ oj generate-input 'python3 generate.py'
# usage: $ oj generate-input --hack-actual=./a.out --hack-expected=./naive 'python3 generate.py'
import random


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    a = random.randint(1, 1000)  # TODO: edit here
    d = [None for _ in range(a)]
    b = random.randint(1, 10**9)  # TODO: edit here
    c = random.randint(1, 10**9)  # TODO: edit here
    for i in range(a):
        d[i] = ''.join([random.choice('abcde') for _ in range(random.randint(1, 100))])  # TODO: edit here
    print(a, b, c)
    for i in range(a):
        print(d[i])


if __name__ == "__main__":
    main()
