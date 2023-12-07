
from utils import Input, printResult, neigthbors2d

# https://adventofcode.com/2023/day/3

input = Input(2023, 3).lines()
input = ['.' + line + '.' for line in input]

w, h = len(input[0]), len(input)
            
def getnum(y, x):
    end = x
    while input[y][end-1].isdigit():
        end -= 1
    return (y, end)

def parsenum(y, x):
    end = x
    while input[y][end].isdigit():
        end += 1
    return int(input[y][x:end])

part2 = 0
all_nums = set()
for y in range(h):
    for x in range(w):
        if input[y][x].isdigit() or input[y][x] == '.':
            continue
        adj_nums = set()
        for y2, x2 in neigthbors2d(y, x, True, limits=[0, h, 0, w]):
            if input[y2][x2].isdigit():
                adj_nums.add(getnum(y2, x2))
        all_nums.update(adj_nums)
        if (input[y][x] == '*') and len(adj_nums) == 2:
            m = 1
            for pt in adj_nums:
                m *= parsenum(*pt)   
            part2 += m 

printResult(1, sum(parsenum(*pt) for pt in all_nums))
printResult(2, part2)
