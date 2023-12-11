import sys
import copy
#from collections import defaultdict
#from os import system
#import time
#from functools import cache
#sys.setrecursionlimit(10**7)
args = str(sys.argv)
real_start ="S"
if ("test" in args):
    f = open("test.txt")
    real_start = "F"
else:
    f = open("real.txt")
    real_start = "|"
lines = f.readlines()

#add . all around the maze so we never check outside the bounds of the arrays
maze = []
dot_row = "."
for i in range(len(lines[0])):
    dot_row += "."
maze.append(dot_row)
for line in lines:
    row = "."
    row += line.strip()
    row += "."
    maze.append(row)
maze.append(dot_row)
 
    
def find_start(maze):
    for x in range(len(maze)):
        for y in range(len(maze[x])):
            if maze[x][y] == "S":
                return (x,y)
    return (-1,-1)

start = find_start(maze)
x,y = start
maze[x] = maze[x][:y] + real_start + maze[x][y+1:]

print(f"start:{start}")

def connects_up(c):
    return c == "|" or c == "J" or c == "L"
    
def connects_down(c):
    return c == "|" or c == "F" or c == "7"

def connects_left(c):
    return c == "-" or c == "7" or c == "J"

def connects_right(c):
    return c == "-" or c == "L" or c == "F"

def find_options(maze,location):
    options = []
    x,y = location
    if connects_up(maze[x][y]) and connects_down(maze[x-1][y]):
        options.append((x-1,y))
    if connects_down(maze[x][y]) and connects_up(maze[x+1][y]):
        options.append((x+1,y))
    if connects_left(maze[x][y]) and connects_right(maze[x][y-1]):
        options.append((x,y-1))
    if connects_right(maze[x][y]) and connects_left(maze[x][y+1]):
        options.append((x,y+1))
    return set(options)

visited = set()
previous = (0,0)
current = start
steps = 1

while True:
    opts = find_options(maze,current)
    opts = opts.difference(visited)
    opts = list(opts)
    if not len(opts) > 0:
        visited.add(current)
        break
    else:
        previous = current
        visited.add(current)
        steps +=1
        current = opts[0]
#print(find_options(maze,(x,y)))

print(f"Part 1 answer: {steps//2}")

def x_path(maze,visited):
    new_maze = copy.deepcopy(maze)
    for v in visited:
        x,y = v
        new_maze[x] = new_maze[x][:y] + "x" + new_maze[x][y+1:]
    return new_maze


def boundaries_looking_left(maze, location):
    x,y = location
    short_row = str(maze[x][:y])
    short_row = short_row.replace("-", "")
    boundary_count = short_row.count("L7") + short_row.count("FJ") + short_row.count ("|")
    #print(short_row)
    return boundary_count
    
def boundaries_looking_right(maze, location):
    x,y = location
    short_row = str(maze[x][y+1:])
    short_row = short_row.replace("-", "")
    boundary_count = short_row.count("L7") + short_row.count("FJ") + short_row.count ("|")
    #print(short_row)
    return boundary_count

def boundaries_looking_up(maze, location):
    y,x = location
    short_row = str(maze[x][:y])
    short_row = short_row.replace("|", "")
    boundary_count = short_row.count("FJ") + short_row.count("7L") + short_row.count ("_")
    #print(short_row)
    return boundary_count

def boundaries_looking_down(maze, location):
    y,x = location
    short_row = str(maze[x][y+1:])
    short_row = short_row.replace("|", "")
    boundary_count = short_row.count("FJ") + short_row.count("7L") + short_row.count ("_")
    #print(short_row)
    return boundary_count
    

def is_inside(maze, t_maze, location):
    x,y = location
    if not maze[x][y] == ".":
        return False
    
    else:
        left_count = boundaries_looking_left(maze, location)
        right_count = boundaries_looking_right(maze, location)
        up_count = boundaries_looking_up(t_maze,location)
        down_count = boundaries_looking_down(t_maze,location)
    
    return (left_count % 2 == 1) or (right_count % 2 == 1) or (up_count % 2 == 1) or (down_count % 2 == 1)

for x in range(len(maze)):
    for y in range(len(maze[0])):
        if not (x,y) in visited:
            maze[x] = maze[x][:y] + "." + maze[x][y+1:]
    

t_maze = list(map(list,zip(*maze)))
x_maze = x_path(maze,visited)
t_x_maze = list(map(list,zip(*x_maze)))


inside_count = 0
for x in range(len(maze)):
    for y in range(len(maze[0])):
        if is_inside(maze, t_maze, (x,y)):
            inside_count +=1



print(f"Part 2 answer: {inside_count}")