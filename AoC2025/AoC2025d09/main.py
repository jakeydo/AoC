import sys
#from collections import defaultdict
#from os import system
#import time
#from functools import cache
#sys.setrecursionlimit(10**7)
#from copy import deepcopy
args = str(sys.argv)
if ("test" in args):
    f = open("test.txt")
else:
    f = open("real.txt")
lines = f.readlines()

red_tiles = []

for line in lines:
    x,y = line.strip().split(",")
    red_tiles.append((int(x),int(y)))
    
red_tile_count = len(red_tiles)

max_rect = 0

for i in range(red_tile_count):
    ix,iy = red_tiles[i]
    for j in range(i+1,red_tile_count):
        jx,jy = red_tiles[j]
        dx = abs(ix-jx) + 1
        dy = abs(iy-jy) + 1
        max_rect = max(max_rect,dx*dy)

print(f"Part 1 answer: {max_rect}")


print(f"Part 2 answer: {0}")