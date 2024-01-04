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
lines = f.read()

blocks = lines.split("\n\n")
blocks[0] = blocks[0].split("\n")
blocks[1] = blocks[1].split("\n")

wf = {}
parts = []

for line in blocks[0]:
    line = line.strip()
    name,process = line.split("{")
    process = process[:-1]
    subp = process.split(",")
    sps = []
    final_sp = subp.pop()
    for sp in subp:
        cond,dest = sp.split(":")
        sps.append((cond,dest))
    sps.append(final_sp)
    wf[name] = sps

for line in blocks[1]:
    line = line.strip()
    line = line.strip("{}")
    cats = line.split(",")
    part = {}
    for c in cats:
        name,val = c.split("=")
        part[name] = val
    parts.append(part)
"""
for w in wf:
    print(f"name:{w} wf:{wf[w]}")
print()
print()

for p in parts:
    print(p)
    print(f"part:{p}")
"""
#put the code here

accepted = []
rejected = []

for p in parts:
    part_done = False
    current_proc = wf['in']
    step_index = 0
    current_step = current_proc[step_index]
    while not part_done:
        if step_index == len(current_proc) - 1:
            if current_step == "A":
                accepted.append(p)
                part_done = True
            elif current_step == "R":
                rejected.append(p)
                part_done = True
            else:
                current_proc = wf[current_step]
                step_index = 0
                current_step = current_proc[step_index]
        else:            
            test = current_step[0]
            cat = test[0]
            catval = p[cat]
            test = test.replace(cat,catval)
            if eval(test):
                if current_step[1] == "A":
                    accepted.append(p)
                    part_done = True
                elif current_step[1] == "R":
                    rejected.append(p)
                    part_done = True
                else:
                    current_proc = wf[current_step[1]]
                    step_index = 0
                    current_step = current_proc[step_index]
            else:
                step_index += 1
                current_step = current_proc[step_index]

"""
print("accepted")
for a in accepted:
    print(a)

print()
print("rejected")
for r in rejected:
    print(r)
"""

total = 0

for a in accepted:
    total += int(a['x']) + int(a['m']) + int(a['a']) + int(a['s'])

print(f"Part 1 answer: {total}")

accepted_count = 0
rejected_count = 0

for x in range(4000):
    x = x+1
    for m in range(4000):
        m=m+1
        for a in range(4000):
            print("new A")
            a=a+1
            for s in range(4000):
                s=s+1
                p = {'x':str(x), 'm':str(m), 'a':str(a), 's':str(s)}
                part_done = False
                current_proc = wf['in']
                step_index = 0
                current_step = current_proc[step_index]
                while not part_done:
                    if step_index == len(current_proc) - 1:
                        if current_step == "A":
                            #accepted.append(p)
                            accepted_count +=1
                            part_done = True
                        elif current_step == "R":
                            #rejected.append(p)
                            rejected_count +=1
                            part_done = True
                        else:
                            current_proc = wf[current_step]
                            step_index = 0
                            current_step = current_proc[step_index]
                    else:            
                        test = current_step[0]
                        cat = test[0]
                        catval = p[cat]
                        test = test.replace(cat,catval)
                        if eval(test):
                            if current_step[1] == "A":
                                #accepted.append(p)
                                accepted_count +=1
                                part_done = True
                            elif current_step[1] == "R":
                                #rejected.append(p)
                                rejected_count +=1
                                part_done = True
                            else:
                                current_proc = wf[current_step[1]]
                                step_index = 0
                                current_step = current_proc[step_index]
                        else:
                            step_index += 1
                            current_step = current_proc[step_index]

print(f"Part 2 answer: {accepted_count}")