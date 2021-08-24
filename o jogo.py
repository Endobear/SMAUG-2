import pygame
from Salas.Player import Player
from Salas.RoomOne import RoomOne
from sys import exit

from pygame import display

pygame.init()
screen = pygame.display.set_mode((854,480))
pygame.display.set_caption('Paradox Dream')
clock = pygame.time.Clock()

rooms = [RoomOne()]
player = Player()
player.currentRoom = rooms[0]

background_surf = pygame.image.load(player.currentRoom.image).convert_alpha()
background_rects = player.currentRoom.interactives

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(background_surf,(0,0))
    
    for rect in background_rects:
        pygame.draw.rect(screen,(255, 0 , 0),rect)

    pygame.display.update()
    clock.tick(60)
