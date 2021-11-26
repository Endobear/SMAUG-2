import pygame
from Salas.Room import Room

from Itens.Arrows import BackArrow

class EscolaBanheiro(Room):
    def __init__(self,map):
        super().__init__()
        self.room_name = "EscolaBanheiro"
        self.image = "graphics/Cenario 4/Banheiro_Porta_item.png"
        self.exits = ["Back"]
        self.exitsName = ["Ventilacao","Porta"]
        self.map = map
        self.banheiroCabines = BanheiroCabines(self)

        self.arrows = [BackArrow((420,450))]

        self.interactives = {"porta": pygame.Rect((153,89),(186,133))}
        

        self.id = "EscolaBanheiro"
    
    def backLocation(self):

        return self.banheiroCabines
    
    def ineractRect(self, rect, player):
        super().ineractRect(rect, player)
        # if rect == self.interactives["porta"]:
        #     player.change_room(self.espelho)




class BanheiroCabines(Room):
    def __init__(self,banheiro):
        super().__init__()
        self.room_name = "BanheiroCabine"
        self.image = "graphics/Cenario 4/espelho.png"
        self.exits = ["Back"]
        self.banheiro = banheiro

        
        self.arrows = [BackArrow((420,450))]

        self.interactives = {"espelho": pygame.Rect((106,25),(621,424))}
        

        self.id = "SalaEspelho"
    
    def backLocation(self):

        return self.sala
    
    # def ineractRect(self, rect, player):
    #     super().ineractRect(rect, player)
    #     if rect == self.interactives["espelho"]:
    #         player.change_room()



        