import pygame
import os
import sys

pygame.init()
pygame.display.set_caption('ding pong')
surface = pygame.display.set_mode((850,450))
background = pygame.Color(80, 160, 240) 
surface.fill(background) 
pygame.display.update()        

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
