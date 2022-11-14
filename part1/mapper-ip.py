#!/usr/bin/env python

from operator import itemgetter
import sys
import re

pattern = re.compile("(?P<ip>\d+.\d+.\d+.\d+.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2}.*?")
for line in sys.stdin:
    # print(line)
    line = line.strip()
    match = pattern.search(line)
    if match: 
        print(f"{match.group('hour')}\t{match.group('ip')}\t1")
    



    

