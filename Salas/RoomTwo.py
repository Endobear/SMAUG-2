import pygame
from Salas.Room import Room
from Itens.Arrows import FrontArrow,BackArrow
from Itens.Itens import KeyItem

class RoomTwo(Room):
    def __init__(self,map):
        super().__init__()
        self.room_name = "Room Two"
        self.room_description = "A Nice Room with Pink Walls"
        self.exits = ["Back"]
        self.map = map
        
        spawnable_pos = [(587,358)]
        
        self.itens.append(KeyItem())
        self.itens[0].rect.center = spawnable_pos[0]

        self.itens_sprites.add(self.itens[0])
        


        self.arrows = [BackArrow((390,446))]
        self.image = "graphics/Room2_ClosedDoor.png"
        self.exitsName = ["BackDoor","FrontDoor"]
        self.id = "RoomTwo"
    
    def backLocation(self):
        return self.RoomExitClassFromMap(self.map,self.exitsName[0])

    
        
        
            


    
    
    