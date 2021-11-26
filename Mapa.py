from Salas.CasaCorredor import CasaCorredor
from Salas.CasaSala import CasaSala
from Salas.Player import Player
from Salas.Quarto import Quarto
# from Salas.RoomOne import RoomOne
# from Salas.RoomTwo import RoomTwo

class Mapa():
    def __init__(self):

        casa = [Quarto(self),CasaCorredor(self),CasaSala(self)]
        self.rooms = casa
        self.player = Player()
        self.exitsList = {
            "Quarto":{"QuartoPorta": self.rooms[1]},
            "CasaCorredor": {"CorredorQuarto":self.rooms[0].quartoPorta, "CorredorSala": self.rooms[2]},
            "CasaSala": {"CasaSalaSaida": self.rooms[1]}
        }
        # self.rooms = [RoomOne(self),RoomTwo(self)]
        # self.exitsList = {
        #     "RoomOne":{"FrontDoor": self.rooms[1]},
        #     "RoomTwo": {"BackDoor":self.rooms[0], "FrontDoor":"RoomThree"}
        # }
        



    
    def update():

        pass
    
    
