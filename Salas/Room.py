import pygame

class Room():
    # Inicialização da classe, definindo os parâmetros dela
    def __init__(self):
        self.room_name = "" # nome da sala
        self.room_description = "" # descrição da sala
        self.exits = [] # Listas de saídas para outras salas, String
        self.image = "" #Imagem da sala, ficará no background
        self.interactives = [] # Lista de retângulos que o Player pode clicar, não incluir itens e setas
        self.id = ""
        self.itens = []
        self.itens_sprites = pygame.sprite.Group(item for item in self.itens)
        self.arrows = []
        self.ArrowSprites = pygame.sprite.Group(arrow for arrow in self.arrows)

        self.room_rects = self.arrows  + self.itens+ self.interactives

   
    # Função que pega uma direção em string e chama a função com a classe da sala daquela direção
    def getLocationFromDirection(self,direction):
        if direction in self.exits:
            if direction == "Up":
                return self.upLocation()
            if direction == "Back":
                return self.backLocation()
            if direction == "Front":
                return self.frontLocation()


    
            
    def upLocation(self):
        return
    def backLocation(self):
        return
    def frontLocation(self):
        return 

    # Função que diz o que cada retângulo interagível faz
    def ineractRect(self,rect,player):
        if rect in [arrow.rect for arrow in self.arrows]:
            for arrow in self.arrows:
                if rect == arrow.rect: 
                    player.currentRoom = self.getLocationFromDirection(arrow.locationName)

        if rect in [item.rect for item in self.itens]:
            index = 0
            for item in self.itens:
                if rect == item.rect: 
                   self.itens_sprites.remove(item) 
                   player.pickItem(self.itens.pop(index))
                   
                   break;      
                index += 1           
        

    def RoomExitClassFromMap(self,mapa,exit):
        return mapa.exitsList[self.id].get(exit)

    def update(self,screen):
        # print(self.itens_sprites)
        self.ArrowSprites.draw(screen)
        self.itens_sprites.draw(screen)
        self.itens_sprites.add(item for item in self.itens)
        self.ArrowSprites.add(arrow for arrow in self.arrows)
        self.room_rects = [arrow.rect for arrow in self.arrows]  + [item.rect for item in self.itens] + self.interactives
        
        


