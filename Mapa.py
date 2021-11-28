import pygame
from Salas.CasaCorredor import CasaCorredor
from Salas.CasaSala import CasaSala
from Salas.Escola.EscolaBanheiro import EscolaBanheiro
from Salas.Escola.EscolaCorredor import EscolaCorredor1
from Salas.Escola.EscolaEnfermaria import EscolaEnfermaria
from Salas.Escola.EscolaSala01 import Sala01
from Salas.Escola.EscolaSala05 import Sala05
from Salas.Escola.Duto import Duto
from Salas.Player import Player
from Salas.Quarto import Quarto
# from Salas.RoomOne import RoomOne
# from Salas.RoomTwo import RoomTwo

class Mapa():
    def __init__(self):

        casa = [Quarto(self),CasaCorredor(self),CasaSala(self)]
        escola = [EscolaBanheiro(self),EscolaCorredor1(self), Sala05(self), Duto(self,"Right"), Sala01(self), EscolaEnfermaria(self) ]
        self.rooms = casa + escola
        self.player = Player()
        self.monstro = Monstro(self.rooms[2])

        self.music_player = pygame.mixer.music;
        self.monstro.spawn(self.monstro.room)


        self.exitsList = {
            "Quarto":{"QuartoPorta": self.rooms[1]},
            "CasaCorredor": {"CorredorQuarto":self.rooms[0].quartoPorta, "CorredorSala": self.rooms[2]},
            "CasaSala": {"CasaSalaSaida": self.rooms[1]},
            "EscolaBanheiro": {"Ventilacao": self.rooms[4]},
            "EscolaCorredor1":{"Banheiro": self.rooms[3], "Sala05": self.rooms[5], "Sala01" : self.rooms[7], "Enfermaria": self.rooms[8]},
            "Sala05": {"Porta": self.rooms[4].corredor2, "Duto" : self.rooms[6]},
            "Duto": {"Entrance": self.rooms[5], "Exit": self.rooms[6]},
            "Sala01": {"Porta" : self.rooms[4]},
            "EscolaEnfermaria": {"Porta": self.rooms[4].corredor2}
        }
        # self.rooms = [RoomOne(self),RoomTwo(self)]
        # self.exitsList = {
        #     "RoomOne":{"FrontDoor": self.rooms[1]},
        #     "RoomTwo": {"BackDoor":self.rooms[0], "FrontDoor":"RoomThree"}
        # }
        


    def change_exit(self, room,exit,newExit):
        self.exitsList[room][exit] = newExit

    def getRoomById(self,id):
        for room in self.rooms:
            if id == room.id:
                return room
    
    def buildVentPath(self,entrance,exit,direction):
        
        self.rooms[6].direction = direction
        self.change_exit(self.rooms[6].id,"Exit",exit)
        self.change_exit(self.rooms[6].id,"Entrance",entrance)
        return self.rooms[6]
        




    def update(self,screen):
        if self.player.currentRoom == self.monstro.room and self.player.currentRoom.monsterSpawnabble == True:
            print("I'm here")
            
            if self.music_player.get_pos() < 0:
                self.music_player.load("audio/Music/Tenssion.mp3")
                self.music_player.play(loops = -1)
            self.player.vida -= 0.25
            screen.blit(self.monstro.surface, self.monstro.rect)
        

class Monstro():
    def __init__(self,room) -> None:
        self.room = room
        self.image = "graphics/Monstro/Parado.png" 
        self.surface = pygame.image.load(self.image).convert_alpha()
        self.rect = self.surface.get_rect(center = (250,250))
        self.chasing = False
        self.spawnabble = False

    def spawn(self,room):
        self.surface = pygame.transform.scale(pygame.image.load(self.image).convert_alpha(), (room.monsterLocation["width"], room.monsterLocation["height"]))
        self.rect = self.surface.get_rect(center = room.monsterLocation["position"])
        self.room = room
        self.spawnabble = False
    
    def despawn(self):
        pygame.mixer.music.fadeout(3000)
        self.room = ""
        self.spawnabble = True


        