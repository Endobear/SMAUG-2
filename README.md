# SMAUG-2

# Salas
Cada sala é separada em uma classe que extende a classe "Room", nela tem alguns argumentos

room_name: Nome da sala
room_description: Descrição da sala
exits: Saidas da sala
image: Imagem da sala

Algumas Salas também tem sub salas como as salas do RoomOne que tem o Ceeling e Door.
Cada sala precisa fazer referência a suas entradas e saídas com o intuito de não perder informações. Por exemplo:

RoomOne têm o argumento roomOneDoor que leva a classe RoomOneDoor() sendo assim, quando é passado para a Room da porta, as informações da Room anterior também ficam salvas na classe, passado como argumento na classe construtora