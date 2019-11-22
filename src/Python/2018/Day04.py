
import itertools
import re
import datetime
from utils import Input, printResult

# https://adventofcode.com/2018/day/4

lines = Input(2018, 4).match(\
        "\\[(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2})\\] "
     + "((Guard #(\\d+) begins shift)|(falls asleep)|(wakes up))")
entries = []
for m in lines:
    time = datetime.datetime(int(m[1]), int(m[2]), int(m[3]), int(m[4]), int(m[5]))
    guard = None
    if m[7]:
        guard = int(m[8])
        action = "SHIFT"
    elif m[9]:
        action = "FALL"
    else:
        action = "WAKEUP"
    entries.append((time, guard, action))

entries.sort(key = lambda x: x[0])
minutes = {}
for e in entries:
    if e[2] == "SHIFT":
        guard = e[1]
    elif e[2] == "FALL":
        lasttime = e[0].minute
        if guard not in minutes:
            minutes[guard] = [0] * 60
    else:
        mas = minutes[guard]
        for m in range(lasttime, e[0].minute):
            mas[m] += 1

guard = max(minutes, key = lambda g: sum(minutes[g]))
minute = minutes[guard].index(max(minutes[guard]))
printResult(1, guard * minute)

maxIndex = 0
mMax = 0
for g in minutes:
    mas = minutes[g]
    idx = mas.index(max(mas))
    if mas[idx] > mMax:
        mMax = mas[idx]
        maxIndex = idx
        guard = g
printResult(2, guard * maxIndex)
