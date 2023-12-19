import sys
from collections import defaultdict
import copy
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

rocks = defaultdict(lambda:".")
index = 0

rocks2 = []

number_lines = len(lines)
number_chars = len(lines[0].strip())

for x, line in enumerate(lines):
    row = []
    for y, c in enumerate(line.strip()):
        row.append(c)
        if c != ".":
            rocks[index] = {'x':x, 'y':y, 'kind':c}
            if c == "#":
                rocks[index]['stopped'] = True
            else:
                rocks[index]['stopped'] = False
            index +=1
    rocks2.append(row)

def can_move(position,rocks):
    x,y = position
    #print(f"checking position {position}")
    if x < 0:
        #print("return false")
        return False
    potentials = [r for r in rocks if (rocks[r]['x'] == x and rocks[r]['y'] ==y)]
    if len(potentials) == 0:
        #print("return true")
        return True
    else:
        #print("return false")
        return False


def print_rocks(rocks,nl,nc):
    for x in range(nl):
        row = ""
        for y in range(nc):                        
            r = [r for r in rocks if (rocks[r]['x'] == x and rocks[r]['y'] ==y)]
            if len(r) > 0:
                #print(f"x:{x} y:{y}")
                r = r[0]
                r = rocks[r]
                #print(r['kind'])
                row += r['kind']
            else:
                #print(".")
                row += "."
        print(row)
        row = ""
            
#print_rocks(rocks,number_lines,number_chars)


"""
for x in range(len(lines)):
    movers = [r for r in rocks if (not rocks[r]['stopped'] and rocks[r]['x'] == x)]
    #print(f"line {x}")
    for r in movers:
        r = rocks[r]
        x,y,kind = r['x'], r['y'], r['kind']
        pos = (x-1,y)
        while can_move(pos,rocks):
            r['x'] = pos[0]
            pos = (pos[0]-1,pos[1])
        r['stopped'] = True
        #print(f"x:{x} y:{y} kind:{kind}")
        
print()
print()
print("after rolling")
#print_rocks(rocks,number_lines,number_chars)

#put the code here

rollers = [r for r in rocks if rocks[r]['kind'] == "O"]
total = 0
for r in rollers:
    r = rocks[r]
    force_factor = (number_lines) - r['x']
    total += force_factor
    x,y = r['x'],r['y']
    #print(f"x:{x} y:{y} ff:{force_factor}")
"""

def print_rocks2(rocks):
    print()
    print("***")
    for x in range(len(rocks)):
        print(rocks[x])
    print()
    
def roll_rock(rocks,position,direction):
    x1,y1= position
    x2,y2= direction
    
    newx = x1+x2
    newy = y1+y2
    
    #print(f"direction:{direction}")
    #if direction == (1,0):
    #    print(f"newx:{newx} newy:{newy}")
    
    if rocks[x1][y1] == "O" and newx in range(len(rocks)) and newy in range(len(rocks[0])) and rocks[newx][newy] == ".":
        rocks[x1][y1] = "."
        rocks[newx][newy] = "O"
    #    if direction == (1,0):
    #        print_rocks2(rocks)
        roll_rock(rocks,(newx,newy),direction)
    else:
        return False

total = 0

rocks = copy.deepcopy(rocks2)
d = (-1,0)
xr = range(len(rocks))
yr = range(len(rocks[0]))
if d[0] == 1:
    xr = reversed(xr)
if d[1] == 1:
    yr = reversed(yr)
#print(f"direction:{d}")
for x in xr:
    yr = range(len(rocks[0]))
    if d[1] == 1:
        yr = reversed(yr)
    for y in yr:
        #print(f"y loop x:{x} y:{y}")
        roll_rock(rocks,(x,y),d)

total = 0
x_size = len(rocks)
y_size = len(rocks[0])
for x in range(x_size):
    force_factor = x_size - x
    for y in range(y_size):
        if rocks[x][y] == "O":
            total += force_factor
print(f"part 1 answer: {total}")

#print_rocks2(rocks2)

directions = [(-1,0),(0,-1),(1,0),(0,1)]

breakout = False

for d in directions:
    xr = range(len(rocks2))
    yr = range(len(rocks2[0]))
    
    if d[0] == 1:
        xr = reversed(xr)
    if d[1] == 1:
        yr = reversed(yr)
    
    
    #print(f"direction:{d}")
    for x in xr:
        yr = range(len(rocks2[0]))
        if d[1] == 1:
            yr = reversed(yr)
        for y in yr:
            #print(f"y loop x:{x} y:{y}")
            roll_rock(rocks2,(x,y),d)
#print_rocks2(rocks2)

original = copy.deepcopy(rocks2)
i = 1
cycle_results = [original]
repeated_indices = set()

while not breakout:
    #print(f"cycle {i}")
    total2 = 0
    x_size = len(rocks2)
    y_size = len(rocks2[0])
    for x in range(x_size):
        force_factor = x_size - x
        for y in range(y_size):
            if rocks2[x][y] == "O":
                total2 += force_factor
    #print(f"after {i} cycles, load: {total2}")
    for d in directions:
        xr = range(len(rocks2))
        yr = range(len(rocks2[0]))
        
        if d[0] == 1:
            xr = reversed(xr)
        if d[1] == 1:
            yr = reversed(yr)
        
        
        #print(f"direction:{d}")
        for x in xr:
            yr = range(len(rocks2[0]))
            if d[1] == 1:
                yr = reversed(yr)
            for y in yr:
                #print(f"y loop x:{x} y:{y}")
                roll_rock(rocks2,(x,y),d)
    #print_rocks2(rocks2)
    match_count = 0
    for ri,result in enumerate(cycle_results):
        #print(f"ri:{ri}")
        match = True
        for x in range(len(rocks2)):
            for y in range(len(rocks2[0])):
                if result[x][y] != rocks2[x][y]:
                    match = False
                    break
            if not match:
                break
        if match:
            match_count +=1
            if match_count > len(repeated_indices):
                repeated_indices.add(i)
            #print(f"cycle repeated after {i} cycles")
            if len(repeated_indices) > 2:
                breakout = True
            
    cycle_results.append(copy.deepcopy(rocks2))
    i = i+1

repeated_indices = list(repeated_indices)
repeated_indices.sort()
#print(repeated_indices)
x,x1,x2 = repeated_indices
r = x2-x1
y=1000000000-x1
y2=y//r*r
a=y-y2
right_rocks = x1+a

right_rocks = cycle_results[right_rocks - 1]
total2 = 0
x_size = len(right_rocks)
y_size = len(right_rocks[0])
for x in range(x_size):
    force_factor = x_size - x
    for y in range(y_size):
        if right_rocks[x][y] == "O":
            total2 += force_factor

print(f"Part 2 answer: {total2}")    
    
    
"""
for x in range(len(rocks2)):
    for y in range(len(rocks2[0])):
        roll_rock(rocks2,(x,y),(-1,0))

print_rocks2(rocks2)

for x in range(len(rocks2)):
    for y in range(len(rocks2[0])):
        roll_rock(rocks2,(x,y),(0,-1))

print_rocks2(rocks2)

for x in range(len(rocks2)):
    for y in range(len(rocks2[0])):
        roll_rock(rocks2,(x,y),(1,0))

print_rocks2(rocks2)

for x in range(len(rocks2)):
    for y in range(len(rocks2[0])):
        roll_rock(rocks2,(x,y),(0,1))        

print_rocks2(rocks2)
"""



