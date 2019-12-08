
from utils import Input, printResult

# https://adventofcode.com/2019/day/1

def calc_fuel(mass, rec):
    mass = mass // 3 - 2
    if rec and mass > 8:
        mass += calc_fuel(mass, rec)
    return mass

input = list(map(int, Input(2019, 1).lines()))

printResult(1, sum(map(lambda x: calc_fuel(x, False), input)))
printResult(2, sum(map(lambda x: calc_fuel(x, True), input)))
