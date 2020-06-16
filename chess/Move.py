import pygame

class Move(pygame.sprite.Sprite):
    def __init__(self, size, init_pos):
        super(Move, self).__init__()
        self.size = size
        self.surf = pygame.Surface((size,size), pygame.SRCALPHA)
        img = pygame.image.load(f"assets/move.png")
        img = pygame.transform.scale(img, (size, size))
        self.surf.blit(img, (0, 0))
        self.rect = self.surf.get_rect()
        self.rect.x, self.rect.y = init_pos[1]*self.size, init_pos[0]*self.size
    
    def get_pos(self):
        return (self.rect.y//self.size, self.rect.x//self.size)