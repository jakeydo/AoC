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

class Number():
    value = 0
    previous = 0
    following = 0
    
    def go_backwards(self):
        #temp_prev = self.previous.previous
        #temp_following = self.previous.following
        spp = self.previous.previous
        sp = self.previous
        sf = self.following
        spp.following = self
        self.previous = spp
        self.following = sp
        sp.previous = self
        sp.following = sf
        sf.previous = sp
        
    def go_forwards(self):
        sff = self.following.following
        sf = self.following
        sp = self.previous       
        sp.following = sf
        sf.previous = sp
        sf.following = self
        self.previous = sf
        self.following = sff
        sff.previous = self


def print_nums(n, steps):
    out_string = ""
    for i in range(steps):
        out_string += f"{n.value} "
        n = n.following
    print(out_string)
    
def get_xth_number(n,x):
    number = n
    for i in range(x):
        number = number.following
    return number

original_array = []
zero_number = 0

for line in lines:
    n = Number()
    n.value = int(line.strip())
    if n.value == 0:
        zero_number = n
    original_array.append(n)
    
last_num = original_array[len(original_array)-1]
first_num = original_array[0]

for i in range(len(original_array)):
    this_num = original_array[i]
    if i == 0:
        this_num.previous = last_num
    else:
        this_num.previous = original_array[i-1]
    
    if i == len(original_array)-1:
        this_num.following = first_num
    else:
        this_num.following = original_array[i+1]


steps = len(original_array)        
for n in original_array:    
    if n.value < 0:
        val = n.value * -1
        for i in range(val):
            n.go_backwards()
    else:
        for i in range(n.value):
            n.go_forwards()

a = get_xth_number(zero_number,1000).value
b = get_xth_number(zero_number,2000).value
c = get_xth_number(zero_number,3000).value

print(f"a:{a}\tb:{b}\tc:{c}")


#put the code here

print(f"Part 1 answer: {sum([a,b,c])}")

#put back in original order
for i in range(len(original_array)):
    this_num = original_array[i]
    if i == 0:
        this_num.previous = last_num
    else:
        this_num.previous = original_array[i-1]
    
    if i == len(original_array)-1:
        this_num.following = first_num
    else:
        this_num.following = original_array[i+1]

for n in original_array:
    n.value = n.value * 811589153

#print_nums(zero_number,steps)
for z in range(10):
    for n in original_array:
        val = n.value % (steps-1)
        if val < 0:
            val = -1 * val
            for i in range(val):
                n.go_backwards()
        else:
            for i in range(val):
                n.go_forwards()

#print_nums(zero_number,steps)

a = get_xth_number(zero_number,1000).value
b = get_xth_number(zero_number,2000).value
c = get_xth_number(zero_number,3000).value

print(f"a:{a}\tb:{b}\tc:{c}")
            
print(f"Part 2 answer: {sum([a,b,c])}")