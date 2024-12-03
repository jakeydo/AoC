import sys
import re
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
lines = f.read()

#put the code here

pairs = re.findall("mul\(\d+,\d+\)", lines)

results = 0
for p in pairs:
    x,y = p.split(",")
    x = x.split("(")[-1]
    x = int(x)
    y = y.split(")")[0]
    y = int(y)
    #print(f"{x},{y}")
    results += x*y

print(f"Part 1 answer: {results}")


ins = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", lines)
doing = True
results = 0

for i in ins:
    #print(i)
    if i == "do()":
        doing = True
    elif i == "don't()":
        doing = False
    else:
        if doing:
            x,y = i.split(",")
            x = x.split("(")[-1]
            x = int(x)
            y = y.split(")")[0]
            y = int(y)
            #print(f"{x},{y}")
            results += x*y
            

print(f"Part 2 answer: {results}")