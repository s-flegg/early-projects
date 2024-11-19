# noinspection PyUnresolvedReferences
import sys
import pygame
#start pygame engine
pygame.init()
#FPS must be locked + setting clock
FPS = 60
clock = pygame.time.Clock()
#Screen Info
#0.0 is top left
screen = pygame.display.set_mode()
x, y = screen.get_size()
pygame.display.quit()
#create the scene
screen = pygame.display.set_mode((x, y - 55), pygame.RESIZABLE)
pygame.display.set_caption("Auto-Notes")
#Initialise constants like colours and fonts
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
largeFont = pygame.font.SysFont("papyrus", int(72*(x/1920)))
text = largeFont.render('Auto-Notes', True, WHITE)
textRect = text.get_rect()
textRect.topleft = (50, 50)
def fonts():
    x, y =screen.get_size()
    largeFont = pygame.font.SysFont("papyrus", int(72*(x/1920)))
    text = largeFont.render('Auto-Notes', True, WHITE)
    textRect = text.get_rect()
    textRect.topleft = (50, 50)
fonts()

backgroundColour = BLUE
#load images

# create a text surface object,
# on which text is drawn on it.
text = largeFont.render('Auto-Notes', True, WHITE)
# create a rectangular object for the
# text surface object
textRect = text.get_rect()
# set the center of the rectangular object.
textRect.topleft = (50, 50)

#Game Loop
while True:
    # put things here that need to be constantly displayed, don't initialise
    screen.fill(backgroundColour)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.VIDEORESIZE:
            oldScreenSaved = screen
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            if event.w != x:
                fonts()
            # On the next line, if only part of the window
            # needs to be copied, there's some other options.
            screen.blit(oldScreenSaved, (0,0))
            del oldScreenSaved


    pygame.display.update()
    clock.tick(FPS)