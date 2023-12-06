import sys
from math import prod
#from collections import defaultdict
#from os import system
#import time
#from functools import cache
#sys.setrecursionlimit(10**7)
args = str(sys.argv)
if ("test" in args):
    test = True
else:
    test = False
if test:
    f = open("test.txt")
else:
    f = open("real.txt")
lines = f.readlines()

times = list(map(int,lines[0].strip().split(":")[1].split()))
distances = list(map(int,lines[1].strip().split(":")[1].split()))

def distance(held,current):
    return held*(current-held)

"""
d=9
i=7
for h in range(8):
    print(f"race distance:{d}\t race time:{i}\t held:{h}\t travel distance:{distance(h,i)}")

print()
print()
"""

winning_counts = []
for i,d in enumerate(distances):
    this_win_count = 0
    for h in range(times[i]+1):
        if d < distance(h,times[i]):
            #print(f"race distance:{d}\t race time:{times[i]}\t held:{h}\t travel distance:{distance(h,times[i])}")
            this_win_count += 1
    winning_counts.append(this_win_count)
    
#print(winning_counts)
                
    

#put the code here



print(f"Part 1 answer: {prod(winning_counts)}")

new_times = ""
new_distances = ""
for t in times:
    new_times += str(t)
times = [int(new_times)]

for d in distances:
    new_distances += str(d)
distances = [int(new_distances)]


winning_counts = []
for i,d in enumerate(distances):
    this_win_count = 0
    for h in range(times[i]+1):
        if d < distance(h,times[i]):
            #print(f"race distance:{d}\t race time:{times[i]}\t held:{h}\t travel distance:{distance(h,times[i])}")
            this_win_count += 1
    winning_counts.append(this_win_count)
    
#print(winning_counts)


#print(f"{times}\n{distances}")
print(f"Part 2 answer: {winning_counts[0]}")