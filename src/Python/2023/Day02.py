
from utils import Input, printResult
from collections import defaultdict

# https://adventofcode.com/2023/day/2

input = Input(2023, 2).lines()

possible = 0
powersum = 0
limits = {"red": 12, "green": 13, "blue": 14}

for s in input:
    game, sets = s.split(": ")
    game = int(game[5:])
    maximums = defaultdict(int)
    for set in sets.split("; "):
        for color in set.split(", "):
            color = color.split(" ")
            n = int(color[0])
            maximums[color[1]] = max(maximums[color[1]], n)
    powersum += maximums["red"] * maximums["green"] * maximums["blue"]
    if all(n <= limits[c] for (c, n) in maximums.items()):
        possible += game
 
printResult(1, possible)
printResult(2, powersum)
