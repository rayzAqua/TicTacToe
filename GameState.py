"""
Lop GameState quan ly trang thai ban co
"""
class GameState:
    def __init__(self):
        # Khoi tao ban co
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        # Luot cua nguoi choi
        self.xToMove = True
        # Dung de luu lai lich su nuoc di
        self.moveLog = []
        # Trang thai ket thuc - Thang
        self.isTheEndState = False
        # Trang thai hoa
        self.isDrawState = False

    # Thuc hien mot nuoc di
    def makeMove(self, row, col, symbol):
        # Make Move chi thuc hien duoc khi ban co con trong (tuc gia tri 0)
        if self.board[row][col] == 0:
            self.board[row][col] = symbol
            # Doi luot cua nguoi choi
            self.xToMove = not self.xToMove
            # Luu lai toa do row, col vao lich su nuoc di
            self.moveLog.append((row, col))

    # Undo mot nuoc di
    def undoMove(self):
        # Chi thuc hien Undo Move khi danh sach moveLog co du lieu
        if len(self.moveLog) != 0:
            # Day toa do cuoi cung duoc luu lai trong danh sach ra va luu lai vao bien pre_pos
            pre_pos = self.moveLog.pop()
            # Luu lai toa do hang` va cot. de gan lai gia tri cu~
            pre_row = pre_pos[0]
            pre_col = pre_pos[1]
            self.board[pre_row][pre_col] = 0
            # Tra lai luot choi cua nguoi thuc hien nuoc di do
            self.xToMove = not self.xToMove

            # Dat lai trang thai ket thuc va trang thai hoa`
            self.isTheEndState = False
            self.isDrawState = False

    # Kiem tra trang thai ket thuc
    def isTheEnd(self):
        # Hang ngang
        for col in range(len(self.board)):
            if self.board[col][0] == self.board[col][1] == self.board[col][2] != 0:
                self.isTheEndState = True
                return self.isTheEndState

        # Hang doc
        for row in range(len(self.board)):
            if self.board[0][row] == self.board[1][row] == self.board[2][row] != 0:
                self.isTheEndState = True
                return self.isTheEndState

        # Hang cheo 1
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            self.isTheEndState = True
            return self.isTheEndState

        # Hang cheo 2
        if self.board[2][0] == self.board[1][1] == self.board[0][2] != 0:
            self.isTheEndState = True
            return self.isTheEndState

    # Kiem tra trang thai hoa` co
    def isDraw(self):
        # Bien dung de dem cac o vuong co gia tri khac 0
        not_zero = 0
        # Neu khong phai ket thuc thi kiem tra hoa co`
        if not self.isTheEnd():
            for r in range(len(self.board)):
                for c in range(len(self.board[r])):
                    # Neu o vuong co gia tri khac khong thi tang gia tri bien not_zero len
                    if self.board[r][c] != 0:
                        not_zero += 1
        # Neu so luong o vuong khac 0 bang voi so luong o vuong tren ban co thi la hoa co
        if not_zero == pow(len(self.board), 2):
            self.isDrawState = True
            return self.isDrawState
