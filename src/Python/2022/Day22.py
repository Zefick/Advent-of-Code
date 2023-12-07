
from utils import Input, printResult

# https://adventofcode.com/2022/day/22

input = Input(2022, 22).lines()

path = input[-1]
input = input[:-2]

w = max(len(s) for s in input) + 2
h = len(input) + 2

for i in range(h-2):
    input[i] = ' ' + input[i]

input = [' ' * w] + input + [' ' * w]
for i in range(h):
    if len(input[i]) < w:
        input[i] += (' ' * (w - len(input[i])))

y = 1
x = 1
while input[y][x] == ' ':
    x += 1
    
steps = []
n = 0
for c in path:
    if '0' <= c <= '9':
        n = n * 10 + int(c)
    else:
        steps.append(n)
        steps.append(c)
        n = 0
steps.append(n)

face = (1, 0)

for s in steps:
    if s == 'R':
        face = (-face[1], face[0])
    elif s == 'L':
        face = (face[1], -face[0])
    else:
        for i in range(int(s)):
            x2, y2 = x + face[0], y + face[1]
            if input[y2][x2] == ' ':
                while True:
                    x2, y2 = x2 - face[0], y2 - face[1]
                    if input[y2][x2] == ' ':
                        x2, y2 = x2 + face[0], y2 + face[1]
                        break
            if input[y2][x2] == '#':
                break
            x, y = x2, y2

facing = {(1, 0): 0, (0, 1): 1, (-1, 0): 2, (0, -1): 3}

printResult(1, y * 1000 + x * 4 + facing[(face)])

# part2

y = 1
x = 1
while input[y][x] == ' ':
    x += 1

face = (1, 0)

for s in steps:
    if s == 'R':
        face = (-face[1], face[0])
    elif s == 'L':
        face = (face[1], -face[0])
    else:
        for i in range(int(s)):
            x2, y2 = x + face[0], y + face[1]
            if input[y2][x2] == ' ':
                prev_face = face
                
                if y2 == 0 and x2 <= 100:
                    x2, y2 = 1, x2 + 100
                    face = (1, 0)
                elif x2 == 0 and y2 > 150:
                    x2, y2 = y2 - 100, 1
                    face = (0, 1)
                    
                elif y2 == 0 and x2 > 100:
                    x2, y2 = x2 - 100, 201
                    face = (0, -1)
                elif y2 == 201:
                    x2, y2 = x2 + 100, 1
                    face = (0, 1)
                    
                elif x2 == 50 and y2 <= 50:
                    x2, y2 = 1, 151 - y2
                    face = (1, 0)
                elif x2 == 0 and y <= 150:
                    x2, y2 = 51, 151 - y2
                    face = (1, 0)
                    
                elif x2 == 50 and y2 > 50:
                    x2, y2 = y2 - 50, 101
                    face = (0, 1)
                elif x2 <= 50 and y2 == 100:
                    x2, y2 = 51, x2 + 50
                    face = (1, 0)
                    
                elif x2 == 51 and y2 > 150:
                    x2, y2 = y2 - 100, 150
                    face = (0, -1)
                elif x2 > 50 and y2 == 151:
                    x2, y2 = 50, x2 + 100
                    face = (-1, 0)
                    
                elif x2 == 101 and y2 > 100:
                    x2, y2 = 150, 151 - y2
                    face = (-1, 0)
                elif x2 == 151:
                    x2, y2 = 100, 151 - y2
                    face = (-1, 0)
                    
                elif x2 == 101 and y2 <= 100:
                    x2, y2 = y2 + 50, 50
                    face = (0, -1)
                elif x2 > 100 and y2 == 51:
                    x2, y2 = 100, x2 - 50
                    face = (-1, 0)
                else:
                    ...
                    
                if input[y2][x2] == '#':
                    face = prev_face

            if input[y2][x2] == '#':
                break
            x, y = x2, y2

printResult(2, y * 1000 + x * 4 + facing[(face)])
