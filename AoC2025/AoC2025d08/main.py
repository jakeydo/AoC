import sys
#from collections import defaultdict
#from os import system
#import time
#from functools import cache
#sys.setrecursionlimit(10**7)
#from copy import deepcopy
args = str(sys.argv)
if ("test" in args):
    f = open("test.txt")
    loops = 10
else:
    f = open("real.txt")
    loops = 1000
lines = f.readlines()

circuits = []

jbs = []
connected_pairs = []

for line in lines:
    x,y,z = line.strip().split(",")
    x = int(x)
    y = int(y)
    z = int(z)
    jbs.append((x,y,z))

unc_jbs = set(jbs)

min_d = 1000000000000
min_ds = []
connected_pairs = []
min_pair = set()

for x in range(loops*10):
    min_ds.append(min_d)
    connected_pairs.append(((0,0,0),(0,0,0)))

for i in range(len(jbs)):
    ix,iy,iz = jbs[i]
    for j in range(i+1,len(jbs)):
        jx,jy,jz = jbs[j]    
        d = ((ix-jx)**2 + (iy-jy)**2 + (iz-jz)**2)**0.5
        if d <= max(min_ds):
            remove_index = min_ds.index(max(min_ds))
            del min_ds[remove_index]
            del connected_pairs[remove_index]
            min_ds.append(d)
            connected_pairs.append(((ix,iy,iz),(jx,jy,jz)))
            """
            min_d = d
            min_pair = set()
            min_pair.add(jbs[i])
            min_pair.add(jbs[j])
            """
#print(min_ds)

#print(connected_pairs)
#put the code here

connected_pairs = [x for _, x in sorted(zip(min_ds,connected_pairs))]

for cp in connected_pairs:
    p1,p2 = cp
    
    if p1 in unc_jbs:
        unc_jbs.remove(p1)
    if p2 in unc_jbs:
        unc_jbs.remove(p2)
    """
    print("circuits:")
    print(circuits)
    print("unc_jbs:")
    print(unc_jbs)
    print("***")
    print()
    """
    if len(circuits) == 1 and len(unc_jbs) == 0:
        
        x1,y1,z1 = p1
        x2,y2,z2 = p2
        #print(x1)
        #print(x2)
        print(f"part 2 answer: {x1*x2}")
        break
    
    #print(f"p1: {p1}")
    #print(f"p2: {p2}")
    #print()
    #connected = False
    connection_count = 0
    connected_indices = []
    for i in range(len(circuits)):
        circuit = circuits[i]
        if p1 in circuit or p2 in circuit:
            circuit.add(p1)
            circuit.add(p2)
            connection_count += 1
            connected_indices.append(i)
    if connection_count == 0:
        c = set()
        c.add(p1)
        c.add(p2)
        circuits.append(c)
    elif connection_count == 1:
        pass
    elif connection_count == 2:
        y,z = connected_indices
        keep_circuit = circuits[z]
        old_circuit = circuits.pop(y)
        for jb in old_circuit:
            keep_circuit.add(jb)
    
circuit_lens = [0,0,0]
    

for circuit in circuits:
    if len(circuit) > min(circuit_lens):
        circuit_lens.remove(min(circuit_lens))
        circuit_lens.append(len(circuit))

#print(circuit_lens)

x,y,z = circuit_lens

#print(x*y*z)
    


    
print(f"Part 1 answer: {x*y*z}")


print(f"Part 2 answer: {0}")