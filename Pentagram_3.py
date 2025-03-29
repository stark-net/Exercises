import pygame, sys
from pygame.locals import *
pygame.init()
Disp = pygame.display.set_mode((300,400))
pygame.display.set_caption("Erfan's Game")
Blue = (100,100,255,128)
White = (255,255,255)
while(True):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    Disp.fill(Blue)
    pygame.draw.polygon(surface=Disp, color=White, points=((100,335),(115,265),(65,215),(130,215),(145,135),(165,215),(235,215),(180,265),(195,335),(145,285)))
    pygame.display.update()