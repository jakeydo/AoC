import sys
import copy
from collections import defaultdict
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

universe = []
for line in lines:
    layer = [c for c in line.strip()]
    universe.append(layer)

def expand(universe):
    universe = copy.deepcopy(universe)
    i = 0
    
    #print("first insertion")
    while True:
        l = universe[i]
        contents = set(l)
        if len(contents) == 1:
            new_l = copy.deepcopy(l)
            universe.insert(i,new_l)
            #print(f"inserting at {i}")
            i += 1
        i += 1
        if i == len(universe):
            break
    
    universe = list(map(list,zip(*universe)))
    i = 0
    
    #print("second pass")
    while True:
        l = universe[i]
        contents = set(l)        
        if len(contents) == 1:
            new_l = copy.deepcopy(l)
            universe.insert(i,new_l)
            #print(f"inserting at {i}")
            i += 1
        i += 1
        if i == len(universe):
            break
    
    universe = list(map(list,zip(*universe)))
    return universe

def find_galaxies(universe):
    galaxies = set()
    for x in range(len(universe)):
        for y in range(len(universe[0])):
            if universe[x][y] == "#":
                galaxies.add((x,y))
    return galaxies

universe = expand(universe)

galaxies = find_galaxies(universe)

g_list = list(galaxies)
pairs = [(a,b) for idx,a in enumerate(g_list) for b in g_list[idx+1:]]

total_distance = 0

for p in pairs:
    g1,g2 = p
    g1x,g1y = g1
    g2x,g2y = g2
    
    total_distance += (abs(g2y-g1y) + abs(g2x-g1x))


print(f"Part 1 answer: {total_distance}")


print(f"Part 2 answer: {0}")