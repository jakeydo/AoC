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

ranges = []
for line in lines:
    rs = line.strip().split(",")
    for r in rs:
        ranges.append(r)

invalid_count = 0
invalid_sum = 0

for r in ranges:
    r0,r1 = r.split("-")
    r0 = int(r0)
    r1 = int(r1)
    for i in range(r0,r1+1):
        i_s = str(i)
        no_diff = True
        if len(i_s) % 2 == 0:
            half_len = len(i_s) // 2
            for x in range(0,half_len):
                if not i_s[x] == i_s[half_len+x]:
                    no_diff = False
            if no_diff:
                invalid_count += 1
                invalid_sum += i
            else:
                no_diff = True
            
print(f"Part 1 answer: {invalid_count}, {invalid_sum}")

#invalid_count = 0
#invalid_sum = 0

invalids = []

for r in ranges:
    r0,r1 = r.split("-")
    r0 = int(r0)
    r1 = int(r1)
    for i in range(r0,r1+1):
        #print()
        #print(f"i: {i}")
        i_s = str(i)
        no_diff = True
        
        digits = set(i_s)
        if len(digits) == 1 and len(i_s) > 1:
            invalids.append(i)
            #invalid_count += 1
            #invalid_sum += i
            #print(i)
        elif len(i_s) > 2: #and len(i_s) % 2 == 0:
            half_len = len(i_s) // 2
            #print(f"half_len: {half_len}")
            for a in range(2, half_len+1):
                if i in invalids:
                    break
                else:
                    #print(f"a: {a}")
                    if len(i_s) % a == 0:
                        sub_len = len(i_s) // a
                        #a is number of substrings, sub_len is the length of each substring
                        for position in range(sub_len):
                            test_digit = i_s[position]
                            for chunk in range(a):
                                #print(f"chunk: {chunk}, position:{position}")
                                #print(f"test_digit: {test_digit}, this digit: {i_s[chunk*sub_len + position]}")
                                if not i_s[chunk*sub_len + position] == test_digit:
                                    #print("FOUND A DIFFERENCE")
                                    no_diff = False
                        if no_diff:
                            #print(i)
                            invalids.append(i)
                            #invalid_count += 1
                            #invalid_sum += i
                        else:
                            no_diff = True


print(invalids)
print(f"Part 2 answer: {len(invalids)}, {sum(invalids)}")
