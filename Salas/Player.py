import pygame
from pygame import surface

from Dialog_manager import Dialog_manager
from Itens.Arrows import UpArrow


class Player():
    def __init__(self):
        self.currentRoom = ""
        self.hits = 0
        self.itemHolding = pygame.sprite.GroupSingle()
        self.dialog_manager = Dialog_manager()
        self.state = "default"

        self.newRoom = ""
        self.transition_lerp = 0

        self.inventory = pygame.sprite.Group()
        self.inventory_surf = pygame.image.load("graphics/Inventario.png").convert_alpha() #pygame.Surface((854,50))
        self.inventory_surf = pygame.transform.scale(self.inventory_surf,(self.inventory_surf.get_width()/1.5,self.inventory_surf.get_height()/1.5))
        self.inventory_rect = self.inventory_surf.get_rect(bottomleft = (50,0))
        self.hover_inventory = False
        self.inventory_lerp = 0

        

    #133
    def pickItem(self,item):
        item.image = item.icon
        item.rect = item.icon.get_rect(center = (10,10))

        if item.dialog != "":
            self.dialog_manager.set_dialog(item.dialog, color = item.dialog_color, overwrite = True)
        self.inventory.add(item)

    def change_room(self,room):
        if self.state == "default":
            self.state = "moving"
            self.newRoom = room
            # self.currentRoom = room

    def update(self,screen):
        screen.blit(self.inventory_surf,self.inventory_rect)
        self.updateInventory(screen,self.inventory_rect)
        
        #TODO Fazer o diálogo aumentar e diminuir a opacidade ao invés de só aparecer
        if (self.dialog_manager.dialog_key != "" and self.state == "default"):
            self.state = "dialog"

        if self.dialog_manager.dialog_key != "" and self.state == "moving":
            self.dialog_manager.clear_dialog()
                 
        elif self.dialog_manager.dialog_key == "" and self.state == "dialog":
            self.state = "default"
        
        

        if self.state == "dialog":
            screen.blit(self.dialog_manager.surface, self.dialog_manager.rect)


            
        if self.newRoom != "":
            
            transition_surface = pygame.Surface((screen.get_width(), screen.get_height()))
            transition_surface.fill((0,0,0))

            if self.currentRoom != self.newRoom:
                if self.transition_lerp < 255:
                    self.transition_lerp += 12
                    
                else:
                    self.transition_lerp = 255
                    self.currentRoom = self.newRoom
                    self.state = "default"
                    

                transition_surface.set_alpha(self.transition_lerp)
                screen.blit(transition_surface,transition_surface.get_rect())

            elif self.transition_lerp > 0:
                self.transition_lerp -= 12
                
                transition_surface.set_alpha(self.transition_lerp)
                screen.blit(transition_surface,transition_surface.get_rect())

            else:
                self.transition_lerp = 0
                self.newRoom == ""
                if self.state != "dialog":
                    self.state = "default"
            



            
        

    
    def updateInventory(self,screen,rect):
        
        
        index = 0
        inventory_slots = [(56,28),(112,28),(160,28),(210,28),(260,28)]
        for item in self.inventory.sprites():
            if self.itemHolding.has(item) == False:
                item.rect.center = (rect.x + inventory_slots[index][0], rect.y + inventory_slots[index][1] )
                # print(item.rect)
                screen.blit(item.image,item.rect)
            else:
                self.itemHolding.draw(screen)
            
            index += 1


        if(self.hover_inventory):
            if self.inventory_lerp + 0.1 <1: 
                self.inventory_lerp += 0.10
            else: 
                self.inventory_lerp = 1
        
        else:
            if self.inventory_lerp - 0.1 > 0:
                self.inventory_lerp -= 0.10
            else:
                self.inventory_lerp = 0
        
        self.inventory_rect.y = (self.inventory_lerp*0)+ ((1-self.inventory_lerp)* -55)
    
    def removeItem(self,item):
        for invItem in self.inventory:
            if item == invItem:
                self.inventory.remove(invItem)
            break;

        pass
    

