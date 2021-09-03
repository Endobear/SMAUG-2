import pygame


class Player():
    def __init__(self):
       self.currentRoom = ""
       self.inventory = pygame.sprite.Group()
       self.hits = 0

    def pickItem(self,item):
        item.rect.center = (10,10)
        self.inventory.add(item)

       
    
    def updateInventory(self,screen,rect):
        index = 0

        for item in self.inventory.sprites():
            item.rect.center = (rect.x + item.image.get_width(), rect.y + item.image.get_height())
            # print(item.rect)
            
            screen.blit(item.image,item.rect)
            index += 1
        

