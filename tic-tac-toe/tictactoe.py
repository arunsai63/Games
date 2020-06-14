import pygame
from pygame import QUIT, KEYDOWN, K_ESCAPE

pygame.init()

SCREEN_SIZE = 600
ICON_SIZE = SCREEN_SIZE // 3

screen = pygame.display.set_mode([SCREEN_SIZE, SCREEN_SIZE])
bg_img = pygame.transform.scale(pygame.image.load("assets/board.png"), (SCREEN_SIZE, SCREEN_SIZE))
coin_x = pygame.transform.scale(pygame.image.load("assets/x.png"), (ICON_SIZE, ICON_SIZE))
coin_o = pygame.transform.scale(pygame.image.load("assets/o.png"), (ICON_SIZE, ICON_SIZE))

board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

next_move = "o"
count = 9
running = True
mouse_click = None

def is_complete(game):
    for i in range(3):
        if game[i][0] != 0 and game[i][0] == game[i][1] and game[i][1] == game[i][2]: #row
            return True
        if game[0][i] != 0 and game[0][i] == game[1][i] and game[1][i] == game[2][i]: #col
            return True
    if game[1][1] != 0 and game[0][0] == game[1][1] and game[1][1] == game[2][2]: #diagnol 1
        return True
    if game[1][1] != 0 and game[0][2] == game[1][1] and game[1][1] == game[2][0]: #diagnol 2
        return True
    return False

while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_click = pygame.mouse.get_pos()
        elif event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False
    screen.blit(bg_img, (0, 0))

    if mouse_click is not None:
        x = mouse_click[1]//ICON_SIZE
        y = mouse_click[0]//ICON_SIZE
        if not board[x][y]:
            board[x][y] = next_move
            count -= 1
            if is_complete(board):
                print(f'{next_move} wins the game')
                running = False
            elif count < 1:
                print("draw match")
                running = False
            next_move = 'x' if next_move == 'o' else 'o'
        mouse_click = None
    
    for row, values in enumerate(board):
        for col, item in enumerate(values):
            if item:
                screen.blit(coin_x if item == 'x' else coin_o, (col * ICON_SIZE, row * ICON_SIZE))
    
    pygame.display.flip()
    