import pygame
from Salas.Room import Room

from Itens.Arrows import BackArrow
from Itens.Itens import Screwdriver

from Itens.Itens import KeyItem

class EscolaEnfermaria(Room):
    def __init__(self,map):
        super().__init__()
        self.room_name = "EscolaEnfermaria"
        self.image = "graphics/Cenario 8/Enfermaria.png"
        self.exitsName = ["Porta","Duto"]
        self.map = map

        self.exits = ["Back"]
        self.arrows = [BackArrow((486,431))]

        chave = KeyItem(id ="Sala01", image ="graphics/key_bronze.png")
        chave.rect.x = 599
        chave.rect.y = 411

        self.itens = [chave]

        
        self.duto = Duto(self)

        self.interactives = {"duto": pygame.Rect((742,309),(100,109)), "armario": pygame.Rect((514,95),(171,302))}
        

        self.id = "EscolaEnfermaria"
    
    def backLocation(self):
        self.map.getRoomById("EscolaCorredor1").corredor2.enfermaria = True
        return self.RoomExitClassFromMap(self.map,self.exitsName[0])
    
    def ineractRect(self, rect, player):
        super().ineractRect(rect, player)

        if rect == self.interactives["armario"]:
            pass

        if rect == self.interactives["duto"]:
            player.change_room(self.duto)

    def update(self, screen):
        if self.map.player.vida < 100:
            self.map.player.vida += 1
        else:
            self.map.player.vida = 100
        return super().update(screen)
            
            





class Duto(Room):
    def __init__(self,enfermaria):
        super().__init__()
        self.room_name = "EnfermariaDuto"
        self.image = "graphics/Cenario 8/Enfermaria_Duto.png"
        self.exits = ["Back"]
        self.enfermaria = enfermaria
        
        self.arrows = [BackArrow((420,450))]

        self.interactives = {"duto": pygame.Rect((107,38),(637,420))}
        

        self.id = "EnfermariaDuto"
    
    def backLocation(self):
        return self.enfermaria
    
    def ineractRect(self, rect, player):
        super().ineractRect(rect, player)
        if rect == self.interactives["duto"]:
             player.change_room(self.enfermaria.map.buildVentPath(self.enfermaria, self.enfermaria.map.rooms[5], "Right" ))
