from move import Move

def get_moves_peaw(board: list[list[str]], start_row: int, start_col: int):
    piece = board[start_row][start_col][0]
    oponent = "b" if piece == "w" else "w"
    moves = []
    inicial_row = 6 if piece == "w" else 1
    direction = -1 if inicial_row == 6 else 1

    if(0 <= (start_row + direction) < 8 ):
        if(board[start_row + direction][start_col] == ""):
            moves.append(str(Move(start_row, start_col,start_row + direction, start_col, board)))
            if(start_row == inicial_row and board[start_row + (2 * direction)][start_col] == ""):
                moves.append(str(Move(start_row, start_col,start_row + (2 * direction), start_col, board)))
        if(start_col -1 >= 0 and board[start_row + direction][start_col - 1 ] != "" and board[start_row + direction][start_col - 1 ][0] == oponent):
            moves.append(str(Move(start_row, start_col,start_row + direction, start_col - 1, board)))
        if(start_col +1 < 8 and board[start_row + direction][start_col + 1 ] != "" and board[start_row + direction][start_col + 1 ][0] == oponent):
            moves.append(str(Move(start_row, start_col,start_row + direction, start_col + 1, board)))

    return moves

def get_moves_rook(board: list[list[str]], start_row: int, start_col: int):
    piece = board[start_row][start_col]
    oponent = "b" if piece[0] == "w" else "w"
    moves = []
    directions = [(1,0),(-1,0),(0,1),(0,-1)]

    for row_direction, col_direction in directions:
        row, col = start_row + row_direction, start_col + col_direction
        while 0 <= row < 8 and 0 <= col < 8:
            piece_captured = board[row][col]
            
            if(piece_captured == ""):
                moves.append(str(Move(start_row, start_col, row, col, board)))
            elif(piece_captured[0] == oponent ):
                moves.append(str(Move(start_row, start_col, row, col, board)))
                break
            elif(piece_captured[0] == piece[0]):
                break
            row += row_direction
            col += col_direction 
    return moves

def get_moves_knight(board: list[list[str]], start_row: int, start_col: int):
    piece = board[start_row][start_col]
    oponent = "w" if piece[0] == "b" else "b"
    moves = []
    directions = [(-2,1),(-2,-1),(2,1),(2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]

    for row_direction, col_direction in directions:
        row, col = start_row + row_direction, start_col + col_direction
        if 0 <= row < 8 and 0 <= col < 8:
            piece_captured = board[row][col]
            if piece_captured == "":
                moves.append(str(Move(start_row, start_col, row, col, board))) 
            elif piece_captured[0] == oponent:
                moves.append(str(Move(start_row, start_col, row, col, board)))
    return moves

def get_moves_bishop(board: list[list[str]], start_row: int, start_col: int):
    piece = board[start_row][start_col]
    oponent = "w" if piece[0] == "b" else "b"
    moves = []
    directions = [(-1,1),(-1,-1),(1,1),(1,-1)]

    for row_direction, col_direction in directions:
        row, col = start_row + row_direction, start_col + col_direction
        while 0 <= row < 8 and 0 <= col < 8:
            piece_captured = board[row][col]
            if piece_captured == "":
                moves.append(str(Move(start_row, start_col, row, col, board)))
            elif piece_captured[0] == oponent:
                moves.append(str(Move(start_row, start_col, row, col, board)))
                break
            elif piece_captured[0] == piece[0]:
                break
            row += row_direction
            col += col_direction
    return moves

def get_moves_king(board: list[list[str]], start_row: int, start_col: int):
    piece = board[start_row][start_col]
    oponent = "w" if piece[0] == "b" else "b"
    moves = []
    directions = [(1,0),(1,1),(1,-1),(-1,0),(-1,1),(-1-1),(0,1),(0,-1)]

    for row_direction, col_direction in directions:
        row, col = start_row + row_direction, start_col + col_direction
        piece_captured = board[row][col]
        if piece_captured == "":
            moves.append(str(Move(start_row, start_col, row, col, board)))
        if piece_captured[0] == oponent:
            moves.append(str(Move(start_row, start_col, row, col, board)))
    return moves

def get_moves_queen(board: list[list[str]], start_row: int, start_col: int):
    moves = []
    moves.extend(get_moves_rook(board,start_row,start_col))
    moves.extend(get_moves_bishop(board,start_row,start_col))
    return moves

get_moves_possibles_piece = {
    "p": get_moves_peaw,
    "r": get_moves_rook,
    "n": get_moves_knight,
    "b": get_moves_bishop,
    "k": get_moves_king,
    "q": get_moves_queen,
}