import pygame
from pygame.constants import MOUSEMOTION
from Salas.Player import Player
from Mapa import Mapa
from sys import exit

from pygame import display

pygame.init()
screen = pygame.display.set_mode((854,480))
pygame.display.set_caption('Paradox Dream')
clock = pygame.time.Clock()

map = Mapa()
player = Player()
player.currentRoom = map.rooms[0]
debug_rects = False

inventory_surf = pygame.Surface((854,50))
inventory_rect = inventory_surf.get_rect(bottomleft = (0,480))
hover_inventory = False
inventory_lerp = 0

background_surf = pygame.image.load(player.currentRoom.image).convert_alpha()
background_rects = player.currentRoom.room_rects

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
            if event.key == pygame.K_c:
                print(background_rects)
        
        if event.type == pygame.MOUSEMOTION:
            
            if event.pos[0] >= 0 and event.pos[1] >= 460 or inventory_rect.collidepoint(event.pos):
                ##print("No Inventário")
                hover_inventory = True
            else:
                ##print("Fora do Inventário")
                hover_inventory = False
                        
    background_surf = pygame.image.load(player.currentRoom.image).convert_alpha()
    background_rects = player.currentRoom.room_rects


    
    
    screen.blit(background_surf,(0,0))
    player.currentRoom.update(screen)

    inventory_surf.fill(("Blue"))
    screen.blit(inventory_surf,inventory_rect)

    if(hover_inventory):
        if inventory_lerp + 0.1 <1: 
            inventory_lerp += 0.15
        else: 
            inventory_lerp = 1
        
    else:
        if inventory_lerp - 0.1 > 0:
            inventory_lerp -= 0.15
        else:
            inventory_lerp = 0

    

    inventory_rect.y = (inventory_lerp*430)+ ((1-inventory_lerp)* 480)

    
    if debug_rects:
        for rect in background_rects:
            pygame.draw.rect(screen,(255, 0 , 0),rect)

    


    pygame.display.update()
    clock.tick(60)
