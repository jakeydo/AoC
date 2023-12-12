import sys
#from collections import defaultdict
#from os import system
#import time
from functools import cache
import re
#sys.setrecursionlimit(10**7)
args = str(sys.argv)
if ("test" in args):
    f = open("test.txt")
else:
    f = open("real.txt")
lines = f.readlines()

conditions = []

for line in lines:
    record, group = line.strip().split()
    group = list(map(int,group.split(",")))
    #record = record + "?" + record + "?" + record + "?" + record + "?" + record
    #group = group*5
    conditions.append([record,group])


@cache
def eval3(record,group):
    if len(record) == 0:
        if len(group) == 0:
            return 1
        else:
            return 0
    if len(group) == 0:
        if "#" in record:
            return 0
        else:
            return 1
    
    count = 0
    
    if record[0] in ".?":
        count += eval3(record[1:],group)
    if record[0] in "#?":
        if group[0] <= len(record) and ("." not in record[:group[0]]) and (group[0] == len(record) or record[group[0]] != "#"):
            count += eval3(record[group[0]+1:], group[1:])
    
    return count
    
total = 0
for c in conditions:
    record,group = c
    total += eval3(record,tuple(group))
print(f"Part 1 answer: {total}")


total2 = 0
for c in conditions:
    record,group = c
    record = record + "?" + record + "?" + record + "?" + record + "?" + record
    group = group * 5
    total2 += eval3(record,tuple(group))
print(f"Part 2 answer: {total2}")