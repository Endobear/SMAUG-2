import pygame
from sys import exit

from pygame import display

pygame.init()
screen = pygame.display.set_mode((854,480))
pygame.display.set_caption('Paradox Dream')
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    

    pygame.display.update()
    clock.tick(60)
