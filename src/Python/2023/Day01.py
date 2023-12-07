
from utils import Input, printResult

# https://adventofcode.com/2023/day/1

input = Input(2023, 1).lines()

dict = {str(i): i for i in range(1, 10)}

def find(line, order):
    for i in order:
        for s, d in dict.items():
            if line[i:i+len(s)] == s:
                return d

def calibrate():
    return sum(find(s, range(len(s))) * 10 + \
               find(s, range(len(s)-1, -1, -1)) for s in input)

printResult(1, calibrate())

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
dict.update({digits[i-1]: i for i in range(1, 10)})

printResult(2, calibrate())
