import pygame
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
        self.monstro = Monstro(self.rooms[2])

        self.music_player = pygame.mixer.music;
        self.monstro.spawn(self.monstro.room,self)


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
    
    def update(self,screen):
        if self.player.currentRoom == self.monstro.room and self.player.currentRoom.monsterSpawnabble == True:
            print("I'm here")
            if self.music_player.get_pos() < 0:
                
                self.music_player.play(loops = -1)

            screen.blit(self.monstro.surface, self.monstro.rect)
        

class Monstro():
    def __init__(self,room) -> None:
        self.room = room
        self.image = "graphics/Monstro/Parado.png" 
        self.surface = pygame.image.load(self.image).convert_alpha()
        self.rect = self.surface.get_rect(center = (250,250))
        self.chasing = False
        self.spawnabble = False

    def spawn(self,room,map):
        self.surface = pygame.transform.scale(pygame.image.load(self.image).convert_alpha(), (room.monsterLocation["width"], room.monsterLocation["height"]))
        self.rect = self.surface.get_rect(center = self.room.monsterLocation["position"])   
        map.music_player.load("audio/Music/Tenssion.mp3")
        


        