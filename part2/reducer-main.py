#!/usr/bin/env python
import sys
from collections import defaultdict
from heapq import nlargest
from operator import itemgetter


hours_dict = defaultdict(lambda: defaultdict(int))
for line in sys.stdin:
    line = line.strip()
    hour, ip, count = line.split('\t')

    hours_dict[hour][ip] += int(count)

for tmph in hours_dict.keys():
    top3 = sorted(hours_dict[tmph], key=hours_dict[tmph].get, reverse=True)[:3]
    # print(top3)
    for key in top3:
        print(f"{tmph}\t{key}\t{hours_dict[tmph][key]}")



    