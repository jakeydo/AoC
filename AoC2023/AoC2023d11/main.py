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

true_universe = defaultdict(lambda: ".")

for x in range(len(universe)):
    for y in range(len(universe[0])):
        if universe[x][y] == "#":
            true_universe[(x,y)] = "#"
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

def expand2(universe,factor):
    factor = factor - 1
    new_u = defaultdict(lambda:".")
    
    empty_rows = []
    empty_columns = []
    max_row = max([x for x,y in universe])
    max_column = max([y for x,y in universe])
    
    #find empty rows
    for x in range(max_row):
        l = [g for g in universe if g[0] == x]
        if len(l) == 0:
            empty_rows.append(x)
    
    #find empty columns
    for y in range(max_column):
        l = [g for g in universe if g[1] == y]
        if len(l) == 0:
            empty_columns.append(y)

    #print(f"empty columns: {empty_columns}")
    #print(f"empty rows: {empty_rows}")

    for g in universe:
        empty_rows_before = len([x for x in empty_rows if x < g[0]])
        empty_columns_before = len([y for y in empty_columns if y < g[1]])
        x,y = g
        new_x = x + factor*empty_rows_before
        new_y = y + factor*empty_columns_before
        new_u[(new_x,new_y)] = "#"
    return new_u
        
def print_true(universe):
    universe = copy.deepcopy(universe)
    max_row = max([x for x,y in universe])
    max_column = max([y for x,y in universe])
    
    for x in range(max_row+1):
        row = ""
        for y in range(max_column+1):
            row += universe[(x,y)]
        print(row)

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

true_universe = expand2(true_universe,1000000)
g_list = list(true_universe)
pairs = [(a,b) for idx,a in enumerate(g_list) for b in g_list[idx+1:]]
total_distance = 0
for p in pairs:
    g1,g2 = p
    g1x,g1y = g1
    g2x,g2y = g2    
    total_distance += (abs(g2y-g1y) + abs(g2x-g1x))

print(f"Part 2 answer: {total_distance}")