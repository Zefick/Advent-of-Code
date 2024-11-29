
from utils import Input, printResult
from collections import defaultdict, deque
from typing import Optional

# https://adventofcode.com/2023/day/20

input = list(Input(2023, 20).lines())

class Module:
    def __init__(self, outputs) -> None:
        self.outputs = outputs
        self.result = None

class FlipFlop (Module) :
    def __init__(self, outputs) -> None:
        Module.__init__(self, outputs)
        self.state = 0

    def send(self, name, signal) -> Optional[int]:
        if signal == 0:
            self.state = 1 - self.state
            return self.state
        else:
            return None

class Conjunction (Module):
    def __init__(self, outputs) -> None:
        Module.__init__(self, outputs)
        self.inputs = {}

    def add_input(self, name):
        self.inputs[name] = 0

    def send(self, src, signal):
        self.inputs[src] = signal
        return int(not all(self.inputs.values()))

mods = {}

for line in input:
    name, src = line.split(" -> ")
    outputs = src.split(", ")
    if name[0] == '%':
        mods[name[1:]] = FlipFlop(outputs)
    elif name[0] == '&':
        mods[name[1:]] = Conjunction(outputs)
    else:
        broadcast = src.split(', ')

for name, mod in mods.items():
    for o in mod.outputs:
        if o in mods and type(mods[o]) == Conjunction:
            mods[o].add_input(name)

cycles = set()
part2 = 1
dst = next(name for name, mod in mods.items() if mod.outputs[0] == 'rx')
counts = [0, 0]
    
for t in range(1, 10000):
    q = deque()
    counts[0] += 1
    for mod in broadcast:
        q.append((mod, 'broadcaster', 0))
    while q:
        mod_name, src, sig = q.popleft()
        counts[sig] += 1
        if mod_name not in mods:
            continue
        if mod_name == dst and sig == 1:
            if src not in cycles:
                part2 *= t
                cycles.add(src)
        mod = mods[mod_name]
        res = mod.send(src, sig)
        if res is not None:
            for o in mod.outputs:
                q.append((o, mod_name, res))
    if t == 1000:
        printResult(1, counts[0] * counts[1])
    if len(cycles) == 4:
        printResult(2, part2)
        break
