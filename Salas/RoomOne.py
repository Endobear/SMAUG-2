from Salas.Room import Room
from Salas.RoomTwo import RoomTwo

class RoomOne(Room):
    def __init__(self):
        super().__init__()
        self.room_name = "Room One"
        self.room_description = "A Nice Room with White Walls"
        self.exits = ["Up","Front"]
        self.image = "graphics/amongus.png"
        self.roomOneDoor = RoomOneDoor(self)
        self.roomOneCeiling = RoomOneCeiling(self)
    
    def upLocation(self):
        return self.roomOneCeiling
    def frontLocation(self):
        return self.roomOneDoor

class RoomOneCeiling(Room):
    def __init__(self,previusRoom):
        super().__init__()
        self.room_name = "Ceiling"
        self.room_description = "The ceiling of the room, It dosen\'t have lights"
        self.exits = ["Back"]
        self.image = "graphics/amongus.png"
        self.returnRoom = previusRoom
    
    def backLocation(self):
        return self.returnRoom
 
class RoomOneDoor(Room):
    def __init__(self,previusRoom):
        super().__init__()
        self.room_name = "Door"
        self.doorStatus = "closed"
        self.room_description = "The door of the white room, it is " + self.doorStatus
        self.exits = ["Back"]
        self.image = "graphics/amongus.png"
        self.returnRoom = previusRoom
        self.roomTwo = RoomTwo(self)
    
    
    def interact(self):
        if self.doorStatus == "closed":
            self.interactMessage = "You opened the door"
            self.doorStatus = "open"
            self.room_description = "The door of the white room, it is " + self.doorStatus
            self.exits.append("Front")
        else:
            self.interactMessage = "You opened the door"

    def frontLocation(self):
        if "Front" in self.exits:
            return self.roomTwo
        else:
            return self

    def backLocation(self):
        return self.returnRoom
