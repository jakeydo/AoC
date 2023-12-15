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

def horizontal_reflection(b):
    #check reflection around horizontal line
    print("finding hr")
    for l in b:
        disp = ""
        for c in l:
            disp+= c
        print(disp)
    print()
    b_size = len(b)
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
            return x+1
    return 0

def vertical_reflection(b):
    print("finding vertical")
    bprime = list(map(list,zip(*b)))
    return horizontal_reflection(bprime)

def find_smudge(b):
    print("finding smudge in block")
    return_val = 0
    b_size = len(b)
    for x in range(b_size-1):
        print(f"checking reflect on row:{x+1}")
        left = b[:x+1]
        sub_size = len(left)
        right_end = min(b_size,x+1+sub_size)
        right = b[x+1:right_end]
        left_biggerness = len(left) - len(right)
        if left_biggerness > 0:
            left = left[left_biggerness:]
        right.reverse()
        
        diff_count = 0
        last_diff = False
        
        for x in range(len(left)):
            return_val = (len(left)+left_biggerness) * 100
            for y in range(len(left[x])):
                if left[x][y] != right[x][y]:
                    diff_count +=1
                    last_diff = (left_biggerness+x,y)
                    print(f"diff count:{diff_count}, loc:{(x,y)}")
                    if diff_count > 1:
                        last_diff = False
                        break
            if diff_count > 1:
                break
        if last_diff:
            print(return_val)
            #return last_diff
            return return_val

    bprime = b[:]
    bprime = list(map(list,zip(*b)))
    b_size = len(bprime)
    for x in range(b_size-1):
        print(f"checking reflect on row:{x+1}")
        left = bprime[:x+1]
        sub_size = len(left)
        right_end = min(b_size,x+1+sub_size)
        right = bprime[x+1:right_end]
        left_biggerness = len(left) - len(right)
        if left_biggerness > 0:
            left = left[left_biggerness:]
        right.reverse()
        
        diff_count = 0
        last_diff = False
        for x in range(len(left)):
            return_val = len(left)+left_biggerness
            for y in range(len(left[x])):
                if left[x][y] != right[x][y]:
                    diff_count +=1
                    last_diff = (left_biggerness+x,y)
                    print(f"diff count:{diff_count}, loc:{(x,y)}")
                    if diff_count > 1:
                        last_diff = False
                        break
            if diff_count > 1:
                break
        if last_diff:
            print(return_val)
            print(f"smudge at: {last_diff}")
            #return last_diff
            return return_val
    print(bprime)

    #return False

#put the code here

total = 0
total2 = 0

for i,b in enumerate(blocks):
    
    print(f"about to check unmessed with block {i}")
    hr = horizontal_reflection(b)
    vr = vertical_reflection(b)
    print(f"b hr:{hr} vr:{vr}")
    total += 100*hr + vr
    """
    x,y = smudge
    bprime = b[:]
    bprime[x] = list(map(str,bprime[x]))
    if bprime[x][y] == "#":
        bprime[x][y] = "."
    else:
        bprime[x][y] = "#"
    print("now on bprime")
    hr = horizontal_reflection(bprime)
    vr = vertical_reflection(bprime)
    print(f"bprime hr:{hr} vr:{vr}")
    total2 += 100*hr + vr 
    """
    
    smudge = find_smudge(b)
    total2 += smudge
    print(f"smudge value: {smudge}")
    print()

print(f"Part 1 answer: {total}")

print(f"Part 2 answer: {total2}")