
class Input:

    def __init__(self, year, day) :
        self.file = "../../../input/%d/input%02d.txt" % (year, day)

    def lines(self) -> list :
        f = open(self.file, "r")
        lines = list(map(str.rstrip, f))
        f.close()
        return lines

    def match(self, pattern: str) :
        import re
        pattern = re.compile(pattern)
        return map(lambda line: pattern.match(line), self.lines())

def printResult(part, result):
    print("Part %d: %s" % (part, result))
