#!/usr/bin/env python

"""
IEEE SB Passau Adventskalender Challenge 04
"""

__author__ = "Sebastian Müller"
__copyright__ = "Copyright 2016 " + __author__

import sys
from io import IOBase


class way:
    def __init__(self, coord, start, exit):
        self.coord = coord
        self.north = None
        self.east = None
        self.south = None
        self.west = None
        self.isexit = exit
        self.isstart = start
        self.path = []

    def weight(self):
        return len(self.path)

def dijkstra(start, ways):
    while len(ways) > 1:
        u = min(ways, key=lambda x: x.weight)
        if u.isexit:
            return u
        del ways[ways.index(u)]
        if u.north != None:
            u.north.weight = u.weight+1
            u.north.path = u.path[:]
            u.north.path.append("N")
            u.north.south = None
        if u.east != None:
            u.east.weight = u.weight+1
            u.east.path = u.path[:]
            u.east.path.append("O")
            u.east.west = None
        if u.south != None:
            u.south.weight = u.weight+1
            u.south.path = u.path[:]
            u.south.path.append("S")
            u.south.north = None
        if u.west != None:
            u.west.weight = u.weight+1
            u.west.path = u.path[:]
            u.west.path.append("W")
            u.west.east = None
    return ways[0]


def find_neighbours(ways):
    for w in ways:
        for v in ways:
            if w.coord[0] == v.coord[0] and w.coord[1] == v.coord[1]+1:
                w.west = v
                v.east = w
            if w.coord[0] == v.coord[0]+1 and w.coord[1] == v.coord[1]:
                w.north = v
                v.south = w

def main():
    dim = str(input()).split(" ")
    height = int(dim[0])
    width = int(dim[1])
    start = None
    ways = []
    for r in range(height):
        row = list(str(sys.stdin.readline(width)))
        sys.stdin.readline(1)
        if "X" in row:
            ways.append([way([r, i], True, False) for i,x in enumerate(row) if x == "X"][0])
            start = ways[-1]
            start.weight = 0
        if r == 0 or r == height-1:
            if "." in row:
                for l in [way([r, i], False, True) for i, x in enumerate(row) if x == "."]:
                    ways.append(l)

        else:
            if row[0] == ".":
                ways.append(way([r, 0], False, True))
            elif row[-1] == ".":
                ways.append(way([r, width-1], False, True))
        if "." in row:
            for l in [way([r, i], False, False) for i,x in enumerate(row) if x == "." and [r, i] not in [w.coord for w in ways]]:
                ways.append(l)

    find_neighbours(ways)
    result = dijkstra(start, ways).path
    result.append(result[-1])
    print("".join(result))

    return 0


if __name__ == '__main__':
    sys.exit(main())
