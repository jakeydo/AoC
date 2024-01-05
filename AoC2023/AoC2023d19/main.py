import sys
import random
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

accepted_nodes = []
rejected_nodes = []
#root = {'parent':False,'name':"s<1351", 'if_true':'px', 'if_false':'qqz'}
#root = {'parent':False}
#root['name'] = wf['in'][0]

def single_overlap(x1, x2, y1, y2):
    return y1 <= x1 <= y2 or y1 <= x2 <= y2

def overlaps(t1,t2):
    t1x0,t1x1,t1m0,t1m1,t1a0,t1a1,t1s0,t1s1 = t1
    t2x0,t2x1,t2m0,t2m1,t2a0,t2a1,t2s0,t2s1 = t2
    
    x_overlap = single_overlap(t1x0,t1x1,t2x0,t2x1)
    m_overlap = single_overlap(t1m0,t1m1,t2m0,t2m1)
    a_overlap = single_overlap(t1a0,t1a1,t2a0,t2a1)
    s_overlap = single_overlap(t1s0,t1s1,t2s0,t2s1)
    
    return x_overlap and m_overlap and a_overlap and s_overlap
    
    

def subtree(wf,cp,cs,parent,accepted_nodes,rejected_nodes):
    node = {'parent':parent}
    current_proc = wf[cp]
    current_step = current_proc[cs]
    
    if cs == len(current_proc) - 1:
        if current_step == "A":
            node['name'] = "A"
            node['if_true'] = False
            node['if_false'] = False
            node['hash'] = random.randint(0,1000000)
            accepted_nodes.append(node)
            return node
        elif current_step == "R":
            node['name'] = "R"
            node['if_true'] = False
            node['if_false'] = False
            node['hash'] = random.randint(0,1000000)
            rejected_nodes.append(node)
            return node
        else:
            next_proc = current_step#wf[current_step]
            next_step = 0
            return subtree(wf,next_proc,next_step,parent,accepted_nodes,rejected_nodes)
    else:
        node['name'] = current_step[0]
        if current_step[1] == "A":
            h = random.randint(1,1000000)
            child = {'parent':node, 'name':'A', 'if_true':False, 'if_false':False, 'hash':h}
            accepted_nodes.append(child)
            node['if_true'] = child
            child = subtree(wf,cp,cs+1,node,accepted_nodes,rejected_nodes)
            node['if_false'] = child
            return node
        if current_step[1] == "R":
            h = random.randint(1,1000000)
            child = {'parent':node, 'name':'R', 'if_true':False, 'if_false':False, 'hash':h}
            rejected_nodes.append(child)
            node['if_true'] = child
            child = subtree(wf,cp,cs+1,node,accepted_nodes,rejected_nodes)
            node['if_false'] = child
            return node
        else:
            child = subtree(wf,current_step[1],0,node,accepted_nodes,rejected_nodes)
            node['if_true'] = child
            child = subtree(wf,cp,cs+1,node,accepted_nodes,rejected_nodes)
            node['if_false'] = child
            return node
        
    
root = subtree(wf,'in',0,False,accepted_nodes,rejected_nodes)

rules = []

for a in accepted_nodes:
    string = ""
    node = a
    last_node = False
    #print()
    #print("@@@")
    #print()
    while not node == False:
        #if node['name'] == "A" or node['name'] == "R" or node['if_true'] == last_node:            
        #print(node['name'])
        if node['if_true'] == last_node:            
            string += " -> " + node['name']
        else:
            string += " -> " + "not " + node['name']
        #string += node['name']
        last_node = node
        node = node['parent']
    rules.append(string)

sorted_rules = []

for r in rules:
    #print(r)
    r = r[9:]
    br = r.split(" -> ")
    x_rules = []
    m_rules = []
    a_rules = []
    s_rules = []
    
    for b in br:
        if "not" in b:
            b = b[4:]
            b = b.replace("<",".")
            b = b.replace(">","<=")
            b = b.replace(".",">=")
    
        if 'x' in b:
            x_rules.append(b)
        elif 'm' in b:
            m_rules.append(b)
        elif 'a' in b:
            a_rules.append(b)
        else:
            s_rules.append(b)
    
    sorted_rules.append({'x_rules':x_rules, 'm_rules':m_rules, 'a_rules':a_rules, 's_rules':s_rules})


