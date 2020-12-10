
from utils import Input, printResult
from intcode import Intcode
from collections import deque

# https://adventofcode.com/2019/day/23

input = Input(2019, 23).lines()[0]

nodes = [Intcode(input, [i, -1]) for i in range(50)]
outs = [nodes[i].run() for i in range(50)]
NAT = None
idle = [False] * 50
prev_NAT_y = None

def sendPacket(addr, x, y):
    nodes[addr].put_input(x)
    nodes[addr].put_input(y)
    idle[addr] = False

while True:
    if all(idle):
        if prev_NAT_y == NAT[1]:
            printResult(2, y)
            break
        sendPacket(0, *NAT)
        prev_NAT_y = NAT[1]
    # select any non idle node (it is assumed that there is at least one of them)
    i = next(filter(lambda i: not idle[i], range(50)))
    addr = next(outs[i], None)
    if addr == "wait":
        idle[i] = True
    else:
        x, y = next(outs[i]), next(outs[i])
        if addr < 50:
            sendPacket(addr, x, y)
        if addr == 255:
            if NAT is None:
                printResult(1, y)
            NAT = [x, y]
