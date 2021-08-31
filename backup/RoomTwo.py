from Salas.Room import Room
class RoomTwo(Room):
    def __init__(self,previusRoom):
        super().__init__()
        self.room_name = "Room Two"
        self.room_description = "A Nice Room with Pink Walls"
        self.exits = ["Back"]
        self.image = "graphics/Room2.png"
        self.returnRoom = previusRoom
        self.id = "RoomTwo"
    
    def backLocation(self):
        return self.returnRoom
    
    
    