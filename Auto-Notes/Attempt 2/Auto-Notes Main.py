import pygame
import sys
pygame.init()


#Get Screen Info
screen = pygame.display.set_mode()
screenWidth, screenHeight = screen.get_size()
pygame.quit()


#set fps
FPS = 60
framePerSecond = pygame.time.Clock()


# Set up the drawing window
pygame.init()
screen = pygame.display.set_mode([screenWidth, screenHeight - 55])
pygame.display.set_caption("Auto-Notes")



#-----Colours-----#
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


#-----Font-----#
largeFont = pygame.font.SysFont("Papyrus", int(72*(screenWidth/1920)))
mainFont = pygame.font.SysFont("Papyrus", int(26*(screenWidth/1920)))
smallFont = pygame.font.SysFont("Papyrus", int(18*(screenWidth/1920)))

backgroundColour = BLACK

#-----Title-----#
text = largeFont.render("Auto-Notes", True, WHITE)
textRect = text.get_rect()
textRect.topleft = (int(50*(screenWidth/1920)), int(50*(screenWidth/1920)))

#-----Data-----#
#def
#    subjects = []



#Game loop
gameLoop = True
while gameLoop == True:


    screen.fill(backgroundColour)


    #quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False

    screen.blit(text, textRect)


    pygame.display.update()
    framePerSecond.tick(FPS)