import sys
import math
#from heapq import heappush,heappop
from collections import defaultdict
import copy
#from os import system
#import time
from functools import cache
sys.setrecursionlimit(10**7)
args = str(sys.argv)
start_fill = (0,0)
if ("test" in args):
    f = open("test.txt")
    start_fill = (1,1)
else:
    f = open("real.txt")
    start_fill = (16,100)
lines = f.readlines()
total = 0
total2 = 0

data = []
world = defaultdict(lambda: ".")
world2 = defaultdict(lambda: ".")

for line in lines:
    line = line.strip()
    direction,count,color = line.split()
    count = int(count)
    data.append((direction,count,color))

position = (0,0)

for d in data:
    #print(d)
    direction,count,color = d
    for i in range(count):
        x,y = position
        #print(position)
        world[position] = "#"
        if direction == "R":
            newx,newy = x,y+1
        elif direction == "D":
            newx,newy = x+1,y
        elif direction == "L":
            newx,newy = x,y-1
        else:
            newx,newy = x-1,y
        position = (newx,newy)
    
minx = miny = maxx = maxy = 0

def print_world(w):
    w = copy.deepcopy(w)
    minx = miny = maxx = maxy = 0
    for x,y in w:
        minx = min(minx,x)
        miny = min(miny,y)
        maxx = max(maxx,x)
        maxy = max(maxy,y)
    
    for x in range(minx,maxx+1):
        row = ""
        for y in range(miny,maxy+1):
            row += w[(x,y)]
        print(row)


for x,y in world:
    minx = min(minx,x)
    miny = min(miny,y)
    maxx = max(maxx,x)
    maxy = max(maxy,y)

sx,sy = start_fill
sx += minx
sy += miny
start_fill = (sx,sy)

print(f"minx:{minx} maxx:{maxx} miny:{miny} maxy:{maxy}")
border_size = len(world)
fill_q = [start_fill]

xrange = range(minx,maxx+1)
yrange = range(miny,maxy+1)

print_world(world)
print("@@@")
print("@@@")

while fill_q:
    pos = fill_q.pop(0)
    if world[pos] == "#":
        continue
    world[pos] = "#"
    x,y = pos
    #print((x,y))
    if x-1 in xrange:
        if y in yrange and world[(x-1,y)] == ".":
            fill_q.append((x-1,y))
    if x+1 in xrange:
        if y in yrange and world[(x+1,y)] == ".":
            fill_q.append((x+1,y))
    if y-1 in yrange:
        if x in xrange and world[(x,y-1)] == ".":
            fill_q.append((x,y-1))
    if y+1 in yrange:
        if x in xrange and world[(x,y+1)] == ".":
            fill_q.append((x,y+1))
print_world(world)

"""
total = 0
for x in range(minx,maxx+1):
    border_count = 0
    for y in range(miny,maxy+1):
        print(f"pos:{(x,y)} bc:{border_count}")
        if world[(x,y)] == "#":
            total += 1
            border_count += 1
        elif border_count % 2 == 1:
            total += 1
"""

total = len(world)
          
print(f"part 1 answer: {total}")

newworld = defaultdict(lambda:".")
position = (0,0)
x=y=0
xs = [x]
ys = [y]
border_size = 0 
for d in data:
    #x,y = position
    direction,count,color = d
    direction = int(color[-2:-1])
    count = int(color[2:-2],16)
    border_size += count
    #print(f"x:{x} y:{y} direction:{direction} count:{count}")
    #count +=1
    if direction == 0:
        y += count
    elif direction == 1:
        x += count 
    elif direction == 2:
        y -= count 
    else:
        x -= count 
    xs.append(x)
    ys.append(y)
    """
    for i in range(count):
        newx,newy = position
        #print(position)
        newworld[position] = "#"
        if direction == 0:
            newx,newy = newx,newy+1
        elif direction == 1:
            newx,newy = newx+1,newy
        elif direction == 2:
            newx,newy = newx,newy-1
        else:
            newx,newy = newx-1,newy
        position = (newx,newy)
    """
    #print((x,y))
    #print(xs)
    #print(ys)
    #print()
#xs.append(x)
#ys.append(y)

num_points = len(xs)
total2 = 0

j = num_points - 1
#border_size = len(newworld)
#xs.reverse()
#ys.reverse()
for i in range(1,num_points):
    j=i-1
    #print(f"x:{xs[j]} y:{ys[j]}")
    #total2 += (xs[j]+xs[i])*(ys[j]-ys[i])
    total2 += (xs[i]*ys[j] - xs[j]*ys[i])
    #j=i

total2 = (total2+border_size)//2 + 1

"""    
minx = miny = maxx = maxy = 0
for x,y in world2:
    minx = min(minx,x)
    miny = min(miny,y)
    maxx = max(maxx,x)
    maxy = max(maxy,y)

xrange = range(minx,maxx+1)
yrange = range(miny,maxy+1)

total2 = len(world2)  

top_line = [(x,y) for x,y in world2 if x==minx]


for x,y in top_line:
    newx = x+1
    if world2[(newx,y)] == ".":
        start_fill == (newx,y)
        break

#print(top_line)
    
fill_q = [start_fill]
while fill_q:
    pos = fill_q.pop(0)
    if world2[pos] == "#":
        continue
    world2[pos] = "#"
    x,y = pos
    #print((x,y))
    if x-1 in xrange:
        if y in yrange and world2[(x-1,y)] == ".":
            fill_q.append((x-1,y))
    if x+1 in xrange:
        if y in yrange and world2[(x+1,y)] == ".":
            fill_q.append((x+1,y))
    if y-1 in yrange:
        if x in xrange and world2[(x,y-1)] == ".":
            fill_q.append((x,y-1))
    if y+1 in yrange:
        if x in xrange and world2[(x,y+1)] == ".":
            fill_q.append((x,y+1))

"""  
print(f"Part 2 answer: {total2}")    