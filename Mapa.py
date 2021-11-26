from Salas.CasaCorredor import CasaCorredor
from Salas.CasaSala import CasaSala
from Salas.Escola.EscolaBanheiro import EscolaBanheiro
from Salas.Escola.EscolaCorredor import EscolaCorredor1
from Salas.Player import Player
from Salas.Quarto import Quarto
# from Salas.RoomOne import RoomOne
# from Salas.RoomTwo import RoomTwo

class Mapa():
    def __init__(self):

        casa = [Quarto(self),CasaCorredor(self),CasaSala(self)]
        escola = [EscolaBanheiro(self),EscolaCorredor1(self)]
        self.rooms = casa + escola
        self.player = Player()
        self.exitsList = {
            "Quarto":{"QuartoPorta": self.rooms[1]},
            "CasaCorredor": {"CorredorQuarto":self.rooms[0].quartoPorta, "CorredorSala": self.rooms[2]},
            "CasaSala": {"CasaSalaSaida": self.rooms[1]},
            "EscolaBanheiro": {"Ventilacao": self.rooms[4]},
            "EscolaCorredor1":{"Banheiro": self.rooms[3]}
        }
        # self.rooms = [RoomOne(self),RoomTwo(self)]
        # self.exitsList = {
        #     "RoomOne":{"FrontDoor": self.rooms[1]},
        #     "RoomTwo": {"BackDoor":self.rooms[0], "FrontDoor":"RoomThree"}
        # }
        


    def change_exit(self, room,exit,newExit):
        self.exitsList[room][exit] = newExit
    
    def update():

        pass
    
    
