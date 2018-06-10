import random

class Player:
	
	# j is jumpshot make percentage, f is free throw make percentage
	# l is layout make percentage, pj is percentage of shots that are jump shots
	def __init__(self, j, f, l, pj):
		self.jump = j
		self.ft = f
		self.layup = l
		self.streak = 0
		self.pjump = pj
		self.score = 0

	# takes a random shot and returns True/False depending on result
	def shoot(self):
		# get random number to determine the type of shot
		r = random.random();
		if r <= self.pjump:
			return self.shoot_jumpshot()
		else:
			return self.shoot_layup()
	
	# shoots a layup
	def shoot_layup(self):
		# get random number
		r = random.random()

		# determine if the shot is a make or miss
		if r <= self.layup:
			return True
		else:
			return False

	# shoot a jumpshot
	def shoot_jumpshot(self):
		# get random number
		r = random.random()

		# determine make or miss
		if r <= self.jump:
			return True
		else:
			return False
	
	# shoot a freethrow
	def shoot_freethrow(self):
		# get random number
		r = random.random()

		# make/miss
		if r <= self.ft:
			return True
		else:
			return False 
