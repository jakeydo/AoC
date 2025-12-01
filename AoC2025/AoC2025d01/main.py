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

dial = 50
zero_count = 0

for line in lines:
    line = line.strip()
    number = line[1:]
    number = int(number)
    if line[0] == "L":
        number = number * -1
    dial += number
    dial = dial % 100
    if dial < 0:
        dial += 100
    if dial > 99:
        dial -= 100
    if dial == 0:
        zero_count +=1
    print(dial)
#put the code here

print(f"Part 1 answer: {zero_count}")


print(f"Part 2 answer: {0}")