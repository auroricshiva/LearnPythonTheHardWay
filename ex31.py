print("You enter a dark room with two doors. Do you go through door #1 or door #2?")

door = input("> ")

if door == "1":
	print("There's a giant bear here eating a cheesecake. What do you do?")
	print("1. Take the cake")
	print("2. Scream at the bear")
	choice = input("> ")
	
	if choice == "1":
		print("You pissed off the bear. The bear sits on you. You die.")
	elif choice == "2":
		print("You disturbed the bear. The bear chases you and mows you down. You die.")
	else:
		print("Well, to %s is probably the best choice. Good job for thinking outside the box!" % choice)

elif door == "2":
	print("You stare into the endless abyss at Cthulhu's retina. (Basically, you become insane.)")
	print("1. Blueberries")
	print("2. Yellow jacket clothespins")
	print("3. Understanding revolvers yelling melodies.")
	insanity = input("> ")
	
	if insanity == "1" or insanity == "2":
		print("Your body survives powered by a mind of jello.")
	else:
		print("The insanity rots your eyes into a pool of muck.")

else:
	print("You stumble around in the dark...")