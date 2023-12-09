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

readings = []

for line in lines:
    r = list(map(int, line.strip().split()))
    readings.append(r)
    #print(r)

def extrapolate(row):
    row = row[:]
    row_index = 0
    triangle = [row]
    while not all(x==0 for x in triangle[row_index]):
        row = triangle[row_index]
        next_row = []
        for i in range(1,len(row)):
            next_row.append(row[i]-row[i-1])
        triangle.append(next_row)
        row_index +=1
        
       
    tri_length = len(triangle)
    for i in range(tri_length):
        row_index = -(i+1)
        if row_index == -1:
            triangle[row_index].append(0)
        else:
            next_row_last = triangle[row_index+1][-1]
            this_row_last = triangle[row_index][-1]
            triangle[row_index].append(this_row_last+next_row_last)

    return triangle[0][-1]
        
new_ends = []
for r in readings:
    new_ends.append(extrapolate(r))

#put the code here

print(f"Part 1 answer: {sum(new_ends)}")


print(f"Part 2 answer: {0}")