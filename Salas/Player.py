import pygame


class Player():
    def __init__(self):
       self.currentRoom = ""
       self.inventory = pygame.sprite.Group()
       self.hits = 0

    def pickItem(self,item):
        self.inventory.add(item)
       
    
    def updateInventory(self,inventory_surface):
        for item in self.inventory.sprites():
            inventory_surface.blit(item.image,item.rect)

