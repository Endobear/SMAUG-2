import pygame
from Salas.Room import Room
from Salas.RoomTwo import RoomTwo

# Esta classe é a RoomOne, uma sala que tem outros cenários, esses outros cenários estão dentro de variáveis para não perder dados ao trocar de sala
class RoomOne(Room):
    def __init__(self):
        super().__init__()
        self.room_name = "Room One"
        self.room_description = "A Nice Room with White Walls"
        self.exits = ["Up","Front"]
        self.image = "graphics/Room1_closedDoor.png"
        # as seguintes salas estão em variáveis para evitar perda de dados
        self.roomOneDoor = RoomOneDoor(self) # Variável com a classe Room da porta
        self.roomOneCeiling = RoomOneCeiling(self)  # Variável com a classe Room do teto

        porta_rect = pygame.Rect((357,205),(90,121))
        seta_rect = pygame.Rect((384,68),(27,40))

        self.interactives = [porta_rect , seta_rect] # lista de retângulos interagíves, porta e seta. Mais tarde alguns desses retângulos terão seus próprios sprites
    
    def upLocation(self):
        return self.roomOneCeiling
    def frontLocation(self):
        if self.roomOneDoor.doorStatus == "Closed":
            return self.roomOneDoor
        else:
            return self.roomOneDoor.roomTwo

        
    def ineractRect(self,rect,player):
        if rect == self.interactives[0]: # porta
            player.currentRoom = self.getLocationFromDirection("Front")
           
        else: # Seta que vai para o teto da sala
            player.currentRoom = self.getLocationFromDirection("Up")


class RoomOneCeiling(Room):
    def __init__(self,previusRoom):
        super().__init__()
        self.room_name = "Ceiling"
        self.room_description = "The ceiling of the room, It dosen\'t have lights"
        self.exits = ["Back"]
        self.image = "graphics/Room1_ceiling.png"
        self.returnRoom = previusRoom

        seta = pygame.Rect((362,366),(39,45))
        self.interactives = [seta]
    
    def backLocation(self):
        return self.returnRoom

    def ineractRect(self,rect,player):
        if rect == self.interactives[0]: # Seta
            player.currentRoom = self.getLocationFromDirection("Back")
 
class RoomOneDoor(Room):
    def __init__(self,previusRoom):
        super().__init__()
        self.room_name = "Door"
        self.doorStatus = "Closed"
        self.room_description = "The door of the white room, it is " + self.doorStatus
        self.exits = ["Back"]
        self.image = "graphics/Room1_door"+self.doorStatus+".png"
        self.returnRoom = previusRoom
        self.roomTwo = RoomTwo(self)

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
       
        if rect == self.interactives[0]: # Porta
            
            if self.doorStatus == "Closed":
                
                self.doorStatus = "Open"
                self.image = "graphics/Room1_door"+self.doorStatus+".png"
                self.exits.append("Front")
                self.returnRoom.image = "graphics/Room1_openDoor.png"
            else:
                player.currentRoom = self.getLocationFromDirection("Front")
                

    def frontLocation(self):
        if "Front" in self.exits:
            return self.roomTwo
        else:
            return self

    def backLocation(self):
        return self.returnRoom
