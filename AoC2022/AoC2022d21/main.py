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


del monkeys['root']

humn_count = -1
while not monkeys[x] == monkeys[y]:
    monkeys = {}
    for line in lines:
        a,b = line.strip().split(":")
        b = b.strip()
        if b.isnumeric():
            b = int(b)
        monkeys[a] = b

    humn_count += 1
    print(humn_count)
    monkeys['humn'] = humn_count
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
             
print(f"Part 2 answer: {monkeys['humn']}")