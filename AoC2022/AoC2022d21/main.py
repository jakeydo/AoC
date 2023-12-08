import sys
from math import copysign
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

monkeys = {}
for line in lines:
    a,b = line.strip().split(":")
    b = b.strip()
    if b.isnumeric():
        b = int(b)
    monkeys[a] = b

root_data = monkeys['root'].split()
x = root_data[0]
y = root_data[2]

def allnumbers(monkeys):
    for m in monkeys:
        if not isinstance(monkeys[m],int):
            return False
    return True

while not allnumbers(monkeys):
    for m in monkeys:
        data = monkeys[m]
        if not isinstance(data,int):
            data = data.split()
            if isinstance(monkeys[data[0]],int) and isinstance(monkeys[data[2]],int):
                if data[1] == "+":
                    monkeys[m] = int(monkeys[data[0]]) + int(monkeys[data[2]])
                elif data[1] == "-":
                    monkeys[m] = int(monkeys[data[0]]) - int(monkeys[data[2]])
                elif data[1] == "*":
                    monkeys[m] = int(monkeys[data[0]]) * int(monkeys[data[2]])
                elif data[1] == "/":
                    monkeys[m] = int(int(monkeys[data[0]]) / int(monkeys[data[2]]))

print(f"Part 1 answer: {monkeys['root']}")


monkeys = {}
"""
for line in lines:
    a,b = line.strip().split(":")
    b = b.strip()
    if b.isnumeric():
        b = int(b)
    monkeys[a] = b
del monkeys['root']
"""

def init_monkeys(monkeys):
    for line in lines:
        a,b = line.strip().split(":")
        b = b.strip()
        if b.isnumeric():
            b = int(b)
        monkeys[a] = b
    del monkeys['root']

def calculate_monkeys(monkeys):
    while not allnumbers(monkeys):
        for m in monkeys:
            data = monkeys[m]
            if not isinstance(data,int):
                data = data.split()
                if isinstance(monkeys[data[0]],int) and isinstance(monkeys[data[2]],int):
                    if data[1] == "+":
                        monkeys[m] = int(monkeys[data[0]]) + int(monkeys[data[2]])
                    elif data[1] == "-":
                        monkeys[m] = int(monkeys[data[0]]) - int(monkeys[data[2]])
                    elif data[1] == "*":
                        monkeys[m] = int(monkeys[data[0]]) * int(monkeys[data[2]])
                    elif data[1] == "/":
                        monkeys[m] = int(int(monkeys[data[0]]) / int(monkeys[data[2]]))    

def diff_from_humn(monkeys,humn,x,y):
    monkeys = {}
    init_monkeys(monkeys)
    monkeys['humn'] = humn
    calculate_monkeys(monkeys)
    return monkeys[x] - monkeys[y]


humn_test = 0
monkeys = {}
diff = diff_from_humn(monkeys,humn_test,x,y)
print(diff)

test_start = 3378273370500

for i in range(test_start,test_start+1000):
    monkeys = {}
    diff = diff_from_humn(monkeys,i,x,y)
    #print(f"humn:{i} diff:{diff}")
    if diff == 0:
        print(f"part 2 answer: {i}")
        break
        

"""
step = 10
humn_test = 0
prev = delta_from_humn(monkeys,humn_test,x,y)
prev_test = humn_test
humn_test += step
current = delta_from_humn(monkeys,humn_test,x,y)
delta = abs(current - prev)
last_delta = 1
current_sign = copysign(1,delta)
prev_sign = current_sign

while not delta==0:
    print(f"prev_test:{prev_test} humn_test:{humn_test} delta:{delta} step:{step}")
    input()
    if (current_sign == prev_sign) and (delta < last_delta):
        last_delta = delta
        prev = current
        prev_test = humn_test
        humn_test += step
        current = delta_from_humn(monkeys,humn_test,x,y)
        delta = abs(current - prev)
        prev_sign = current_sign
        current_sign = copysign(1,delta)
    else:
        humn_test = prev_test
        step = step // 10
        last_delta = delta
        prev = current
        humn_test = humn_test + step
        prev_test = humn_test
        current = delta_from_humn(monkeys,humn_test,x,y)
        delta = abs(current - prev)
        prev_sign = current_sign
        current_sign = copysign(1,delta)



print(f"Part 2 answer: {humn_test}")


#make new monkeys for part 2
monkeys = {}
init_monkeys(monkeys)
monkeys['humn'] = 0
calculate_monkeys(monkeys)
first_run = monkeys[x] - monkeys[y]
monkeys = {}
init_monkeys(monkeys)
monkeys['humn'] = 1
calculate_monkeys(monkeys)
second_run = monkeys[x] - monkeys[y]

direction = 0
if first_run > second_run:
    direction = -1
else:
    direction = 1
print(f"direction:{direction}")
input()

humn_min = 6200000000000
humn_max = 6500000000000
humn_test = (humn_min+humn_max)//2
last_delta = humn_max

#humn_test = 500
last_delta = second_run - first_run
#while not monkeys[x] == monkeys[y]:
        


while not monkeys[x] == monkeys[y]:
    #delta = monkeys[x] - monkeys[y]
    #direction = delta - last_delta
    #last_delta = delta
    #print(delta)
    if direction<1:
        if monkeys[x] < monkeys[y]:
            humn_min = humn_test
            humn_test = humn_min + (humn_max-humn_min)//2
        else:
            humn_max = humn_test
            humn_test = humn_max - (humn_max-humn_min)//2
    else:
        if monkeys[x] > monkeys[y]:
            humn_max = humn_test
            humn_test = humn_min + (humn_max-humn_min)//2
        else:
            humn_min = humn_test
            humn_test = humn_min + (humn_max-humn_min)//2
            
    
    monkeys = {}
    init_monkeys(monkeys)
    monkeys['humn'] = humn_test
    calculate_monkeys(monkeys)
    while not allnumbers(monkeys):
        for m in monkeys:
            data = monkeys[m]
            if not isinstance(data,int):
                data = data.split()
                if isinstance(monkeys[data[0]],int) and isinstance(monkeys[data[2]],int):
                    if data[1] == "+":
                        monkeys[m] = int(monkeys[data[0]]) + int(monkeys[data[2]])
                    elif data[1] == "-":
                        monkeys[m] = int(monkeys[data[0]]) - int(monkeys[data[2]])
                    elif data[1] == "*":
                        monkeys[m] = int(monkeys[data[0]]) * int(monkeys[data[2]])
                    elif data[1] == "/":
                        monkeys[m] = int(int(monkeys[data[0]]) / int(monkeys[data[2]]))
    print(f"min:{humn_min} max:{humn_max} test:{humn_test} x:{monkeys[x]}\t y:{monkeys[y]}")

             
print(f"Part 2 answer: {monkeys['humn']}")
"""