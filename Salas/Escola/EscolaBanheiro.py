import pygame
from Salas.Room import Room

from Itens.Arrows import BackArrow
from Itens.Itens import Screwdriver

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

        self.interactives = {"porta": pygame.Rect((382,91),(158,298)),
                             "screwdriver": pygame.Rect((268,384),(48,17))}
        

        self.id = "EscolaBanheiro"
    
    def backLocation(self):

        return self.banheiroCabines
    
    def ineractRect(self, rect, player):
        super().ineractRect(rect, player)
        if "screwdriver" in self.interactives and rect == self.interactives["screwdriver"]:
            self.image = "graphics/Cenario 4/Banheiro_Porta.png"
            self.interactives.pop("screwdriver")
            player.pickItem(Screwdriver())
        if rect == self.interactives["porta"]:
            # TODO Diálogo da porta trancada
            pass




class BanheiroCabines(Room):
    def __init__(self,banheiro):
        super().__init__()
        self.room_name = "BanheiroCabines"
        self.image = "graphics/Cenario 4/Banheiro_cabine_fechada.png"
        self.exits = ["Back"]
        self.banheiro = banheiro
        self.porta_cabine = False
        self.cabine = Cabine(self)
        self.teto = BanheiroTeto(self)
        
        self.arrows = [BackArrow((420,450))]

        self.interactives = {"cabineDestrancada": pygame.Rect((257,88),(40,292)),
                             "cabinesTrancadas": pygame.Rect((0,26),(248,430))}
        

        self.id = "BanheiroCabines"
    
    def backLocation(self):

        return self.banheiro
    
    def ineractRect(self, rect, player):
        super().ineractRect(rect, player)
        if rect == self.interactives["cabineDestrancada"]:
            if self.porta_cabine == False:
                self.image = "graphics/Cenario 4/Banheiro_cabine_aberta.png"
                self.porta_cabine = True
            else:
                player.change_room(self.cabine)

        if "carrinho" in self.interactives and rect == self.interactives["carrinho"]:
            player.change_room(self.teto)

class Cabine(Room):
    def __init__(self,banheiroCabines):
        super().__init__()
        self.room_name = "CabineBanheiro"
        self.image = "graphics/Cenario 4/Cabine_carrinho.png"
        self.exits = ["Back"]
        self.banheiroCabines = banheiroCabines

        
        self.arrows = [BackArrow((420,450))]

        self.interactives = {"carrinho": pygame.Rect((381,31),(289,449))}
        

        self.id = "CabineBanheiro"
    
    def backLocation(self):

        return self.banheiroCabines
    
    def ineractRect(self, rect, player):
        super().ineractRect(rect, player)
        if "carrinho" in self.interactives and rect == self.interactives["carrinho"]:
            self.image = "graphics/Cenario 4/Cabine.png"
            self.interactives.pop("carrinho")
            self.banheiroCabines.image = "graphics/Cenario 4/Banheiro_cabine_carrinho.png"
            self.banheiroCabines.interactives["carrinho"] = pygame.Rect((293,198),(207,178))
        


class BanheiroTeto(Room):
    def __init__(self,banheiroCabines):
        super().__init__()
        self.room_name = "BanheiroTeto"
        self.image = "graphics/Cenario 4/Duto_fechado.png"
        self.exits = ["Back"]
        self.banheiroCabines = banheiroCabines
        self.duto_status = False
        
        self.arrows = [BackArrow((420,450))]

        self.interactives = {"duto": pygame.Rect((77,75),(721,195))}
        

        self.id = "BanheiroTeto"
    
    def backLocation(self):
        return self.banheiroCabines
    

    def useItem(self, rect, player):
        itemHolding = player.itemHolding.sprites()[0]
        if rect in [interactives for interactives in self.interactives.values()]:
            if rect == self.interactives["duto"] and itemHolding.type == Screwdriver().type:
                self.image = "graphics/Cenario 4/Duto_aberto.png"
                self.banheiroCabines.image = "graphics/Cenario 4/Cabine_carrinho_duto.png"
                self.duto_status = True



    # def ineractRect(self, rect, player):
    #     super().ineractRect(rect, player)
    #     if rect == self.interactives["cabineDestrancada"]:
    #         if self.porta_cabine == False:
    #             self.image = "graphics/Cenario 4/Banheiro_cabine_fechada.png"
    #             self.porta_cabine = True
    #         else:
    #             pass
