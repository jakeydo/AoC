from functools import cache

simulation_time = 30
test = False
if test:
    f = open("test.txt")
else:
    f = open("real.txt")

lines = f.readlines()

flows = {}
neighbors = {}

for line in lines:
    a,b = line.strip().split("; ")
    name,rate = a.split("=")
    rate = int(rate)
    name = name.split()[1]
    n = b.split(",")
    
    for i in range(len(n)):
        n[i] = n[i][-2:]
    
    flows[name] = rate
    neighbors[name] = n

@cache
def solve(position,time,opened,ele_waiting=False):
    if time == 0:
        if ele_waiting:
            return solve("AA",26,opened)
        return 0
    
    #print(neighbors[position])
    score = max(solve(n,time-1,opened,ele_waiting) for n in neighbors[position])
    
    #this_flow = 0
    
    if flows[position] > 0 and position not in opened:
        new_opened = set(opened)
        new_opened.add(position)
        new_opened = frozenset(new_opened)
        this_flow = flows[position] * (time - 1)
        score = max(score, this_flow + solve(position,time-1,new_opened,ele_waiting))
    
    return score 
        

part1 = solve("AA",30,frozenset())
print(f"Part 1: {part1}")
    
part2 = solve("AA",26,frozenset(),True)
print(f"Part 2: {part2}")