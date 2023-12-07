
from utils import Input, printResult
import re

# https://adventofcode.com/2023/day/5

input = Input(2023, 5).lines()
seeds = list(map(int, input[0][7:].split(" ")))

maps = []
for line in input[2:]:
    if line:
        if line[0].isalpha():
            maps.append([])
        else:
            dst, src, ln = list(map(int, line.split(" ")))
            maps[-1].append((src, ln, dst))
        
for m in maps:
    m.sort()

def get_location1(seed):
    value = seed
    for transition in maps:
        for a, b, c in transition:
            if a <= value < a + b:
                value += c - a
                break
    return value

printResult(1, min(map(get_location1, seeds)))

def get_location2(input_range):
    ranges = [input_range]
    for transition in maps:
        next_ranges = []
        for first, last in ranges:
            if first > transition[-1][0] + transition[-1][1]:
                next_ranges.append((first, last))
                continue
            for src, ln, dst in transition:
                end = src + ln
                if src >= first:
                    if (src >= last):
                        next_ranges.append((first, last))
                        break
                    else:
                        if src > first:
                            next_ranges.append((first, src))
                        if end < last:
                            next_ranges.append((dst, dst + ln))
                            first = end
                        else:
                            next_ranges.append((dst, dst + (last - src)))
                            break
                else:
                    if end >= first:
                        if end >= last:
                            next_ranges.append((dst + (first - src), dst + last - src))
                            break
                        else:
                            next_ranges.append((dst + (first - src), dst + ln))
                            first = end
        ranges = next_ranges
    return min(r[0] for r in ranges)


min_loc = float('inf')
for i in range(0, len(seeds), 2):
    dst, src = seeds[i:i+2]
    min_loc = min(min_loc, get_location2([dst, dst+src]))

printResult(2, min_loc)
