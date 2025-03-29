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
Blue = (100,100,255,128)
White = (255,255,255)
while(True):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    Disp.fill(Blue)
    pygame.draw.polygon(surface=Disp, color=White, points=((100,350),(150,100),(200,350),(200,350),(50,200),(250,200)),width=0)
    pygame.draw.line(surface=Disp, color=White, start_pos=(100,350), end_pos=(150,100), width=4)
    pygame.draw.line(surface=Disp, color=White, start_pos=(150,100), end_pos=(200,350), width=4)
    pygame.draw.line(surface=Disp, color=White, start_pos=(200,350), end_pos=(50,200), width=4)
    pygame.draw.line(surface=Disp, color=White, start_pos=(50,200), end_pos=(250,200), width=4)
    pygame.draw.line(surface=Disp, color=White, start_pos=(250,200), end_pos=(100,350), width=4)
    pygame.display.update()