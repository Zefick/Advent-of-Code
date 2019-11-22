
from utils import Input, printResult

# https://adventofcode.com/2018/day/23

class Region:

    def __init__(self, x, y, z, r, bots):
        self.x = x
        self.y = y
        self.z = z
        self.r = r
        self.bots = sum(1 for _ in filter(self.contains, bots))

    def contains(self, bot):
        return bot[3] >= \
                max(self.x - bot[0], 0) + max(bot[0] - self.x - self.r, 0) \
              + max(self.y - bot[1], 0) + max(bot[1] - self.y - self.r, 0) \
              + max(self.z - bot[2], 0) + max(bot[2] - self.z - self.r, 0) \

    def __lt__(self, other):
        if self.bots != other.bots: return self.bots < reg.bots
        if self.r != other.r: return other.r < self.r
        return self.x + self.y + self.z < other.x + other.y + other.z

bots = []
for m in Input(2018, 23).match("pos=<(.+),(.+),(.+)>, r=(.+)"):
    bots.append((int(m[1]), int(m[2]), int(m[3]), int(m[4])))

maxBot = max(bots, key = lambda b: b[3])
pred = lambda b: abs(b[0]-maxBot[0]) + abs(b[1]-maxBot[1]) + abs(b[2]-maxBot[2]) <= maxBot[3]
part1 = sum(1 for _ in filter(pred, bots))
printResult(1, part1)

xMin = min(bots, key = lambda b: b[0])[0]
xMax = max(bots, key = lambda b: b[0])[0]
yMin = min(bots, key = lambda b: b[1])[1]
yMax = max(bots, key = lambda b: b[1])[1]
zMin = min(bots, key = lambda b: b[2])[2]
zMax = max(bots, key = lambda b: b[2])[2]
rMax = max(xMax - xMin, yMax - yMin, zMax - zMin)
R = 1
while R < rMax: R *= 2

regions = [Region((xMax + xMin - R) / 2, (yMax + yMin - R) / 2, (zMax + zMin - R) / 2, R, bots)]
for boxes in range(1000):
    regions.sort()
    reg = regions.pop()
    if reg.r == 0:
        printResult(2, int(reg.x + reg.y + reg.z))
        print("%d bots, %d boxes scanned" % (reg.bots, boxes))
        break
    r = reg.r // 2
    for i in range(8):
        regions.append(Region(reg.x + r*(i&1), reg.y + r*(i//2&1), reg.z + r*(i//4&1), r, bots))
