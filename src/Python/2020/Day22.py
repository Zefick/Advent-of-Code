
from utils import Input, printResult
import re

# https://adventofcode.com/2020/day/22

input = Input(2020, 22).match("^\\d+")

deck = [int(m[0]) for m in input if m]

deck1 = deck[:len(deck)//2]
deck2 = deck[len(deck)//2:]

def play(deck1, deck2, recursion):
    cache = []
    while len(deck1) > 0 and len(deck2) > 0:
        if deck1 in cache:
            return (1, [])
        else:
            cache.append(deck1.copy())
        a, b = deck1.pop(0), deck2.pop(0)

        if recursion and len(deck1) >= a and len(deck2) >= b:
            winner = play(deck1[:a], deck2[:b], True)[0]
        else:
            winner = 1 if a > b else 2

        if winner == 1:
            deck1 += [a, b]
        else:
            deck2 += [b, a]
    winner = 1 if len(deck2) == 0 else 2
    return (winner, deck1 + deck2)

def scores(deck):
    n = len(deck)
    return sum((n - i) * deck[i] for i in range(n))

deck = play(deck1.copy(), deck2.copy(), False)[1]
printResult(1, scores(deck))

deck = play(deck1.copy(), deck2.copy(), True)[1]
printResult(2, scores(deck))
