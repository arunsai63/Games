import pygame
from pygame import QUIT, KEYDOWN, K_ESCAPE, K_SPACE, K_r, K_p, K_0, K_9
from time import sleep

pygame.init()

SCREEN_SIZE = 630
ICON_SIZE = SCREEN_SIZE // 9

screen = pygame.display.set_mode([SCREEN_SIZE, SCREEN_SIZE])
bg_img = pygame.transform.scale(pygame.image.load("assets/board.png"), (SCREEN_SIZE, SCREEN_SIZE))
numbers = [pygame.transform.scale(pygame.image.load(f"assets/{i}.png"), (ICON_SIZE, ICON_SIZE)) for i in range(1,10)]
highlight = pygame.transform.scale(pygame.image.load("assets/highlight.png"), (ICON_SIZE, ICON_SIZE))

board = [
    [0, 0, 0,  7, 0, 0,  0, 0, 0],
    [1, 0, 0,  0, 0, 0,  0, 0, 0],
    [5, 0, 0,  4, 0, 6,  2, 0, 0],

    [0, 0, 0,  0, 0, 0,  0, 0, 6],
    [0, 0, 0,  0, 0, 9,  0, 0, 0],
    [0, 0, 0,  0, 0, 0,  0, 1, 8],

    [7, 0, 0,  0, 8, 1,  9, 0, 0],
    [0, 0, 0,  0, 0, 0,  0, 5, 0],
    [0, 0, 0,  0, 0, 0,  0, 0, 0]
]

running = True
mouse_click = None

def render_board(board):
    screen.blit(bg_img, (0, 0))
    for row, items in enumerate(board):
        for col, num in enumerate(items):
            if num != 0:
                screen.blit(numbers[num - 1], (col*ICON_SIZE, row*ICON_SIZE))
    if mouse_click is not None:
        screen.blit(highlight, (mouse_click[1]*ICON_SIZE, mouse_click[0]*ICON_SIZE))
    pygame.display.flip()

def valid(board):
    for row in board:
        r = [i for i in row if i != 0]
        if len(set(r)) != len(r):
            return False
    for i in range(9):
        r = [board[c][i] for c in range(9) if board[c][i] != 0]
        if len(set(r)) != len(r):
            return False
    for i in [0,3,6]:
        for j in [0,3,6]:
            r = [board[i+a][j+b] for a in range(3) for b in range(3) if board[i+a][j+b] != 0]
            if len(set(r)) != len(r):
                return False
    return True

def solve(board, render_func):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for i in range(1,10):
                    board[row][col] = i
                    if valid(board):
                        render_func(board)
                        if solve(board, render_func):
                            return True
                board[row][col] = 0            
                return False
    return True

while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            mouse_click = y // ICON_SIZE, x // ICON_SIZE
        elif event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_SPACE:
                print("processing...")
                solve(board, lambda x: None)
                print("done")
            elif event.key == K_p:
                solve(board, render_board)
            elif event.key == K_r:
                print("resetting board")
                board = [[0 for _ in range(9)] for i in range(9)]
            elif event.key >= K_0 and event.key <= K_9:
                if mouse_click is not None:
                    board[mouse_click[0]][mouse_click[1]] = event.key - K_0
                    if not valid(board):
                        print(f"{event.key - K_0} cannot be placed here")
                        board[mouse_click[0]][mouse_click[1]] = 0
                    mouse_click = None
            
    render_board(board)

pygame.quit()