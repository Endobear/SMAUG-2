import pygame
from Salas.Room import Room
from Itens.Arrows import FrontArrow,BackArrow

class RoomTwo(Room):
    def __init__(self):
        super().__init__()
        self.room_name = "Room Two"
        self.room_description = "A Nice Room with Pink Walls"
        self.exits = ["Back"]
        self.ArrowSprites = pygame.sprite.Group(FrontArrow(),BackArrow())
        self.image = "graphics/Room2.png"
        self.exitsName = ["BackDoor","FrontDoor"]
        self.id = "RoomTwo"
    
    def backLocation(self):
        return self

    
    
    