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

directions = lines[0].strip()

nodes = {}
for line in lines[2:]:
    node = line.split("=")[0].strip()
    left,right = line.split("=")[1].replace("(","").replace(")","").split(",")
    right = right.strip()
    left = left.strip()
    n = {}
    nodes[node] = {'name':node, 'right':right, 'left':left}
    

current_node = "AAA"
#print(nodes)
step_count = 0

while not current_node == "ZZZ":
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



#put the code here

print(f"Part 1 answer: {step_count}")


print(f"Part 2 answer: {0}")