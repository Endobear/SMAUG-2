import pygame
from Salas.Room import Room
from Itens.Arrows import FrontArrow,BackArrow,UpArrow

class Quarto(Room):
    def __init__(self):
        super().__init__()
        self.room_name = "Quarto"
        self.exits = ["Up","Front"]
        self.exitsName = ["FrontDoor"]
        self.image = "graphics/Quarto.jpg"
        
        