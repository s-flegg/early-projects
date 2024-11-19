# noinspection PyUnresolvedReferences
import pygame
import sys
#start pygame engine
pygame.init()
#FPS must be locked + setting clock
FPS = 60
clock = pygame.time.Clock()
#Screen Info
#0.0 is top left
screen = pygame.display.set_mode()
screenWidth, screenHeight = screen.get_size()
pygame.display.quit()
x, y = screenWidth, screenHeight - 55 #-55 to allow for top bar
#create the scene
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Auto-Notes")
#Initialise constants like colours and fonts
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

largeFont = pygame.font.SysFont("papyrus", 72)
midFont = pygame.font.SysFont("papyrus", 36)
smallFont = pygame.font.SysFont("papyrus", 18)

backgroundColour = BLUE
#load images


#Game Loop
while True:
    # put things here that need to be constantly displayed, don't initialise
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(FPS)