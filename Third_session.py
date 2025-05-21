""" 
...
import pygame
W = 600
H - 800
a = "PATH"
b = "PATH"
pygame.image.load(a)
pygame.image.load(b)
bin_new = pygame.transform.scale(bi, (W, H))
"""


import pygame, sys
from pygame.locals import *
pygame.init()
image = "/home/stark/Pictures/546694.jpg"
W = 800
H = 600


Disp = pygame.display.set_mode((W,H))
pygame.display.set_caption("Game")
while(True):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        bi = pygame.image.load(image)
        bi_new = pygame.transform.scale(bi, (W,H))
        pygame.display.update()