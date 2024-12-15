
from utils import Input, printResult

# https://adventofcode.com/2024/day/14

input = Input(2024, 14).match("p=(\d+),(\d+) v=(-?\d+),(-?\d+)")
robots =[list(map(int, [m.group(i+1) for i in range(4)])) for m in input]
w, h = 101, 103

for i in range(1, w * h):
    pos = set()
    for r in robots:
        r[0] = (r[0] + r[2]) % w
        r[1] = (r[1] + r[3]) % h
        pos.add((r[0], r[1]))

    if i == 100:
        qudrants = [0] * 4
        for r in robots:
            if r[0] != w // 2 and r[1] != h // 2:
                n = (r[0] > (w // 2)) + (r[1] > (h // 2)) * 2
                qudrants[n] += 1
        part1 = 1
        for q in qudrants:
            part1 *= q

    # count the number of robots that are adjacent to each other
    m = sum(((r[0]-1, r[1]) in pos or (r[0]+1, r[1]) in pos or \
            (r[0], r[1]-1) in pos or (r[0], r[1]+1) in pos for r in robots))
    if m > 300:
        canvas = [[' '] * w for _ in range(h)]
        for r in robots:
            canvas[r[1]][r[0]] = '#'
        print("\n".join("".join(line) for line in canvas))
        part2 = i

printResult(1, part1)
printResult(2, part2)
