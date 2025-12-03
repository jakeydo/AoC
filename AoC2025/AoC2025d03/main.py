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

maxes = []
for line in lines:
    line = line.strip()
    bank_max = int(line[:2])
    for i in range(len(line)-1):
        d1 = line[i]
        d2 = max(line[i+1:])
        bank_max = max(bank_max,int(d1+d2))
    maxes.append(bank_max)
    #print(bank_max)

#put the code here

print(f"Part 1 answer: {sum(maxes)}")

batteries = []

for line in lines:
    line = line.strip()
    digits_left = 12
    battery = ""
    for digits_left in range(12,0,-1):
        sub_line = line[:len(line)-digits_left+1]
        max_d = max(sub_line)
        i = sub_line.index(max_d)
        battery += max_d
        line = line[i+1:]
        """
        #print(".")
        x = len(line) - digits_left
        sub_line = line[:-x]
        print(f"old line is {line}")
        print(f"sub_line is {sub_line}")
        max_d = max(sub_line)
        i = sub_line.index(max_d)
        battery += max_d        
        line = line[i+1:]
        print(f"new line is {line}")
        print(f"max_d:{max_d}, i: {i}, battery: {battery}, digits_left: {digits_left}")
        print()
        """
    batteries.append(int(battery))


print(f"Part 2 answer: {sum(batteries)}")