#from collections import defaultdict
#from os import system
from functools import cache
import sys
import time
sys.setrecursionlimit(10**7)

test = False
if test:
    f = open("test.txt")
else:
    f = open("real.txt")

class Blueprint():
    ore_robot_ore_cost = 0
    clay_robot_ore_cost = 0
    obsidian_robot_ore_cost = 0
    obsidian_robot_clay_cost = 0
    geode_robot_ore_cost = 0
    geode_robot_obsidian_cost = 0
    
    max_ore_needed = 0
    max_clay_cost = 0
    max_obsidian_cost = 0

    def __init__(self, ore_robot_ore_cost,clay_robot_ore_cost,obsidian_robot_ore_cost,obsidian_robot_clay_cost,geode_robot_ore_cost,geode_robot_obsidian_cost):
        self.ore_robot_ore_cost = ore_robot_ore_cost
        self.clay_robot_ore_cost = clay_robot_ore_cost
        self.obsidian_robot_ore_cost = obsidian_robot_ore_cost
        self.obsidian_robot_clay_cost = obsidian_robot_clay_cost
        self.geode_robot_ore_cost = geode_robot_ore_cost
        self.geode_robot_obsidian_cost = geode_robot_obsidian_cost
        
        self.max_ore_needed = max(ore_robot_ore_cost, clay_robot_ore_cost, obsidian_robot_ore_cost, geode_robot_ore_cost)
        self.max_clay_needed = obsidian_robot_clay_cost
        self.max_obsidian_needed = geode_robot_obsidian_cost

    def __str__(self):
        s = f"Ore Robot Ore Cost = {self.ore_robot_ore_cost}, Clay Robot Ore Cose = {self.clay_robot_ore_cost}, Obsidian Robot Ore Cost = {self.obsidian_robot_ore_cost}, Obsidian Robot Clay Cost = {self.obsidian_robot_clay_cost}, Geode Robot Ore Cost = {self.geode_robot_ore_cost}, Geode Robot Obsidian Cost = {self.geode_robot_obsidian_cost}"
        return s


blueprints = []
lines = f.readlines()

for line in lines:
    sentences = line.split(".")
    ore_robot_ore_cost = int(sentences[0].split(" ")[-2])
    clay_robot_ore_cost = int(sentences[1].split(" ")[-2])
    obsidian_robot_ore_cost = int(sentences[2].split(" ")[-5])
    obsidian_robot_clay_cost = int(sentences[2].split(" ")[-2])
    geode_robot_ore_cost = int(sentences[3].split(" ")[-5])
    geode_robot_obsidian_cost = int(sentences[3].split(" ")[-2])
    bp = Blueprint(ore_robot_ore_cost,clay_robot_ore_cost,obsidian_robot_ore_cost,obsidian_robot_clay_cost,geode_robot_ore_cost,geode_robot_obsidian_cost)
    #print(bp)
    blueprints.append(bp)

number_ore_robots = 1
number_clay_robots = 0
number_obsidian_robots = 0
number_geode_robots = 0
ore = 0
clay = 0
obsidian = 0
geodes = 0

triangle = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528]

