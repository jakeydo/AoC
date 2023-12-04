import sys
#from collections import defaultdict
#from os import system
#import time
from functools import cache
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

sumscores = 0
cards = {}

for line in lines:
  winnerside = line.split("|")[0]
  gid, winnerside = winnerside.split(":")
  gid = gid.split()[1]
  winners = set(winnerside.split())
  haveside = line.split("|")[1]
  haves = set(haveside.split())
  winnershave = haves.intersection(winners)
  if len(winnershave) == 0:
    numberwh = 0
  else:
    numberwh = len(winnershave)
    sumscores += 2**(numberwh-1)
  cards[int(gid)] = (int(gid),numberwh)


print(f"Part 1 answer: {sumscores}")

@cache
def cards_added(card):
  numcards = 1
  gid,numwh = cards[card]
  for i in range(numwh):
    numcards += cards_added(gid+i+1)
    #print(numcards)
  return numcards

score=0

for card in cards:
  score += cards_added(card)

print(f"Part 2 answer: {score}")

"""
mystack = []
for c in cards:
  mystack.append(cards[c])

myplayed = []

while len(mystack) > 0:
  gid,numwins= mystack.pop(0)
  for i in range(numwins):
    mystack.append(cards[gid+i+1])
  myplayed.append((gid, numwins))


"""