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

blocks = []
block = []
for line in lines:
    if line == "\n":
        blocks.append(block)
        block = []
    else:
        block.append(line.strip())
blocks.append(block)

total = 0
for b in blocks:
    #check reflection around horizontal line
    b_size = len(b)
    h_reflect = False
    h_reflect_rows = 0
    for x in range(b_size-1):
        left = b[:x+1]
        sub_size = len(left)
        right_end = min(b_size,x+1+sub_size)
        right = b[x+1:right_end]
        left_biggerness = len(left) - len(right)
        if left_biggerness > 0:
            left = left[left_biggerness:]
        right.reverse()
        if left == right:
            h_reflect = True
            h_reflect_rows = x+1

    #check reflection around vertical line
    b = list(map(list,zip(*b)))
    b_size = len(b)
    v_reflect = False
    v_reflect_rows = 0
    for x in range(b_size-1):
        left = b[:x+1]
        sub_size = len(left)
        right_end = min(b_size,x+1+sub_size)
        right = b[x+1:right_end]
        left_biggerness = len(left) - len(right)
        if left_biggerness > 0:
            left = left[left_biggerness:]
        right.reverse()
        if left == right:
            v_reflect = True
            v_reflect_rows = x+1
    
    if h_reflect:
        print(f"h reflection with {h_reflect_rows} rows")
        total += 100*h_reflect_rows
        
    if v_reflect:
        print(f"v reflection with {v_reflect_rows} rows")
        total += v_reflect_rows

#put the code here

print(f"Part 1 answer: {total}")


print(f"Part 2 answer: {0}")