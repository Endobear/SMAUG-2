import pygame
from Salas.Room import Room

from Itens.Arrows import BackArrow, FrontArrow

class EscolaCorredor1(Room):
    def __init__(self,map):
        super().__init__()
        self.room_name = "EscolaCorredor1"
        self.image = "graphics/Cenario 5/Corredor_armario_disponivel.png"
        self.exits = ["Front"]
        self.exitsName = ["Banheiro","Sala05","Sala01","Diretoria","Enfermaria"]
        self.map = map

        self.corredor2 = EscolaCorredor2(self)
        self.arrows = [FrontArrow((420,450))]

        self.interactives = {"armario": pygame.Rect((382,91),(158,298))}
        

        self.id = "EscolaCorredor1"
    
    def frontLocation(self):
        return self.corredor2
    
    # def ineractRect(self, rect, player):
    #     super().ineractRect(rect, player)
    #     if "screwdriver" in self.interactives and rect == self.interactives["screwdriver"]:
    #         self.image = "graphics/Cenario 4/Banheiro_Porta.png"
    #         self.interactives.pop("screwdriver")
    #         player.pickItem(Screwdriver())
    #     if rect == self.interactives["porta"]:
    #         # TODO Diálogo da porta trancada
    #         pass




class EscolaCorredor2(Room):
    def __init__(self,corredor1):
        super().__init__()
        self.room_name = "EscolaCorredor2"
        self.image = "graphics/Cenario 5/Corredor_diretoria_fechada.png"
        self.exits = ["Back"]
        self.corredor1 = corredor1
        self.porta_sala = False

        self.arrows = [BackArrow((420,450))]

        self.interactives = {"portaSala": pygame.Rect((314,203),(27,94)),
                             "PortaDiretoria": pygame.Rect((411,220),(30,32))}
        

        self.id = "EscolaCorredor2"
    
    def backLocation(self):

        return self.corredor1
        
    
    def ineractRect(self, rect, player):
        super().ineractRect(rect, player)
        if rect == self.interactives["portaSala"]:
            if self.porta_sala == False: 
                self.image = "graphics/Cenario 5/Corredor_diretoria_aberta.png"
                self.porta_sala = True
            else:
                player.change_room(self.corredor1.RoomExitClassFromMap(self.corredor1.map, self.corredor1.exitsName[1]))
        if rect == self.interactives["PortaDiretoria"]:
            player.change_room(self.corredor1.RoomExitClassFromMap(self.corredor1.map, self.corredor1.exitsName[3]))

