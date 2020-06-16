import pygame
from pygame import QUIT, KEYDOWN, K_ESCAPE

pygame.init()

SCREEN_SIZE = 720


screen = pygame.display.set_mode([SCREEN_SIZE, SCREEN_SIZE])
bg_img = pygame.transform.scale(pygame.image.load("assets/board.png"), (SCREEN_SIZE, SCREEN_SIZE))



running = True
mouse_click = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_click = pygame.mouse.get_pos()
        elif event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False
    screen.blit(bg_img, (0, 0))

    if mouse_click is not None:
        mouse_click = None
    else:
        pass

    pygame.display.flip()

pygame.quit()