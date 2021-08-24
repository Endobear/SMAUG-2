class Room():
    # Inicialização da classe, definindo os parâmetros dela
    def __init__(self):
        self.room_name = "" # nome da sala
        self.room_description = "" # descrição da sala
        self.exits = [] # Listas de saídas para outras salas, String
        self.image = "" #Imagem da sala, ficará no background
        self.interactives = [] # Lista de retângulos que o Player pode clicar

    def change_location(self,location): 
        if location in self.exits:
            return self.getLocationFromDirection(location)

    # Função que pega uma direção em string e chama a função com a classe da sala daquela direção
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

    # Função que diz o que cada retângulo interagível faz
    def ineractRect(self,rect,player):
        return




