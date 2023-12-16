
from utils import Input, printResult

# https://adventofcode.com/2023/day/9

input = [list(map(int, s.split())) for s in Input(2023, 9).lines()]

def predict(h):
    if all(x == h[0] for x in h):
        return h[0], h[0]
    else:
        diffs = [h[i+1] - h[i] for i in range(len(h)-1)]
        d1, d2 = predict(diffs)
        return h[0] - d1, h[-1] + d2
    
results = list(map(predict, input))

printResult(1, sum(x[1] for x in results))
printResult(2, sum(x[0] for x in results))
