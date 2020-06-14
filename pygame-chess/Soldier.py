import pygame
from Elephant import Elephant


class Soldier(pygame.sprite.Sprite):
    def __init__(self, color, size, init_pos):
        super(Soldier, self).__init__()
        self.color = color
        self.size = size
        self.surf = pygame.Surface((size, size), pygame.SRCALPHA)
        img = pygame.image.load(f"assets/{self.color}_soldier.png")
        img = pygame.transform.scale(img, (size, size))
        self.surf.blit(img, (0, 0))
        self.rect = self.surf.get_rect()
        self.move_to(init_pos)

    def get_pos(self):
        return (self.rect.y//self.size, self.rect.x//self.size)
    
    def move_to(self, pos):
        self.rect.x, self.rect.y = pos[1]*self.size, pos[0]*self.size

    def get_possible_moves(self, board):
        x, y = self.get_pos()
        moves = []
        if self.color == "black":
            if board[x+1][y] == 0:
                moves.append((x+1, y))
                if x == 1 and board[3][y] == 0:
                    moves.append((3, y))
            if y != 0 and board[x+1][y-1] != 0 and (board[x+1][y-1]).color != self.color:
                moves.append((x+1, y-1))
            if y != 7 and board[x+1][y+1] != 0 and (board[x+1][y+1]).color != self.color:
                moves.append((x+1, y+1))
        else:
            if board[x-1][y] == 0:
                moves.append((x-1, y))
                if x == 6 and board[4][y] == 0:
                    moves.append((4, y))
            if y != 0 and board[x-1][y-1] != 0 and (board[x-1][y-1]).color != self.color:
                moves.append((x-1, y-1))
            if y != 7 and board[x-1][y+1] != 0 and (board[x-1][y+1]).color != self.color:
                moves.append((x-1, y+1))
        return moves
