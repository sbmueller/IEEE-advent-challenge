#!/usr/bin/env python3

"""
Description
"""

__author__ = "Sebastian Müller"
__copyright__ = "Copyright 2016 " + __author__

import sys

cachelist = []

class general_cache:
    def __init__(self, length):
        self.length = length
        self.cache = []
        self.misses = 0
        self.hits = 0

    def push(self, pair):
        return

    def pop(self, key):
        return "method not overwritten"

class FIFO(general_cache):
    def __init__(self, length):
        super(FIFO, self).__init__(length)
        self.name = "FIFO"

    def push(self, pair):
        self.cache.insert(0, pair)
        if len(self.cache) > self.length:
            self.cache.pop()

    def pop(self, key):
        if self.cache[-1][0] == key:
            self.hits += 1
            return self.cache.pop()[1]
        else:
            self.misses += 1
            return "miss"

class LFU(general_cache):
    def __init__(self, length):
        super(LFU, self).__init__(length)
        self.name = "LFU"

    def sort_cache(self):
        self.cache = sorted(self.cache, key=lambda x: x[2], reverse=True)

    def push(self, pair):
        if len(self.cache)+1 > self.length:
            self.cache.pop()
        self.cache.insert(0, pair+[0])
        self.sort_cache()

    def pop(self, key):
        if self.cache[-1][0] == key:
            return self.cache.pop()[1]
            self.hits += 1
        else:
            try:
                request = [x for x in self.cache if x[0] == key][0]
                request[2] += 1
            except:
                pass
            self.misses += 1
            return "miss"


class MRU(general_cache):
    def __init__(self, length):
        super(MRU, self).__init__(length)
        self.name = "MRU"

    def push(self, pair):
        if len(self.cache)+1 > self.length:
            self.cache.pop()
        self.cache.insert(0, pair)

    def pop(self, key):
        if self.cache[-1][0] == key:
            return self.cache.pop()[1]
            self.hits += 1
        else:
            try:
                request = [x for x in self.cache if x[0] == key][0]
                index = self.cache.index(request)
                self.cache.append(request)
                self.cache.pop(index)
            except:
                pass
            self.misses += 1
            return "miss"


class LRU(general_cache):
    def __init__(self, length):
        super(LRU, self).__init__(length)
        self.name = "LRU"

    def push(self, pair):
        if len(self.cache)+1 > self.length:
            self.cache.pop()
        self.cache.insert(0, pair)

    def pop(self, key):
        if self.cache[-1][0] == key:
            return self.cache.pop()[1]
            self.hits += 1
        else:
            try:
                request = [x for x in self.cache if x[0] == key][0]
                index = self.cache.index(request)
                self.cache.insert(0, request)
                self.cache.pop(index)
            except:
                pass
            self.misses += 1
            return "miss"


def create_caches(caches, length):
    cachelist = []
    for n in caches:
        if n == "0":
            cachelist.append(FIFO(length))
        elif n == "1":
            cachelist.append(LRU(length))
        elif n == "2":
            cachelist.append(MRU(length))
        elif n == "3":
            cachelist.append(LFU(length))
    return cachelist

def get_best_cache():
    bestcache = cachelist[0]
    for c in cachelist[1:]:
        if c.hits > bestcache.hits:
            bestcache = c
    return bestcache
                    

def main():
    global cachelist
    ncases = int(input())
    for n in range(ncases):
        settings = str(input()).split(" ")
        length = int(settings[0])
        ncaches = int(settings[1])
        nqueries = int(settings[2])
        caches = str(input()).split(" ")
        cachelist = create_caches(caches, length)
        for k in range(nqueries):
            query = str(input()).split(" ")
            o = int(query[0])
            k = int(query[1])
            if o == 0:
                v = int(query[2])
                for c in cachelist:
                    c.push([k, v])
            else:
                for c in cachelist:
                    print(c.pop(k))
        bestcache = get_best_cache()
        print(bestcache.name+": H:"+str(bestcache.hits)+" M:"+str(bestcache.misses))

    return 0

if __name__ == '__main__':
    sys.exit(main())
