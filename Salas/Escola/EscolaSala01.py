import pygame
from Salas.Room import Room

from Itens.Arrows import BackArrow, FrontArrow
from Itens.Itens import Screwdriver

class Sala01(Room):
    def __init__(self,map):
        super().__init__()
        self.room_name = "Sala01"
        self.image = "graphics/Cenario 6/Sala05_porta_True_duto_False.png"
        # self.exits = ["Front"]
        self.exitsName = ["Porta","Duto"]
        self.map = map

        self.porta = True
        self.duto = Duto(self)
        # self.arrows = [FrontArrow((420,450))]

        self.interactives = {"duto": pygame.Rect((579,291),(98,66)), "saida": pygame.Rect((729,97),(98,346)), "porta": pygame.Rect((613,130),(119,260))}
        

        self.id = "Sala05"
    
    # def frontLocation(self):
    #     return self.corredor2
    
    def ineractRect(self, rect, player):
        super().ineractRect(rect, player)
        if rect == self.interactives["saida"]:
            if self.porta == True:
                player.change_room(self.RoomExitClassFromMap(self.map,self.exitsName[0]))
            else:
                self.porta = True
                self.image = "graphics/Cenario 6/Sala05_porta_"+ str(self.porta) +"_duto_"+ str(self.duto.duto_status) + ".png"
                

        if rect == self.interactives["porta"]:
            if self.porta == True:
                self.porta = False
                self.image = "graphics/Cenario 6/Sala05_porta_"+ str(self.porta) +"_duto_"+ str(self.duto.duto_status) + ".png"

        if rect == self.interactives["duto"]:
            if self.porta == False:
                player.change_room(self.duto)
            
            





class Duto(Room):
    def __init__(self,sala05):
        super().__init__()
        self.room_name = "Sala05Duto"
        self.image = "graphics/Cenario 6/Duto_fechado.png"
        self.exits = ["Back"]
        self.sala05 = sala05
        self.duto_status = False
        
        self.arrows = [BackArrow((420,450))]

        self.interactives = {"duto": pygame.Rect((77,75),(721,195))}
        

        self.id = "Sala05Duto"
    
    def backLocation(self):
        return self.sala05
    

    def useItem(self, rect, player):
        itemHolding = player.itemHolding.sprites()[0]
        if rect in [interactives for interactives in self.interactives.values()]:
            if rect == self.interactives["duto"] and itemHolding.type == Screwdriver().type:
                self.image = "graphics/Cenario 6/Duto_aberto.png"
                self.duto_status = True
                self.sala05.image = "graphics/Cenario 6/Sala05_porta_"+ str(self.sala05.porta) +"_duto_"+ str(self.duto_status) + ".png"
                



    def ineractRect(self, rect, player):
        super().ineractRect(rect, player)
        if rect == self.interactives["duto"] and self.duto_status:
            player.change_room(self.sala05.RoomExitClassFromMap(self.sala05.map,self.sala05.exitsName[1]))
