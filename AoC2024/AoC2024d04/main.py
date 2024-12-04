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

for line in lines:
    pass

#put the code here

def word_u(x,y,letters):
    wl = 4
    xd = -1
    yd = 0
    if x < wl-1:
        return
    else:
        #w = letters[x][y] + letters[x-1][y] + letters[x-2][y] + letters[x-3][y]
        w = ""
        for i in range(wl):
            w += letters[x+i*xd][y+i*yd]
        return w

def word_ur(x,y,letters):
    wl = 4
    xd = -1
    yd = 1
    
    if x < wl-1 or y > len(letters[0])-wl:
        return
    else:
        w = ""
        for i in range(wl):
            w += letters[x+i*xd][y+i*yd]    
        return w

def word_r(x,y,letters):
    wl = 4
    xd = 0
    yd = 1
    
    if y > len(letters[0])-wl:
        return
    else:
        w = ""
        for i in range(wl):
            w += letters[x+i*xd][y+i*yd]    
        return w

def word_dr(x,y,letters):
    wl = 4
    xd = 1
    yd = 1
    
    if x > len(letters)-wl or y > len(letters[0])-wl:
        return
    else:
        w = ""
        for i in range(wl):
            w += letters[x+i*xd][y+i*yd]    
        return w

def word_d(x,y,letters):
    wl = 4
    xd = 1
    yd = 0
    
    if x > len(letters)-wl:
        return
    else:
        w = ""
        for i in range(wl):
            w += letters[x+i*xd][y+i*yd]    
        return w

def word_dl(x,y,letters):
    wl = 4
    xd = 1
    yd = -1
    
    if x > len(letters)-wl or y < wl-1:
        return
    else:
        w = ""
        for i in range(wl):
            w += letters[x+i*xd][y+i*yd]    
        return w

def word_l(x,y,letters):
    wl = 4
    xd = 0
    yd = -1
    
    if y < wl-1:
        return
    else:
        w = ""
        for i in range(wl):
            w += letters[x+i*xd][y+i*yd]    
        return w

def word_ul(x,y,letters):
    wl = 4
    xd = -1
    yd = -1
    
    if x < wl-1 or y < wl-1:
        return
    else:
        w = ""
        for i in range(wl):
            w += letters[x+i*xd][y+i*yd]    
        return w

def words_at_pos(x,y,letters):
    words = []
    words.append(word_u(x,y,letters))
    words.append(word_ur(x,y,letters))
    words.append(word_r(x,y,letters))
    words.append(word_dr(x,y,letters))
    words.append(word_d(x,y,letters))
    words.append(word_dl(x,y,letters))
    words.append(word_l(x,y,letters))
    words.append(word_ul(x,y,letters))
    return words

xmas_count = 0
    
for i in range(len(lines)):
    for j in range(len(lines[0])):
        #print(f"i:{i} j:{j}")
        words = words_at_pos(i,j,lines)
        xmas_count += words.count("XMAS")

print(f"Part 1 answer: {xmas_count}")

def chunk_at_pos(x,y,letters):
    if not ((0 < x < len(letters)-1) and (0 < y < len(letters[0])-2)):
        #print("bad indices")
        return
    else:
        #print(f"i:{x} j:{y}")
        w = ""
        xs = x-1
        ys = y-1
        dot_indices = {(xs+0,ys+1),(xs+1,ys+0),(xs+1,ys+2),(xs+2,ys+1)}
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                #print(f"inside i:{i} j:{j}")
                if (i,j) in dot_indices:
                    w += "."
                else:
                    w += letters[i][j]
        #print(f"w is: {w}")
        return w

crosses = {"M.S.A.M.S","S.S.A.M.M","S.M.A.S.M","M.M.A.S.S",".M.MAS.S.",".S.MAS.M.",".M.SAM.S.",".S.SAM.M."}

#print(chunk_at_pos(1,2,lines))

x_mas_count = 0

for i in range(len(lines)):
    for j in range(len(lines[0])):
        #print(f"i:{i} j:{j}")
        chunk = chunk_at_pos(i,j,lines)
        if chunk in crosses:
            x_mas_count +=1

print(f"Part 2 answer: {x_mas_count}")