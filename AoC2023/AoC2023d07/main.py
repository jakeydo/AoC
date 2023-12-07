import sys
from functools import cmp_to_key
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

def count_cards(hand):
    counts = {}
    for c in hand['cards']:
        if not c in counts:
            counts[c] = 1
        else:
            counts[c] += 1
    hand['counts'] = counts

def isFive(hand):
    if 5 in hand['counts'].values():
        #print('five of a kind')        
        return True
    else:
        return False

def isFour(hand):
    if 4 in hand['counts'].values():
        #print('four of a kind')        
        return True
    else:
        return False

def isFH(hand):
    vals = hand['counts'].values()
    if (3 in vals) and (2 in vals):
        #print("full house")
        return True
    else:
        return False

def isTrips(hand):
    vals = hand['counts'].values()
    if (3 in vals) and not (2 in vals):
        #print("trips")
        return True
    else:
        return False

def is2Pair(hand):
    number_pairs = 0
    for card in hand['counts']:
        if hand['counts'][card] == 2:
            number_pairs += 1
    if number_pairs == 2:
        #print("two pairs")
        return True
    else:
        return False

def isPair(hand):
    number_pairs = 0
    for card in hand['counts']:
        if hand['counts'][card] == 2:
            number_pairs += 1
    if number_pairs == 1:
        #print("pair")
        return True
    else:
        return False

def score_hand(hand):
    if isFive(hand):
        hand['score'] = 6
    elif isFour(hand):
        hand['score'] = 5
    elif isFH(hand):
        hand['score'] = 4
    elif isTrips(hand):
        hand['score'] = 3
    elif is2Pair(hand):
        hand['score'] = 2
    elif isPair(hand):
        hand['score'] = 1
    else:
        hand['score'] = 0

def compare_cards(x,y):
    if x.isdigit():
        x = int(x)
    elif x == "T":
        x = 10
    elif x == "J":
        x = 11
    elif x == "Q":
        x = 12
    elif x == "K":
        x = 13
    elif x == "A":
        x = 14
        
    if y.isdigit():
        y = int(y)
    elif y == "T":
        y = 10
    elif y == "J":
        y = 11
    elif y == "Q":
        y = 12
    elif y == "K":
        y = 13
    elif y == "A":
        y = 14

    #print(f"x:{x} y:{y}")
    if x < y:
        #print(f"x smaller, return -1")
        return -1
    elif x > y:
        #print(f"x bigger, return 1")
        return 1
    else:
        #print(f"x equal, return 0")
        return 0

def compare_hands(x,y):
    if x['score'] < y['score']:
        return -1
    elif x['score'] > y['score']:
        return 1
    else:
        a = x['cards']
        b = y['cards']
        
        for i in range(len(a)):
            #print()
            #print("comparing hands")
            #print(f"a:{a} b:{b} i:{i}")
            if compare_cards(a[i],b[i]) > 0:
                #print(f"a[i]:{a[i]} b[i]:{b[i]}")
                #print("a is bigger, returning 1")
                return 1
            elif compare_cards(a[i],b[i]) < 0:
                #print(f"a[i]:{a[i]} b[i]:{b[i]}")
                #print("a is smaller, returning -1")
                return -1
    return 0

hands = []
for line in lines:
    hand = {}
    x,y = line.strip().split()
    hand['cards'] = x
    hand['bid'] = y
    count_cards(hand)
    score_hand(hand)
    hands.append(hand)

hands.sort(key=cmp_to_key(compare_hands))


winnings = 0
for i, hand in enumerate(hands):
    winnings += int(hand['bid']) * (i+1)

#put the code here



print(f"Part 1 answer: {winnings}")

def p2_score_hand(hand):
    real_cards = ["2","3","4","5","6","7","8","9","T","Q","K","A"]
    
    max_score = 0
    for card in real_cards:
        new_cards = hand['cards'].replace("1",card)
        new_hand = {}
        new_hand['cards'] = new_cards
        count_cards(new_hand)
        score_hand(new_hand)
        max_score = max(max_score,new_hand['score'])
    hand['score'] = max_score

for hand in hands:
    hand['cards'] = hand['cards'].replace("J","1")

for hand in hands:
    hand['counts'] = {}
    count_cards(hand)
    p2_score_hand(hand)
hands.sort(key=cmp_to_key(compare_hands))

winnings = 0
for i, hand in enumerate(hands):
    winnings += int(hand['bid']) * (i+1)

print(f"Part 2 answer: {winnings}")