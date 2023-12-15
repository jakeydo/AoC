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

rocks = defaultdict(lambda:".")
index = 0

number_lines = len(lines)
number_chars = len(lines[0].strip())

for x, line in enumerate(lines):
    for y, c in enumerate(line.strip()):
        if c != ".":
            rocks[index] = {'x':x, 'y':y, 'kind':c}
            if c == "#":
                rocks[index]['stopped'] = True
            else:
                rocks[index]['stopped'] = False
            index +=1

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
print(f"Part 1 answer: {total}")


print(f"Part 2 answer: {0}")