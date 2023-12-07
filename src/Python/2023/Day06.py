
from utils import printResult

# https://adventofcode.com/2023/day/6

input = ["7 15 30", "9 40 200"]

time = list(map(int, input[0].split()))
distance = list(map(int, input[1].split()))

res1 = 1
for i in range(len(time)):
    for j in range(time[i]):
        if j * (time[i] - j) > distance[i]:
            res1 *= time[i] - j * 2 + 1
            break
            
printResult(1, res1)

time = int(input[0].replace(" ", ""))
distance = int(input[1].replace(" ", ""))

# solving t^2 - t * time + distange < 0

import math
D = math.sqrt(time * time - 4 * distance)
t1 = (time - D) / 2
t2 = (time + D) / 2

printResult(2, int(math.floor(t2)) - int(math.ceil(t1)) + 1)
