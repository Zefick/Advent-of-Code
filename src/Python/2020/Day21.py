
from utils import Input, printResult
import re

# https://adventofcode.com/2020/day/21

input = Input(2020, 21).match("(.*) \\(contains (.*)\\)$")

ingredients = set()
allergens = set()
recipes = []

for m in input:
    ings, alls = set(m[1].split()), set(m[2].split(", "))
    ingredients |= ings
    allergens |= alls
    recipes.append((ings, alls))

def can_contain(ingredient, allergen):
    return not any(allergen in alls and ingredient not in ings for (ings, alls) in recipes)

inert = [i for i in ingredients 
    if not any(can_contain(i, al) for al in allergens)]

printResult(1, sum(sum(1 for i in inert if i in ings) for ings, _ in recipes))

dangerous = ingredients.difference(inert)

for ings, _ in recipes:
    for i in inert:
        if i in ings:
            ings.remove(i)

possibles = {
    ing: [a for a in allergens if can_contain(ing, a)]
    for ing in dangerous
}

while any(len(v) > 1 for v in possibles.values()):
    singles = [list(v)[0] for k, v in possibles.items() if len(v) == 1]
    for s in singles:
        for v in possibles.values():
            if len(v) > 1 and s in v:
                v.remove(s)

possibles = ",".join(map(lambda x: x[0], sorted(possibles.items(), key = lambda x: list(x[1])[0])))
printResult(2, possibles)
