import pygame
from Salas.Room import Room
from Itens.Arrows import FrontArrow,BackArrow
from Itens.Itens import KeyItem

class RoomTwo(Room):
    def __init__(self,map):
        super().__init__()
        self.room_name = "Room Two"
        self.room_description = "A Nice Room with Pink Walls"
        self.exits = ["Back","Front"]
        self.map = map
        
        spawnable_pos = [(587,358)]
        
        self.itens.append(KeyItem())
        self.itens[0].rect.center = spawnable_pos[0]

        self.itens_sprites.add(self.itens[0])
        
        porta_rect = pygame.Rect((349,236),(79,126))
        espelho_rect = pygame.Rect((515,222),(40,50))
        self.interactives = [porta_rect,espelho_rect]

        self.roomTwoDoor = RoomTwoDoor(self)

        self.arrows = [BackArrow((390,446))]
        self.image = "graphics/Room2_ClosedDoor.png"
        self.exitsName = ["BackDoor","FrontDoor"]
        
        self.id = "RoomTwo"
    
    def backLocation(self):
        return self.RoomExitClassFromMap(self.map,self.exitsName[0])

    def frontLocation(self):
        if self.roomTwoDoor.doorStatus == "Closed":
            return self.roomTwoDoor
        else:
            return self.RoomExitClassFromMap(self.map,self.exitsName[1])

    def ineractRect(self, rect, player):
        super().ineractRect(rect, player)
        if rect == self.interactives[0]: # Porta da sala
            player.currentRoom = self.getLocationFromDirection("Front")

    

class RoomTwoDoor(Room):
    def __init__(self,roomTwo):
        super().__init__()
        self.room_name = "Room Two"
        self.doorStatus = "Closed"
        self.image = "graphics/Room2_doorClosed.png"
        self.exits = ["Back"]
        self.roomTwo = roomTwo
        self.arrows = [BackArrow((390,446))]
        self.id = "RoomTwoDoor"

        
        keyHole_rect = pygame.Rect((428,230),(32,56))
        door_rect = pygame.Rect((284,93),(191,295))
        self.interactives = [keyHole_rect,door_rect]

    
    def backLocation(self):
        return self.roomTwo

    def frontLocation(self):
        return self.RoomTwo.RoomExitClassFromMap(self.RoomTwo.map, self.RoomTwo.exitsName[0])

    def ineractRect(self, rect, player):
        super().ineractRect(rect, player)
        if rect == (self.interactives[1] or self.interactives[0]) and self.doorStatus == "Open": # Porta da sala
            player.currentRoom = self.getLocationFromDirection("Front")
    
    def useItem(self, rect, item):
       if rect in self.interactives:
           if rect == self.interactives[0] and item.type == KeyItem().type:
               self.doorStatus = "Open"
               self.image = "graphics/Room2_doorOpen.png"
               self.roomTwo.image = "graphics/Room2_OpenDoor.png"
               
        
        
            


    
    
    