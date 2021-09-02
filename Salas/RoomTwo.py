import pygame
from Salas.Room import Room
from Itens.Arrows import FrontArrow,BackArrow

class RoomTwo(Room):
    def __init__(self,map):
        super().__init__()
        self.room_name = "Room Two"
        self.room_description = "A Nice Room with Pink Walls"
        self.exits = ["Back"]
        self.map = map
        backArrow = BackArrow((390,446))

        self.ArrowSprites = pygame.sprite.Group(backArrow)
        self.image = "graphics/Room2.png"
        self.exitsName = ["BackDoor","FrontDoor"]
        self.id = "RoomTwo"
        self.interactives = [backArrow.rect]
    
    def backLocation(self):
        return self.RoomExitClassFromMap(self.map,self.exitsName[0])

    def ineractRect(self,rect,player):
       
        if rect == self.interactives[0]: # BackArrow
            
            player.currentRoom = self.backLocation()


    
    
    