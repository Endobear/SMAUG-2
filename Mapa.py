from Salas.RoomOne import RoomOne
from Salas.RoomTwo import RoomTwo

class Mapa():
    def __init__(self):
        self.rooms = [RoomOne(self),RoomTwo(self)]
        self.exitsList = {
            "RoomOne":{"FrontDoor": self.rooms[1]},
            "RoomTwo": {"BackDoor":self.rooms[0], "FrontDoor":"RoomThree"}
        }

    

    
    
