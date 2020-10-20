import numpy as np


class NQueens():
    def solveNQueens(self, n):
        res = []
        self.dfs([-1]*n, 0, [], res)
        return res

    # nums is a one-dimension array, like [1, 3, 0, 2] means
    # first queen is placed in column 1, second queen is placed
    # in column 3, etc.
    def dfs(self, nums, index, path, res):
        if index == len(nums):
            res.append(path)
            return  # backtracking
        for i in range(len(nums)):
            nums[index] = i
            if self.valid(nums, index):  # pruning
                tmp = "."*len(nums)
                self.dfs(nums, index+1, path+[tmp[:i]+"Q"+tmp[i+1:]], res)

    # check whether nth queen can be placed in that column
    def valid(self, nums, n):
        for i in range(n):
            if abs(nums[i]-nums[n]) == n - i or nums[i] == nums[n]:
                return False
        return True

        def byHeur_fake(self):
        r = self.range % 12
        seq1, seq2 = [], []
        seq1 = [i for i in range(4, self.range+1, 2)].append(2) if (
            r in [3, 9]) else [i for i in range(2, self.range+1, 2)]
        seq2 = [i for i in range(1, self.range+1, 2)]
        if (r == 8):
            for i in range(len(seq2)-1):
                if (i % 2 == 0):
                    seq2[i], seq2[i+1] = seq2[i+1], seq2[i]
        if (r == 2):
            seq2[0], seq2[1] = seq2[1], seq2[0]
            seq2.remove(5)
            seq2.append(5)
        if (r in [3, 9]):
            seq2 = seq2[2:]
            seq2 += [1, 3]
        seq = seq1+seq2
        return list(map(lambda x: x-1, seq))


me = NQueens()
print(np.array(me.solveNQueens(11)))
