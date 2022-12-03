
from utils import Input, printResult
import itertools

# https://adventofcode.com/2021/day/19

input = Input(2021, 19).lines()

scanners = []
for s in input:
    if s[:3] == "---":
        scanner = []
        scanners.append(scanner)
    elif len(s) > 0:
        scanner.append(tuple(map(int, s.split(","))))

def transform(array, basis):
    return list(map(lambda vector: (\
            vector[0]*basis[0][0] + vector[1]*basis[1][0] + vector[2]*basis[2][0] + basis[3][0], \
            vector[0]*basis[0][1] + vector[1]*basis[1][1] + vector[2]*basis[2][1] + basis[3][1], \
            vector[0]*basis[0][2] + vector[1]*basis[1][2] + vector[2]*basis[2][2] + basis[3][2]), array))

axes = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
xyz = []
for k in range(0, 24):
    l = k//4
    x = axes[l]
    y = axes[(l+1+(k%4)+((l+1)%2))%6]
    z = [x[1]*y[2] - x[2]*y[1], -(x[0]*y[2] - y[0]*x[2]), x[0]*y[1] - x[1]*y[0]]
    xyz.append((x, y, z))

''' distances between all combinationa os pairs of respective points in two arrays '''
def distances2(s1, s2) :
    result = {}
    for p1, p2 in itertools.product(s1, s2):
        d = (p1[0]-p2[0], p1[1]-p2[1], p1[2]-p2[2])
        result[d] = result.get(d, 0) + 1
    return result

''' distances between any two points in an array '''
''' if two arrays has 66 or more identical distances then they overlap '''
def distances1(points):
    result = []
    for p1, p2 in itertools.combinations(points, 2):
        vec = (abs(p1[0]-p2[0]), abs(p1[1]-p2[1]), abs(p1[2]-p2[2]))
        result.append(tuple(sorted(vec)))
    return list(sorted(result))

distances = list(map(distances1, scanners))

''' Assuming that all values are unique we can use sets '''
def matched_lines(n, m):
    return len(set(distances[n]) & set(distances[m]))

basis = {0: [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]}
beakons = set(scanners[0])
queue = [0]
while len(queue) > 0:
    i = queue.pop()
    scanner1 = transform(scanners[i], basis[i])
    for j in range(len(scanners)):
        if j in basis or matched_lines(i, j) < 66:
            continue
        found = False
        for k in range(0, 24):
            x, y, z = xyz[k]
            scanner2 = transform(scanners[j], [x, y, z, [0, 0, 0]])
            dir = list(filter(lambda item: item[1] >= 12, distances2(scanner1, scanner2).items()))
            if len(dir) == 0:
                continue
            dx, dy, dz = dir[0][0]
            scanner2 = set(map(lambda b: (b[0]+dx, b[1]+dy, b[2]+dz), scanner2))
            queue.append(j)
            beakons |= scanner2
            found = True
            basis[j] = (x, y, z, (dx, dy, dz))
            # print(i, j, basis[j])
            break

printResult(1, len(beakons))

m = 0
for a in basis.values():
    for b in basis.values():
        m = max(sum(abs(a[3][i]-b[3][i]) for i in range(3)), m)

printResult(2, m)
