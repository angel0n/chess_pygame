import pygame
from board import draw_board, load_piece_images
from state import GameState

# Inicialização
pygame.init()
WIDTH, HEIGHT = 640, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Xadrez com Pygame")
gs = GameState()

load_piece_images()

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Clique do mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            row = mouse_y // 80
            col = mouse_x // 80
            clicked_piece = gs.board[row][col]
            gs.select_pieces(row,col)

    draw_board(screen, gs.board)
    pygame.display.flip()

pygame.quit()
