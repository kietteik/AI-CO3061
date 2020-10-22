def notConflict(board):
    for i in range(len(board)-1):
        lastIndex = len(board)-1
        if (abs(board[i]-board[-1]) == lastIndex - i) or board[i] == board[-1]:
            return False
    return True


print(notConflict([3, 1, 0, 2]))
