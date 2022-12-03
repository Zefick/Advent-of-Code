
from utils import Input, printResult

# https://adventofcode.com/2021/day/4

input = Input(2021, 4).lines()

n = len(input) // 6
boards = []

# read boards
for j in range(n):
    board = []
    for i in range(5):
        board += list(map(int, input[j*6 + i + 2].split()))
    boards.append(board)

wins = [False] * n
scores = []
arr = map(int, input[0].split(","))

# scoring
for x in arr:
    for i in range(n):
        if wins[i]:
            continue
        board = boards[i]
        for j in range(25):
            if board[j] == x:
                board[j] = "#"
                row, col = j // 5, j % 5
                if board[row*5:row*5+5] == ['#'] * 5 or board[col::5] == ['#'] * 5:
                    s = sum(x for x in board if x != '#') * x
                    scores.append(s)
                    wins[i] = True
    
printResult(1, scores[0])
printResult(2, scores[-1])
