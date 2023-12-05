import sys
#from collections import defaultdict
#from os import system
#import time
#from functools import cache
#sys.setrecursionlimit(10**7)
args = str(sys.argv)
if ("test" in args):
    test = True
else:
    test = False
if test:
    f = open("test.txt")
else:
    f = open("real.txt")
lines = f.readlines()

current_mapping = ""
current_map = []
maps = {}
seed_line = ""
for line in lines:
    if line == "\n":
        if not current_mapping == "":
            maps[current_mapping] = current_map
            current_map = []
    elif "seeds" in line.strip():
        seed_line = line.strip()
        seeds = lines[0].split(":")[1].split()
    elif "map" in line.strip():
        current_mapping = line.split(" ")[0]
    else:
        e = {}
        
        d,s,r = line.strip().split()
        e['d_start'], e['s_start'], e['r'] = int(d),int(s),int(r)
        current_map.append(e)
maps[current_mapping] = current_map        

for i in range(len(seeds)):
    seeds[i] = int(seeds[i])
"""
for m in maps:
    print("*****")
    print(m)
    print(maps[m])
    print()
"""

for seed in seeds:
    print(seed)
    

#def convert(d_start,s_start,r,value):
def convert(e,value):
    d_start = e['d_start']
    s_start = e['s_start']
    r = e['r']
    mapped_range = range(s_start,s_start+r)
    #print(f"value:{value} ds:{d_start} ss{s_start} r:{r}")
    if not value in mapped_range:
        return value
    else:
        delta = value-s_start
        return d_start + delta

def convert_backwards(e,value):
    d_start = e['d_start']
    s_start = e['s_start']
    r = e['r']
    delta = value-d_start
    return s_start + delta
    
def convert_from_map_backwards(entries,value):
    for e in entries:
        mr = range(e['d_start'],e['d_start']+e['r'])
        if value in mr:
            return convert_backwards(e, value)
    return value

def convert_from_map(entries,value):
    for e in entries:        
        mr = range(e['s_start'], e['s_start'] + e['r'])
        """
        print()
        print("#####")
        print(mr)
        print(value)
        """
        if value in mr:
            #print(f"found value: {value}!")
            return convert(e, value)
    return value

def seed_to_location(seed,maps):
    soil = convert_from_map(maps['seed-to-soil'],seed)
    fert = convert_from_map(maps['soil-to-fertilizer'],soil)
    water = convert_from_map(maps['fertilizer-to-water'],fert)
    light = convert_from_map(maps['water-to-light'],water)
    temp = convert_from_map(maps['light-to-temperature'],light)
    hum = convert_from_map(maps['temperature-to-humidity'],temp)
    loc = convert_from_map(maps['humidity-to-location'],hum)
    return loc
    
def location_to_seed(loc,maps):
    hum = convert_from_map_backwards(maps['humidity-to-location'],loc)
    temp = convert_from_map_backwards(maps['temperature-to-humidity'],hum)
    light = convert_from_map_backwards(maps['light-to-temperature'],temp)
    water = convert_from_map_backwards(maps['water-to-light'],light)
    fert = convert_from_map_backwards(maps['fertilizer-to-water'],water)
    soil = convert_from_map_backwards(maps['soil-to-fertilizer'],fert)
    seed = convert_from_map_backwards(maps['seed-to-soil'],soil)
    return seed

#put the code here
"""
print("!!!!!")
print(maps['seed-to-soil'])
print()
"""

locations = set()
for seed in seeds:
    soil = convert_from_map(maps['seed-to-soil'],seed)
    fert = convert_from_map(maps['soil-to-fertilizer'],soil)
    water = convert_from_map(maps['fertilizer-to-water'],fert)
    light = convert_from_map(maps['water-to-light'],water)
    temp = convert_from_map(maps['light-to-temperature'],light)
    hum = convert_from_map(maps['temperature-to-humidity'],temp)
    loc = convert_from_map(maps['humidity-to-location'],hum)
    print(f"{seed} {soil} {fert} {water} {light} {temp} {hum} {loc}")
    locations.add(loc)


print(f"Part 1 answer: {min(locations)}")

print(convert_from_map_backwards(maps['humidity-to-location'],61))

seed_ranges = set()
for i in range(len(seeds)):
    if i%2==0:
        r = range(seeds[i],seeds[i]+seeds[i+1])
        seed_ranges.add(r)

def isinseedranges(seed, seed_ranges):
    for sr in seed_ranges:
        if seed in sr:
            return True
    return False

loc = 0
keep_going = True
while keep_going:
    hum = convert_from_map_backwards(maps['humidity-to-location'],loc)
    temp = convert_from_map_backwards(maps['temperature-to-humidity'],hum)
    light = convert_from_map_backwards(maps['light-to-temperature'],temp)
    water = convert_from_map_backwards(maps['water-to-light'],light)
    fert = convert_from_map_backwards(maps['fertilizer-to-water'],water)
    soil = convert_from_map_backwards(maps['soil-to-fertilizer'],fert)
    seed = convert_from_map_backwards(maps['seed-to-soil'],soil)
    #print(f"loc: {loc} seed: {seed}")
    if isinseedranges(seed,seed_ranges):
        keep_going = False
    else:
        loc +=1

