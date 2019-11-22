
from utils import Input, printResult

# https://adventofcode.com/2018/day/12

state =".....##.####..####...#.####..##.#..##..#####.##.#..#...#.###.###....####.###...##..#...##.#.#...##.##"
notes = dict(s.strip().split(" => ") for s in Input(2018, 12).lines())

def count(state):
    return sum(i-5 for i in range(len(state)) if state[i] == "#")

for i in range(1, 10000):
    prevState = state
    state = "..." + state + "...."
    state = "".join([notes[state[n:n+5]] for n in range(len(state)-4)])
    state = state[1:].rstrip(".")
    if i == 20:
        printResult(1, count(state))
    if state == "." + prevState:
        n = state.count("#")
        printResult(2, (5 * 10**10 - i) * n + count(state))
        break
