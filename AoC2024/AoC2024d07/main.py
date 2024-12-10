import sys
#from collections import defaultdict
#from os import system
#import time
#from functools import cache
#sys.setrecursionlimit(10**7)
args = str(sys.argv)
if ("test" in args):
    f = open("test.txt")
else:
    f = open("real.txt")
lines = f.readlines()

tvs = []
eqs = [] 

for line in lines:
    tv, eq = line.strip().split(": ")
    tv = int(tv)
    eq = eq.split()
    for i,e in enumerate(eq):
        eq[i] = e
    tvs.append(tv)
    eqs.append(eq)

tcv = 0
bad_eqs = []

for i in range(len(tvs)):
    good = False
    tv = tvs[i]
    eq = eqs[i]
    number_operators = (len(eqs[i])-1) 
    combo_count = (2**number_operators)      

        
    for j in range(combo_count):
        if not good:
            e_str = ""
            #bin_count = format(number_operators,bin(i))
            bin_count = format(j,f"0{number_operators}b")
            #print(bin_count)
            bin_count = bin_count.replace("0","+").replace("1","*")
            
            value = eq[0]
            for k in range(number_operators):
                e_str = str(value) + bin_count[k] + eq[k+1]
                value = eval(e_str)
                #if j < number_operators:
                #    e_str = e_str + bin_count[j]
            #print(e_str)
            #ev = eval(e_str)
            #print(ev)
            ev = value
            #print(ev)
            if tv == ev:
                tcv += tv
                #print(f"adding:{tv} ")
                #print(f"total tcv: {tcv}")
                good = True
    if not good:
        bad_eqs.append(i)
    
  

#put the code here

print(f"Part 1 answer: {tcv}")

def ternary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))


for i in bad_eqs:
    eq = eqs[i]    
    tv = tvs[i]
    good = False
    
    number_operators = (len(eqs[i])-1) 
    combo_count = (3**number_operators)
    
    for j in range(combo_count):
        if not good:
            e_str = ""
            value = eq[0]
            
            
            #ter_count = format(j,f"0{number_operators}b")
            ter_count = ternary(j).zfill(number_operators)
            #print(bin_count)
            ter_count = ter_count.replace("0","+").replace("1","*").replace("2","|")
            
            value = eq[0]
            #print(f"tv:{tv} eq:{eq}  ter_count:{ter_count}")
            for k in range(number_operators):
                if ter_count[k] == "|":
                    value = eval(str(value) + eq[k+1])
                else:
                    e_str = str(value) + ter_count[k] + eq[k+1]
                    #print(f"es:{e_str}")
                    value = eval(e_str)
                    #print(f"value:{value}")
                #if j < number_operators:
                #    e_str = e_str + bin_count[j]
            #print(e_str)
            #ev = eval(e_str)
            #print(ev)
            ev = value
            
            #print(ev)
            if tv == ev:
                tcv += tv
                #print(f"adding:{tv} ")
                #print(f"total tcv: {tcv}")
                good = True
    
    
print(f"Part 2 answer: {tcv}")