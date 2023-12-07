
class Input:

    def __init__(self, year, day) :
        self.file = "input/%d/input%02d.txt" % (year, day)

    def lines(self) -> list :
        with open(self.file, "r") as f:
            return list(map(str.rstrip, f))

    def match(self, pattern: str) :
        import re
        pattern = re.compile(pattern)
        return map(lambda line: pattern.match(line), self.lines())

def printResult(part, result, time=None):
    print(f"Part {part}: {result}" \
        + ("" if not time else f' ({time:.3f} sec)'))

def neigthbors2d(y: int, x: int, diagonal: bool, limits=None):
    dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]] \
        if diagonal else [[-1, 0], [0, -1], [0, 1], [1, 0]]
    for dy, dx in dirs:
        y2, x2 = y + dy, x + dx
        if limits is None or (limits[0] <= y2 < limits[1] and limits[2] <= x2 < limits[3]):
            yield(y2, x2)
