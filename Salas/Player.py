import pygame

from Dialog_manager import Dialog_manager
from Itens.Arrows import UpArrow


class Player():
    def __init__(self):
        self.currentRoom = ""
        self.inventory = pygame.sprite.Group()
        self.hits = 0
        self.itemHolding = pygame.sprite.GroupSingle()
        self.dialog_manager = Dialog_manager()
        self.state = "default"

            
        self.inventory_surf = pygame.image.load("graphics/Inventario.png").convert_alpha() #pygame.Surface((854,50))
        self.inventory_surf = pygame.transform.scale(self.inventory_surf,(self.inventory_surf.get_width()/1.5,self.inventory_surf.get_height()/1.5))
        self.inventory_rect = self.inventory_surf.get_rect(bottomleft = (50,0))
        self.hover_inventory = False
        self.inventory_lerp = 0

    def pickItem(self,item):
        item.rect.center = (10,10)
        self.inventory.add(item)

    def change_room(self,room):
        self.currentRoom = room

    def update(self,screen):
        screen.blit(self.inventory_surf,self.inventory_rect)
        self.updateInventory(screen,self.inventory_rect)
        
        if (self.dialog_manager.dialog_key != ""):
            self.state = "dialog"
            screen.blit(self.dialog_manager.surface, self.dialog_manager.rect)
        else:
            self.state = "default"
        
        

    
    def updateInventory(self,screen,rect):
        
        
        index = 0

        for item in self.inventory.sprites():
            if self.itemHolding.has(item) == False:
                item.rect.center = (rect.x + item.image.get_width(), rect.y + item.image.get_height())
                # print(item.rect)
                screen.blit(item.image,item.rect)
            else:
                self.itemHolding.draw(screen)
            
            index += 1


        if(self.hover_inventory):
            if self.inventory_lerp + 0.1 <1: 
                self.inventory_lerp += 0.10
            else: 
                inventory_lerp = 1
        
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
    

