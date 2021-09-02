class Room():
    # Inicialização da classe, definindo os parâmetros dela
    def __init__(self):
        self.room_name = "" # nome da sala
        self.room_description = "" # descrição da sala
        self.exits = [] # Listas de saídas para outras salas, String
        self.image = "" #Imagem da sala, ficará no background
        self.interactives = [] # Lista de retângulos que o Player pode clicar
        self.id = ""

   
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
        return

    def RoomExitClassFromMap(self,mapa,exit):
        return mapa.exitsList[self.id].get(exit)



