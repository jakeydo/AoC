import sys
import copy
#from collections import defaultdict
#from os import system
#import time
#from functools import cache
#sys.setrecursionlimit(10**7)
args = str(sys.argv)
if ("test" in args):
    step_count = 6
    f = open("test.txt")
else:
    step_count = 64
    f = open("real.txt")
lines = f.readlines()

maze = []

for line in lines:
    maze.append(line.strip())

h = len(maze)
w = len(maze[0])

start = (0,0)

def reachable(maze,pos):
    x,y = pos
    h = len(maze)
    w = len(maze[0])
    r = set()
    for d in [(0,1),(0,-1),(1,0),(-1,0)]:
        dx, dy = d
        newx,newy = x+dx,y+dy
        if newx in range(h) and newy in range(w) and (maze[newx][newy] == "." or maze[newx][newy] == "S"):
            r.add((newx,newy))
    return r

def steps_to_fill(maze,start, total_spots):
    maze = copy.deepcopy(maze)
    for i in range(len(maze)):
        maze[i] = list(maze[i])
    filled_spots = 0
    q = [(start,0)]
    while filled_spots < total_spots and q:
        pos,sc = q.pop()
        
        print()
        print(f"step count: {sc}")
        for l in maze:
            print(l)
        
        sc += 1
        for r in reachable(maze,pos):
            x,y = r
            if maze[x][y] == "." or maze[x][y] == "S":
                maze[x][y] = "#"
                filled_spots += 1
                q.append((r,sc))
    
    return sc
            
            
        

for i,r in enumerate(maze):
    for j,c in enumerate(r):
        if maze[i][j] == "S":
            start = (i,j)

#print(start)
seen = set()
possible_stops = set()
q = [(start,0)]

while q:
    step = q.pop(0)
    if step in seen:
        continue
    seen.add(step)
    pos,sc = step
    sc +=1
    for r in reachable(maze,pos):
        if sc == step_count:
            possible_stops.add(r)
        else:
            q.append((r,sc))





#put the code here
total = len(possible_stops)
print(f"Part 1 answer: {total}")

total_spots = 0

for i in range(h):
    for j in range(w):
        if maze[i][j] == "." or maze[i][j] == "S":
            total_spots +=1

s = start
s_to_f = steps_to_fill(maze,s,total_spots)

print(f"Total spots available: {total_spots}")
print(f"Takes {s_to_f} steps to fill when starting at position {s}")

print(f"Part 2 answer: {0}")