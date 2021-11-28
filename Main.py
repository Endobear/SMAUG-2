import pygame
from pygame.constants import MOUSEMOTION
from Salas.Escola.Duto import Duto
from Salas.Player import Player
from Mapa import Mapa
from sys import exit


pygame.init()
screen = pygame.display.set_mode((854,480))
pygame.display.set_caption('Paradox Dream')
clock = pygame.time.Clock()

map = Mapa()
player = Player()
map.player = player
player.currentRoom = map.rooms[3]

debug_rects = False


# inventory_icon_image = pygame.image.load("graphics/InvIcon.png").convert_alpha()
# inventory_icon_image = pygame.transform.scale(inventory_icon_image,(inventory_icon_image.get_width()/3,inventory_icon_image.get_height()/3))
# inventory_icon_rect = inventory_icon_image.get_rect(topleft = (20,-65))

background_surf = pygame.image.load(player.currentRoom.image).convert_alpha()
background_rects = player.currentRoom.room_rects + player.itemHolding.sprites()
# player.pickItem(KeyItem())
# player.pickItem(Screwdriver())
# player.pickItem(Screwdriver())
# player.pickItem(Screwdriver())
# player.pickItem(Screwdriver())


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if  event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                if player.state == "dialog":
                    player.dialog_manager.next_line()
                
                elif player.itemHolding.sprites() == []:
                    
                    for rect in background_rects:
                        if rect.collidepoint(event.pos):
                            print("clicou", rect)
                            print(player.currentRoom)
                            player.currentRoom.ineractRect(rect,player)

                
                    for item in player.inventory.sprites():
                        if item.rect.collidepoint(event.pos):
                            player.itemHolding.add(item)

        if  event.type == pygame.MOUSEBUTTONUP:
            if player.itemHolding.sprites() != []:
                for rect in background_rects:
                        if rect.collidepoint(event.pos):
                            player.currentRoom.useItem(rect,player)
                
                player.itemHolding.empty()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                
                debug_rects = not debug_rects
                
            if event.key == pygame.K_c:
                print(background_rects)
                print(player.state)

            if event.key == pygame.K_a:
                print(player.inventory.sprites())
                print(player.itemHolding.sprites())

            if event.key == pygame.K_s:
                print(player.inventory)
                print(player.itemHolding)
        
        if event.type == pygame.MOUSEMOTION:
            
            if  player.inventory_rect.collidepoint(event.pos):
                ##print("No Inventário")
                player.hover_inventory = True
            else:
                ##print("Fora do Inventário")
                player.hover_inventory = False

            if player.itemHolding.sprites() != []: 
                
                player.itemHolding.sprites()[0].rect.center = event.pos
                
                        
    background_surf = pygame.image.load(player.currentRoom.image).convert_alpha()
    background_rects = player.currentRoom.room_rects


    
    
    screen.blit(background_surf,(0,0))
    player.currentRoom.update(screen)

    map.update(screen)

    # inventory_surf.fill(pygame.Color(0,0,255))
    # inventory_surf.set_alpha(123)

    # screen.blit(inventory_surf,inventory_rect)
    # screen.blit(inventory_icon_image,inventory_icon_rect)
    
    # pygame.draw.rect(inventory_surf,pygame.Color(255, 255 , 0),inventory_rect)
    # player.updateInventory(screen,inventory_rect)
   

    player.update(screen)

    
    # if(hover_inventory):
    #     if inventory_lerp + 0.1 <1: 
    #         inventory_lerp += 0.10
    #     else: 
    #         inventory_lerp = 1
        
    # else:
    #     if inventory_lerp - 0.1 > 0:
    #         inventory_lerp -= 0.10
    #     else:
    #         inventory_lerp = 0

    

    # inventory_rect.y = (inventory_lerp*0)+ ((1-inventory_lerp)* -55)
    # inventory_icon_rect.y = (inventory_lerp*0)+ ((1-inventory_lerp)* -65)

    if debug_rects:
       
        for rect in background_rects:
            pygame.draw.rect(screen,(255, 0 , 0),rect)

    

    
    pygame.display.update()
    clock.tick(60)