@cache
def max_geodes_possible(bp,time,ore_robots,clay_robots,obsidian_robots,geode_robots,ore,clay,obsidian,geodes):
    #print(f"time: {time}, orebots: {ore_robots}, claybots: {clay_robots}, obsbots: {obsidian_robots}, gbots: {geode_robots}")

    if time == 0:
        return geodes
        
    if time == 1:
        return geodes + geode_robots

    new_time = time-1
    
    new_ore = ore + ore_robots
    new_ore = min(new_ore, 3*bp.max_ore_needed)
    
    new_clay = clay + clay_robots
    new_clay = min(new_clay, 3*bp.max_clay_needed)
    
    new_obsidian = obsidian + obsidian_robots
    new_obsidian = min(new_obsidian, 3*bp.max_obsidian_needed)
    
    new_geodes = geodes + geode_robots
    """
    max_possible_geodes = geodes + (new_time * geode_robots) + triangle[new_time]

    #max_ore_needed = max(bp.ore_robot_ore_cost,bp.clay_robot_ore_cost,bp.obsidian_robot_ore_cost,bp.geode_robot_ore_cost)
    """ 
    max_geodes = max_geodes_possible(bp,new_time,ore_robots,clay_robots,obsidian_robots,geode_robots,new_ore,new_clay,new_obsidian,new_geodes)
    #if max_possible_geodes <= max_geodes:
    #    return max_geodes
   
    if ore_robots < bp.max_ore_needed and ore >= bp.ore_robot_ore_cost:
        #max_geodes = max(max_geodes,max_geodes_possible(bp,new_time,ore_robots,clay_robots,obsidian_robots,geode_robots,new_ore,new_clay,new_obsidian,new_geodes))
        this_ore = new_ore - bp.ore_robot_ore_cost
        max_geodes = max(max_geodes,max_geodes_possible(bp,new_time,ore_robots+1,clay_robots,obsidian_robots,geode_robots,this_ore,new_clay,new_obsidian,new_geodes))
        

    if clay_robots < bp.max_clay_needed and ore >= bp.clay_robot_ore_cost:
        #max_geodes = max(max_geodes,max_geodes_possible(bp,new_time,ore_robots,clay_robots,obsidian_robots,geode_robots,new_ore,new_clay,new_obsidian,new_geodes))
        this_ore = new_ore - bp.clay_robot_ore_cost
        max_geodes = max(max_geodes,max_geodes_possible(bp,new_time,ore_robots,clay_robots+1,obsidian_robots,geode_robots,this_ore,new_clay,new_obsidian,new_geodes))
    
    if obsidian_robots < bp.max_obsidian_needed and (ore >= bp.obsidian_robot_ore_cost and clay >= bp.obsidian_robot_clay_cost):
        #max_geodes = max(max_geodes,max_geodes_possible(bp,new_time,ore_robots,clay_robots,obsidian_robots,geode_robots,new_ore,new_clay,new_obsidian,new_geodes))
        this_ore = new_ore - bp.obsidian_robot_ore_cost
        this_clay = new_clay - bp.obsidian_robot_clay_cost
        max_geodes = max(max_geodes,max_geodes_possible(bp,new_time,ore_robots,clay_robots,obsidian_robots+1,geode_robots,this_ore,this_clay,new_obsidian,new_geodes))

    if ore >= bp.geode_robot_ore_cost and obsidian >= bp.geode_robot_obsidian_cost:
        #max_geodes = max(max_geodes,max_geodes_possible(bp,new_time,ore_robots,clay_robots,obsidian_robots,geode_robots,new_ore,new_clay,new_obsidian,new_geodes))
        this_ore = new_ore - bp.geode_robot_ore_cost
        this_obsidian = new_obsidian - bp.geode_robot_obsidian_cost
        max_geodes = max(max_geodes,max_geodes_possible(bp,new_time,ore_robots,clay_robots,obsidian_robots,geode_robots+1,this_ore,new_clay,this_obsidian,new_geodes))
    
    return max_geodes

bp = blueprints[1]
#mg = max_geodes_possible(bp,24,1,0,0,0,0,0,0,0)
#print(f"Max geodes for this blueprint is: {mg}")

sum_ql = 0
bp_id = 1

max_geodes = [1,1,1]
for i in range(3):
    if i > len(blueprints)-1:
        break
    bp = blueprints[i]
    start = time.time()
    mg = max_geodes_possible(bp,32,1,0,0,0,0,0,0,0)
    end = time.time()
    max_geodes[i] = mg
    print(f"Max geodes for this blueprint is: {mg}")
    print(f"elapsed time: {end-start}")
print(f"Product of max geodes is: {max_geodes[0]*max_geodes[1]*max_geodes[2]}")

"""
for bp in blueprints:
    start = time.time()
    mg = max_geodes_possible(bp,24,1,0,0,0,0,0,0,0)
    end = time.time()
    ql = bp_id * mg
    sum_ql = sum_ql + ql
    bp_id += 1
    print(f"Max geodes for this blueprint is: {mg}")
    print(f"Quality level for this blueprint is: {ql}")
    print(f"elapsed time: {end-start}")

print(f"Sum of Quality Levels is: {sum_ql}")
"""