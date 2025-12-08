import sys
from copy import deepcopy
#from collections import defaultdict
#from os import system
#import time
from functools import lru_cache
#sys.setrecursionlimit(10**7)
args = str(sys.argv)
if ("test" in args):
    f = open("test.txt",encoding="utf-16")
else:
    f = open("real.txt",encoding="utf-16")
lines = f.readlines()

for i in range(len(lines)):
    l = []
    for j in range(len(lines[i])):
        if not lines[i][j] == "\n":
            l.append(lines[i][j])
    lines[i] = l
#put the code here

bottom = len(lines)
edge = len(lines[0])

clean_lines = deepcopy(lines)

#first propogate the beams
for i in range(bottom):
    for j in range(edge):
        if lines[i][j] == "S":
            lines[i+1][j] = "|"
        elif lines[i][j] == "^" and lines[i-1][j] == "|":            
            if j-1 > -1:
                lines[i][j-1] = "|"
            if j+1 < edge:
                lines[i][j+1] = "|"
        elif lines[i][j] == "." and lines[i-1][j] == "|":
            lines[i][j] = "|"

#for line in lines:
#    print(line)

#now count splits

splits = 0
for i in range(1,bottom):
    for j in range(edge):
        if lines[i][j] == "^" and lines[i-1][j] == "|":
            splits += 1
print(f"Part 1 answer: {splits}")

@lru_cache
def universe_count(position):
    x,y = position
    if x == bottom:
        return 1
    elif clean_lines[x][y] == ".":
        return universe_count((x+1,y))
    elif clean_lines[x][y] == "^":
        return universe_count((x,y-1)) + universe_count((x,y+1))

start_pos = (0,0)
for i in range(len(lines[0])):
    if lines[0][i] == "S":
        start_pos = (1,i)

print(f"Part 2 answer: {universe_count(start_pos)}")