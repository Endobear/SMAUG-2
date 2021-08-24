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
debug_rects = False

background_surf = pygame.image.load(player.currentRoom.image).convert_alpha()
background_rects = player.currentRoom.interactives

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if  event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for rect in background_rects:
                    if rect.collidepoint(event.pos):
                        print("clicou", rect)
                        player.currentRoom.ineractRect(rect,player)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if debug_rects:
                    debug_rects = False
                else:
                    debug_rects = True
                        
    background_surf = pygame.image.load(player.currentRoom.image).convert_alpha()
    background_rects = player.currentRoom.interactives
    
    screen.blit(background_surf,(0,0))
    
    if debug_rects:
        for rect in background_rects:
            pygame.draw.rect(screen,(255, 0 , 0),rect)
        


    pygame.display.update()
    clock.tick(60)
