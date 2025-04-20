class Move:
    def __init__(self, start_row, start_col, end_row, end_col, board):
        self.start_row = start_row
        self.start_col = start_col
        self.end_row = end_row
        self.end_col = end_col
        self.piece_moved = board[start_row][start_col]

    def __str__(self):
        return f"{self.piece_moved}: ({self.start_row + 1},{self.start_col + 1}) -> ({self.end_row + 1},{self.end_col + 1})"