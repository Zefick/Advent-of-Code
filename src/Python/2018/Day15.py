
# https://adventofcode.com/2018/day/15

class Unit:
    def __init__(self, x, y, type):
        self.x, self.y = x, y
        self.hp = 200
        self.type = type

    def opposite(self):
        return "E" if self.type == "G" else "G"

dirs = [[0, -1], [-1, 0], [1, 0], [0, 1]]

def wave(field, predicate, start):
    points = [start]
    visited = set()
    while len(points) > 0:
        nextPoints = []
        for p in sorted(points, key = lambda p: p[1] * 100 + p[0]):
            for dir in dirs:
                p2 = (p[0] + dir[0], p[1] + dir[1])
                if p2 in visited:
                    continue
                if predicate(p2):
                    return p
                if field[p2[1]][p2[0]] == ".":
                    nextPoints.append(p2)
                    visited.add(p2)
        points = nextPoints

def simulate(field, power):
    t = 0
    units = []
    # collect units
    for y in range(len(field)):
        for x in range(len(field[y])):
            if field[y][x] == "E" or field[y][x] == "G":
                units.append(Unit(x, y, field[y][x]))
    # simulate the buttle
    end = False
    while not end:
        end = True
        units.sort(key = lambda u: u.y*1000 + u.x)
        for u in units:
            if u.hp <= 0: continue
            # finding a target
            target = wave(field, lambda p: field[p[1]][p[0]] == u.opposite(), (u.x, u.y))
            if not target: continue
            end = False
            # move
            if target != (u.x, u.y):
                target = wave(field, lambda p: (p[0], p[1]) == (u.x, u.y), target)
                field[u.y][u.x] = '.'
                field[target[1]][target[0]] = u.type
                u.x, u.y = target
            # attack
            targets = []
            for dir in dirs:
                if field[u.y + dir[1]][u.x + dir[0]] == u.opposite():
                    targets.append(next(filter(lambda u2: (u2.x, u2.y) == (u.x + dir[0], u.y + dir[1]) and u2.hp > 0, units)))
            if len(targets) > 0:
                u2 = min(targets, key = lambda u: u.hp * 10000 + u.y * 100 + u.x)
                u2.hp -= power if u.type == "E" else 3
                if u2.hp <= 0:
                    field[u2.y][u2.x] = "."
        t += 1
    return (t - 1, units)

from utils import Input, printResult
import copy

results = []
field = list(map(list, Input(2018, 15).lines()))
for power in range(3, 100):
    t, units = simulate(copy.deepcopy(field), power)
    sumHP = sum(u.hp for u in units if u.hp > 0)
    results.append("power = %d, %d * %d = %d" % (power, t-1, sumHP, (t-1) * sumHP))
    # All elves are alife
    if not any(u.type == "E" and u.hp <= 0 for u in units):
        break

printResult(1, results[0])
printResult(2, results[-1])
