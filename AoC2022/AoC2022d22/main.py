import sys
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

directions = lines[-1]
lines = lines[:-2]

world = defaultdict(lambda:" ")

x_size = len(lines)
y_size = max([len(x) for x in lines])

for x in range(x_size):
    for y in range(len(lines[x])-1):
        world[(x,y)] = lines[x][y]

start_y = min([y for x,y in world if x==0 and world[(x,y)]=="."])
start = (0,start_y)

#0 -> right, 1 -> down, 2 -> left, 3 -> up
facing = 0

#put the code here

print(f"Part 1 answer: {0}")


print(f"Part 2 answer: {0}")