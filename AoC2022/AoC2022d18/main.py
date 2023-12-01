#from collections import defaultdict
#from os import system
from functools import cache
import sys
sys.setrecursionlimit(10**7)

test = False
if test:
    f = open("test.txt")
else:
    f = open("real.txt")

lines = f.readlines()

class Cube():
    x = 0
    y = 0
    z = 0
    
    def __init__(self,x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z
        
    def __str__(self):
        return str((self.x,self.y,self.z))
        
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def __hash__(self):
        return hash((self.x,self.y,self.z))
        
    def neighbors(self,maxx,maxy,maxz):
        bros = set()
        x,y,z = self.x,self.y,self.z
        for i in range(-1,2):
            newx = x+i
            if newx in range(0,maxx+1):
                bros.add(Cube(newx,y,z))
        for j in range(-1,2):
            newy = y+j
            if newy in range(0,maxy+1):
                bros.add(Cube(x,newy,z))
        for k in range(-1,2):
            newz = z+k
            if newz in range(0,maxz+1):
                bros.add(Cube(x,y,newz))
        bros.remove(self)
        return bros
            
cubes = set()
maxx,maxy,maxz = 0,0,0
for line in lines:
    line = line.strip()
    x,y,z = line.split(",")
    c = Cube(int(x),int(y),int(z))
    maxx=max(maxx,int(x))
    maxy=max(maxy,int(y))
    maxz=max(maxz,int(z))
    cubes.add(c)

def faces_from_cube(c):
    faces = set()
    xs = (c.x-1,c.x)
    ys = (c.y-1,c.y)
    zs = (c.z-1,c.z)
    x1,x2 = xs
    y1,y2 = ys
    z1,z2 = zs
    
    f = frozenset([(x1,y1,z1),(x2,y1,z1),(x2,y2,z1),(x1,y2,z1)])
    faces.add(f)
    f = frozenset([(x1,y1,z2),(x2,y1,z2),(x2,y2,z2),(x1,y2,z2)])
    faces.add(f)
    f = frozenset([(x1,y1,z1),(x1,y1,z2),(x1,y2,z1),(x1,y2,z2)])
    faces.add(f)
    f = frozenset([(x2,y1,z1),(x2,y1,z2),(x2,y2,z1),(x2,y2,z2)])
    faces.add(f)
    f = frozenset([(x1,y1,z1),(x1,y1,z2),(x2,y1,z1),(x2,y1,z2)])
    faces.add(f)
    f = frozenset([(x1,y2,z1),(x1,y2,z2),(x2,y2,z1),(x2,y2,z2)])
    faces.add(f)
    return faces

def is_surrounded(c,cubes,maxx,maxy,maxz):
    x,y,z = c.x,c.y,c.z
    surrounded_x = False
    surrounded_y = False
    surrounded_z = False
    #first walk x backwards and see if you hit lava
    prev_x = False
    next_x = False
    for i in range(0,x):
        if Cube(i,y,z) in cubes:
            prev_x = True
    for i in range (x+1,maxx+1):
        #print((i,y,z))
        if Cube(i,y,z) in cubes:
            #print("it's here")
            next_x = True
    surrounded_x = prev_x and next_x
    
    prev_y = False
    next_y = False
    for j in range(0,y):
        if Cube(x,j,z) in cubes:
            prev_y = True
    for j in range(y+1,maxy+1):
        if Cube(x,j,z) in cubes:
            next_y = True
    surrounded_y = prev_y and next_y
    
    prev_z = False
    next_z = False
    for k in range(0,z):
        if Cube(x,y,k) in cubes:
            prev_z = True
    for k in range(z+1,maxz+1):
        if Cube(x,y,k) in cubes:
            next_z = True
    surrounded_z = prev_z and next_z
    """
    print(prev_x)
    print(next_x)
    print(prev_y)
    print(next_y)
    print(prev_z)
    print(next_z)
    """
    
    return surrounded_x and surrounded_y and surrounded_z
 
@cache
def can_reach_origin(c,cubes,emptycubes):
    print(c)
    w=c
    o = Cube(0,0,0)
    #print(c)
    got_there = False
    
    #visited = set()
    if c == o:
        return True
    
    x,y,z = c.x,c.y,c.z
    neighbors = set()
    for i in range(-1,2):
        t = Cube(x+i,y,z)
        neighbors.add(t)
    for j in range(-1,2):
        t = Cube(x,y+j,z)
        neighbors.add(t)
    for k in range(-1,2):
        t = Cube(x,y,z+k)
        neighbors.add(t)
  
    for n in neighbors:
        if n.x in range(0,maxx+1) and n.y in range(0,maxy+1) and n.z in range(0,maxz+1):
            if n in emptycubes:
                got_there = got_there or can_reach_origin(n,cubes,emptycubes)
    
    return got_there
    
 
outside = set()

for c in cubes:
    faces = faces_from_cube(c)
    outside = outside.symmetric_difference(faces)

print(f"Exterior face count (not exactly): {len(outside)}")
print(f"Maxes are: {(maxx,maxy,maxz)}")

emptycubes = set()
for i in range(maxx+1):
    for j in range(maxy+1):
        for z in range(maxz+1):
            c = Cube(i,j,z)
            if not c in cubes:
                emptycubes.add(c)

steam = set()
c = Cube(0,0,0)
q = [c]

visited = set()
while(len(q)) > 0:
    c = q.pop(0)    
    if not c in steam:
        steam.add(c)
        for n in c.neighbors(maxx,maxy,maxz):
            if not n in cubes and not n in steam:
                q.append(n)


empty_not_steamy = set()
for e in emptycubes:
    if not e in steam:
        empty_not_steamy.add(e)
        print(f"{e} is empty but not steamy")
        
not_steamy_faces = set()
for e in empty_not_steamy:
    for f in faces_from_cube(e):
        not_steamy_faces.add(f)

true_outside = set(outside)
for f in not_steamy_faces:
    if f in true_outside:
        true_outside.remove(f)


"""
e = Cube(2,2,5)
print(e)
print("***")
is_surrounded(e,cubes,maxx,maxy,maxz)

"""
"""
surroundedcubes = set()
emptycount = 0
for e in emptycubes:
    if is_surrounded(e,cubes,maxx,maxy,maxz):
        #print(e)
        surroundedcubes.add(e)
        emptycount +=1

print(f"Empty count: {emptycount}")

allfaces = set()
for c in cubes:
    for f in faces_from_cube(c):
        allfaces.add(f)
"""

"""
for s in surroundedcubes:
    faces = faces_from_cube(s)
    for f in faces:
        if f in outside:
            outside.remove(f)
"""
"""
bubbles = set()
for e in emptycubes:
    if not can_reach_origin(e,frozenset(cubes),frozenset(emptycubes)):
        bubbles.add(e)

for c in bubbles:
    print(c)

for c in bubbles:
    for f in faces_from_cube(c):
        if f in outside:
            outside.remove(f)
"""            
print(f"Exterior face count (yes exactly): {len(true_outside)}")