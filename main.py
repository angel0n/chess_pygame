import pygame
from board import draw_board, load_piece_images, draw_log_moves
from state import GameState

# Inicialização
pygame.init()
WIDTH, HEIGHT = 850, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Xadrez com Pygame")
gs = GameState()

load_piece_images()
gs.get_moves_possibles()

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
            if(row >= 0 and row < 8 and col >= 0 and col < 8):
                clicked_piece = gs.board[row][col]
                gs.select_pieces(row,col, screen)
                gs.get_moves_possibles()

    if(not gs.check_mate):
        screen.fill((0, 0, 0)) 
        draw_board(screen, gs.board,gs)
        draw_log_moves(screen, gs)
    pygame.display.flip()

pygame.quit()
