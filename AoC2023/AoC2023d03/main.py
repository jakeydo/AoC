import sys
#from collections import defaultdict
#from os import system
#import time
#from functools import cache
#sys.setrecursionlimit(10**7)
args = str(sys.argv)
if ("test" in args):
    test = True
else:
    test = False
if test:
    f = open("test.txt")
else:
    f = open("real.txt")
lines = f.readlines()

class Number():
    line = -1
    start = -1
    end = -1
    value = -1
    
    def coords(self):
        coords = set()
        for i in range(self.start,self.end+1):
            coords.add((self.line,i))
        return coords

numbers = set()
universe_coords = set()

for line_number, line in enumerate(lines):
    buffer = ""
    start = -1
    line = line.strip()
    
    for i, c in enumerate(line):
        if i == 10:
            print("!!!!!!!!")
            print(c)
        universe_coords.add((line_number,i))
        if c.isdigit():
            buffer = buffer + c
            if start == -1:
                start = i
            if len(line) == i+1 or not line[i+1].isdigit():
                n = Number()
                n.line = line_number
                n.start = start
                n.end = i
                n.value = int(buffer)
                n.max_lines = len(lines)
                
                buffer = ""
                start = -1
                numbers.add(n)

def adjacent_coordinates(n,universe):
    coords = set()
    prev_line = n.line - 1
    next_line = n.line + 1
    prev_x = n.start - 1
    next_x = n.end + 1
    
    for i in range(prev_line,next_line+1):
        for j in range(prev_x,next_x+1):
            coords.add((i,j))
    
    for i in range(n.start,n.end+1):
        coords.remove((n.line,i))
    
    to_remove = set()
    for c in coords:
        if not c in universe:
            to_remove.add(c)
    for c in to_remove:
        coords.remove(c)
    
    return coords

#print(universe_coords)    
part_numbers = []
for n in numbers:
    adj = adjacent_coordinates(n,universe_coords)
    part_number = False
    for x,y in adj:
        if not lines[x][y] == '.':
            part_number = True
            break
    if part_number:
        part_numbers.append(n.value)



print(f"Part 1 answer: {sum(part_numbers)}")
print(f"Part 2 answer: {0}")