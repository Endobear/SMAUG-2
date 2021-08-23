from Salas.RoomTwo import RoomTwo
from Salas.Player import Player
from Salas.RoomOne import RoomOne


rooms = [RoomOne()]
player = Player()
player.currentRoom = rooms[0]



print('Write the action')
action = input().lower()
commands = ['help', 'go','interact', 'exit']
look_commands = ['look around', 'look', 'inspect around']
go_commands = ['go', 'go to']
interact_commands = ['interact','use','interact with']

while action != 'exit':
	
	if action == 'help':
		print(commands)
		action = input().lower()
	elif action in look_commands:
		print(player.currentRoom.room_description)
		action = input().lower()
	elif action in go_commands:
		print('Where? possible locations: ', player.currentRoom.exits)
		nextAction = input()
		if nextAction in player.currentRoom.exits:
			player.currentRoom = player.currentRoom.getLocationFromDirection(nextAction)
			print('You went ' + nextAction)
			print(player.currentRoom.room_description)
			action = input().lower()
		else:
			print('room not found! Type next action:')
			action = input().lower()
	elif action in interact_commands:
		player.currentRoom.interact()
		print(player.currentRoom.interactMessage)
		action = input().lower()
	else:
		print('command does not exist, type a new command. type \'help\' for possible commands')
		action = input().lower()