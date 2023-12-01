from collections import defaultdict
from os import system

test = False
if test:
    f = open("test.txt")
else:
    f = open("real.txt")

lines = f.readlines()

data = ""
for line in lines:
    data = line.strip()
data = list(data)
#print(data)
    
class Shape():
    category = 0
    position = (0,0)
    is_moving = False

    def ___init___(self, category, position, is_moving=False):
        self.category = category
        self.position = position
        self.is_moving = is_moving

    def ___str___(self):
        return ""

    def points(self):
        x,y = self.position
        points = set()
        if self.category == 0:
            for i in range(4):
                points.add((x,y+i))
        elif self.category == 1:
            for i in range(3):
                points.add((x+1,y+i))
                points.add((x+i,y+1))
        elif self.category == 2:
            for i in range(3):
                points.add((x,y+i))
                points.add((x+i,y+2))
        elif self.category == 3:
            for i in range(4):
                points.add((x+i,y))
        elif self.category == 4:
            for i in range(2):
                for j in range(2):
                    points.add((x+i,y+j))
        return points
        
    def move_down(self,w):
        for x,y in self.points():            
            if w[(x-1,y)] == "#" or x==0:
                self.is_moving = False
                return False
        #nothing below me case below        
        x,y = self.position
        self.position = (x-1,y)
        return True
        
    def move_left(self,w):
        x,y = self.position
        if y<1:
            return
        
        for x,y in self.points():
            if w[(x,y-1)] == "#":
                return
        
        x,y = self.position
        self.position = (x,y-1)
    
    def move_right(self,w):
        x,y = self.position
        max_y = y
        if self.category == 0:
            max_y = y + 3
        elif self.category == 1 or self.category == 2:
            max_y = y + 2
        #cat 3 => max_y = y
        elif self.category == 4:
            max_y = y + 1
        
        if max_y > 5:
            #self.position = (x,y+1)
            return
            
        for x,y in self.points():
            if w[(x,y+1)] == "#":
                return
        
        x,y = self.position
        self.position = (x,y+1)
            

def shape(n):
    n = n % 5
    
    if n == 0:
        return ["####"]
    elif n == 1:
        return [".#.","###",".#."]
    elif n == 2:
        return ["..#","..#","###"]
    elif n ==3 :
        return ["#","#","#","#"]
    else:
        return ["##","##"]

def world_height(w):
    keys = w.keys()
    if keys:
        return max(x if not w[(x,y)]=="." else 0 for x,y in keys)+1
    else:
        return 0

def print_world(w):
    print()
    print("Printing world")
    height = world_height(w)
    for i in reversed(range(height+5)):
        line = ""
        for j in range(7):
            line += world[(i,j)]
        print(line)

def clear_moving(w):
    for p in w.keys():
        if w[p] == "@":
            w[p] = "."

def add_shape(s,w):
    for p in s.points():
        w[p] = "@" if s.is_moving else "#"

#test_print()

world = defaultdict(lambda:".")

#world_height = 0
resting_shapes = 0
shape_moving = False
   
    
world = defaultdict(lambda:".")

di = 0

for i in range(1000000000000):
    #clear_moving(world)
    n = i % 5
    h = world_height(world)
    next_x = h + 3
    s = Shape(n,(next_x,2),True)
    #add_shape(s,world)
    #print_world(world)
    #input()
    if i == 3610:
        print(f"world height at 1739: {h}")
    di = di % len(data)
    if di == 5:
        print(f"di: {di}")
        print(f"i: {i}")
        print(f"n: {n}")
        print(f"world height: {h}")
    #print(f"di: {di}")
    direction = data[di]
    di+=1
    if direction == "<":
        s.move_left(world)
    else:
        s.move_right(world)

    while s.move_down(world):
        di = di % len(data)
        direction = data[di]
        di+=1
        if direction == "<":
            s.move_left(world)
        else:
            s.move_right(world)
    
    clear_moving(world)
    add_shape(s,world)

print_world(world)
print("World height is:")
print(world_height(world))
