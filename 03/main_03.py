#!/usr/bin/env python

"""
IEEE SB Passau Adventskalender Challenge 03
"""

__author__ = "Sebastian Müller"
__copyright__ = "Copyright 2016 " + __author__

import sys

def get_nbranches(h, w):
    fit_height = 1
    fit_width = (w-1)//2 - 3
    if fit_width < 1:
        fit_width = 1
    if h > 6:
        fit_height = (h-1)//5
    return min([fit_height, fit_width])


def get_trunk(n):
    return ' ' * ((n-1)//2) + '#'

def get_branch(h, w, b):
    res = []
    u = 1
    start = w-8
    if w < 9:
        start = 1
    for i in range(start, w+2, 2):
        res.append(' ' * ((b-i)//2) + '*' * (i))
        u += 1
        if u > h:
            break
    return res

def main():
    raw_input = int(input())
    for t in range(raw_input):
        height = int(input())
        width = int(input())
        nbranches = get_nbranches(height, width)
        rows = 5
        if nbranches == 1:
            rows = (width - 1) // 2 + 1
        for b in range(nbranches):
            branch = get_branch(rows, width-((nbranches-b)-1)*2, width)
            for l in range(rows):
                print(branch[l])
        for t in range(height-rows*nbranches):
            print(get_trunk(width))
    #tree = get_branch()
    #for i in range(5):
    #    print(tree[i])
    return 0

if __name__ == '__main__':
    sys.exit(main())