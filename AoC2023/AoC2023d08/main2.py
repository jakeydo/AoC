import sys
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
#print(nodes)
step_count = 0

all_z = False

print(current_nodes)
input()

while not all_z:
    #print(current_node)
    #input()
    next_i = step_count % len(directions)
    next_step = directions[next_i]
    #all_z = True
    #print(current_nodes)
    #print(next_step)
    
    for index,current_node in enumerate(current_nodes):
        #current_node = nodes[current_node]
        next_node = ""
        if next_step == "R":
            next_node = nodes[current_node]['right']
        else:
            next_node = nodes[current_node]['left']
        current_nodes[index] = next_node
        #print(f"cn:{current_node} nn:{next_node} ns:{next_step} index:{index}")
        if not "Z" in next_node:
            all_z = False
    
    step_count += 1



#put the code here

print(f"Part 2 answer: {step_count}")