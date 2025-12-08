import sys
#from collections import defaultdict
#from os import system
#import time
#from functools import cache
#sys.setrecursionlimit(10**7)
import copy
args = str(sys.argv)
if ("test" in args):
    f = open("test.txt", "r", encoding="utf-16")
else:
    f = open("real.txt", "r", encoding="utf-16")
lines = f.readlines()
clean_lines = copy.deepcopy(lines)

for i in range(len(lines)):
    #lines[i] = lines[i].replace("\x00"," ")
    lines[i] = lines[i].strip().split()
    #print(lines[i].strip().split())

operators = lines.pop()

#put the code here

answers = []

for j in range(len(operators)):
    if operators[j] == "+":
        answers.append(0)
    elif operators[j] == "*":
        answers.append(1)
    for i in range(len(lines)):
        if operators[j] == "+":
            answers[j] += int(lines[i][j])
        elif operators[j] == "*":
            answers[j] *= int(lines[i][j])
            

print(f"Part 1 answer: {sum(answers)}")

lines = clean_lines

operators = lines.pop()

lefts = []

x = 0
for i in range(len(operators)):
    if operators[i] != " ":
        lefts.append(x)
    x += 1
#print(lefts)
operators = operators.split()
answers = []

for j in range(len(operators)):
    s = lefts[j]
    e = 0
    if j+1 < len(operators):
        e = lefts[j+1]-1
    else:
        e = len(lines[x])-1
    #print(f"s:{s} e:{e}")
    
    operands = []
    for i in range(s,e):
        operands.append("")
    
    for x in range(len(lines)):
        for y in range(s,e):
            operands[y-s] += lines[x][y]
        #op = int(op)
        #print(operands)
    
    if operators[j] == "+":
        answer = 0
    elif operators[j] == "*":
        answer = 1
        
    for op in operands:
        if operators[j] == "+":
            answer += int(op)
        elif operators[j] == "*":
            answer *= int(op)
    answers.append(answer)


#print(answers)    
 

print(f"Part 2 answer: {sum(answers)}")