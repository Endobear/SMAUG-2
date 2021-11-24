import pygame
from Salas.Room import Room
from Itens.Arrows import FrontArrow,BackArrow,UpArrow,DiagonalArrow
from Dialog_manager import Dialog_manager 

class Quarto(Room):
    def __init__(self):
        super().__init__()
        self.room_name = "Quarto"
        self.image = "graphics/Cenario 1/Quarto_gaveta_fechada.png"
        self.exits = ["Up","Back"]
        self.exitsName = ["QuartoPorta"]
        
        self.arrows = [BackArrow((420,450))]
        
        self.gaveta = QuartoGaveta(self)
        self.quartoPorta = QuartoPorta(self)
        self.quartoTeto = QuartoTeto(self)

        self.id = "Quarto"

        

    
    def backLocation(self):
        return self.quartoPorta
    def upLocation(self):
        if len(self.interactives) < 1:
            self.addRect(pygame.Rect((355,327),(129,136)))
        return self.quartoTeto


    def ineractRect(self,rect,player):
        super().ineractRect(rect,player)
        if len(self.interactives) > 0:
            if rect == self.interactives[0]: # Cômoda do quarto
                player.currentRoom = self.gaveta
                self.image = "graphics/Cenario 1/Quarto_gaveta_aberta.png"
                self.quartoTeto.image = "graphics/Cenario 1/Teto_gaveta_aberta.png"


class QuartoGaveta(Room):
    def __init__(self,quarto):
        super().__init__()
        self.room_name = "QuartoGaveta"
        self.exits = ["Back"]
        self.arrows = [BackArrow((42,385))]
        self.quarto = quarto
        self.image = "graphics/Cenario 1/gaveta_gancho.png"

    def backLocation(self):
        return self.quarto



class QuartoPorta(Room):
    def __init__(self,quarto):
        super().__init__()
        self.room_name = "QuartoPorta"
        self.exits = ["Back","Up"]
        self.image = "graphics/Cenario 1/Quarto_porta_fechada.png"
        self.arrows = [BackArrow((486,431))]
        self.quarto = quarto


        porta_rect = pygame.Rect((409,103),(165,314))
        self.interactives = [porta_rect]
        
    def backLocation(self):
        return self.quarto

    def ineractRect(self,rect,player):
        super().ineractRect(rect,player)
        if len(self.interactives) > 0:
            if rect == self.interactives[0]: # Porta
                player.dialog_manager.set_dialog("interacao_porta")
                if len(self.quarto.arrows) < 2:
                    self.quarto.arrows.append(UpArrow((420,100)))
              


class QuartoTeto(Room):
    def __init__(self,quarto):
        super().__init__()
        self.room_name = "QuartoTeto"
        self.exits = ["Back"]
        self.arrows = [DiagonalArrow( (127,425), -90)]
        self.image = "graphics/Cenario 1/Teto_gaveta_fechada.png"
        self.quarto = quarto

    def backLocation(self):
        return self.quarto


        

        