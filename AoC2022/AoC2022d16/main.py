from collections import defaultdict
from functools import lru_cache
from copy import deepcopy
simulation_time = 30
f = open("real.txt")
lines = f.readlines()

class Valve():
  name = "AA"
  rate = 0
  neighbors = set()

  def __init__(self, name, rate, neighbors):
    self.name = name
    self.rate = rate
    self.neighbors = neighbors

  def __str__(self):
    a = "name is: " + self.name + "\n"
    b = "rate is: " + str(self.rate) + "\n"
    c = "neighbors are: " + str(self.neighbors) + "\n"
    return a+b+c

valves = []

for line in lines:
  a,b = line.strip().split("; ")
  name,rate = a.split("=")
  rate = int(rate)
  name = name.split()[1]

  neighbors = b.split(",")
  for i in range(len(neighbors)):
    neighbors[i] = neighbors[i][-2:]

  v = Valve(name,rate,neighbors)
  valves.append(v)

def valve_by_name(name,valves):
  v = next(filter(lambda x: x.name == name,valves))
  return v

def total_flow(name, valves, on_time, simulation_time):
  run_time = simulation_time - on_time;
  v = valve_by_name(name,valves)
  rate = run_time * v.rate
  return rate

@lru_cache(maxsize=None)
def distance(v1,v2,valves):
  valves = list(valves)
  v1 = valve_by_name(v1,valves)
  v2 = valve_by_name(v2, valves)
  if v1 == v2:
    return 0  
  distance_to_here = defaultdict(lambda: 10000)
  distance_to_here[v1.name] = 0
  #distance_to_here[v2.name] = 1
  visited = set()
  to_visit = [v1.name]
  while len(to_visit) > 0:
    v = to_visit.pop()
    #print("popping: " + v)
    if not v in visited:
      #print("visiting: " + v)
      visited.add(v)
      v = valve_by_name(v,valves)
      for n in v.neighbors:
        #print(n)
        n = valve_by_name(n,valves)
        new_dist = min(distance_to_here[n.name], distance_to_here[v.name]+1)
        #print(n.name +" " + str(new_dist))
        #print(n.name + " " + str(distance_to_here[n.name]))
        distance_to_here[n.name] = new_dist
        #print(n.name + " " + str(distance_to_here[n.name]))
        to_visit.append(n.name)
  return distance_to_here[v2.name]

def candidate_paths(so_far,remaining_valves,valves):
  if len(remaining_valves) == 0:
    return []
  if len(remaining_valves) == 1:
    so_far.append(remaining_valves[0])
    #print(so_far)
    return [so_far]

  paths = []
  t_v = tuple(valves)
  paths.append(so_far)
  for i in range(len(remaining_valves)):
    m = remaining_valves[i]
    new_remaining_valves = remaining_valves[:i] + remaining_valves[i+1:]
    new_so_far = so_far + [m]
    #paths.append(so_far)
    new_distance = path_distance(new_so_far,valves)
    #for i in range(1,len(new_so_far)):
    #  new_distance += distance(new_so_far[i-1],new_so_far[i],t_v)
    
    if new_distance <30:    
      c_paths = candidate_paths(new_so_far,new_remaining_valves,valves)
      for c in c_paths:
        paths.append(c)
    else:
      pass
      #paths.append(so_far)
      #paths.append(new_so_far)
  return paths

def path_distance(path,valves):
  total_distance = 0
  t_v = tuple(valves)
  for i in range(len(path)):
    total_distance += distance(path[i-1],path[i],t_v)
  return total_distance

def possible_paths(valves):
  #THIS NEEDS TO BE FIXED!!!
  path_time = 0
  if len(valves) == 0:
    return []

  if len(valves) == 1:
    return [valves]

  path = []

  for i in range(len(valves)):
    m = valves[i]
    remValves = valves[:i] + valves[i+1:]
    for p in possible_paths(remValves):
      path.append([m]+p)
      total_dist = 0
      for i in range(1, len(path)):
        total_dist += distance(path[i-1],path[i],valves)
      if total_dist <30:
        return path
      else:
        return []
  return path

def total_flow_for_path(path,valves,simulation_time):
  path.reverse()
  current_node = "EF"
  current_time = 0
  cumulative_flow = 0

  while len(path)>0:
    #print(current_node)
    next_node = path.pop()
    time_to_next_node = distance(current_node,next_node,tuple(valves))
    current_time += time_to_next_node
    cumulative_flow += total_flow(next_node,valves, current_time,simulation_time)
    current_time +=1
    current_node = next_node

  return cumulative_flow


def uniq(lst):
    last = object()
    for item in lst:
        if item == last:
            continue
        yield item
        last = item

def sort_and_deduplicate(l):
    return list(uniq(sorted(l, reverse=True)))
  
#print(valve_by_name("AA",valves))
#print(distance("AA","GG",tuple(valves)))

positive_flow_valves = set(filter(lambda x: x.rate>0, valves))
#valves_to_turn_on = set(filter(lambda x: x.rate>0, valves))
valves_to_turn_on = set(map(lambda x: x.name,positive_flow_valves))
valve_names = set(map(lambda x: x.name,valves))

#print(possible_paths(list(valves_to_turn_on)))

#path = ["AA","DD","BB","JJ","HH","EE","CC"]

#c_flow = total_flow_for_path(path,valves,simulation_time)

#print("c flow is: " + str(c_flow))

#candidates = candidate_paths(["AA"], list(valves_to_turn_on),valves)
candidates = candidate_paths(["AA"], list(valve_names) ,valves)
candidates = sort_and_deduplicate(candidates)
#candidates.remove([])
x = ["BB","CC","DD"]
#candidates = candidate_paths(["AA"], x)

#for c in candidates:
  #print(c)
print(len(candidates))

#print(candidates[200000])

max_flow = 0
for c in candidates:
  #print(c)
  d = deepcopy(c)
  old_max = max_flow
  max_flow = max(max_flow,total_flow_for_path(c,valves,simulation_time))
  if old_max != max_flow:
    print(d)
    print(max_flow)

print("part 1 answer: " + str(max_flow))

"""
current_location = "AA"
current_time = 1
all_time_flow = 0
somewhere_to_go = True

while len(valves_to_turn_on) > 0 and current_time < 31 and somewhere_to_go:
  print(current_location)
  max_additional_flow = 0
  delta_time = 0
  next_valve = ""
  somewhere_to_go = False
  for v in valves_to_turn_on:
    d = distance(current_location,v,tuple(valves))
    if current_time+d+1 < 31:
      v = valve_by_name(v,valves)
      potential_on_time = simulation_time - current_time - d
      potential_total_flow = potential_on_time * v.rate
      if potential_total_flow > max_additional_flow:
        max_additional_flow = potential_total_flow
        next_valve = v.name
        delta_time = d + 1
        somewhere_to_go = True
  valves_to_turn_on.remove(next_valve)
  current_time += delta_time
  all_time_flow += max_additional_flow
  current_time += delta_time
  current_location = next_valve

print(all_time_flow)
"""