import pygame
from pygame import freetype
from pygame import locals


pygame.init()

screen = pygame.display.set_mode((1600, 900))
# font = pygame.freetype.SysFont("Courier", 20, False)
# surf_main = pygame.Rect(100, 100, 50, 50)
# surf1, _ = font.render("test")
# img1 = surf1.convert_alpha()
# rect1 = img1.get_rect(center=(50, 50))
#
# surf_main.blit(img1, rect1)
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#     screen.fill((255, 255, 255))
#     screen.blit(img1, rect1)
#     pygame.display.flip()

surf1 = pygame.Surface((100, 100))
surf1.fill((128, 128, 128))

surf2 = surf1.copy()
surf2.fill((0, 0, 0))

surf_3 = pygame.Surface((300, 300))
surf_3.fill((255, 255, 255))
surf_3.blit(surf1, (0, 0))
surf_3.blit(surf2, (100,100))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill((255, 255, 255))
    screen.blit(surf_3, (800, 450))
    pygame.display.flip()
