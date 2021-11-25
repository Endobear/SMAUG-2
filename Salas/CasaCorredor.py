import pygame
from Salas.Room import Room

from Itens.Arrows import BackArrow,FrontArrow

class CasaCorredor(Room):
    def __init__(self,map):
        super().__init__()
        self.room_name = "CasaCorredor"
        self.image = "graphics/Cenario 2/corredor.png"
        self.exits = ["Front","Back"]
        self.exitsName = ["CorredorSaida"]
        self.map = map
        
        self.arrows = [BackArrow((420,450))]
        

        self.id = "CasaCorredor"
    
    def backLocation(self):

        return self.RoomExitClassFromMap(self.map,self.exitsName[0])


        