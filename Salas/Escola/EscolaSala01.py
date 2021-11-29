import pygame
from Salas.Room import Room

from Itens.Arrows import BackArrow, FrontArrow
from Itens.Itens import KeyItem, Screwdriver

class Sala01(Room):
    def __init__(self,map):
        super().__init__()
        self.room_name = "Sala01"
        self.image = "graphics/Cenario 7/sala01_gaveta_fechada.png"
        self.exitsName = ["Porta"]
        self.map = map

        self.gaveta = False

        self.interactives = {"gaveta": pygame.Rect((507,262),(93,79)),"porta": pygame.Rect((318,131),(151,257))}
        

        self.id = "Sala01"
    
    # def frontLocation(self):
    #     return self.corredor2
    
    def ineractRect(self, rect, player):
        super().ineractRect(rect, player)
        if rect == self.interactives["gaveta"]:
            if self.gaveta == False:
                self.image = "graphics/Cenario 7/sala01_gaveta_aberta.png"
                player.pickItem(KeyItem(id = "Diretoria", image ="graphics/key_silver.png"))

        if rect == self.interactives["porta"]:
           
            player.change_room(self.RoomExitClassFromMap(self.map,self.exitsName[0]))
            
            


