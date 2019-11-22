
from utils import Input, printResult
import copy
import re

# https://adventofcode.com/2018/day/24

class Group:

    def __init__(self, f, u, hp, init, immune, weak, atk, pwr):
        self.faction, self.initiative = f, init
        self.units, self.hp = u, hp
        self.immune, self.weak = immune, weak
        self.attack, self.power = atk, pwr
    
    def effectivePower(self, enemy):
        return self.units * self.power * (2 if self.attack in enemy.weak else 1)

def simulate(groups, boost):
    groups = copy.deepcopy(groups)
    faction = None
    for g in groups:
        if g.faction:
            g.power += boost
    for t in range(10000):
        targets = dict()
        groups = sorted(groups, key = lambda g: (-g.units * g.power, -g.initiative))
        # select targets
        for g in groups:
            groups2 = list(filter(lambda g2: g.faction != g2.faction and g.attack not in g2.immune and g2 not in targets.values(), groups))
            if len(groups2) > 0:
                targets[g] = max(groups2, key = lambda g2: (g.effectivePower(g2), g2.units * g2.power, g2.initiative))
        # attack
        for g in sorted(targets.keys(), key = lambda g: -g.initiative):
            if g.units > 0:
                g2 = targets[g]
                g2.units -= g.effectivePower(g2) // g2.hp
        # check results
        groups = list(filter(lambda g: g.units > 0, groups))
        if all(g.faction for g in groups) or all(not g.faction for g in groups):
            faction = groups[0].faction
            break
    result = "boost %d: time %d, %s, %d" % (boost, t, faction, sum(g.units for g in groups))
    return (faction, result)

input = Input(2018, 24).lines()
pattern = re.compile("(\\d+) units each with (\\d+) hit points " # 1, 2
            + "(\\((\\w+) to ([a-z, ]+)(; (\\w+) to ([a-z, ]+))?\\) )?"  # (3 (4 5) (6 (7 8))))
            + "with an attack that does (\\d+) (\\w+) damage at initiative (\\d+)")  # 9, 10, 11

groups = []
faction = True
for s in input:
    if s.startswith("Infection:"):
        faction = False
    m = pattern.match(s)
    if m:
        units, hp = int(m[1]), int(m[2])
        immune, weak = "", ""
        pwr, atk, init = int(m[9]), m[10], int(m[11]),
        for g in [4, 7]:
            if m[g] == "immune":
                immune = m[g+1]
            elif m[g]:
                weak = m[g+1]
        groups.append(Group(faction, units, hp, init, immune, weak, atk, pwr))

import time
tm = time.time()

if False:
    # sequencial search
    results = []
    faction = False
    boost = 0
    while not faction:
        faction, result = simulate(groups, boost)
        results.append(result)
        print(result)
        boost += 1

    printResult(1, results[0])
    printResult(2, results[-1])

else:
    # binary search
    minBoost = 0
    maxBoost = 1000
    while True:
        boost = (maxBoost + minBoost) // 2
        faction, result = simulate(groups, boost)
        print(result)
        if faction:
            maxBoost = boost
        else:
            minBoost = boost
        if maxBoost - minBoost <= 1:
            break

print(time.time() - tm)
