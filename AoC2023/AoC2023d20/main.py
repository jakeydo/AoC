import sys
from heapq import heappush,heappop
from collections import defaultdict
#from os import system
#import time
from time import time, sleep
from math import prod,lcm
#from functools import cache
#sys.setrecursionlimit(10**7)
args = str(sys.argv)
if ("test" in args):
    f = open("test.txt")
else:
    f = open("real.txt")
lines = f.readlines()



class Flipflop:
    #name = ""
    #inputs = []
    #outputs = []
    #state = False
    def __init__(self,name):
        self.name = name
        self.inputs = []
        self.outputs = []
        self.state = False
        
    def __str__(self):
        ins = ""
        for i in self.inputs:
            ins += i + " "
        outs = ""
        for o in self.outputs:
            outs += o + " "
        return f"FF {self.name} || inputs: {ins} || outputs: {outs}"

    def get_outputs(self):
        return self.outputs
    
    def get_inputs(self):
        return self.inputs
    
    def peek(self):
        if self.state:
            return "1"
        else:
            return "0"
    
    def add_input(self,ni):
        self.inputs.append(ni)
        
    def add_output(self,no):
        self.outputs.append(no)
        
    def proc_msg(self,msg):
        _,_,sender,pulse = msg
        if pulse == True:
            return []
        else:
            sleep(1/10000000000)
            t = time()
            self.state = not self.state
            msgs = []
            for o in self.outputs:
                m = (t,o,self.name,self.state)
                msgs.append(m)
            return msgs

class Conjunction:
    #name = ""
    #inputs = {}
    #outputs = []
    
    def __init__(self,name):
        self.name = name
        self.inputs = {}
        self.outputs = []
        self.state = True
        
    def __str__(self):
        ins = ""
        for i in self.inputs:
            ins += i + " "
        outs = ""
        for o in self.outputs:
            outs += o + " "
        return f"CONJ {self.name} || inputs: {ins} || outputs: {outs}"
    
    def get_outputs(self):
        return self.outputs
    
    def get_inputs(self):
        return self.inputs
    
    def peek(self):
        if self.state:
            return "1"
        else:
            return "0"
    
    def add_input(self,ni):
        self.inputs[ni] = False
        
    def add_output(self,no):
        self.outputs.append(no)
        
    def proc_msg(self,msg):
        sleep(1/10000000000)
        t = time()
        _,_,sender,pulse = msg
        self.inputs[sender] = pulse
        #print()
        #print("processing conj")
        #print(msg)
        #print()
        acc = False
        for i in self.inputs:
            #print(f"input:{i} state:{self.inputs[i]}")
            if not self.inputs[i]:
                acc = True
                break
        self.state = acc
        msgs = []
        for o in self.outputs:
            m = (t,o,self.name,acc)
            msgs.append(m)
        #print(f"returning: {msgs}")
        return msgs

parts = defaultdict(lambda:Flipflop('crap'))

for line in lines:
    p,o = line.strip().split(" -> ")
    pn = p[1:]
    if "%" in p:
        part = Flipflop(pn)
        parts[pn] = part
    elif "&" in p:
        part = Conjunction(pn)
        parts[pn] = part
    else:
        #da broadcaster
        b = {'name':'broadcaster','outputs':[]}
        parts['broadcaster'] = b

for line in lines:
    p,o = line.strip().split(" -> ")
    pn = p[1:]
    ops = o.split(",")
    if p == "broadcaster":
        b = parts['broadcaster']
        for op in ops:
            op = op.strip()
            b['outputs'].append(op)
            parts[op].add_input("broadcaster")
    else:
        this_part = parts[pn]
        for op in ops:
            op = op.strip()
            this_part.add_output(op)
            parts[op].add_input(pn)    
        #print(this_part)
        #print()
        #print("***")
    

mq = []
pq = []
low_count = 0
hi_count = 0
button_count = 0

out_part = ""

for p in parts:
    #print(parts[p])
    if not isinstance(parts[p],dict) and 'rx' in parts[p].get_outputs():
        out_part = p
        
outpart_inputs = parts[out_part].get_inputs()

periods = {}
for i in outpart_inputs:
    periods[i] = 0

for i in range(1000):
    button_count += 1
    low_count += 1 #accounting for button press
    b = parts['broadcaster']
    for o in b['outputs']:
        t = time()
        m = (t,o,'broadcaster',False)
        heappush(mq,m)
    
    #for m in mq:
    #    print(m)
    
    while(mq):
        m = heappop(mq)
        pq.append(m)
        #print(f"processing: {m}")
        _,r,s,pulse = m
        if pulse and (s in outpart_inputs):
            #print(f"bc:{button_count}  vg:{parts['vg'].peek()}  kp:{parts['kp'].peek()}  gc:{parts['gc'].peek()}  tx:{parts['tx'].peek()}")
            if periods[s] == 0:
                periods[s] = button_count
        if r == "rx" and not pulse:
            rx_bc = button_count
        if pulse:
            hi_count += 1
        else:
            low_count += 1
        part = parts[r]
        new_msgs = part.proc_msg(m)
        #print("new messages out:")
        #for nm in new_msgs:
        #    print(nm)
        for nm in new_msgs:
            heappush(mq,nm)
        
#put the code here
print(f"lows: {low_count} highs: {hi_count}")
total = low_count * hi_count
print(f"Part 1 answer: {total}")

pp = 0

while pp == 0:
    button_count += 1
    low_count += 1 #accounting for button press
    b = parts['broadcaster']
    for o in b['outputs']:
        t = time()
        m = (t,o,'broadcaster',False)
        heappush(mq,m)
    
    #for m in mq:
    #    print(m)
    
    while(mq):
        m = heappop(mq)
        pq.append(m)
        #print(f"processing: {m}")
        _,r,s,pulse = m
        if pulse and (s in outpart_inputs):
            #print(f"bc:{button_count}  vg:{parts['vg'].peek()}  kp:{parts['kp'].peek()}  gc:{parts['gc'].peek()}  tx:{parts['tx'].peek()}")
            if periods[s] == 0:
                periods[s] = button_count
        if r == "rx" and not pulse:
            rx_bc = button_count
        if pulse:
            hi_count += 1
        else:
            low_count += 1
        part = parts[r]
        new_msgs = part.proc_msg(m)
        #print("new messages out:")
        #for nm in new_msgs:
        #    print(nm)
        for nm in new_msgs:
            heappush(mq,nm)

    ipvals = periods.values()
    #print(ipvals)
    pp = prod(ipvals)

total2 = lcm(*ipvals)

print(f"Part 2 answer: {total2}")