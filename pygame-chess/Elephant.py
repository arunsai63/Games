import pygame


class Elephant(pygame.sprite.Sprite):
    def __init__(self, color, size, init_pos):
        super(Elephant, self).__init__()
        self.color = color
        self.size = size
        self.surf = pygame.Surface((size, size), pygame.SRCALPHA)
        img = pygame.image.load(f"assets/{self.color}_elephant.png")
        img = pygame.transform.scale(img, (size, size))
        self.surf.blit(img, (0, 0))
        self.rect = self.surf.get_rect()
        self.move_to(init_pos)
        self.isMoved = False

    def get_pos(self):
        return (self.rect.y//self.size, self.rect.x//self.size)

    def move_to(self, pos):
        self.isMoved = True
        self.rect.x, self.rect.y = pos[1]*self.size, pos[0]*self.size

    def get_possible_moves(self, board):
        x, y = self.get_pos()
        moves = []
        for row in range(x+1, 8):  # down
            if board[row][y] == 0:
                moves.append((row, y))
            elif board[row][y].color != self.color:
                moves.append((row, y))
                break
            else:
                break
        for row in range(x-1, -1, -1):  # up
            if board[row][y] == 0:
                moves.append((row, y))
            elif board[row][y].color != self.color:
                moves.append((row, y))
                break
            else:
                break
        for col in range(y-1, -1, -1):  # left
            if board[x][col] == 0:
                moves.append((x, col))
            elif board[x][col].color != self.color:
                moves.append((x, col))
                break
            else:
                break
        for col in range(y+1, 8):  # left
            if board[x][col] == 0:
                moves.append((x, col))
            elif board[x][col].color != self.color:
                moves.append((x, col))
                break
            else:
                break
        return moves
