import pygame
from state import GameState
# Cores
WHITE = (240, 217, 181)
BROWN = (181, 136, 99)

SQUARE_SIZE = 80
BOARD_SIZE = 8

# Dicionário para armazenar as imagens carregadas
piece_images = {}

def load_piece_images():
    pieces = ['wp', 'wr', 'wn', 'wb', 'wq', 'wk',
              'bp', 'br', 'bn', 'bb', 'bq', 'bk']
    for piece in pieces:
        image = pygame.image.load(f"assets/{piece}.png")
        piece_images[piece] = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))

def draw_board(screen, board_state, gs):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            # Alterna cor das casas
            color = WHITE if (row + col) % 2 == 0 else BROWN
            rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, color, rect)
            if(gs.move != None and gs.move.start_row == row and gs.move.start_col == col):
                pygame.draw.rect(screen, (255, 0, 0), rect, 3)

            # Desenha a peça se houver
            piece = board_state[row][col]
            if piece != "":
                screen.blit(piece_images[piece], rect)

def draw_log_moves(screen, gs: GameState):
    font = pygame.font.SysFont("Arial", 20)
    text_y = 10
    text_x = 650
    logs = gs.move_logs[-30:]
    for  move in logs:
        index = gs.move_logs.index(move)
        text = font.render(str(index + 1) + ". " + str(move), True, (250, 0, 0))
        screen.blit(text, (text_x, text_y))
        text_y += 20