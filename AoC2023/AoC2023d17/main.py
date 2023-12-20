import sys
#from collections import defaultdict
#import copy
#from os import system
#import time
from functools import cache
sys.setrecursionlimit(10**7)
args = str(sys.argv)
if ("test" in args):
    f = open("test.txt")
else:
    f = open("real.txt")
lines = f.readlines()
total = 0
total2 = 0


maze = []
for line in lines:
    maze.append(line.strip())

maze = tuple(maze)
for l in maze:
    print(l)

start = (0,0)
target = (len(maze)-1,len(maze[0])-1)

@cache
def total_heat_loss(maze,location,hl_so_far,direction,straight_count,target):
    #print("doing stuff")
    x,y = location
    new_hl = hl_so_far + int(maze[x][y])
    print(f"loc:{location} hl:{int(maze[x][y])}  hl_so_far:{hl_so_far} target:{target}")
    if location == target:
        print(f"at target hl: {new_hl}")
        return new_hl
        
    possible_directions = [(1,0),(-1,0),(0,1),(0,-1)]
    if straight_count == 3:
        possible_directions.remove(direction)
    dx,dy = direction
    bx = dx * -1
    by = dy * -1
    backwards = (bx,by)
    possible_directions.remove(backwards)
    
    min_hl = float('inf')
    for d in possible_directions:
        if d == direction:
            straight_count += 1
        dx,dy = d
        newx = x + dx
        newy = y + dy
        new_loc = (newx,newy)
        if (newx in range(len(maze))) and (newy in range(len(maze[0]))):
            min_hl = min(min_hl, total_heat_loss(maze,new_loc,new_hl,d,straight_count,target))
    return min_hl
        

down = (1,0)
right = (0,1)
print("hello world")
total = min(total_heat_loss(maze,start,-2,down,0,target),total_heat_loss(maze,start,-2,right,0,target))
    
print("testing 1 2 3")
print(f"part 1 answer: {total}")


    
print(f"Part 2 answer: {total2}")    