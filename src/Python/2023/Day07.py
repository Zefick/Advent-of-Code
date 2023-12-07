
from utils import Input, printResult
from collections import Counter

# https://adventofcode.com/2023/day/7

hands = list(map(str.split, Input(2023, 7).lines()))

def key1(hand):
    s = hand[0].replace("A", "Z").replace("K", "Y").replace("T", "B")
    return (sorted(Counter(s).values(), reverse=True), s)

def key2(hand):
    s = hand[0].replace("A", "Z").replace("K", "Y").replace("T", "B").replace("J", "0")
    if "0" in s and s != "00000":
        s2 = s.replace("0", "")
        cnt = Counter(s2)
        cnt[cnt.most_common()[0][0]] += 5 - len(s2)
    else:
        cnt = Counter(s)
    return (sorted(cnt.values(), reverse=True), s)

def play(hands, keyfunc):
    hands = sorted(hands, key=keyfunc)
    return sum(int(h[1]) * (i+1) for i, h in enumerate(hands))
    
printResult(1, play(hands, key1))
printResult(2, play(hands, key2))
