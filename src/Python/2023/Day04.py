
from utils import Input, printResult

# https://adventofcode.com/2023/day/4

input = Input(2023, 4).lines()
n = len(input)

def score_card(card: str) -> int:
    card = card.split(":")
    n1, n2 = card[1].split(" |")
    n1 = set(n1[i:i+3] for i in range(0, len(n1), 3))
    n2 = set(n2[i:i+3] for i in range(0, len(n2), 3))
    return len(n1 & n2)

scores = list(map(score_card, input))
printResult(1, sum(1 << scores[i] >> 1 for i in range(n)))

winners = [1] * n
for i in range(n-2, -1, -1):
    winners[i] = 1 + sum(winners[i+1:i+scores[i]+1])

printResult(2, sum(winners))
