#!/usr/bin/env python

"""
IEEE SB Passau Adventskalender Challenge 02
"""

__author__ = "Sebastian Müller"
__copyright__ = "Copyright 2016 " + __author__

import sys

def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    return a//b

def neg(a):
    return -a

def mod(a, b):
    return a % b

def lshift(a, shift):
    return a << shift

def rshift(a, shift):
    return a >> shift

def andd(a, b):
    return a & b

def orr(a, b):
    return a | b

def comp(a):
    return ~a

def xor(a, b):
    return a ^ b

def find_operator(list):
    for i in range(len(list)):
        if not is_number(list[i]):
            return i, str(list[i])

def is_number(number):
    try:
        test = int(number)
    except ValueError:
        return False
    return True

def main():
    #raw_input = str(input())
    raw_input = "3 4 2 mul 1 5 sub 2 3 sub mul div add"
    fragments = raw_input.split(" ")
    while len(fragments) > 1:
        i, op = find_operator(fragments)
        eat = 0
        if op == "add":
            res = [add(int(fragments[i-2]), int(fragments[i-1]))]
            eat = 2
        elif op == "sub":
            res = [sub(int(fragments[i-2]), int(fragments[i-1]))]
            eat = 2
        elif op == "mul":
            res = [mul(int(fragments[i-2]), int(fragments[i-1]))]
            eat = 2
        elif op == "div":
            res = [div(int(fragments[i-2]), int(fragments[i-1]))]
            eat = 2
        elif op == "neg":
            res = [neg(int(fragments[i-1]))]
            eat = 1
        elif op == "mod":
            res = [mod(int(fragments[i-2]), int(fragments[i-1]))]
            eat = 2
        elif op == "lshift":
            res = [lshift(int(fragments[i-2]), int(fragments[i-1]))]
            eat = 2
        elif op == "rshift":
            res = [rshift(int(fragments[i-2]), int(fragments[i-1]))]
            eat = 2
        elif op == "and":
            res = [andd(int(fragments[i-2]), int(fragments[i-1]))]
            eat = 2
        elif op == "or":
            res = [orr(int(fragments[i-2]), int(fragments[i-1]))]
            eat = 2
        elif op == "comp":
            res = [comp(int(fragments[i-1]))]
            eat = 1
        elif op == "xor":
            res = [xor(int(fragments[i-2]), int(fragments[i-1]))]
            eat = 2
        else:
            raise ValueError("Operator "+op+" not known")
        res = [str(r) for r in res]
        fragments = fragments[:i-eat] + res + fragments[i+1:]
        print(fragments)

    print(fragments[0])
    return 0


if __name__ == '__main__':
    sys.exit(main())