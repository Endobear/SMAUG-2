rooms = {
		'roomOne' : {
			'image' : '',
			'description': 'A nice room with white walls',
			'ways':['roomOne-ceiling','roomOne-door']

			},
		'roomOne-ceiling' : {
			'image' : '',
			'description': 'The ceiling of the white room, it looks nice but I don\'t know where the light is comming from',
			
			'ways':['roomOne']

			},
		'roomOne-door' : {
			'image' : '',
			'description': 'The door of the room, it\'s closed',
			'condition': False,
			'conditionTrueMessage': 'looks like it wasn\'t that hard to open'

			},
		'roomTwo' : {
			'image' : '',
			'description': 'A room with light pink walls'



			}
	}

player_inv = []
player_location = 'roomOne'

print('Write the action')
action = input().lower()
commands = ['help', 'go', 'exit']
look_commands = ['look around', 'look', 'inspect around']
go_commands = ['go', 'go to']

while action != 'exit':
	
	if action == 'help':
		print(commands)
		action = input().lower()
	elif action in look_commands:
		print(rooms.get(player_location).get('description'))
		action = input().lower()
	elif action in go_commands:
		print('Where? possible locations: ', rooms.get(player_location).get('ways'))
		nextAction = input()
		if nextAction in rooms.get(player_location).get('ways'):
			player_location = nextAction
			print('You went to: ' + player_location)
			print(rooms.get(player_location).get('description'))
			action = input().lower()
		else:
			print('room not found! Type next action:')
			action = input().lower()
	else:
		print('command does not exist, type a new command. type \'help\' for possible commands')
		action = input().lower()