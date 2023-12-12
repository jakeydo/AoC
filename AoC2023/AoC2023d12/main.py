import sys
#from collections import defaultdict
#from os import system
#import time
from functools import cache
import re
#sys.setrecursionlimit(10**7)
args = str(sys.argv)
if ("test" in args):
    f = open("test.txt")
else:
    f = open("real.txt")
lines = f.readlines()

conditions = []

for line in lines:
    record, group = line.strip().split()
    group = list(map(int,group.split(",")))
    record = record + "?" + record + "?" + record + "?" + record + "?" + record
    group = group*5
    conditions.append([record,group])

def evaluate(c):
    counts = []
    current_count = 0
    for ch in c:
        if ch == "." and current_count != 0:
            counts.append(current_count)
            current_count = 0
        elif ch!= ".":
            current_count += 1
    if current_count !=0:
        counts.append(current_count)
    return counts

@cache    
def options(c):
    options = []
    bits = c.count("?")
    for i in range(2**bits):
        opt = c[:]
        b = format(i,"0"+str(bits)+"b")
        b = b.replace("0",".")
        b = b.replace("1","#")
        for ch in b:
            opt = opt.replace("?",ch,1)
        options.append(opt)
    return options

@cache
def matching_options(record,group):
    match_count = 0
    #record,group = condition
    opts = options(record)
    group = list(group)
    for o in opts:
        #input()
        #print(f"o: {o}\t eval(o): {evaluate(o)}\t group: {group}")
        if evaluate(o) == group:
            #print(f"o matches:{o}")
            match_count += 1
    return match_count
"""
total_options = 0
for c in conditions:
    #print(f"record:{c[0]}\t group: {c[1]}\t count: {matching_options(c)}")
    total_options += matching_options(c)

#put the code here

print(f"Part 1 answer: {total_options}")
"""

@cache
def mo3(record,group):
    #print(f"r:{record}\t g:{group}")
    record = record.strip(".")
    #group = list(group)
    if len(group) == 1 or record.count(".") == 0:
        return matching_options(record,group)
    else:
        group = list(group)
        records = record.split(".")
        start_r = ""
        for r in records[:-1]:
            start_r += r + "."
        start_g = group[:-1]
        end_r = records[-1]
        end_g = [group[-1]]
        return mo3(start_r,tuple(start_g)) * mo3(end_r,tuple(end_g))
    
    

@cache
def evaluate2(record, group):
    record = record.strip(".")
    group = list(group)
    #print(record)
    hash_count = record.count("#")
    if (hash_count == len(record)) and (len(group) == 1):
        #print("doing the ### thing")
        if hash_count == group[0]:
            #print("returning 1")
            return 1
        else:
            #print("returning 0")
            return 1

    record = re.sub("\.+",".",record)
    #print(f"record: {record}\t dot count:{record.count('.')}")
    if record.count(".") < 1:
        #print("no dots in record")
        ans = matching_options([record,group])
        #print(f"record for old method:{record}\t group:{group}")
        #print(f"returning from old method: {ans}")
        return ans
    else:
        if len(group) == 0:
            return 1
        record = record.split(".")
        r2 = record[-1]
        g2 = group[-1]
        r1 = record[:-1]
        new_g = group[:-1]
        new_r = ""
        for r in r1:
            new_r += (r + ".")
        new_r = new_r.strip(".")
        #print(f"new_r:{new_r}\t new_g:{new_g}\t r2:{r2}\t g2:{g2}")
        ans = evaluate2(new_r,tuple(new_g)) * evaluate2(r2,tuple([g2]))
        #print(f"returning: {ans}")
        return ans
@cache
def eval3(record,group):
    if len(record) == 0:
        if len(group) == 0:
            return 1
        else:
            return 0
    if len(group) == 0:
        if "#" in record:
            return 0
        else:
            return 1
    
    count = 0
    
    if record[0] in ".?":
        count += eval3(record[1:],group)
    if record[0] in "#?":
        if group[0] <= len(record) and ("." not in record[:group[0]]) and (group[0] == len(record) or record[group[0]] != "#"):
            count += eval3(record[group[0]+1:], group[1:])
    
    return count
    

total2 = 0

for c in conditions:
    #print(c)
    record,group = c
    #e2 = mo3(record,tuple(group))
    #print(f"e2:{e2}")
    #total2 += e2
    total2 += eval3(record,tuple(group))
print(f"Part 2 answer: {total2}")