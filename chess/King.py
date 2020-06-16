import pygame
from Elephant import Elephant


class King(pygame.sprite.Sprite):
    def __init__(self, color, size):
        super(King, self).__init__()
        self.color = color
        self.size = size
        self.isMoved = False
        self.surf = pygame.Surface((size, size), pygame.SRCALPHA)
        img = pygame.image.load(f"assets/{self.color}_king.png")
        img = pygame.transform.scale(img, (size, size))
        self.surf.blit(img, (0, 0))
        self.rect = self.surf.get_rect()
        self.rect.x, self.rect.y = (
            (4*size, 7*size) if self.color == "white" else (4*size, 0))  # inital position

    def get_pos(self):
        return (self.rect.y//self.size, self.rect.x//self.size)

    def move_to(self, pos):
        self.isMoved = False
        self.rect.x, self.rect.y = pos[1]*self.size, pos[0]*self.size

    def tryGetBoardValue(self, board, x, y):
        try:
            if x > -1 and y > -1 and (board[x][y] == 0 or board[x][y].color != self.color):
                return (x, y)
            else:
                return None
        except:
            return None

    def do_castling(self, board, pos):
        if not pos in [(0,6),(0,2),(7,6),(7,2)]:
            return False
        x,y = pos
        if y == 6:
            self.move_to(pos)
            board[x][7].move_to((x,5))
            board[x][6] = board[x][4]
            board[x][4] = 0
            board[x][5] = board[x][7]
            board[x][7] = 0
        else:
            self.move_to(pos)
            board[x][0].move_to((x,3))
            board[x][2] = board[x][4]
            board[x][4] = 0
            board[x][3] = board[x][0]
            board[x][0] = 0


    def check_casting(self, board):
        moves = []
        if self.color == "white":
            if self.get_pos() == (7, 4) and type(board[7][7]) is Elephant and not board[7][7].isMoved and board[7][5] == 0 and board[7][6] == 0:
                moves.append((7, 6))
            if self.get_pos() == (7, 4) and type(board[7][0]) is Elephant and not board[7][0].isMoved and board[7][3] == 0 and board[7][2] == 0 and board[7][1] == 0:
                moves.append((7, 2))
        else:
            if self.get_pos() == (0, 4) and type(board[0][7]) is Elephant and not board[0][7].isMoved and board[0][5] == 0 and board[0][6] == 0:
                moves.append((0, 6))
            if self.get_pos() == (0, 4) and type(board[0][0]) is Elephant and not board[0][0].isMoved and board[0][3] == 0 and board[0][2] == 0 and board[0][1] == 0:
                moves.append((0, 2))
        return moves

    def get_possible_moves(self, board):
        x, y = self.get_pos()
        moves = [  # 8 possible moves for king
            self.tryGetBoardValue(board, x+1, y+1),
            self.tryGetBoardValue(board, x+1, y),
            self.tryGetBoardValue(board, x+1, y-1),

            self.tryGetBoardValue(board, x, y+1),
            self.tryGetBoardValue(board, x, y-1),

            self.tryGetBoardValue(board, x-1, y+1),
            self.tryGetBoardValue(board, x-1, y),
            self.tryGetBoardValue(board, x-1, y-1)
        ]
        if not self.isMoved:
            moves += self.check_casting(board)
        return [m for m in moves if m is not None]