range_rules = []

for r in sorted_rules:
    mins = {'x':1,'m':1,'a':1,'s':1}
    maxs = {'x':4000,'m':4000,'a':4000,'s':4000}
    sub_rules = ['x','m','a','s']
    for sr in sub_rules:
        sr = sr + "_rules"
        srs = r[sr]
        for s in srs:
            #print(s)
            if "<" in s:
                if not "=" in s:
                    new_max = int(s[2:])
                    new_max -= 1
                else:
                    new_max = int(s[3:])
                #print("found <")
                #print(new_max)
                #print(s[0])
                maxs[s[0]] = min(new_max,maxs[s[0]])
            else:
                #print("found >?")
                if not "=" in s:
                    new_min = int(s[2:])
                    new_min += 1
                else:
                    new_min = int(s[3:])
                mins[s[0]] = max(new_min,mins[s[0]])
    #print(mins)
    #print(maxs)
    if mins['x'] <= maxs['x'] and mins['m'] <= maxs['m'] and mins['a'] <= maxs['a'] and mins['s'] <= maxs['s']:
        rule = {'xmin':mins['x'], 'xmax':maxs['x'], 'mmin':mins['m'], 'mmax':maxs['m'], 'amin':mins['a'], 'amax':maxs['a'], 'smin':mins['s'], 'smax':maxs['s']}
        range_rules.append(rule)

rr_tuples = []

for rr in range_rules:
    #print(rr)
    #print(f"{rr['xmin']},{rr['xmax']},,{rr['mmin']},{rr['mmax']},,{rr['amin']},{rr['amax']},,{rr['smin']},{rr['smax']}")
    rr_tuples.append((rr['xmin'],rr['xmax'],rr['mmin'],rr['mmax'],rr['amin'],rr['amax'],rr['smin'],rr['smax']))

rr_tuples.sort()

total2 = 0

for rt in rr_tuples:
    #print(rt)
    xr = len(range(rt[0],rt[1]+1))
    mr = len(range(rt[2],rt[3]+1))
    ar = len(range(rt[4],rt[5]+1))
    sr = len(range(rt[6],rt[7]+1))
    total2 += xr*mr*ar*sr

"""      
print(f"number of rules: {len(accepted_nodes)}")
print(f"number of actual rules: {len(range_rules)}")

print()
print()
"""
"""
for i in range(len(rr_tuples)):
    for j in range(i+1,len(rr_tuples)):
        x = rr_tuples[i]
        y = rr_tuples[j]
        if overlaps(x,y):
            print("These two overlap!!!")
            print(x)
            print(y)
            print()

"""
"""
def eval_part(sr,x,m,a,s):
    accepted = True
    #print((x,m,a,s))
    while accepted:
        for r in sr:
            #print(r)
            for xr in r['x_rules']:
                xr.replace('x',str(x))
                #print(xr)
                accepted = eval(xr)
                if not accepted:
                    #print("x no good")
                    break
            if not accepted:
                break
            for mr in r['m_rules']:
                mr.replace('m',str(m))
                accepted = eval(mr)
                if not accepted:
                    #print("m no good")
                    break
            if not accepted:
                break
            for ar in r['a_rules']:
                ar.replace('a',str(a))
                accepted = eval(ar)
                if not accepted:
                    #print("a no good")
                    break
            if not accepted:
                break
            for sr in r['s_rules']:
                sr.replace('s',str(s))
                accepted = eval(sr)
                if not accepted:
                    #print("s no good")
                    break
            if accepted:
                return accepted
    return accepted


for x in range(4000):
    x = x+1
    for m in range(4000):
        m = m+1
        for a in range(4000):
            a = a+1
            print(accepted_count)
            for s in range(4000):
                s = s+1
                if eval_part(sorted_rules,x,m,a,s):
                    accepted_count += 1
                
"""

print(f"Part 2 answer: {total2}")