from sys import exit

def gold_room():
	""" Brings player to room full of gold """
	print("This room is full of gold. How much do you take?")
	next = input("> ")
	
	for i in range(0, 10):
		if str(i) in next:
			how_much = int(next)
			break
	else:
		dead("Man, learn to type a number.")
	
	if how_much < 50:
		print("Nice, you're not greedy. You win!")
		exit(0)
	else:
		dead("You greedy bastard!")

def bear_room():
	""" Player enters if s/he selected the "left" door at start
	
		Player exits this room by dying or proceeding to the gold room """
	print("There is a bear here.")
	print("The bear has a bunch of honey.")
	print("The fat bear is in front of another door.")
	print("How are you going to move the bear?")
	print("Do you take his honey, or taunt the bear?")
	bear_moved = False
	
	while True:
		next = input("> ")
		
		if next == "take honey":
			dead("The bear looks at you and then slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			print("The bear has moved from the door. You can go through it now.")
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print("I got no idea what that means.")

def cthulhu_room():
	""" Player enters this room if s/he selected "right" door at start
	
		Player exits this room by fleeing and returning to start, or dying """
	print("Here you see the great evil Cthulhu.")
	print("He, it - whatever - stares at you and you go insane.")
	print("Do you flee for your life or eat your head?")
	next = input("> ")
	
	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		cthulhu_room()

def dead(why):
	""" Kills player and exits. Receives a string argument for "why player has died" """
	print(why, "So sad.")
	exit(0)

def start():
	print("You are in a dark room")
	print("There is a door to your right and left.")
	print("Which one do you take?")
	next = input("> ")
	
	if next == "left":
		bear_room()
	elif next == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")

start()