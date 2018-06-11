from player import Player
import random

# plays horse until one player scores a letter
def play_round(player_list, current_player_index):
	num_players =  len(player_list)
	made_shot = False
	shot_type = 0 #shot_type represents the type of shot thata was made if applicable, layup is > 0, jump shot is < 0
	made_shot_count = 0 #counts the number of times a particular shot was made

	# loop until a player makes a shot that the next player misses
	while True:
		# get the current player
		p = player_list[current_player_index]
		
		# check if the last player made a shot
		if made_shot:
			# check shot type and determine if the player makes the shot
			if shot_type > 0: # layup
				make = p.shoot_layup()
			else: # jumpshot
				make = p.shoot_jumpshot()

			# check if shot was a make or miss
			if not make: # means that a player gets a letter
				p.score = p.score + 1
				return current_player_index
			else:
				made_shot_count = made_shot_count + 1
		else:
			# if the last shot wasn't a make then shoot a new shot
			# first determine what type of shot 
			percent_jump = p.pjump
			r = random.random()
			if r < percent_jump:
				made_shot = p.shoot_jumpshot()
				shot_type = -1
			else:
				made_shot = p.shoot_layup()
				shot_type = 1
			
			# if made_shot then increment made_shot count
			if made_shot:
				made_shot_count = 1

		#check how many times a shot has been made to determine if the game has looped back around
		if made_shot_count == num_players:
			made_shot_count = 0

		# adjust current_player_index, but check for loop around
		current_player_index = current_player_index + 1
		
		# this means that we got to the last player in the list and have to reset to the initial player
		if current_player_index >= num_players:
			current_player_index = 0
		
	return current_player_index

# plays a full game of horse until one player gets five points
def play_game(player_list, current_player_index):
	# contains a list of the players who have lost
	lost_players = []
	# loop until there is only one player remaining
	while len(player_list) > 1:
		#  play a round
		current_player_index = play_round(player_list, current_player_index)
		
		# get the player who lost the last round
		p = player_list[current_player_index]

		# check if the player has 5 points, if so shoot ft
		if p.score == 5:
			made_ft = p.shoot_freethrow()
			if made_ft:
				p.score = p.score - 1
			else: # remove player from the game if they lsot
				lost_players.append(player_list.pop(current_player_index))
		
		# continue to next player
		current_player_index = current_player_index + 1
		if current_player_index >= len(player_list):
			current_player_index = 0
	
	# add the lost_players back into the list
	player_list.extend(lost_players)
	
	# reset player score values
	for i in range(0, len(player_list)):
		player_list[i].score = 0

	return player_list[0]
	
# runs through N games with the provided player list
def run_simulation(player_list, N):
	current_player_index = 0
	for i in range(0, N):
		# play game and get winner
		winning_player = play_game(player_list, current_player_index)

		# update wins for the player
		winning_player.wins = winning_player.wins + 1

		# randomize the list of players
		random.shuffle(player_list)
	return player_list

players = []
N = 10000
p1 = Player(0.25, .40, .85, 0)
p2 = Player(0.40, .40, .80, 1)
players.append(p1)
players.append(p2)
run_simulation(players, N)
print("Layups only score: " + str(p1.wins))
print("Jumpshots only score: " + str(p2.wins))
