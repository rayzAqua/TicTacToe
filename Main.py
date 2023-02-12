import sys
import pygame as p
from CONFIG import *
import GameState
import TicTacToeAI as AI

'''
Phan main van hanh chuong trinh
'''

# Ham Main
def main(player_one, player_two):
    # Khoi tao pygame
    p.init()
    # Dat tieu de cho man hinh game
    p.display.set_caption("TicTacToe")
    # Dat kich thuoc cho man hinh game
    screen = p.display.set_mode((WIDTH, HEIGHT))
    # To mau cho man hinh game
    screen.fill(BG_COLOR)

    # Goi den lop trang thai de xu ly giao dien
    gs = GameState.GameState()
    # Gioi han so lan lap trong 1 giay
    clock = p.time.Clock()

    # Xu ly luot choi va trang thai ket thuc
    player1 = player_one
    player2 = player_two
    gameOver = False

    # Xu ly AI
    undoMove = False

    # Vong lap game
    running = True
    while running:
        # Bien nay dung de kiem tra xem luot hien tai co phai la nguoi choi ko
        humanTurn = (gs.xToMove and player1) or (not gs.xToMove and player2)
        # Bat su kien
        for e in p.event.get():
            # Tat man hinh
            if e.type == p.QUIT:
                p.quit()
                sys.exit()
            # Bat su kien click chuot
            elif e.type == p.MOUSEBUTTONDOWN:
                # Neu khong phai la Game Over thi nguoi choi duoc phep thuc hien nuoc di
                if not gameOver:
                    # Luu lai toa do ma nguoi choi click chuot
                    pos = p.mouse.get_pos()
                    row = pos[1] // SQUARE_SIZE
                    col = pos[0] // SQUARE_SIZE
                    print(row, col)
                    # Chi khi la luot cua nguoi choi va o duoc chon trong' thi moi duoc thuc hien nuoc di
                    if humanTurn:
                        if gs.board[row][col] == 0:
                            symbol = 1 if gs.xToMove else 2
                            gs.makeMove(row, col, symbol)
                            undoMove = False
                            # print(gs.xToMove)

            # Bat su kien ban phim
            elif e.type == p.KEYDOWN:
                # Tat man hinh game de quay lai menu
                if e.key == p.K_ESCAPE:
                    running = False
                # Thuc hien chuc nang Undo Move
                elif e.key == p.K_z:
                    print("Undo Move")
                    gs.undoMove()
                    gameOver = False
                    undoMove = True

                # Thuc hien chuc nang Reset ban co
                elif e.key == p.K_r:
                    print("Reset")
                    gs = GameState.GameState()
                    gameOver = False
                    undoMove = False

        if not gameOver and not humanTurn and not undoMove:
            ai_move = AI.findBestMoveMinMax(gs)
            if ai_move is None:
                ai_move = AI.randomAIMove(gs.xToMove)
            # print(ai_move)
            gs.makeMove(ai_move[0], ai_move[1], ai_move[2])
        elif len(gs.moveLog) == 0:
            undoMove = False

        # Ve ban co
        drawGameState(screen, gs.board)

        # Trang thai ket thuc
        if gs.isTheEnd():
            gameOver = True
            text = "Player 'O' win " if gs.xToMove else "Player 'X' win "
            # Xu ly su kien ket thuc game
            case = drawOverScreen(screen, text, gameOver)
            if case == "new_game":
                print("New Game")
                gs = GameState.GameState()
                gameOver = False
            elif case == "back":
                print("back")
                running = False

        # Trang thai hoa co
        elif gs.isDraw():
            gameOver = True
            # Xu ly su kien ket thuc game
            case = drawOverScreen(screen, "DRAW", gameOver)
            if case == "new_game":
                print("New Game")
                gs = GameState.GameState()
                gameOver = False
            elif case == "back":
                print("back")
                running = False

        # Xu ly cap nhat giao dien sau moi lan lap va so lan lap trong 1 giay
        clock.tick(MAX_FPS)
        p.display.flip()


