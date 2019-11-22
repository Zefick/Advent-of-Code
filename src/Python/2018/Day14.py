
from utils import printResult

# https://adventofcode.com/2018/day/14

inputStr = "290431"
input = int(inputStr)
recipes = "37"
elf1, elf2 = 0, 1
inputLen = len(inputStr)
part1 = False

while True:
    s = str(int(recipes[elf1]) + int(recipes[elf2]))
    recipes += s
    elf1 = (elf1 + int(recipes[elf1]) + 1) % len(recipes)
    elf2 = (elf2 + int(recipes[elf2]) + 1) % len(recipes)

    if not part1 and len(recipes) >= input + 10:
        printResult(1, recipes[input:input+10])
        part1 = True
    
    if part1:
        for i in range(len(s)):
            j = len(recipes) - inputLen - i
            scores = recipes[j:j+inputLen]
            if scores == inputStr:
                printResult(2, j)
                exit()
