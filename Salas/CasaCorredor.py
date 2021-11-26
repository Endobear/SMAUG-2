import pygame
from Salas.Room import Room

from Itens.Arrows import BackArrow,FrontArrow

class CasaCorredor(Room):
    def __init__(self,map):
        super().__init__()
        self.room_name = "CasaCorredor"
        self.image = "graphics/Cenario 2/corredor.png"
        self.exits = ["Back"]
        self.exitsName = ["CorredorQuarto","CorredorSala"]
        self.map = map
        
        self.arrows = [BackArrow((420,450))]

        self.interactives = {"saida": pygame.Rect((323,3),(183,326))}
        

        self.id = "CasaCorredor"
    
    def backLocation(self):

        return self.RoomExitClassFromMap(self.map,self.exitsName[0])
    
    def ineractRect(self, rect, player):
        super().ineractRect(rect, player)
        if rect == self.interactives["saida"]:
            player.change_room(self.RoomExitClassFromMap(self.map, self.exitsName[1]))



        