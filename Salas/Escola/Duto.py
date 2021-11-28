import pygame
from Salas.Room import Room
from Itens.Arrows import BackArrow, FrontArrow
from random import randint


class Duto(Room):
    def __init__(self,map,direction):
        super().__init__()
        self.room_name = "Duto"
        self.direction = direction

        if direction == "Left":
            image = "VentFront1.png"
        else: 
            image = "VentFront2.png"

        self.image = "graphics/Vents/" + image

        

        self.exits = ["Front","Back"]
        self.exitsName = ["Exit","Entrance"]
        self.map = map

        self.middle = DutoMiddle(self)

        
        self.arrows = [BackArrow((420,450)),FrontArrow((420,250))]
        

        self.id = "Duto"

    def frontLocation(self):
        return self.middle
    def backLocation(self):
        return self.RoomExitClassFromMap(self.map,self.exitsName[1])


class DutoMiddle(Room):
    def __init__(self, entrance):
        super().__init__()
        self.room_name = "Duto"
        self.entrance = entrance

        if entrance.direction == "Left":
            image = "VentLeft.png"
        else:
            image = "VentRight.png"
        
        self.image = "graphics/Vents/" + image

        self.exit = DutoExit(self)
        

        self.exits = ["Front","Back"]
        
        

        self.arrows = [BackArrow((420,450)),FrontArrow((420,250))]  
        

        self.id = "Duto"

    def frontLocation(self):
        return self.exit
    def backLocation(self):
        return self.entrance 


class DutoExit(Room):
    def __init__(self, middle):
        super().__init__()
        self.room_name = "Duto"
        self.middle = middle

        if self.middle.entrance.direction == "Left":
            image = "VentFront2.png"
        else: 
            image = "VentFront1.png"

        self.image = "graphics/Vents/" + image


        

        self.exits = ["Front","Back"]
     

        self.arrows = [BackArrow((420,450)),FrontArrow((420,250))]
        

        self.id = "Duto"

    def frontLocation(self):
        return self.middle.entrance.RoomExitClassFromMap(self.middle.entrance.map,self.middle.entrance.exitsName[0])
    def backLocation(self):
        return self.middle 
