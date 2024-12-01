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

ll = []
rl = []

ll2 = []
rl2 = []

for line in lines:
    lle, rle = line.split("   ")
    lle = int(lle)
    rle = int(rle)
    ll.append(lle)
    ll2.append(lle)
    rl.append(rle)
    rl2.append(rle)

ll.sort()
rl.sort()
#put the code here

sum_dist = 0
for i,lle in enumerate(ll):
    rle = rl[i]
    dist = abs(lle-rle)
    sum_dist += dist


print(f"Part 1 answer: {sum_dist}")

sim_sum = 0

for lle in ll2:
    count_in_rl = rl2.count(lle)
    sim = lle * count_in_rl
    sim_sum += sim


print(f"Part 2 answer: {sim_sum}")