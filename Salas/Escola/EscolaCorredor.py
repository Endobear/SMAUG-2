import pygame
from Salas.Room import Room

from Itens.Arrows import BackArrow, FrontArrow

class EscolaCorredor1(Room):
    def __init__(self,map):
        super().__init__()
        self.room_name = "EscolaCorredor1"
        self.image = "graphics/Cenario 5/Corredor_armario_disponivel.png"
        self.exits = ["Front"]
        self.exitsName = ["Banheiro","Sala","Diretoria","Enfermaria"]
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
        self.image = "graphics/Cenario 5/Corredor_diretoria.png"
        self.exits = ["Back"]
        self.corredor1 = corredor1
        self.porta_cabine = False

        self.arrows = [BackArrow((420,450))]

        self.interactives = {"portaSala": pygame.Rect((257,88),(40,292)),
                             "PortaDiretoria": pygame.Rect((0,26),(248,430))}
        

        self.id = "EscolaCorredor2"
    
    def backLocation(self):

        return self.corredor1
    
    # def ineractRect(self, rect, player):
    #     super().ineractRect(rect, player)
    #     if rect == self.interactives["cabineDestrancada"]:
    #         if self.porta_cabine == False:
    #             self.image = "graphics/Cenario 5/Banheiro_cabine_aberta.png"
    #             self.porta_cabine = True
    #         else:
    #             player.change_room(self.cabine)

    #     if "carrinho" in self.interactives and rect == self.interactives["carrinho"]:
    #         player.change_room(self.teto)

