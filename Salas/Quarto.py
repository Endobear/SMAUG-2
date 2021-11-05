import pygame
from Salas.Room import Room
from Itens.Arrows import FrontArrow,BackArrow,UpArrow

class Quarto(Room):
    def __init__(self):
        super().__init__()
        self.room_name = "Quarto"
        self.image = "graphics/Quarto.jpg"
        self.exits = ["Up","Back"]
        self.exitsName = ["QuartoPorta"]
        
        self.arrows = [BackArrow((380,366))]
        
        self.comoda = QuartoComoda(self)
        self.quartoPorta = QuartoPorta(self)
        self.quartoTeto = QuartoTeto(self)

        self.id = "Quarto"

        comoda_rect = pygame.Rect((355,327),(129,136))
        self.interactives = [comoda_rect]

    
    def backLocation(self):
        return self.quartoPorta
    def upLocation(self):
        return self.quartoTeto


    def ineractRect(self,rect,player):
        super().ineractRect(rect,player)
        if rect == self.interactives[0]: # Cômoda do quarto
            player.currentRoom = self.comoda


class QuartoComoda(Room):
    def __init__(self,quarto):
        super().__init__()
        self.room_name = "QuartoComoda"
        self.exits = ["Back"]
        self.image = "graphics/Room1_closedDoor.png"
    


class QuartoPorta(Room):
    def __init__(self,quarto):
        super().__init__()
        self.room_name = "QuartoPorta"
        self.exits = ["Back","Up"]
        self.image = "graphics/Quarto_porta_fechada.png"
        self.arrows = [BackArrow((486,431))]
        self.quarto = quarto


        porta_rect = pygame.Rect((409,103),(165,314))
        self.interactives = [porta_rect]
        
    def backLocation(self):
        return self.quarto


class QuartoTeto(Room):
    def __init__(self,quarto):
        super().__init__()
        self.room_name = "QuartoTeto"
        self.exits = ["Back"]
        self.image = "graphics/Room1_closedDoor.png"

        

        