
from utils import Input, printResult
from functools import reduce

# https://adventofcode.com/2024/day/14

input = Input(2024, 14).match("p=(\d+),(\d+) v=(-?\d+),(-?\d+)")
robots =[list(map(int, [m.group(i+1) for i in range(4)])) for m in input]
w, h = 101, 103

def get_positions(i):
    return (((r[0] + r[2] * i) % w, \
             (r[1] + r[3] * i) % h) for r in robots)

quadrants = [0] * 4
for x, y in get_positions(100):
    if x != w // 2 and y != h // 2:
        n = (x > (w // 2)) + (y > (h // 2)) * 2
        quadrants[n] += 1
part1 = reduce(int.__mul__, quadrants, 1)

def display(positions):
    tiles = " ▀▄█"
    for y in range(0, h+1, 2):
        line = []
        for x in range(w):
            n = ((x, y) in positions) + ((x, y+1) in positions) * 2
            line.append(tiles[n])
        print("".join(line))

for i in range(1, w * h):
    # count the number of robots that are adjacent to each other
    pos = set(get_positions(i))
    m = sum(((x-1, y) in pos or (x+1, y) in pos or \
             (x, y-1) in pos or (x, y+1) in pos for (x, y) in pos))
    if m > 300:
        display(pos)
        part2 = i
        break

printResult(1, part1)
printResult(2, part2)
