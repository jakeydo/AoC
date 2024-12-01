import sys
import copy
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

class Brick:
    #s = (0,0,1)
    #e = (0,0,1)
    def __init__(self,s,e):
        self.s = s
        self.e = e
    
    def __str__(self):
        return f"Start: {self.s} \nEnd: {self.e}\nW: {self.w()}\tD: {self.d()}\tH: {self.h()}"
        
    def h(self):
        return abs(self.e[2] - self.s[2]) + 1
        
    def w(self):
        return abs(self.e[0] - self.s[0]) + 1
    
    def d(self):
        return abs(self.e[1] - self.s[1]) + 1
        
    def points(self):
        p = set()
        for x in range(self.s[0],self.e[0]+1):
            for y in range(self.s[1],self.e[1]+1):
                for z in range(self.s[2],self.e[2]+1):
                    p.add((x,y,z))
        return(p)
    
    def bottom(self):
        return min(self.s[2],self.e[2])

bricks = set()
for line in lines:
    s,e = line.strip().split("~")
    s = s.split(",")
    s = (int(s[0]),int(s[1]),int(s[2]))
    e = e.split(",")
    e = (int(e[0]),int(e[1]),int(e[2]))
    b = Brick(s,e)
    bricks.add(b)

original_bricks = copy.deepcopy(bricks)
settled_bricks = set()

world = defaultdict(lambda: ".")

"""
for b in bricks:
    print(b)
    print(b.points())
    print(f"bottom is {b.bottom()}")
    print()
"""    
#put the code here

for o in original_bricks:
    print(o)

print("and here are the fbs")
foundation_bricks = [b for b in original_bricks if (b.bottom() == 1)]
for fb in foundation_bricks:
    print(fb)


print(f"Part 1 answer: {0}")


print(f"Part 2 answer: {0}")