
from utils import Input, printResult
from intcode import Intcode

# https://adventofcode.com/2019/day/15

def printScreen(screen):
    minx = min(p[0] for p in screen)
    maxx = max(p[0] for p in screen)
    miny = min(p[1] for p in screen)
    maxy = max(p[1] for p in screen)
    palette = {0: "  ", 1: "[]", 2: "* ", 3:"+ "}
    image = ""
    for y in range(miny, maxy+1):
        image += "\n" + "".join(
            palette[screen.get((x, y), 1)]
            for x in range(minx, maxx+1))
    print(image)

dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
def move(p, dir):
    return (p[0] + dirs[dir][0], p[1] + dirs[dir][1])

class Robot:

    def __init__(self, intcode):
        self.position = (0, 0)
        self.intcode = intcode
        self.output = self.intcode.run()

    def scan(self):
        ''' explore nearest squares but stand still after that '''
        global goal
        for i in range(4):
            self.intcode.put_input(i+1)
            answer = next(self.output)
            p2 = move(self.position, i)
            if answer == 0:
                field[p2] = 1
            else:
                field[p2] = 0
                if answer == 2:
                    goal = p2
                # step back
                self.intcode.put_input({0: 2, 1: 1, 2:4, 3:3}[i])
                next(self.output)

    def move(self, dir):
        ''' move to an adjacent cell in dir direction.
            It implies that the cell is empty'''
        self.intcode.put_input(dir + 1)
        next(self.output)
        self.position = move(self.position, dir)

deadCells = set()
visitedCells = set()
field = {(0, 0): 0}
goal = None
robot = Robot(Intcode(Input(2019, 15).lines()[0]))

while True:
    robot.scan()
    moves = [(dir, move(robot.position, dir)) for dir in range(4)]
    moves = [m for m in moves if field[m[1]] == 0 and m[1] not in deadCells]
    if len(moves) == 0:
        break
    if len(moves) == 1:
        deadCells.add(robot.position)
    robot.move(min(moves, key = lambda m: m[1] in visitedCells)[0])
    visitedCells.add(robot.position)

field[goal] = 2
field[(0, 0)] = 3
printScreen(field)

from pathfinder import Pathfinder2D

pf = Pathfinder2D(lambda p: field.get(p, 0) != 1)
printResult(1, pf.run((0, 0), lambda p: p == goal)[1])

pf.run(goal)
printResult(2, max(pf.get_visited().values()))

