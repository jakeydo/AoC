import sys
from copy import deepcopy
#from itertools import chain
#from intervaltree import IntervalTree, Interval
#from collections import defaultdict
#from os import system
#import time
#from functools import cache
#sys.setrecursionlimit(10**7)
args = str(sys.argv)
if ("test" in args):
    f = open("test.txt")
else:
    f = open("real.txt")
lines = f.read()

ranges,ids = lines.split("\n\n")

ranges = ranges.split("\n")
ids = ids.split("\n")

range_objects = []
old_ranges = []

for r in ranges:
    start, end = r.split("-")
    start = int(start)
    end = int(end)
    range_objects.append(range(start,end+1))
    old_ranges.append((start,end))

fresh_count = 0

for id in ids:
    id = int(id)
    
    fresh = False
    for r in range_objects:
        if id in r:
            fresh = True
            break
    if fresh:
        fresh_count +=1

#put the code here

print(f"Part 1 answer: {fresh_count}")
"""


for r in range_objects:
    combined_range.extend(r)
"""
#combined_range = set(combined_range)

"""
fresh_total = 0

            
        
        
"""

"""
tree = IntervalTree()

for r in range_objects:
    print(min(r))
    print(max(r))
    print(Interval(min(r),max(r)))
    print()
    tree.add(Interval(min(r),max(r)+1))
    

print(tree)    
merged_intervals = tree.merge_overlaps()
print(tree)

fresh_count = 0
for i in tree:
    print(i)
    fresh_count += (i.end - i.begin)
"""
"""
overlap = True

new_ranges = []

#z = len(old_ranges)
overlap = True
any_overlap = True
while any_overlap:
    print("old ranges before big loop")
    print(old_ranges)
    any_overlap = False
    z = len(old_ranges)
    for x in range(z):
        overlap = False
        for y in range(x+1,z):
            x0,x1 = old_ranges[x]
            y0,y1 = old_ranges[y]
            print(f"checking {(x0,x1)} vs {(y0,y1)} ")
            if x0 == y0 and x1 == y1:
                overlap = True
                any_overlap = True
                print("duplicate, not adding")
            if max(x0,y0) <= min(x1,y1):
                overlap = True
                any_overlap = True
                r1 = (min(x0,y0),max(x0,y0))
                r2 = (max(x0,y0)+1,min(x1,y1))
                r3 = (min(x1,y1)+1,max(x1,y1))
                print("overlap")
                if r1[0] <= r1[1]:
                    new_ranges.append(r1)
                    print(f"adding r1 {r1}")
                if  r2[0] <= r2[1]:
                    new_ranges.append(r2)
                    print(f"adding r2 {r2}")
                if r3[0] <= r3[1]:
                    new_ranges.append(r3)
                    print(f"adding r3 {r3}")
                #print(f"overlap adding {r1} and {r2} and {r3}")
        if not overlap:
            print(f"no overlap adding {old_ranges[x]}")
            new_ranges.append(old_ranges[x])
    old_ranges = set(new_ranges)
    print(old_ranges)
    old_ranges = list(old_ranges)
    print(old_ranges)
    print("new ranges after big loop")
    print(new_ranges)
    print()
    print()
    new_ranges = []
"""

overlap = True
new_ranges = []

while overlap:
    overlap = False
    z = len(old_ranges)
    for x in range(z):
        if overlap:
            break
        x0,x1 = old_ranges[x]
        for y in range(x+1, z):
            if overlap:
                break
            y0,y1 = old_ranges[y]            
            if max(x0,y0) <= min(x1,y1):
                overlap = True
                r1 = (min(x0,y0),max(x0,y0))
                r2 = (max(x0,y0)+1,min(x1,y1))
                r3 = (min(x1,y1)+1,max(x1,y1))
                old_ranges.pop(y)
                old_ranges.pop(x)
                new_ranges = deepcopy(old_ranges)
                if r1[0] <= r1[1]:
                    new_ranges.append(r1)
                if r2[0] <= r2[1]:
                    new_ranges.append(r2)
                if r3[0] <= r3[1]:
                    new_ranges.append(r3)
                old_ranges = new_ranges
                new_ranges = []
                

fresh_count = 0
#print()
for r in old_ranges:
    #print(r)
    fresh_count += r[1]-r[0]+1
    
print(f"Part 2 answer: {fresh_count}")