import sys
from math import lcm
#from collections import defaultdict
#from os import system
#import time
#from functools import cache
#sys.setrecursionlimit(10**7)
args = str(sys.argv)
if ("test" in args):
    f = open("test2.txt")
else:
    f = open("real.txt")
lines = f.readlines()

directions = lines[0].strip()

nodes = {}
for line in lines[2:]:
    node = line.split("=")[0].strip()
    left,right = line.split("=")[1].replace("(","").replace(")","").split(",")
    right = right.strip()
    left = left.strip()
    n = {}
    nodes[node] = {'name':node, 'right':right, 'left':left}
    
temp_starting_nodes = [nodes[node] for node in nodes if "A" in node]
starting_nodes = {}
for node in temp_starting_nodes:
    starting_nodes[node['name']] = node

current_nodes = [n for n in starting_nodes]

print(current_nodes)

cycle_lengths = []

#print(nodes)
step_count = 0

for current_node in current_nodes:
    while not "Z" in current_node:
        #print(current_node)
        next_i = step_count % len(directions)
        next_step = directions[next_i]
        next_node = ""
        
        if next_step == "R":
            next_node = nodes[current_node]['right']
        else:
            next_node = nodes[current_node]['left']
        current_node = next_node
        
        step_count += 1
    cycle_lengths.append(step_count)
    step_count = 0
    
print(cycle_lengths)
answer = lcm(*cycle_lengths)



#put the code here

print(f"Part 2 answer: {answer}")