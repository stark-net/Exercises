# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pygame, sys
from pygame.locals import *
pygame.init()
Disp = pygame.display.set_mode((300,400))
pygame.display.set_caption("Erfan's Game")
Red = (100,100,255,128)
White = (255,255,255)
while(True):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    Disp.fill(Red)
    pygame.draw.line(surface=Disp, color=White, start_pos=(100,200), end_pos=(200,200), width=6)
    pygame.draw.line(surface=Disp, color=White, start_pos=(150,250), end_pos=(150,150), width=6)
    pygame.draw.line(surface=Disp, color=White, start_pos=(125,225), end_pos=(175,175), width=8)
    pygame.draw.line(surface=Disp, color=White, start_pos=(175,225), end_pos=(125,175), width=8)
    pygame.display.update()