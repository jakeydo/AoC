import sys
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

world = []

for line in lines:
    world.append(line.strip())


#put the code here

pos = (0,0)
for i in range(len(world)):
    for j in range(len(world[i])):
        if world[i][j] == "^":
            pos = (i,j)

x,y = pos
up = (-1,0)
down = (1,0)
left = (0,-1)
right = (0,1)
direction = up

ip = pos
start = (pos,up)

visited = set()

def next_direction(current):
    up = (-1,0)
    down = (1,0)
    left = (0,-1)
    right = (0,1)
    if current == up:
        return right
    elif current == right:
        return down
    elif current == down:
        return left
    else:
        return up

while (x in range(len(world))) and (y in range(len(world[0]))):
    #print(pos)
    visited.add(pos)
    dx,dy = direction
    x,y = pos
    newx = x+dx
    newy = y+dy
    if (newx in range(len(world)) and newy in range(len(world[0]))) and (world[newx][newy] == "#"):
        direction = next_direction(direction)
        dx,dy = direction
        newx = x+dx
        newy = y+dy
    x = newx
    y = newy
    pos = (x,y)
    
print(f"Part 1 answer: {len(visited)}")


obstacles = set()
for i in range(len(world)):
    for j in range(len(world[0])):
        if world[i][j] == "#":
            obstacles.add((i,j))

loop_obstacles = set()

for ox in range(len(world)):
    for oy in range(len(world)):
        print(f"checking:{ox,oy}")
        if ((ox,oy) in obstacles) or ((ox,oy)==ip):
            pass
        else:
            obstacles.add((ox,oy))
            visited = set()
            pos_v = start
            pos,direction = pos_v
            x,y = pos
            
            while (x in range(len(world))) and (y in range(len(world[0]))):
                if pos_v in visited:
                    loop_obstacles.add((ox,oy))
                    break
                else:
                    visited.add(pos_v)
                    dx,dy = direction
                    pos,direction = pos_v
                    x,y = pos
                    newx = x+dx
                    newy = y+dy
                    while (newx,newy) in obstacles:
                        direction = next_direction(direction)
                        dx,dy = direction
                        newx = x+dx
                        newy = y+dy
                    x = newx
                    y = newy
                    pos = (x,y)
                    pos_v = (pos,direction)
            obstacles.remove((ox,oy))

"""
for ox in range(len(world)):
    for oy in range(len(world[0])):
        print(f"checking:{ox,oy}")
        visited = set()
        loop = False
        pos_v = start
        pos,direction = pos_v
        x,y = pos
        
        while (not loop) and (x in range(len(world))) and (y in range(len(world[0]))):
                if pos_v in visited:
                    loop_obstacles.add((ox,oy))
                    #print(pos_v)
                    print(f"adding {(ox,oy)} to loop obstacles")
                    break
                else:
                    visited.add(pos_v)
                    #print(len(visited))
                
                pos,direction = pos_v
                dx,dy = direction
                x,y = pos
                newx = x+dx
                newy = y+dy
                if (newx in range(len(world)) and newy in range(len(world[0]))) and ((world[newx][newy] == "#") or (newx,newy)==(ox,oy)):
                    direction = next_direction(direction)
                    dx,dy = direction
                    newx = x+dx
                    newy = y+dy
                x = newx
                y = newy
                pos_v = ((x,y),direction)                


"""
print(f"Part 2 answer: {len(loop_obstacles)}")