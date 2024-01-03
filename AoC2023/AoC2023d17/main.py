import sys
import math
from heapq import heappush,heappop
#from collections import defaultdict
#import copy
#from os import system
#import time
from functools import cache
sys.setrecursionlimit(10**7)
args = str(sys.argv)
if ("test2" in args):
    f = open("test2.txt")
elif ("test" in args):
    f = open("test.txt")
else:
    f = open("real.txt")
lines = f.readlines()
total = 0
total2 = 0


maze = []
for line in lines:
    line = line.strip()
    row = []
    for c in line:
        row.append(int(c))
    maze.append(row)

min_heatmap = []
for row in maze:
    new_row = []
    for e in row:
        new_row.append(math.inf)
    min_heatmap.append(new_row)

h = len(maze)
w = len(maze[0])
min_heatmap[0][0] = 0

def reachable(maze,location,direction,straight_count):
    h = len(maze)
    w = len(maze[0])
    x,y = location
    deltax,deltay = direction
    #print(direction)
    reachable_locs = set()
    possible_d = [(1,0),(-1,0),(0,1),(0,-1)]
    possible_d.remove((-deltax,-deltay))
    if straight_count >= 3:
        possible_d.remove(direction)
    for d in possible_d:
        pdx,pdy = d
        newx = x+pdx
        newy = y+pdy
        if newx in range(h) and newy in range(w):
            reachable_locs.add((newx,newy))
    #print("rls:")
    #print(reachable_locs)
    #print("***")
    return reachable_locs

def reachable2(maze,location,direction,straight_count):
    h = len(maze)
    w = len(maze[0])
    x,y = location
    deltax,deltay = direction
    #print(direction)
    reachable_locs = set()
    possible_d = [(1,0),(-1,0),(0,1),(0,-1)]
    possible_d.remove((-deltax,-deltay))
    if straight_count < 4:
        possible_d = [direction]
    if straight_count >= 10:
        possible_d.remove(direction)
    for d in possible_d:
        pdx,pdy = d
        newx = x+pdx
        newy = y+pdy
        if newx in range(h) and newy in range(w):
            reachable_locs.add((newx,newy))
    #print("rls:")
    #print(reachable_locs)
    #print("***")
    return reachable_locs


"""
visited = set()
start = (0,0)
to_visit = set()

   
#location, hl so far, straight count, direction
v1 = (start,0,0,(0,1))
v2 = (start,0,0,(1,0))
go_visit = [v1,v2]
visited.add((0,0))


while len(go_visit) > 0:
    v = go_visit.pop(0)
    location,hl_so_far,straight_count,direction = v
    print(f"visiting: {location}")
    #visited.add(location)
    x,y = location
    hl_so_far += maze[x][y]
    if x == 0 and y == 0:
        hl_so_far = 0
        
    min_heatmap[x][y] = min(min_heatmap[x][y],hl_so_far)
    
    for r in reachable(maze,location,direction,straight_count):
        newx,newy = r
        newdx = newx-x
        newdy = newy-y
        newd = (newdx,newdy)
        newsc = 0
        if newd == direction:
            newsc = straight_count + 1
        else:
            newsc = 0
        new_visit = (r,hl_so_far,newsc,newd)
        new_pair = (r,newd)
        new_min = min(min_heatmap[newx][newy],hl_so_far+maze[newx][newy])
        if new_min < min_heatmap[newx][newy]:
            min_heatmap[newx][newy] = new_min
            print(f"len of visited:{len(visited)}")
            print(f"len of go_visit:{len(go_visit)}")
            go_visit.append(new_visit)
            visited.add(r)

    


for x in range(len(min_heatmap)):
    row = []
    for y in range(len(min_heatmap[0])):
        row.append(min_heatmap[x][y])
    print(row)

print("testing 1 2 3")

total = min_heatmap[h-1][w-1]
"""

pq = []
heappush(pq,(0,(0,0),(0,1),0))
heappush(pq,(0,(0,0),(1,0),0))
seen = set()

while pq:
    hl, location, direction, straight_count = heappop(pq)
    if location == (h-1,w-1):
        print("THIS IS THE ANSWER!!!")
        print(hl)
        total = hl
        break
    
    if (location,direction,straight_count) in seen:
        continue
    
    seen.add((location,direction,straight_count))
    x,y = location
    #print(f"l:{location} d:{direction} sc:{straight_count}")
    for newx,newy in reachable(maze,location,direction,straight_count):
        #print((newx,newy))
        dx = newx-x
        dy = newy-y
        if (dx,dy) == direction:
            heappush(pq,(hl+maze[newx][newy],(newx,newy),direction,straight_count+1))
        else:
            heappush(pq,(hl+maze[newx][newy],(newx,newy),(dx,dy),1))
    

print(f"part 1 answer: {total}")

pq = []
heappush(pq,(0,(0,0),(0,1),0))
heappush(pq,(0,(0,0),(1,0),0))
seen = set()
total2 = 0

while pq:
    hl, location, direction, straight_count = heappop(pq)
    if location == (h-1,w-1) and 4<= straight_count <= 10:
        print("THIS IS THE ANSWER!!!")
        print(hl)
        total2 = hl
        break
    
    if (location,direction,straight_count) in seen:
        continue
    
    seen.add((location,direction,straight_count))
    x,y = location
    #print(f"l:{location} d:{direction} sc:{straight_count}")
    for newx,newy in reachable2(maze,location,direction,straight_count):
        #print((newx,newy))
        dx = newx-x
        dy = newy-y
        if (dx,dy) == direction:
            heappush(pq,(hl+maze[newx][newy],(newx,newy),direction,straight_count+1))
        else:
            heappush(pq,(hl+maze[newx][newy],(newx,newy),(dx,dy),1))

    
print(f"Part 2 answer: {total2}")    