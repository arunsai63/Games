import pygame
from pygame import QUIT, KEYDOWN, K_ESCAPE
from King import King
from Queen import Queen
from Elephant import Elephant
from Camel import Camel
from Horse import Horse
from Soldier import Soldier
from Move import Move


pygame.init()
SCREEN_SIZE = 720
ICON_SIZE = SCREEN_SIZE//8

screen = pygame.display.set_mode([SCREEN_SIZE, SCREEN_SIZE])
bg_img = pygame.transform.scale(pygame.image.load("assets/board.png"), (SCREEN_SIZE, SCREEN_SIZE))
move_indicator = pygame.transform.scale(pygame.image.load("assets/move.png"), (SCREEN_SIZE, SCREEN_SIZE))

Board = [ 
    [Elephant("black", ICON_SIZE, (0, 0)), Horse("black", ICON_SIZE, (0,1)), Camel("black", ICON_SIZE, (0,2)), Queen("black", ICON_SIZE),
     King("black", ICON_SIZE), Camel("black", ICON_SIZE, (0,5)), Horse("black", ICON_SIZE, (0,6)), Elephant("black", ICON_SIZE, (0,7))],
    [Soldier("black", ICON_SIZE, (1,0)), Soldier("black", ICON_SIZE, (1,1)), Soldier("black", ICON_SIZE, (1,2)), Soldier("black", ICON_SIZE, (1,3)),
     Soldier("black", ICON_SIZE, (1,4)), Soldier("black", ICON_SIZE, (1,5)), Soldier("black", ICON_SIZE, (1,6)), Soldier("black", ICON_SIZE, (1,7))],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [Soldier("white", ICON_SIZE, (6, 0)), Soldier("white", ICON_SIZE, (6,1)), Soldier("white", ICON_SIZE, (6,2)), Soldier("white", ICON_SIZE, (6,3)),
     Soldier("white", ICON_SIZE, (6,4)), Soldier("white", ICON_SIZE, (6,5)), Soldier("white", ICON_SIZE, (6,6)), Soldier("white", ICON_SIZE, (6,7))],
    [Elephant("white", ICON_SIZE, (7,0)), Horse("white", ICON_SIZE, (7,1)), Camel("white", ICON_SIZE, (7,2)), Queen("white", ICON_SIZE),
     King("white", ICON_SIZE), Camel("white", ICON_SIZE, (7,5)), Horse("white", ICON_SIZE, (7,6)), Elephant("white", ICON_SIZE, (7,7))]
]

mouse_click = (-1, -1)
possible_moves = []
next_move = "white"
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_click = pygame.mouse.get_pos()
        elif event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False
        
    screen.blit(bg_img, (0, 0))  # background image

    for row in Board:
        for piece in row:
            if piece:
                screen.blit(piece.surf, piece.rect)
                if mouse_click[0] != -1 and piece.rect.collidepoint(mouse_click) and piece.color == next_move: #if clicked on sprite 
                    clicked_coin = piece.get_pos() #save clicked coin position
                    possible_moves = [Move(ICON_SIZE, move) for move in piece.get_possible_moves(Board)] #save all possible_moves
                    mouse_click = (-1, -1) #reset mouseclick status after clicking on sprite
    
    if mouse_click[0] != -1: #if not clicked on sprite
        for move in possible_moves:
            if move.rect.collidepoint(mouse_click): #if clicked on possible move
                x,y = move.get_pos()
                if type(Board[x][y]) is King:
                    print(f"{next_move} wins the game")
                    running = False
                    continue
                
                if Board[x][y]:
                    print(f"{next_move} {type(Board[clicked_coin[0]][clicked_coin[1]]).__name__} killed " + ("white " if next_move == "black" else "black ") + f"{type(Board[x][y]).__name__} at {(clicked_coin)}")
                else:
                    if type(Board[clicked_coin[0]][clicked_coin[1]]) is King and abs(clicked_coin[1] - y) == 2: #castling
                        Board[clicked_coin[0]][clicked_coin[1]].do_castling(Board, (x,y))
                        next_move = "white" if next_move == "black" else "black"
                        mouse_click = (-1, -1)
                        continue
                    print(f"{next_move} {type(Board[clicked_coin[0]][clicked_coin[1]]).__name__} moved to {(x,y)}")
                
                Board[clicked_coin[0]][clicked_coin[1]].move_to((x,y)) #move the coin to possible_move co-ordinate
                Board[x][y] = Board[clicked_coin[0]][clicked_coin[1]] #update value in board
                Board[clicked_coin[0]][clicked_coin[1]] = 0 #make old position as empty

                next_move = "white" if next_move == "black" else "black"
                mouse_click = (-1, -1) #reset mouseclick status after moving
                break
        #if clicked anywhere else
        possible_moves = []
        clicked_coin = None
        mouse_click = (-1, -1)

    for move in possible_moves:
        screen.blit(move.surf, move.rect)
    pygame.display.flip()

pygame.quit()
