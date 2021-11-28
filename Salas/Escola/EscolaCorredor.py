import pygame
from Salas.Room import Room

from Itens.Arrows import BackArrow, FrontArrow, DiagonalArrow

class EscolaCorredor1(Room):
    def __init__(self,map):
        super().__init__()
        self.room_name = "EscolaCorredor1"
        self.image = "graphics/Cenario 5/Corredor_armario_disponivel.png"
        self.exits = ["Front","Back"]
        self.exitsName = ["Banheiro","Sala05","Sala01","Diretoria","Enfermaria","Saida"]
        self.map = map

        self.corredor2 = EscolaCorredor2(self)
        self.exitDoor = EscolaSaida(self)
        self.arrows = [FrontArrow((420,450)), DiagonalArrow( (127,450), -90)]

        self.interactives = {"armario": pygame.Rect((726,108),(75,358)), "sala01": pygame.Rect((279,192),(37,125))}
        

        self.id = "EscolaCorredor1"
    
    def frontLocation(self):
        return self.corredor2

    def backLocation(self):
        return self.exitDoor
    
    def ineractRect(self, rect, player):
        super().ineractRect(rect, player)
        if rect == self.interactives["sala01"]:
            player.change_room(self.RoomExitClassFromMap(self.map,self.exitsName[2]))




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
        
        self.portaDiretoria = EscolaPortaDiretoria(self)

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
            player.change_room(self.portaDiretoria)

class EscolaPortaDiretoria(Room):
    def __init__(self,corredor2):
        super().__init__()
        self.room_name = "EscolaPortaDiretoria"
        self.image = "graphics/Cenario 5/Corredor_diretoria_porta_False.png"
        self.exits = ["Back"]
        self.corredor2 = corredor2
        self.porta_sala = False

        self.arrows = [BackArrow((420,450))]

        self.interactives = {"PortaDiretoria": pygame.Rect((411,220),(30,32))}
        

        self.id = "EscolaPortaDiretoria"
    
    def backLocation(self):

        return self.corredor2
        
    
    def ineractRect(self, rect, player):
        super().ineractRect(rect, player)
        if rect == self.interactives["PortaDiretoria"]:
            player.change_room(self.corredor2.corredor1.RoomExitClassFromMap(self.corredor2.corredor1.map, self.corredor2.corredor1.exitsName[3]))

class EscolaSaida(Room):
    def __init__(self,corredor1):
        super().__init__()
        self.room_name = "EscolaSaida"
        self.image = "graphics/Cenario 5/corredor_saida_fechada.png"
        self.exits = ["Back"]
        self.corredor1 = corredor1
        self.porta_sala = False

        self.arrows = [BackArrow((420,450))]

        self.interactives = {"PortaSaida": pygame.Rect((411,220),(30,32))}
        

        self.id = "EscolaSaida"
    
    def backLocation(self):

        return self.corredor1
        
    
    def ineractRect(self, rect, player):
        super().ineractRect(rect, player)
        if rect == self.interactives["PortaSaida"]:
            player.change_room(self.corredor1.RoomExitClassFromMap(self.corredor1.map, self.corredor1.exitsName[5]))

