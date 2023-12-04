def checkShort(a, b, counter, board):
    if a < 0 or a > (chess-1):
        return False
    if b < 0 or b > (chess-1):
        return False
    if (not board[a][b]) or (board[a][b] > counter):
        board[a][b] = counter
        return True
    return False

chess = int(input().strip())
for row in range(1, chess):
    for col in range(1, chess):
        board = [[0]*chess for _ in range(chess)]
        board[0][0] = 1

        q = [(0,0)]
        while q:
            li = []
            while q:
                n, m = q.pop()
                if checkShort(n-row, m-col, board[n][m]+1, board):
                    li.append((n-row, m-col))
                if checkShort(n-col, m-row, board[n][m]+1, board):
                    li.append((n-col, m-row))
                if checkShort(n+row, m-col, board[n][m]+1, board):
                    li.append((n+row, m-col))
                if checkShort(n-row, m+col, board[n][m]+1, board):
                    li.append((n-row, m+col))
                if checkShort(n+col, m-row, board[n][m]+1, board):
                    li.append((n+col, m-row))
                if checkShort(n-col, m+row, board[n][m]+1, board):
                    li.append((n-col, m+row))
                if checkShort(n+row, m+col, board[n][m]+1, board):
                    li.append((n+row, m+col))
                if checkShort(n+col, m+row, board[n][m]+1, board):
                    li.append((n+col, m+row))
            q = li
        print(board[-1][-1] - 1, end=' ')
    print()
