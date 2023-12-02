
from utils import Input, printResult

# https://adventofcode.com/2022/day/17

input = Input(2022, 17).lines()[0]

shapes = [
    ((0, 0), (0, 1), (0, 2), (0, 3)),
    ((0, 1), (1, 0), (1, 1), (1, 2), (2, 1)),
    ((0, 0), (0, 1), (0, 2), (1, 2), (2, 2)),
    ((0, 0), (1, 0), (2, 0), (3, 0)),
    ((0, 0), (0, 1), (1, 0), (1, 1))
]

jet = input
jet_len = len(jet)

chamber = set([(0, x) for x in range(7)])

def move(rock, dx, dy):
    return tuple((y+dy, x+dx) for y, x in rock)

h, j = 0, 0

def fall(rock):
    global j, h, chamber
    rock = move(rock, 2, h + 4)
    while True:
        rock2 = move(rock, -1 if jet[j] == '<' else 1, 0)
        j = (j + 1) % jet_len
        if any(x < 0 or x >=7 for (_, x) in rock2) or any(r in chamber for r in rock2):
            rock2 = rock
        rock3 = move(rock2, 0, -1)
        if any(r in chamber for r in rock3):
            chamber |= set(rock2)
            h = max(h, max(y for (y, _) in rock2))
            break
        rock = rock3
    

for i in range(2022):
    fall(shapes[i % 5])

printResult(1, h)

n = 1000000000000
mem_j = j
loop_i = i
loop_h = h
while True:
    # let rocks fall in groups of 5
    for _ in range(5):
        i += 1
        fall(shapes[i % 5])
    # detecting a loop
    if j == mem_j:
        # length of the rocks cycle
        cycle = i - loop_i
        # number of full cycles until the end from the current moment
        cycles = (n - i) // cycle
        # how taller the tower of rocks will become
        dh = (h - loop_h) * cycles
        # how many rocks must fall after the last cycle
        rem = (n - i) % cycle
        break

for i in range(i + 1, i + rem):
    fall(shapes[i % 5])
    
printResult(2, h + dh)
