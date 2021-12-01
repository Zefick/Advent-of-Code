
from utils import Input, printResult
import functools

# https://adventofcode.com/2020/day/20

input = Input(2020, 20).lines()

tiles = {}

for i in range((len(input)+3) // 12):
    j = i*12
    tiles[int(input[j][5:9])] = input[j+1:j+11]

def codify(line):
    return int(line.replace('#', '1').replace('.', '0'), 2)

def variations(tile):
    top1 = codify(tile[0])
    top2 = codify(tile[0][::-1])
    bottom1 = codify(tile[-1])
    bottom2 = codify(tile[-1][::-1])
    right = "".join(map(lambda t: t[-1], tile))
    right1 = codify(right)
    right2 = codify(right[::-1])
    left = "".join(map(lambda t: t[0], tile))
    left1 = codify(left)
    left2 = codify(left[::-1])

    return [
        [top1, right1, bottom1, left1],
        [right1, bottom2, left1, top2],
        [bottom2, left2, top2, right2],
        [left2, top1, right2, bottom1],
        [left1, bottom1, right1, top1],
        [bottom1, right2, top1, left2],
        [right2, top2, left2, bottom2],
        [top2, left1, bottom2, right1]
    ]

def unique(variations):
    return functools.reduce(set.union, variations, set())

orientations = {n: variations(x) for n, x in tiles.items()}
corners = []
for n, x in orientations.items():
    codes = unique(x)
    adj = sum([(1 if len(codes & unique(y)) > 0 else 0) for m, y in orientations.items() if n != m])
    if adj == 2:
        corners.append(n)

printResult(1, str(corners[0] * corners[1] * corners[2] * corners[3]))

##########################################

canvas = [[corners[0], 1]]
N = 12

for y in range(N):
    for x in range(int(y == 0), N):
        prevN, prevOr = canvas[y*N+x-(12 if x == 0 else 1)]
        prev = tiles[prevN]
        sides = variations(prev)[prevOr]
        for n in tiles:
            if n != prevN:
                sides2 = variations(tiles[n])
                if x == 0:
                    newOr = list(filter(lambda x: x[0] == sides[2], sides2))
                else:
                    newOr = list(filter(lambda x: x[3] == sides[1], sides2))
                if newOr:
                    canvas.append([n, sides2.index(newOr[0])])
                    break

def rotateCCW(tile):
    w, h = len(tile[0]), len(tile)
    return ["".join(tile[j][w-i-1] for j in range(h)) for i in range(w)]

def orient(tile, orientation):
    if orientation < 4:
        for _ in range(orientation):
            tile = rotateCCW(tile)
        return tile
    else:
        return orient(tile[::-1], (orientation-1) % 4)

result = [([0] * (N*8)) for _ in range(N*8)]

for k in range(len(canvas)):
    n, ori = canvas[k]
    y = k // N
    x = k % N
    tile = orient(tiles[n], ori)
    for i in range(8):
        result[y*8+i][x*8:(x+1)*8] = tile[i+1][1:-1]

monster = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   "
]

def countMonsters(sea):
    w, h = len(sea[0]), len(sea)
    l = len(monster[0])
    cnt = 0
    for i in range(h-2):
        for j in range(w-l-1):
            cnt += not any(monster[y][x] == '#' and sea[i+y][j+x] != '#' for x in range(l) for y in range(3))
    return cnt

sea = list(map("".join, result))

for ori in range(8):
    m = countMonsters(orient(sea, ori))
    if m > 0:
        printResult(2, "".join(sea).count("#") - m * 15)
