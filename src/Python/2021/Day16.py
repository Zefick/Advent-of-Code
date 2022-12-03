
import math
from utils import Input, printResult

# https://adventofcode.com/2021/day/16

input = Input(2021, 16).lines()[0]
input = "".join(bin(int(c, 16))[2:].zfill(4) for c in input)

def readPacket(i):
    global s
    s += int(input[i:i+3], 2)
    T = input[i+3:i+6]
    if T == '100':
        j = i + 6
        bits = ""
        while True:
            bits += input[j+1:j+5]
            if input[j] == '0':
                break
            j += 5
        bits = int(bits, 2)
        return (j + 5, bits)
    else:
        subs = []
        if input[i+6] == '0':
            j = i + 22
            l = j + int(input[i+7:j], 2)
            while j < l:
                j, a = readPacket(j)
                subs.append(a)
        else:
            j = i + 18
            l = int(input[i+7:j], 2)
            for _ in range(l):
                j, a = readPacket(j)
                subs.append(a)
        if T == '000':
            return j, sum( subs)
        elif T == '001':
            return j, math.prod(subs)
        elif T == '010':
            return j, min(subs)
        elif T == '011':
            return j, max(subs)
        elif T == '101':
            return j, (subs[0] > subs[1])
        elif T == '110':
            return j, (subs[0] < subs[1])
        elif T == '111':
            return j, (subs[0] == subs[1])

s = 0
j, x = readPacket(0)

printResult(1, s)
printResult(2, x)
