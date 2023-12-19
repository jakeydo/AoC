import sys
from collections import defaultdict
#import copy
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

inseq = lines[0].strip().split(",")
boxes = defaultdict(lambda:[])

def ha(i):
    cv = 0
    for c in i:
        cv += ord(c)
        cv *=17
        cv = cv % 256
    return cv

def process_eq(boxes,box,label,fl):
    box = boxes[box]
    for i,lens in enumerate(box):
        bl,bfl = lens
        if bl == label:
            box[i] = (label,fl)
            break
    else:
        box.append((label,fl))

def process_minus(boxes,box,label):
    box = boxes[box]
    print(box)
    for i in range(len(box)):
        bl,bfl = box[i]
        if bl==label:
            print(f"bl:{bl} bfl:{bfl} i:{i}")
            del box[i]
            break

total = 0

for i in inseq:
    h = ha(i)
    total += h
    print(f"instruction:{i} value:{h}")


print(f"part 1 answer: {total}")

for i in inseq:
    if "=" in i:
        label,fl = i.split("=")
        fl = int(fl)
        box = ha(label)
        process_eq(boxes,box,label,fl)
    else:
        label = i[:-1]
        box = ha(label)
        print(f"i:{i} label:{label} box:{box}")
        process_minus(boxes,box,label)

total2 = 0

for i,box in enumerate(boxes):
    """
    print(box)
    print(boxes[box])
    print()
    print("---")
    print()
    """
    b = boxes[box]
    for j,l in enumerate(b):
        ll,lfl = l
        adjustment = (box+1)*(j+1)*lfl
        print(adjustment)
        total2 += adjustment
    

print(f"Part 2 answer: {total2}")    