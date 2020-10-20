import numpy as np


def isSafe(board, row, col):
    # check left row
    for y in range(col):
        if board[row][y] == 1:
            return False
    # check diagonal left top
    for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False
    # check diagonal left bottom
    for x, y in zip(range(row, N, 1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False

    return True


def generateSolution(board, col):
    # terminating condition
    # all columns covered
    global N
    if col >= N:
        return True
    # loop over all the rows
    for i in range(N):
        if isSafe(board, i, col) == True:
            board[i][col] = 1
            # recursively place other queens
            if generateSolution(board, col + 1) == True:
                return True
            # unmark queen spot
            board[i][col] = 0
    # backtrack
    return False


N = int(input())
startCol = 0
board = [[0 for i in range(N)] for j in range(N)]
# print(board)

if generateSolution(board, startCol) == False:
    print("No Solution Exists")
else:
    print("Solution exists")
    print(np.array(board))
