import pygame

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

def draw_board(screen, board_state):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            # Alterna cor das casas
            color = WHITE if (row + col) % 2 == 0 else BROWN
            rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, color, rect)

            # Desenha a peça se houver
            piece = board_state[row][col]
            if piece != "":
                screen.blit(piece_images[piece], rect)
