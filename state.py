from move import Move

class GameState:
    def __init__(self):
        self.board =[
            ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
            ["bp"] * 8,
            [""] * 8,
            [""] * 8,
            [""] * 8,
            [""] * 8,
            ["wp"] * 8,
            ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]
        ]
        self.turn_of_white = True
        self.move_logs = []
        self.move = None

    def select_pieces(self, row, col):
        if(self.move == None):
            if(self.board[row][col] == ""):
                return
            if(self.turn_of_white and self.board[row][col][0] != "w"):
                return
            else:
                if(not self.turn_of_white and self.board[row][col][0] != "b"):
                    return
            self.move = Move(row, col, None, None, self.board)
        else:
            end_piece = self.board[row][col]
            if(end_piece != "" and end_piece[0] == self.move.piece_moved[0]):
                return
            self.move.end_row = row
            self.move.end_col = col
            self.move_piece()

    def move_piece(self):
        self.board[self.move.start_row][self.move.start_col] = ""
        self.board[self.move.end_row][self.move.end_col] = self.move.piece_moved
        self.move_logs.append(self.move)
        self.move = None
        self.turn_of_white = not self.turn_of_white