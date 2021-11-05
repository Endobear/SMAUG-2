import pygame
from Salas.Room import Room
from Itens.Arrows import FrontArrow,BackArrow,UpArrow

# Esta classe é a RoomOne, uma sala que tem outros cenários, esses outros cenários estão dentro de variáveis para não perder dados ao trocar de sala
class RoomOne(Room):
    def __init__(self,map):
        super().__init__()
        self.room_name = "Room One"
        self.room_description = "A Nice Room with White Walls"
        self.exits = ["Up","Front"]
        self.exitsName = ["FrontDoor"]
        self.image = "graphics/Room1_closedDoor.png"
        

        self.arrows = [UpArrow((400,100))]

        # as seguintes salas estão em variáveis para evitar perda de dados
        self.roomOneDoor = RoomOneDoor(self) # Variável com a classe Room da porta
        self.roomOneCeiling = RoomOneCeiling(self)  # Variável com a classe Room do teto
        self.id = "RoomOne"
        self.map = map
        

        # TODO colocar retângulos e setas em uma classe diferente
        porta_rect = pygame.Rect((357,205),(90,121))

        self.interactives = [porta_rect] # lista de retângulos interagíves, porta e seta. Mais tarde alguns desses retângulos terão seus próprios sprites

    
    
    def upLocation(self):
        return self.roomOneCeiling
        
    def frontLocation(self):
        if self.roomOneDoor.doorStatus == "Closed":
            return self.roomOneDoor
        else:
            return self.RoomExitClassFromMap(self.map, self.exitsName[0])

        
    def ineractRect(self,rect,player):
        super().ineractRect(rect,player)
        if rect == self.interactives[0]: # Porta da sala
            player.currentRoom = self.getLocationFromDirection("Front")


class RoomOneCeiling(Room):
    def __init__(self,RoomOne):
        super().__init__()
        self.room_name = "Ceiling"
        self.room_description = "The ceiling of the room, It dosen\'t have lights"
        self.exits = ["Back"]

        self.arrows = [BackArrow((380,366))]
        self.image = "graphics/Room1_ceiling.png"
        self.RoomOne = RoomOne
        self.id = "RoomOneCeiling"

    
    def backLocation(self):
        return self.RoomOne

  
class RoomOneDoor(Room):
    def __init__(self,RoomOne):
        super().__init__()
        self.room_name = "Door"
        self.doorStatus = "Closed"
        self.room_description = "The door of the white room, it is " + self.doorStatus
        self.exits = ["Back"]
        
        self.arrows = [BackArrow((390,446))]

        self.image = "graphics/Room1_door"+self.doorStatus+".png"
        self.RoomOne = RoomOne
        self.id = "RoomOneDoor"

        porta = pygame.Rect((270,68),(262,336))
        self.interactives = [porta]
    
    
    def interact(self):
        if self.doorStatus == "Closed":
            self.interactMessage = "You opened the door"
            self.doorStatus = "Open"
            self.room_description = "The door of the white room, it is " + self.doorStatus
            self.image = "graphics/Room1_door"+self.doorStatus+".png"
            self.exits.append("Front")
        else:
            self.interactMessage = "You opened the door"

    def ineractRect(self,rect,player):
        super().ineractRect(rect,player)
        if rect == self.interactives[0]: # Porta
            
            if self.doorStatus == "Closed":
                
                self.doorStatus = "Open"
                self.image = "graphics/Room1_door"+self.doorStatus+".png"
                self.exits.append("Front")
                self.RoomOne.image = "graphics/Room1_openDoor.png"
            else:
                player.currentRoom = self.frontLocation()

            
                

    def frontLocation(self):
        if "Front" in self.exits:
            return self.RoomOne.RoomExitClassFromMap(self.RoomOne.map, self.RoomOne.exitsName[0])
        else:
            return self

    def backLocation(self):
        return self.RoomOne
