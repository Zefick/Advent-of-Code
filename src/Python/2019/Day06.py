
from utils import Input, printResult

# https://adventofcode.com/2019/day/6

input = Input(2019, 6).lines()
orbits = dict(reversed(x.split(")")) for x in input)

def getOrbits(x):
    while x in orbits:
        x = orbits[x]
        yield x

printResult(1, sum(1 for obj in orbits for _  in getOrbits(obj)))
printResult(2, len(set(getOrbits("YOU")) ^ set(getOrbits("SAN"))))
