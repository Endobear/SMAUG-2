import pygame

from Dialog_manager import Dialog_manager


class Player():
    def __init__(self):
       self.currentRoom = ""
       self.inventory = pygame.sprite.Group()
       self.hits = 0
       self.itemHolding = pygame.sprite.GroupSingle()
       self.dialog_manager = Dialog_manager()
       self.state = "default"

    def pickItem(self,item):
        item.rect.center = (10,10)
        self.inventory.add(item)

    def change_room(self,room):
        self.currentRoom = room

    def update(self,screen):
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
    
    def removeItem(self,item):
        for invItem in self.inventory:
            if item == invItem:
                self.inventory.remove(invItem)
            break;

        pass
    

