"""
Дан многомерный список в котором находится результат игры в крестики нолики,
выяснить какой игрок победил (x или o), если никто не победил вывести "Ничья".
Необходимо учитывать то, что есть разные выигрышные варианты и программа должна их распознавать.
"""

board = [
    ['x', 'x', 'x', 'o'],
    ['o', 'x', 'o', 'o'],
    ['o', 'o', 'x', 'o'],
    ['o', 'x', 'x', 'o'],

]

winner = None

for i in range(4):
    if board[i][0] == board[i][1] == board[i][2] == board[i][3]:
        winner = board[i][0]
    if board[0][i] == board[1][i] == board[2][i] == board[3][i]:
        winner = board[0][i]
if board[0][0] == board[1][1] == board[2][2] == board[3][3]:
    winner = board[0][0]
if board[0][3] == board[1][2] == board[2][1] == board[3][0]:
    winner = board[0][3]
if winner:
    print(f'Winner is {winner}')
else:
    print('Draw')
