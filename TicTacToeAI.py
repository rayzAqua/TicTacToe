import random

REWARD = 10
MAX_SCORE = 1050
DRAW_SCORE = 0

DEPTH = 2

# Tra ve gia tri ngau nhien row, col va gia tri cua symbol dua vao bien turn cua nuoc di do AI thuc hien
def randomAIMove(turn):
    row = random.randint(0, 2)
    col = random.randint(0, 2)
    symbol = 1 if turn else 2
    return row, col, symbol
    # print(randomAIMove(True))

# Ham ho tro goi de quy MinMax
def findBestMoveMinMax(gs):
    global bestMove
    bestMove = None
    minMaxAlgorithm(gs, DEPTH, 1 if gs.xToMove else -1)
    return bestMove

# Giai thuat minmax de tim kiem nuoc di tot nhat
def minMaxAlgorithm(gs, depth, turnValue):
    global bestMove
    if depth == 0:
        print(turnValue, turnValue * scoreBoard(gs))
        return turnValue * scoreBoard(gs)

    bestScore = -MAX_SCORE
    for row in range(len(gs.board)):
        for col in range(len(gs.board[row])):
            if gs.board[row][col] == 0:
                symbol = 1 if gs.xToMove else 2
                gs.makeMove(row, col, symbol)
                score = -minMaxAlgorithm(gs, depth - 1, -turnValue)
                if score > bestScore:
                    bestScore = score
                    print(bestScore)
                    if depth == DEPTH:
                        print("OK")
                        bestMove = (row, col, symbol)
                        print(bestScore, bestMove)
                gs.undoMove()
    return bestScore

# Kiem tra xem ai thang
def checkPlayerWin(gs):
    # Hang ngang
    for col in range(len(gs.board)):
        if gs.board[col][0] == gs.board[col][1] == gs.board[col][2] != 0:
            return gs.board[col][1]

    # Hang doc
    for row in range(len(gs.board)):
        if gs.board[0][row] == gs.board[1][row] == gs.board[2][row] != 0:
            return gs.board[1][row]

    # Hang cheo 1
    if gs.board[0][0] == gs.board[1][1] == gs.board[2][2] != 0:
        return gs.board[1][1]

    # Hang cheo 2
    if gs.board[0][2] == gs.board[1][1] == gs.board[2][0] != 0:
        return gs.board[1][1]

# Danh gia nuoc di
def scoreBoard(gs):
    # Ban dau co 1000 diem
    score = 1000
    # Neu la trang thai ket thuc thi kiem tra xem ai thang, neu x thang thi x duoc + 10, o thang thi tru di 10
    if gs.isTheEnd():
        if checkPlayerWin(gs) == 1:
            score += REWARD
            return score
        elif checkPlayerWin(gs) == 2:
            score -= REWARD
            return score
    # Neu la trang thai hoa` thi score + 0
    elif gs.isDraw():
        score += DRAW_SCORE
        return score
    # Neu la nuoc di binh thuong thi score -1
    else:
        score -= 1
    return score






