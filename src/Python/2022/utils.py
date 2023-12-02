
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
    
