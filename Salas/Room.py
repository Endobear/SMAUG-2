class Room():
    def __init__(self):
        self.room_name = ""
        self.room_description = ""
        self.exits = []
        self.image = ""
        self.interactives = []

    def change_location(self,location):
        if location in self.exits:
            return self.getLocationFromDirection(location)

    def getLocationFromDirection(self,direction):
        if direction in self.exits:
            if direction == "Up":
                return self.upLocation()
            if direction == "Back":
                return self.backLocation()
            if direction == "Front":
                return self.frontLocation()

    def interact(self):
      self.interactMessage = "There is nothing to interact"
            
    def upLocation(self):
        return
    def backLocation(self):
        return
    def frontLocation(self):
        return 
    




