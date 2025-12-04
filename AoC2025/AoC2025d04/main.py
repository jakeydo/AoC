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

adjacent = []
for q in [-1,0,1]:
    for w in [-1,0,1]:
        adjacent.append((q,w))
adjacent.remove((0,0))

for i in range(len(lines)):
    lines[i] = lines[i].strip()
    
max_x = len(lines)
max_y = len(lines[0])

def adjacent_rolls(x,y):
    adj_roll_count = 0
    for d_x,d_y in adjacent:
        x0 = x + d_x
        y0 = y + d_y
        if not ((x0 in range(max_x)) and (y0 in range(max_y))):
            pass
        else:
            if lines[x0][y0] == "@":
                adj_roll_count += 1
    return adj_roll_count

accessible = []

for i in range(max_x):
    for j in range(max_y):
        if lines[i][j] == "@":
            if adjacent_rolls(i,j) < 4:
                accessible.append((i,j))
        
#put the code here
#print(accessible)
print(f"Part 1 answer: {len(accessible)}")

removed = []
for a in accessible:
    removed.append(a)
    i,j = a
    lines[i] = lines[i][:j] + "." + lines[i][j+1:]

accessible = []
keep_going = True

while keep_going:
    for i in range(max_x):
        for j in range(max_y):
            if lines[i][j] == "@":
                    if adjacent_rolls(i,j) < 4:
                        accessible.append((i,j))
    
    if len(accessible) == 0:
        keep_going = False
    else:
        for a in accessible:
            removed.append(a)
            i,j = a
            lines[i] = lines[i][:j] + "." + lines[i][j+1:]
        accessible = []

print(f"Part 2 answer: {len(removed)}")