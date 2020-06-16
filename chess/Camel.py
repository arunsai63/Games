import pygame


class Camel(pygame.sprite.Sprite):
    def __init__(self, color, size, init_pos):
        super(Camel, self).__init__()
        self.color = color
        self.size = size
        self.surf = pygame.Surface((size, size), pygame.SRCALPHA)
        img = pygame.image.load(f"assets/{self.color}_camel.png")
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
        count = 1
        while  x + count < 8 and y + count < 8: #diagnol right bottom
            if board[x+count][y+count] == 0:
                moves.append((x+count,y+count))
                count += 1
            elif board[x+count][y+count].color != self.color:
                moves.append((x+count,y+count))
                count += 1
                break
            else:
                break
        count = 1
        while  x + count < 8 and y - count < 8: #diagnol left bottom
            if board[x+count][y-count] == 0:
                moves.append((x+count,y-count))
                count += 1
            elif board[x+count][y-count].color != self.color:
                moves.append((x+count,y-count))
                count += 1
                break
            else:
                break
        count = 1
        while  x - count < 8 and y - count < 8: #diagnol left top
            if board[x-count][y-count] == 0:
                moves.append((x-count,y-count))
                count += 1
            elif board[x-count][y-count].color != self.color:
                moves.append((x-count,y-count))
                count += 1
                break
            else:
                break
        count = 1
        while  x - count < 8 and y + count < 8: #diagnol left top
            if board[x-count][y+count] == 0:
                moves.append((x-count,y+count))
                count += 1
            elif board[x-count][y+count].color != self.color:
                moves.append((x-count,y+count))
                count += 1
                break
            else:
                break
        return moves
