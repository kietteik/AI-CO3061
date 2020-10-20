class Q:
    def __init__(self, row, col):
        self.row = row
        self.col = col
    # see method check if a Queen can see another one

    def see(self, queen):
        return ((self.row-queen.row == abs(self.col-queen.col)) or self.col == queen.col)

    def move(self, nrange):
        if (self.col >= nrange - 1):
            return False
        else:
            self.col += 1
            return True


class Board:
    # Qlist = [Q(1, 1), Q(2, 3)]

    def __init__(self, nrange):
        self.range = nrange
        self.Qlist = [Q(-1, -1)]*nrange

    def addQ(self, q):
        if (len(self.Qlist) >= self.range):
            return False
        else:
            self.Qlist.append(q)
            return True

    def stateIsValid(self, q):
        for oq in self.Qlist:
            if (q.see(oq)):
                return False
        return True


class SolveNQ:
    def __init__(self, nrange):
        self.board = Board(nrange)
        self.range = nrange

        def byDFS_old(self, row, board, backTrack=0):
        if (self.notConflict(row, board) and not backTrack):
            if (row+1 == self.range):
                return True
            board.append(0)
            self.byDFS(row+1, board)
        elif (board[-1] < self.range-1):
            board[-1] += 1
            self.byDFS(row, board)
        else:
            board.pop()
            self.byDFS(row-1, board, 1)

    def byDFS(self, row, board):

    def byBFS(self):
        pass

    def byHeur(self):
        pass


a = SolveNQ(4)
a.byDFS(0, a.board)

for q in a.board.Qlist:
    print(q.col, " ")
