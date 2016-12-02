#!/usr/bin/env python

"""
IEEE SB Passau Adventskalender Challenge 01
"""

__author__ = "Sebastian Müller"
__copyright__ = "Copyright 2016 " + __author__

import sys

def flip_string(string):
    return string[::-1]

def flip_number(num):
    return int(str(num)[::-1])

def main():
    results = []  # sum list
    ncases = int(input())
    for i in range(ncases):
        numbers = str(input()).split(" ")  # grab list of numbers as strings
        flipped = []  # flipped numbers list
        for n in numbers:
            flipped.append(flip_string(n))  # add flipped number to list
        results.append((sum([int(i) for i in flipped])))  # append non-flipped sum to result list
        print(flip_string(str(sum([int(i) for i in flipped]))))  # print flipped sum
    print("Totale Summe: "+str(sum(results)))  # final output with total sum
    return 0

if __name__ == '__main__':
    sys.exit(main())