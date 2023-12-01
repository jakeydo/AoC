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

sum  = 0
for line in lines:
    #print(line)
    line = line.strip()
    print()
    print(line)
    
    minwordindex = 1000
    minwordvalue = "xx"
    index1 = line.find("1")
    indexone = line.find("one")
    if indexone == -1:
        indexone = 1000
    if indexone < minwordindex:
        minwordindex = indexone
        minwordvalue = 1
    
    index2 = line.find("2")
    indextwo = line.find("two")
    if indextwo == -1:
        indextwo = 1000
    if indextwo < minwordindex:
        minwordindex = indextwo
        minwordvalue = 2
        
    index3 = line.find("3")
    indexthree = line.find("three")
    if indexthree == -1:
        indexthree = 1000
    if indexthree < minwordindex:
        minwordindex = indexthree
        minwordvalue = 3
        
    index4 = line.find("4")
    indexfour = line.find("four")
    if indexfour == -1:
        indexfour = 1000
    if indexfour < minwordindex:
        minwordindex = indexfour
        minwordvalue = 4
    
    index5 = line.find("5")
    indexfive = line.find("five")
    if indexfive == -1:
        indexfive = 1000
    if indexfive < minwordindex:
        minwordindex = indexfive
        minwordvalue = 5
        
    index6 = line.find("6")
    indexsix = line.find("six")
    if indexsix == -1:
        indexsix = 1000
    if indexsix < minwordindex:
        minwordindex = indexsix
        minwordvalue = 6
        
    index7 = line.find("7")
    indexseven = line.find("seven")
    if indexseven == -1:
        indexseven = 1000
    if indexseven < minwordindex:
        minwordindex = indexseven
        minwordvalue = 7
        
    index8 = line.find("8")
    indexeight = line.find("eight")
    if indexeight == -1:
        indexeight = 1000
    if indexeight < minwordindex:
        minwordindex = indexeight
        minwordvalue = 8
        
    index9 = line.find("9")
    indexnine = line.find("nine")
    if indexnine == -1:
        indexnine = 1000
    if indexnine < minwordindex:
        minwordindex = indexnine
        minwordvalue = 9
        
    index0 = line.find("0")
    indexzero = line.find("zero")
    if indexzero == -1:
        indexzero = 1000
    if indexzero < minwordindex:
        minwordindex = indexzero
        minwordvalue = 0
        
    if minwordvalue == 0:
        #line = line.replace("zero","0",1)
        line = line[:minwordindex] + "0" + line[minwordindex:]
    elif minwordvalue == 1:
        #line = line.replace("one","1",1)
        line = line[:minwordindex] + "1" + line[minwordindex:]
    elif minwordvalue == 2:
        #line = line.replace("two","2",1)
        line = line[:minwordindex] + "2" + line[minwordindex:]
    elif minwordvalue == 3:
        #line = line.replace("three","3",1)
        line = line[:minwordindex] + "3" + line[minwordindex:]
    elif minwordvalue == 4:
        #line = line.replace("four","4",1)           
        line = line[:minwordindex] + "4" + line[minwordindex:]
    elif minwordvalue == 5:
        #line = line.replace("five","5",1)
        line = line[:minwordindex] + "5" + line[minwordindex:]
    elif minwordvalue == 6:
        #line = line.replace("six","6",1)
        line = line[:minwordindex] + "6" + line[minwordindex:]
    elif minwordvalue == 7:
        #line = line.replace("seven","7",1)
        line = line[:minwordindex] + "7" + line[minwordindex:]
    elif minwordvalue == 8:
        #line = line.replace("eight","8",1)
        line = line[:minwordindex] + "8" + line[minwordindex:]
    elif minwordvalue == 9:
        #line = line.replace("nine","9",1)
        line = line[:minwordindex] + "9" + line[minwordindex:]
        
    line = line[::-1]
    print(line)
    
    #this is where the new stuff started
    ###
    
    minwordindex = 1000
    minwordvalue = "xx"
    index1 = line.find("1")
    indexone = line.find("eno")
    if indexone == -1:
        indexone = 1000
    if indexone < minwordindex:
        minwordindex = indexone
        minwordvalue = 1
    
    index2 = line.find("2")
    indextwo = line.find("owt")
    if indextwo == -1:
        indextwo = 1000
    if indextwo < minwordindex:
        minwordindex = indextwo
        minwordvalue = 2
        
    index3 = line.find("3")
    indexthree = line.find("eerht")
    if indexthree == -1:
        indexthree = 1000
    if indexthree < minwordindex:
        minwordindex = indexthree
        minwordvalue = 3
        
    index4 = line.find("4")
    indexfour = line.find("ruof")
    if indexfour == -1:
        indexfour = 1000
    if indexfour < minwordindex:
        minwordindex = indexfour
        minwordvalue = 4
    
    index5 = line.find("5")
    indexfive = line.find("evif")
    if indexfive == -1:
        indexfive = 1000
    if indexfive < minwordindex:
        minwordindex = indexfive
        minwordvalue = 5
        
    index6 = line.find("6")
    indexsix = line.find("xis")
    if indexsix == -1:
        indexsix = 1000
    if indexsix < minwordindex:
        minwordindex = indexsix
        minwordvalue = 6
        
    index7 = line.find("7")
    indexseven = line.find("neves")
    if indexseven == -1:
        indexseven = 1000
    if indexseven < minwordindex:
        minwordindex = indexseven
        minwordvalue = 7
        
    index8 = line.find("8")
    indexeight = line.find("thgie")
    if indexeight == -1:
        indexeight = 1000
    if indexeight < minwordindex:
        minwordindex = indexeight
        minwordvalue = 8
        
    index9 = line.find("9")
    indexnine = line.find("enin")
    if indexnine == -1:
        indexnine = 1000
    if indexnine < minwordindex:
        minwordindex = indexnine
        minwordvalue = 9
        
    index0 = line.find("0")
    indexzero = line.find("orez")
    if indexzero == -1:
        indexzero = 1000
    if indexzero < minwordindex:
        minwordindex = indexzero
        minwordvalue = 0
        
    if minwordvalue == 0:
        #line = line.replace("orez","0",1)
        line = line[:minwordindex] + "0" + line[minwordindex:]
    elif minwordvalue == 1:
        #line = line.replace("eno","1",1)
        line = line[:minwordindex] + "1" + line[minwordindex:]
    elif minwordvalue == 2:
        #line = line.replace("owt","2",1)
        line = line[:minwordindex] + "2" + line[minwordindex:]
    elif minwordvalue == 3:
        #line = line.replace("eerht","3",1)
        line = line[:minwordindex] + "3" + line[minwordindex:]
    elif minwordvalue == 4:
        #line = line.replace("ruof","4",1)           
        line = line[:minwordindex] + "4" + line[minwordindex:]
    elif minwordvalue == 5:
        #line = line.replace("evif","5",1)
        line = line[:minwordindex] + "5" + line[minwordindex:]
    elif minwordvalue == 6:
        #line = line.replace("xis","6",1)
        line = line[:minwordindex] + "6" + line[minwordindex:]
    elif minwordvalue == 7:
        #line = line.replace("neves","7",1)
        line = line[:minwordindex] + "7" + line[minwordindex:]
    elif minwordvalue == 8:
        #line = line.replace("thgie","8",1)
        line = line[:minwordindex] + "8" + line[minwordindex:]
    elif minwordvalue == 9:
        #line = line.replace("enin","9",1)
        line = line[:minwordindex] + "9" + line[minwordindex:]
 
    line = line[::-1]
   
    print(line)
    digits = []
    for c in line:
        #print(c)
        if c.isdigit():
            #print(c)
            digits.append(c)
    digits = "".join(digits)
    if digits:
        digits = digits[0] + digits[-1]
        digits = int(digits)
        print(digits)
        sum = sum + digits
        #num = digits[0] + digits[-1]
        #print(num)




#print(f"Part 1 answer: {sum}")
print(f"Part 2 answer: {sum}")