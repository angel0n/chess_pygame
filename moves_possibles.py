from move import Move

def get_moves_peaw(board: list[list[str]], start_row: int, start_col: int):
    piece = board[start_row][start_col]
    moves = []
    if(piece[0] == "w"):
        if(start_row == 6):
            if(board[start_row - 1][start_col] == ""):
                moves.append(str(Move(start_row, start_col,start_row - 1, start_col, board)))
                if(board[start_row - 2][start_col] == ""):
                    moves.append(str(Move(start_row, start_col,start_row - 2, start_col, board)))
        else:
            if(start_row - 1 >= 0 and board[start_row - 1][start_col] == ""):
                moves.append(str(Move(start_row, start_col,start_row - 1, start_col, board)))  

        if((start_col - 1 >= 0 and start_row - 1 >= 0) and board[start_row - 1][start_col - 1] != "" and board[start_row - 1][start_col - 1][0] == "b"): 
             moves.append(str(Move(start_row, start_col,start_row - 1, start_col - 1, board)))
        if((start_col + 1 < 8 and start_row - 1 >= 0) and board[start_row - 1][start_col + 1] != "" and board[start_row - 1][start_col + 1][0] == "b"): 
             moves.append(str(Move(start_row, start_col,start_row - 1, start_col + 1, board)))
    else:
        if(start_row == 1):
            if(board[start_row + 1][start_col] == ""):
                moves.append(str(Move(start_row, start_col,start_row + 1, start_col, board)))
                if(board[start_row + 2][start_col] == ""):
                    moves.append(str(Move(start_row, start_col,start_row + 2, start_col,board)))
        else:
            if(start_row + 1 <= 7 and board[start_row + 1][start_col] == ""):
                moves.append(str(Move(start_row, start_col,start_row + 1, start_col,board)))  
        
        if((start_col - 1 >= 0 and start_row + 1 < 8) and board[start_row + 1][start_col - 1] != "" and board[start_row + 1][start_col - 1][0] == "w"): 
             moves.append(str(Move(start_row, start_col,start_row + 1, start_col - 1, board)))
        if((start_col + 1 < 8 and start_row + 1 < 8) and board[start_row + 1][start_col + 1] != "" and board[start_row + 1][start_col + 1][0] == "w"): 
             moves.append(str(Move(start_row, start_col,start_row + 1, start_col + 1, board)))
    
    return moves

def get_moves_rook(board: list[list[str]], start_row: int, start_col: int):
    piece = board[start_row][start_col]
    oponent = "b" if piece[0] == "w" else "w"
    moves = []
    if(start_row < 7):
        for row in range(start_row + 1, 8):
            if(board[row][start_col] == ""):
               moves.append(str(Move(start_row, start_col, row, start_col, board))) 
            elif(board[row][start_col][0] == piece[0]):
               break
            elif(board[row][start_col][0] == oponent):
               moves.append(str(Move(start_row, start_col, row, start_col, board))) 
               break

    if(start_row > 0):
        for row in range(start_row - 1, -1, -1):
            if(board[row][start_col] == ""):
               moves.append(str(Move(start_row, start_col, row, start_col, board)))
            elif(board[row][start_col][0] == piece[0]):
               break
            elif(board[row][start_col][0] == oponent):
               moves.append(str(Move(start_row, start_col, row, start_col, board))) 
               break
                 
    if(start_col < 7):
        for col in range(start_col + 1, 8):
            if(board[start_row][col] == ""):
               moves.append(str(Move(start_row, start_col, start_row, col, board))) 
            elif(board[start_row][col][0] == piece[0]):
               break
            elif(board[start_row][col][0] == oponent):
               moves.append(str(Move(start_row, start_col, start_row, col, board))) 
               break
             
    if(start_col > 0):
        for col in range(start_col - 1, -1, -1):
            if(board[start_row][col] == ""):
               moves.append(str(Move(start_row, start_col, start_row, col, board))) 
            elif(board[start_row][col][0] == piece[0]):
               break
            elif(board[start_row][col][0] == oponent):
               moves.append(str(Move(start_row, start_col, start_row, col, board))) 
               break
    return moves

get_moves_possibles_piece = {
    "wp": get_moves_peaw,
    "bp": get_moves_peaw,
    "wr": get_moves_rook,
    "br": get_moves_rook,
}