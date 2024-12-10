import sys
from copy import deepcopy
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
lines = f.readlines()

freqs = set()
freq_locs = {}
grid = []
antinodes = set()
p2_antinodes = set()

for i,line in enumerate(lines):
    line = line.strip()
    grid.append(line)
    for j,c in enumerate(line):
        if not (c == "."):
            if not (c in freqs):
                freq_locs[c] = set()
            freqs.add(c)            
            freq_locs[c].add((i,j))

max_x = len(grid)
max_y = len(grid[0])

for f in freqs:
    locs = freq_locs[f]
    for l in locs:
        other_locs = deepcopy(locs)
        other_locs.remove(l)
        for o in other_locs:
            lx,ly = l
            ox,oy = o
            dx = lx-ox
            dy = ly-oy
        
            newx = lx+dx
            newy = ly+dy
        
            if (newx in range(max_x)) and (newy in range(max_y)):
                antinodes.add((newx,newy))
                #print(f"l:{l} o:{o}, new:{(newx,newy)}")  
            
            for m in range(-max_x,max_x+1):
                newx = lx+m*dx
                newy = ly+m*dy
            
                if (newx in range(max_x)) and (newy in range(max_y)):
                    p2_antinodes.add((newx,newy))
                    #print(f"l:{l} o:{o}, new:{(newx,newy)}")
"""
for line in grid:
    print(line)

for c in freqs:
    print(c)
    print(freq_locs[c])
    print()

for a in antinodes:
    print(a)
"""
#put the code here

print(f"Part 1 answer: {len(antinodes)}")


print(f"Part 2 answer: {len(p2_antinodes)}")