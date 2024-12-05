import sys
import random
from itertools import permutations
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

rules,updates = lines.split("\n\n")

rules = rules.split("\n")
p_rules = []
for r in rules:
    x,y = r.strip().split("|")
    r = []
    r.append(int(x))
    r.append(int(y))
    p_rules.append(r)
rules = p_rules

updates = updates.split("\n")
p_updates = []
for u in updates:
    if len(u) > 1:
        u = u.strip().split(",")
        new_u = []
        for p in u:
            new_u.append(int(p))
        p_updates.append(new_u)
updates = p_updates

sum_middle = 0

bad_updates = []

for no,u in enumerate(updates):
    #print(u)
    
    indices = {}
    for i,page in enumerate(u):
        indices[page] = i
    #print(indices)
    #print()

    good = True
    for r in rules:
        x,y = r
        if (x in u) and (y in u):
            if not indices[x] < indices[y]:
                good = False
                if not u in bad_updates:
                    bad_updates.append(u)
                #print(f"update no:{no} is bad")
    if good:
        mid = len(u) // 2
        sum_middle += u[mid]
        #print(f"update no:{no} is good, adding {u[mid]}")

    

#put the code here


print(f"Part 1 answer: {sum_middle}")

bad_sum_middle = 0
for b in bad_updates:
    check = True
    indices = {}
    for i,page in enumerate(b):
        indices[page] = i
    while check:
        check = False
        for r in rules:
            x,y = r
            if (x in b) and (y in b):
                #print(f"x:{x} y:{y} b:{b} indices:{indices}")
                if not indices[x] < indices[y]:
                    temp = indices[x]
                    indices[x] = indices[y]
                    indices[y] = temp
                    check = True
    #print(indices)
    for page,i in indices.items():
       # print(f"i:{i} page:{page}")
        if i == len(b) // 2:
            #print(f"adding stuff i:{i} page:{page}")
            bad_sum_middle += page
"""
    perms = permutations(b)
    
    
    for p in perms:
        found = False
        if not found:
            indices = {}
            for i,page in enumerate(p):
                indices[page] = i
            
            good = True
            for r in rules:
                x,y = r
                if (x in b) and (y in b):
                    if not indices[x] < indices[y]:
                        good = False
            if good:
                found = True
                mid = len(p) // 2
                bad_sum_middle += p[mid]
           
"""
           
"""
    again = True
    while again:
        random.shuffle(b)
        indices = {}
        for i,page in enumerate(b):
            indices[page] = i
        
        good = True
        for r in rules:
            x,y = r
            if (x in b) and (y in b):
                if not indices[x] < indices[y]:
                    good = False
        
        if good:
            mid = len(b) // 2
            bad_sum_middle += b[mid]
            print(b)
            again = False

"""
print(f"Part 2 answer: {bad_sum_middle}")