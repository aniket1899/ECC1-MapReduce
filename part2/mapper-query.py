#!/usr/bin/env python

from operator import itemgetter
import sys
import re

args = sys.argv

if len(args) == 1:
    range_hrs = (0, 24)
else:
    assert len(args) == 2
    assert '-' in args[-1]

    l, h = args[-1].split('-')
    range_hrs = (int(l), int(h))
    
pattern = re.compile("(?P<ip>\d+.\d+.\d+.\d+.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2}.*?")
for line in sys.stdin:
    # print(line)
    line = line.strip()
    match = pattern.search(line)
    if match and range_hrs[0] <= int(match.group('hour')) < range_hrs[1]: 
        print(f"{match.group('hour')}\t{match.group('ip')}\t1")
    



    

