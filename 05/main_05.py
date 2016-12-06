#!/usr/bin/env python

"""
Description
"""

__author__ = "Sebastian Müller"
__copyright__ = "Copyright 2016 " + __author__

import sys
import datetime

weekdays = {0: "Montag", 1: "Dienstag", 2: "Mittwoch", 3: "Donnerstag", 4: "Freitag", 5: "Samstag", 6: "Sonntag"}
fixday = datetime.datetime(1970, 1, 5) # Monday

def unwrap_date(datelist): 
    datelist = datelist.split(" ")
    day = int(datelist[2])
    year = int(datelist[0])
    month = int(datelist[1])
    if year < 1 or year > 9999:
        year = year % 400 + 400
    date = datetime.datetime(year, month, day)
    return (date - fixday).days


def get_weekday(diff):
    daydiff = diff % 7
    if daydiff < 0:
        return weekdays[-daydiff]
    return weekdays[daydiff]

def main():
    ncases = int(input())
    for n in range(ncases):
        print(get_weekday(unwrap_date(input())))
    return 0


if __name__ == '__main__':
    sys.exit(main())