print(f"Part 2 answer: {loc}")

quit()
print("@@@@@")

seed_ranges = []
for i in range(len(seeds)):
    if i%2==0:
        r = range(seeds[i],seeds[i]+seeds[i+1])
        seed_ranges.append(r)
       
min_location = 1000000000000000
i = 1
for r in seed_ranges:
    print(f"new range {i}")
    i += 1
    for seed in r:
        soil = convert_from_map(maps['seed-to-soil'],seed)
        fert = convert_from_map(maps['soil-to-fertilizer'],soil)
        water = convert_from_map(maps['fertilizer-to-water'],fert)
        light = convert_from_map(maps['water-to-light'],water)
        temp = convert_from_map(maps['light-to-temperature'],light)
        hum = convert_from_map(maps['temperature-to-humidity'],temp)
        loc = convert_from_map(maps['humidity-to-location'],hum)
        min_location = min(min_location, loc)
        print(f"seed:{seed} soil:{soil} fert:{fert} water:{water} light:{light} temp:{temp} hum:{hum} loc:{loc}")
    

print(f"Part 2 answer: {min_location}")

for i in range(100):
    pass
    print(f"seed: {i} loc: {seed_to_location(i,maps)}")

quit()

discontinuous_seeds = set()
discontinous_humidities = set()
for ma in maps['humidity-to-location']:
    minh = ma['s_start']
    maxh = ma['s_start']+ma['r']
    discontinous_humidities.add(minh)
    discontinous_humidities.add(maxh)

for h in discontinous_humidities:
    convert_from_map_backwards(maps['humidity-to-location'],h)

def find_subrange(x,y):
    #x = set(x)
    #y = set(y)
    #sect = x.intersection(y)
    rmin = max(x[0],y[0])
    rmax = min(x[-1],y[-1])
    if rmin < rmax:
        sect = range(max(x[0],y[0]),min(x[-1], y[-1])+1)
        return sect
    else:
        return range(0,0)
    #print(f"sect: {sect}")
    if len(sect)>0:
        mins = min(sect)
        #print(f"mins: {mins}")
        maxs = max(sect)
        #print(f"maxs: {maxs}")
        new_range = range(mins,maxs+1)
        return new_range
    else:
        return range(0,0)

def find_subranges(entries, input_range):
    subranges = []
    for e in entries:
        ss = e['s_start']
        r = e['r']
        e_range = range(ss,ss+r)
        #print(f"e range: {e_range}")
        sr = find_subrange(e_range,input_range)
        subranges.append(sr)
    return subranges


order_mappings = ["seed-to-soil","soil-to-fertilizer","fertilizer-to-water","water-to-light","light-to-temperature","temperature-to-humidity","humidity-to-location"]

seed_ranges_to_check = set()
for r in seed_ranges:
    #print(f"input: {r}")
    print("@@@@@")
    ranges = find_subranges(maps['seed-to-soil'],r)
    print(ranges)
    seed_ranges_to_check = seed_ranges_to_check.union(ranges)

print()
print("$$$$")
print(seed_ranges)
print(seed_ranges_to_check)

soil_ranges = set()
for sr in seed_ranges_to_check:
    if len(sr) > 0:
        x = min(sr)
        y = max(sr)+1
        x = convert_from_map(maps['seed-to-soil'],x)
        y = convert_from_map(maps['seed-to-soil'],y)
        r = range(x,y)
        soil_ranges.add(r)
print(soil_ranges)

"""
true_seeds = []
for i in range(len(seeds)):
    if i % 2 == 0:
        start = seeds[i]
        delta = seeds[i+1]
        for j in range(start,start+delta):
            true_seeds.append(j)

#print(true_seeds)            

stscount
"""

seed_ranges = []
for i in range(len(seeds)):
    if i%2==0:
        r = range(seeds[i],seeds[i]+seeds[i+1])
        seed_ranges.append(r)
       
min_location = 1000000000000000
i = 1
for r in seed_ranges:
    print(f"new range {i}")
    i += 1
    for seed in r:
        soil = convert_from_map(maps['seed-to-soil'],seed)
        fert = convert_from_map(maps['soil-to-fertilizer'],soil)
        water = convert_from_map(maps['fertilizer-to-water'],fert)
        light = convert_from_map(maps['water-to-light'],water)
        temp = convert_from_map(maps['light-to-temperature'],light)
        hum = convert_from_map(maps['temperature-to-humidity'],temp)
        loc = convert_from_map(maps['humidity-to-location'],hum)
        min_location = min(min_location, loc)
    

print(f"Part 2 answer: {min_location}")