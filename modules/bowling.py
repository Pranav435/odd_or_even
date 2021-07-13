import globals
import time
from random import randint

def bowling(name):
	globals.name=name
	out=False
	comp=0
	player_choice=""
	print("Yay! You're bowling first! Let's get this underway!")
	while not out:
		comp=randint(1,6)
		try:
			player_choice=int(input("Enter a number between 1 and 6: "))
		except:
			print("Please enter a number, not something else!!!!!!!")
			continue
		if player_choice < 1 or player_choice > 6:
			print("Whoops! That number does not comply with the bounds created for this game by whoever created this game! ENTER, a, number, from, 1, to, 6!")
			continue
		if comp == player_choice:
			out=True
		else:
			globals.score+=comp
			print("My current score is " + str(globals.score) + " runs!")

	time.sleep(0.1)
	globals.target=globals.score+1
	print("I scored " + str(globals.score) + "runs!")
	print("Your target is " + str(globals.target) + " runs!")
	globals.score=0
	out=False
	print("Pad up! You're up to hit some sixes, or actually get out! :)))")

	while not out:
		comp=randint(1,6)
		try:
			player_choice=int(input("Enter a number between 1 and 6: "))
		except:
			print("Please enter a number, not something else!!!!!!!")
			continue
		if player_choice < 1 or player_choice > 6:
			print("Whoops! That number does not comply with the bounds created for this game by whoever created this game! ENTER, a, number, from, 1, to, 6!")
			continue
		if comp == player_choice:
			out=True
		else:
			globals.score+=player_choice
			print("Your current score is " + str(globals.score) + " runs!")
		if globals.score >= globals.target:
			break

	if globals.score >= globals.target:
		print("Ohhh! You won! Good game bruh!")
	else:
		print("Guess I'm better! I knew that, of course! I've beaten my two year old son before!")

bowling("Pranav")