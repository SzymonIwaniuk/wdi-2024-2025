def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == "H":
            return False

        if col - (row - i) >= 0 and board[i][col - (row - i)] == "H":
            return False

        if col + (row - i) < 8 and board[i][col + (row - i)] == "H":
            return False

    return True

def hetmany():
    board = [[0 for _ in range(8)] for _ in range(8)]

    def rek(board, h):
        if h == 8:
            return 1

        cnt = 0

        for j in range(8):
            if is_safe(board,h,j):
                board[h][j] = "H"
                cnt += rek(board, h + 1)
                board[h][j] = 0
        return cnt

    result = rek(board,0)

    return result

print(hetmany())