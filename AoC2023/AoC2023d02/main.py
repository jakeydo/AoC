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

games = {}

for line in lines:
    line = line.strip()
    gid, handfuls = line.split(':')
    gid = gid.split(' ')[1]
    handfuls = handfuls.split(';')
    final_handfuls = []
    for h in handfuls:
        final_h = {"red":0,"green":0,"blue":0}
        colors = h.split(',')
        for c in colors:
            c.strip();
            number, color = c.split()
            final_h[color] = int(number)
        final_handfuls.append(final_h)
    games[gid] = final_handfuls

test = {"red":12,"green":13,"blue":14}

possible_games = []
for game in games:
    possible = True
    handfuls = games[game]
    for h in handfuls:
        if h["red"] > test["red"] or h["green"] > test["green"] or h["blue"] > test["blue"]:
            possible = False
    if possible:
        possible_games.append(int(game))

print(f"Part 1 answer: {sum(possible_games)}")

game_powers = []

for game in games:
    min_cubes_needed = {"red":0,"green":0,"blue":0}
    handfuls = games[game]
    for h in handfuls:
        min_cubes_needed["red"] = max(min_cubes_needed["red"],h["red"])
        min_cubes_needed["green"] = max(min_cubes_needed["green"],h["green"])
        min_cubes_needed["blue"] = max(min_cubes_needed["blue"],h["blue"])
    game_powers.append(min_cubes_needed["red"]*min_cubes_needed["green"]*min_cubes_needed["blue"])
    


print(f"Part 2 answer: {sum(game_powers)}")