
from utils import Input, printResult

# https://adventofcode.com/2018/day/13

dirs = [[1, 0, 3, 1], [0, 1, 2, 0], [-1, 0, 1, 3], [0, -1, 0, 2]]

class Cart:

    def __init__(self, x, y, dir):
        self.x, self.y = x, y
        self.dir = dir
        self.nextTurn = -1

    def move(self, path):
        if path == "+":
            self.dir = (self.dir + self.nextTurn + 4) % 4
            self.nextTurn = (self.nextTurn + 2) % 3 - 1
        elif path == "/":
            self.dir = dirs[self.dir][2]
        elif path == "\\":
            self.dir = dirs[self.dir][3]
        self.x += dirs[self.dir][0]
        self.y += dirs[self.dir][1]

track = Input(2018, 13).lines()
carts = []
for i in range(len(track)):
    for j in range(len(track[0])):
        c = track[i][j]
        if c == ">": carts.append(Cart(j, i, 0))
        if c == "v": carts.append(Cart(j, i, 1))
        if c == "<": carts.append(Cart(j, i, 2))
        if c == "^": carts.append(Cart(j, i, 3))

cartsToRemove = []
while len(carts) > 1:
    carts.sort(key = lambda c: c.y * 1000 + c.x)
    for c in carts:
        c.move(track[c.y][c.x])
        for c2 in carts:
            if c2 is not c and [c.x, c.y] == [c2.x, c2.y]:
                cartsToRemove.extend([c, c2])
                break
    for c in cartsToRemove:
        if c in carts: carts.remove(c)

printResult(1, ("%d,%d" % (cartsToRemove[0].x, cartsToRemove[0].y)))
printResult(2, ("%d,%d" % (carts[0].x, carts[0].y)))
