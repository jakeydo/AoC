import sys
#from collections import defaultdict
#import copy
#from os import system
#import time
#from functools import cache
sys.setrecursionlimit(10**7)
args = str(sys.argv)
if ("test" in args):
    f = open("test.txt")
else:
    f = open("real.txt")
lines = f.readlines()

layout = []
for line in lines:
    line = line.strip()
    layout.append(line)
    #print(line)

def walk(maze,beam,history):
    if beam in history:
        return history
    #print(f"beam:{beam} lenvl:{len(history)}")
    location,direction = beam
    x,y = location
    #print(maze)
    #print(f"x:{x} y:{y} do i return?")
    if (not x in range(len(maze))) or (not y in range(len(maze[0]))):
        #print("returning at top")
        return history
    history.add(beam)
    deltax,deltay = direction

    
    if maze[x][y] == "." or (maze[x][y] == "-" and deltax==0) or (maze[x][y] == "|" and deltay==0):
        newx = x+deltax
        newy = y+deltay
        new_location = (newx,newy)
        new_beam = (new_location,direction)
        return walk(maze,new_beam,history)
    elif deltay != 0 and maze[x][y] == "|":
        new_l1 = (x+1,y)
        new_l2 = (x-1,y)
        new_d1 = (1,0)
        new_d2 = (-1,0)
        b1 = (new_l1,new_d1)
        b2 = (new_l2,new_d2)
        return walk(maze,b1,history).union(walk(maze,b2,history))
    elif deltax != 0 and maze[x][y] == "-":
        new_l1 = (x,y+1)
        new_l2 = (x,y-1)
        new_d1 = (0,1)
        new_d2 = (0,-1)
        b1 = (new_l1,new_d1)
        b2 = (new_l2,new_d2)
        #print(f"b1:{b1} b2:{b2}")
        return walk(maze,b1,history).union(walk(maze,b2,history))
    elif maze[x][y] == "/":
        if direction == (0,1):
            deltax = -1
            deltay = 0
            newx = x + deltax
            newy = y + deltay
            newl = (newx,newy)
            newd = (deltax,deltay)
            b = (newl,newd)
            return walk(maze,b,history)
        if direction == (0,-1):
            deltax = 1
            deltay = 0
            newx = x + deltax
            newy = y + deltay
            newl = (newx,newy)
            newd = (deltax,deltay)
            b = (newl,newd)
            return walk(maze,b,history)
        if direction == (1,0):
            deltax = 0
            deltay = -1
            newx = x + deltax
            newy = y + deltay
            newl = (newx,newy)
            newd = (deltax,deltay)
            b = (newl,newd)
            return walk(maze,b,history)
        if direction == (-1,0):
            deltax = 0
            deltay = 1
            newx = x + deltax
            newy = y + deltay
            newl = (newx,newy)
            newd = (deltax,deltay)
            b = (newl,newd)
            return walk(maze,b,history)
    elif maze[x][y] == "\\":
        if direction == (0,1):
            deltax = 1
            deltay = 0
            newx = x + deltax
            newy = y + deltay
            newl = (newx,newy)
            newd = (deltax,deltay)
            b = (newl,newd)
            return walk(maze,b,history)
        if direction == (0,-1):
            deltax = -1
            deltay = 0
            newx = x + deltax
            newy = y + deltay
            newl = (newx,newy)
            newd = (deltax,deltay)
            b = (newl,newd)
            return walk(maze,b,history)
        if direction == (1,0):
            deltax = 0
            deltay = 1
            newx = x + deltax
            newy = y + deltay
            newl = (newx,newy)
            newd = (deltax,deltay)
            b = (newl,newd)
            return walk(maze,b,history)
        if direction == (-1,0):
            deltax = 0
            deltay = -1
            newx = x + deltax
            newy = y + deltay
            newl = (newx,newy)
            newd = (deltax,deltay)
            b = (newl,newd)
            return walk(maze,b,history)
    else:
        print("why am i returning here?")
    
    
    

location = (0,0)
direction = (0,1)
beam = (location,direction)
history = set()
history = walk(layout,beam,history)

visited_locations = set()
for b in history:
    visited_locations.add(b[0])

#print(visited_locations)

print(f"part 1 answer: {len(visited_locations)}")

max_energized = 0

direction = (0,1)
y = 0
for x in range(len(layout)):
    location = (x,y)
    b2 = (location,direction)
    h2 = set()
    h2 = walk(layout,b2,h2)
    vl2 = set()
    for b in h2:
        vl2.add(b[0])
    max_energized = max(max_energized,len(vl2))

direction = (0,-1)
y = len(layout[0])-1
for x in range(len(layout)):
    location = (x,y)
    b2 = (location,direction)
    h2 = set()
    h2 = walk(layout,b2,h2)
    vl2 = set()
    for b in h2:
        vl2.add(b[0])
    max_energized = max(max_energized,len(vl2))

direction = (1,0)
x = 0
for y in range(len(layout[0])):
    location = (x,y)
    b2 = (location,direction)
    h2 = set()
    h2 = walk(layout,b2,h2)
    vl2 = set()
    for b in h2:
        vl2.add(b[0])
    max_energized = max(max_energized,len(vl2))    

direction = (-1,0)
x = len(layout)-1
for y in range(len(layout[0])):
    location = (x,y)
    b2 = (location,direction)
    h2 = set()
    h2 = walk(layout,b2,h2)
    vl2 = set()
    for b in h2:
        vl2.add(b[0])
    max_energized = max(max_energized,len(vl2)) 
    
print(f"Part 2 answer: {max_energized}")    