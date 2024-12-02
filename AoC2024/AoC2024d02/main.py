import sys
from copy import deepcopy
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

reports = []

for line in lines:
    levels = line.split()
    for i,l in enumerate(levels):
        levels[i] = int(l)
    reports.append(levels)

#put the code here

number_safe = 0

def sign(x,y):
    if y-x > 0:
        return 1
    elif y-x < 0:
        return -1
    else:
        return 0

def is_unsafe(r):
    unsafe = False
    bad_level_index = -1
    s = sign(r[1],r[0])
    delta = abs(r[1] - r[0])
    if delta > 3 or delta < 1:
        #unsafe = True
        #bad_level_index = 1
        return (True, 1)
    for i in range(2,len(r)):
        #print(r[i])
        if unsafe:
            pass
        else:
            x = r[i]
            y = r[i-1]
            delta = abs(x-y)
            new_s = sign(r[i],r[i-1])
            if (new_s != s) or (delta >3) or (delta <1):
                #print(f"x: {x} y:{y} sign:{s} delta:{delta}")
                unsafe = True
                bad_level_index = i
                return (True, i)
    return (False, -1)

for j,r in enumerate(reports):
    unsafe, bad_level_index = is_unsafe(r)
    if not unsafe:
        number_safe += 1
    else:
        pass
        #print(f"{j} is unsafe")
            

print(f"Part 1 answer: {number_safe}")

unsafe_list = []

for j,r in enumerate(reports):
    unsafe,bad_level_index = is_unsafe(r)
    if unsafe:
        unsafe_list.append(r)

#print("unsafe list")
#print(unsafe_list)

safe_reports_in_unsafe_list = []

for u in unsafe_list:
    #print()
    #print(u)
    original_u = u
    u = deepcopy(original_u)
    removed = False
    for i in range(len(u)):
        if not removed:
            u.pop(i)
            unsafe,bad_level_index = is_unsafe(u)
            if not unsafe:
                #print(original_u)
                #unsafe_list.remove(original_u)
                safe_reports_in_unsafe_list.append(original_u)
                removed = True
            else:
                u = deepcopy(original_u)

for u in safe_reports_in_unsafe_list:
    unsafe_list.remove(u)

number_safe = len(reports) - len(unsafe_list)
#print(f"len report:{len(reports)}, len unsafe:{len(unsafe_list)}")

"""
number_safe = 0
bad_level_index = -1
for j,r in enumerate(reports):
    unsafe, bad_level_index = is_unsafe(r)
    if not unsafe:
        number_safe += 1
    else:
        original_r = deepcopy(r)
        print(f"original report at index {j} was unsafe, bad_level_index: {bad_level_index}")
        print(f"old_report: {r}")        
        r.pop(bad_level_index)
        print(f"new_report: {r}")
        unsafe,bad_level_index = is_unsafe(r)
        if not unsafe:
            number_safe += 1
        else:
            original_r.pop(0)
            unsafe,bad_level_index = is_unsafe(original_r)
            if not unsafe:
                number_safe += 1
            else:
                print(f"{j} is unsafe")
        print()
        
"""    

print(f"Part 2 answer: {number_safe}")