'''
Xu ly giao dien
'''

# Ve trang thai ban co
def drawGameState(screen, board):
    drawSquare(screen, board)
    drawMark(screen, board)

# Ve ban co. Cu the la ve nhung o vuong len man hinh
def drawSquare(screen, board):
    # Ve mau` nen de lay mau nen lam vien
    screen.fill(BG_COLOR)
    # Vi tri ve hinh vuong
    RECT_LOCATION = SQUARE_SIZE + LINE_WIDTH
    # Chieu dai chieu rong hinh vuong
    RECT_SIZE = SQUARE_SIZE - LINE_WIDTH
    for r in range(len(board)):
        for c in range(len(board[r])):
            p.draw.rect(screen, SQUARE_COLOR, p.Rect(RECT_LOCATION * c, RECT_LOCATION * r, RECT_SIZE, RECT_SIZE))

# Ve dau x va dau o
def drawMark(screen, board):
    for r in range(len(board)):
        for c in range(len(board[r])):
            # Toa do bat dau ve
            x_position = c * SQUARE_SIZE
            y_position = r * SQUARE_SIZE
            # Ve dau X
            if board[r][c] == 1:
                # Part 1
                start = (x_position + SQUARE_SIZE // 4, y_position + SQUARE_SIZE // 4)
                end = (x_position + SQUARE_SIZE - SQUARE_SIZE // 4, y_position + SQUARE_SIZE - SQUARE_SIZE // 4)
                p.draw.line(screen, CROSS_COLOR, start, end, CROSS_WIDTH)
                # Part 2
                start = (x_position + SQUARE_SIZE - SQUARE_SIZE // 4, y_position + SQUARE_SIZE // 4)
                end = (x_position + SQUARE_SIZE // 4, y_position + SQUARE_SIZE - SQUARE_SIZE // 4)
                p.draw.line(screen, CROSS_COLOR, start, end, CROSS_WIDTH)

            # Ve dau O
            if board[r][c] == 2:
                center = (x_position + SQUARE_SIZE // 2, y_position + SQUARE_SIZE // 2)
                p.draw.circle(screen, CIRCLE_COLOR, center, RADIUS, CIRCLE_WIDTH)

# Ve man hinh the end
def drawOverScreen(screen, text, gameOver):
    # Ve mot man hinh de` len man hinh game
    end_screen = p.Surface((WIDTH, HEIGHT))
    end_screen.fill(END_COLOR)
    end_screen.set_alpha(200)
    screen.blit(end_screen, (0, 0))

    # Ve chu len man hinh
    font1 = p.font.Font("Image/font.ttf", 22)
    textObject = font1.render(text, True, p.Color("White"))
    textLocation = p.Rect(0, 0, WIDTH, HEIGHT).move(WIDTH/2 - textObject.get_width()/2, HEIGHT/2 - textObject.get_height()/2 - 20)
    screen.blit(textObject, textLocation)

    # Ve chu Click to Reset len man hinh
    font2 = p.font.Font("Image/font.ttf", 12)
    nof_string = font2.render("<<Click any or press 'R' to start a new game>>", True, p.Color("White"))
    nof_location = p.Rect(0, 0, WIDTH, HEIGHT).move(WIDTH/2 - nof_string.get_width()/2 + 2, HEIGHT/2 - nof_string.get_height()/2 + 30)
    screen.blit(nof_string, nof_location)

    while gameOver:
        for e in p.event.get():
            if e.type == p.QUIT:
                p.quit()
                sys.exit()
            elif e.type == p.MOUSEBUTTONDOWN:
                mouse_endgame_pos = p.mouse.get_pos()
                col = mouse_endgame_pos[0] // SQUARE_SIZE
                row = mouse_endgame_pos[1] // SQUARE_SIZE
                if row in range(DIMENSION) and col in range(DIMENSION):
                    return "new_game"
            elif e.type == p.KEYDOWN:
                if e.key == p.K_ESCAPE:
                    return "back"
                if e.key == p.K_r:
                    return "new_game"

        p.display.update()

