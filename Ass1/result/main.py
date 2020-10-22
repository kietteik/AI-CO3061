import random as rd
import time


class SolveNQ:
    def __init__(self, nrange):
        self.range = nrange

    def byDFS(self, board):
        if (len(board) >= self.range):
            return True
        for i in range(self.range):
            board.append(i)
            if (self.notConflict(board)):
                if (self.byDFS(board) == True):
                    return True
            board.pop()
        return False

    def byBFS(self, queue):
        while queue != []:
            board = queue.pop(0)
            if (self.notConflict(board)):
                if (len(board) == self.range):
                    return board
                for i in range(self.range):
                    nboard = board.copy()
                    nboard.append(i)
                    queue.append(nboard)
        return []

    def byHeur(self):
        if self.range <= 3 & self.range != 1:
            return[]
        initBoard = rd.sample(range(0, self.range), self.range)
        while (not self.finalState(initBoard)):
            boardChanged = 0
            for row in range(self.range):
                if (boardChanged == 1):
                    break
                conflict = self.conflictValue(row, initBoard, initBoard[row])
                if (conflict == 0):
                    continue
                for col in range(self.range):
                    # print(initBoard)
                    if (col == initBoard[row]):
                        continue
                    nextConflict = self.conflictValue(row, initBoard, col)
                    if (nextConflict < conflict):
                        initBoard[row] = col
                        conflict = nextConflict
                        boardChanged = 1
            if (boardChanged == 0):
                # print('After:  ', initBoard)
                initBoard[rd.randint(0, self.range-1)] = rd.randint(
                    0, self.range-1)
                # print('Before: ', initBoard)
        return initBoard

    def notConflict(self, board):
        for i in range(len(board)-1):
            lastIndex = len(board)-1
            if (abs(board[i]-board[-1]) == lastIndex - i) or board[i] == board[-1]:
                return False
        return True

    def conflictValue(self, queenIndex, board, checkValue):
        numOfConflict = 0
        for i in range(self.range):
            if (i == queenIndex):
                continue
            if (abs(board[i]-checkValue) == abs(i-queenIndex)):
                numOfConflict += 1
            if (board[i] == checkValue):
                numOfConflict += 1
        return numOfConflict

    def finalState(self, board):
        for i in range(self.range):
            for j in range(self.range):
                if (i == j):
                    continue
                if (abs(j-i) == abs(board[j]-board[i])) | (board[i] == board[j]):
                    return False
        return True

    def solve(self):
        case = int(
            input("Choose search algorithm:\n1.DFS\n2.BFS\n3.Heuristics\n"))
        start_time = time.time()
        if case == 1:
            print("Using DFS...", end=' ')
            board = []
            result = self.byDFS(board)
            result = board
        elif case == 2:
            print("Using BFS...", end=' ')
            board = [[]]
            result = self.byBFS(board)
        elif case == 3:
            print("Using Heuristics...", end=' ')
            result = self.byHeur()
        else:
            raise(SyntaxError)
        end_time = time.time()
        print("DONE")
        print("--- %s seconds ---" % (end_time - start_time))
        return result


def printBoard(board):
    print("\n")
    a = 0 if board == [] else max(board)+1
    for i in board:
        print("-"*(a*4+1))
        print("|"+"   |"*i+" Q |"+"   |"*(a-i-1))
    print("-"*(a*4+1))


if __name__ == "__main__":
    a = SolveNQ(int(input("Enter n:")))
    resutl = a.solve()
    print(resutl)
