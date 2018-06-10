from player import Player
import random

p = Player(.35 , .50 , .80, 0)
print(" Jumpshot make %: " + str(p.jump))
print(" Freethrow make %: " + str(p.ft))
print(" Layup make %: " + str(p.layup))

count = 0
N = 10000
for i in range(0, N):
	if p.shoot():
		count = count + 1
print(count/N)
