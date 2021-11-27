import pygame
from Salas.Room import Room

from Itens.Arrows import BackArrow

class CasaSala(Room):
    def __init__(self,map):
        super().__init__()
        self.room_name = "CasaSala"
        self.image = "graphics/Cenario 3/sala.png"
        self.exits = ["Back"]
        self.exitsName = ["CasaSalaSaida"]
        self.map = map
        self.espelho = SalaEspelho(self)

        self.arrows = [BackArrow((420,450))]

        self.interactives = {"espelho": pygame.Rect((153,89),(186,133))}
        
        self.monsterSpawnabble = False
        self.monsterLocation = [(240,500)]

        self.id = "CasaSala"
    
    def backLocation(self):

        return self.RoomExitClassFromMap(self.map,self.exitsName[0])
    
    def ineractRect(self, rect, player):
        super().ineractRect(rect, player)
        if rect == self.interactives["espelho"]:
            player.change_room(self.espelho)



class SalaEspelho(Room):
    def __init__(self,sala):
        super().__init__()
        self.room_name = "SalaEspelho"
        self.image = "graphics/Cenario 3/espelho.png"
        self.exits = ["Back"]
        self.sala = sala

        
        self.arrows = [BackArrow((420,450))]

        self.interactives = {"espelho": pygame.Rect((106,25),(621,424))}
        

        self.id = "SalaEspelho"
    
    def backLocation(self):
        self.sala.map.change_exit("CasaCorredor","CorredorQuarto",self.sala.map.rooms[3])
        return self.sala
    
    # def ineractRect(self, rect, player):
    #     super().ineractRect(rect, player)
    #     if rect == self.interactives["espelho"]:
    #         player.change_room()



        