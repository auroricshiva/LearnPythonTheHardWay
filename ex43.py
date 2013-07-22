from sys import exit
from random import randint

class Scene(object):
	
	def enter(self):
		pass

class Engine(object):
	
	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene() # Since scene_map is just the Map object
		# we pass into the initialization of Engine, scene_map already has 'central_corridor'
		# stored in itself (because we made the Map object initialize with 'central_corridor')
		# we just call scene_map.opening_scene() to go into CentralCorridor().
		
		while True:
			print("\n--------")
			next_scene_name = current_scene.enter() # Each scene we must "enter" and the "enter"
			# function of each scene will return 'death' or the next scene's name.
			current_scene = self.scene_map.get_scene(next_scene_name) # We just use the Map object
			# we have (scene_map) and the functions it has (get_scene) to open the next scene.

class Death(Scene):
	
	message = [
		"You have died.",
		"You died.",
		"You fail.",
		"You have failed.",
		"Well, at least you know not to do that again."
	]
	
	def enter(self):
		print(Death.message[randint(0, len(self.message) - 1)])
		exit(0)

class CentralCorridor(Scene):
	
	def enter(self):
		print("The Gothons of Planet Percal #25 have invaded your ship and destroyed \n\
		\ryour entire crew. You are the last surviving member and your mission \n\
		\ris to get the Sergei High-Intensity Mining Beam from the Laser \n\
		\rWeapons Armory, arm it in the bridge, and blow the \n\
		\rship up (after you get into an escape pod, of course.) \n\
		\r\n\
		\rYou awaken on the floor beside your crewmates. You nudge the \n\
		\rcommander next to you, but his body feels limp and passive. \n\
		\rYou find your way out the room and as you stumble \n\
		\rthrough the dust-filled corridor towards the armory, \n\
		\ra Gothon jumps out - red scaly skin, dark grimy teeth, and \n\
		\ra strange clown-like face. He's blocking the door to the \n\
		\rarmory and is about to pull a weapon to blast you.")
		print("Do you try to PULL your gun out before it does, DODGE his shot, or DUCK in fear?")
		action = input("> ")
		
		if action == 'PULL' or action == 'pull':
			print()
			print("Quick on the draw you yank out your blaster and fire it at the Gothon. \n\
			\rIts quick movements coupled with the dim, smoky air throw \n\
			\roff your aim. Your laser hits it - or so you thought. Out of the shadows \n\
			\rit emerges and swiftly disarms you. Your face becomes a punching bag until \n\
			\ryou are dead. Then it eats you.")
			return 'death'
		
		elif action == 'DODGE' or action == 'dodge':
			print()
			print("Like a world class boxer you dodge, weave, and slip and slide right \n\
			\ras the Gothon's blaster cranks a laser past your head. In the middle of \n\
			\ryour artful dodge your foot slips and you bang your head on the metal \n\
			\rwall and pass out. You wake up shortly after only to enjoy the view of \n\
			\ra grotesque Gothon's face as it crushes your skull and eats you.")
			return 'death'
		
		elif action == 'DUCK' or action == 'duck':
			print()
			print("You duck and squat like into a little ball, huddling in the shadows and \n\
			\rletting loose a whimper like a little girl. In the dim, dusty corridor, the Gothon loses \n\
			\rsight of you and proceeds towards your last position. You cower in fear as \n\
			\rthe green glaring eyes of the Gothon tower over you. \n\
			\rLuckily, it doesn't spot you on the ground and trips over you. You are lying on \n\
			\ryour back and aren't sure what just happened, but take the chance to pull your weapon \n\
			\rout and fire it right into its heart, face, groin, hands, neck, and feet. \n\
			\rJust to make sure it's dead, of course. \n\
			\rYou proceed through the armory door.")
			input()
			return 'laser_weapon_armory'
		
		else:
			print("What?")
			return 'central_corridor'

class LaserWeaponArmory(Scene):
	
	def enter(self):
		print("You do a dive roll into the Weapon Armory, crouch and scan the room \n\
		\rfor more Gothons that might be hiding.  It's dead quiet, too quiet. \n\
		\rYou stand up and run to the far side of the room and find the \n\
		\rSergei HI M-Beam in its container.  There's a keypad lock on the box \n\
		\rand you need the code to get the laser out.  If you get the code \n\
		\rwrong 10 times then the lock closes forever and you can't \n\
		\rget the laser.  The code is 2 digits.")
		code = "%d%d" % (randint(1, 9), randint(1, 9))
		guess = input("> ")
		guesses = 0
		
		while guess != code and guesses < 10:
			print("nerp!")
			guesses += 1
			guess = input("> ")
		
		if guess == code:
			print()
			print("The container clicks open and the seal breaks, letting gas out. \n\
			\rYou grab the laser and run as fast as you can to the bridge \n\
			\rwhere you must place it in the best spot.")
			input()
			return 'the_bridge'
		else:
			print()
			print("The lock creates its strange noise one last time before you \n\
			\rhear a sickening melting sound as the mechanism fuses together. \n\
			\rdecide to sit there, and finally the Gothons blow up the ship \n\
			\rfrom their ship and you die - wondering 'What if I had tried the \n\
			\rcode %s?'" % code)
			return 'death'

class TheBridge(Scene):
	
	def enter(self):
		print("You burst onto the Bridge with the High-Intensity laser under your \n\
		\rarm and surprise 5 Gothons who are trying to take control of the ship. \n\
		\rEach of them has a strange clown costume on to, you figure, complement \n\
		\rtheir ugly clown faces. They haven't pulled their weapons out yet, as \n\
		\rthey see the charged laser under your arm and don't want to disintegrate \n\
		\rinto dust.")
		print("Do you SWEEP the charged laser across the room, hoping to kill everything \n\
		\r(including, possibly, yourself) - or do you slowly PLACE the laser?")
		action = input("> ")
		
		if action == 'SWEEP' or action == 'sweep':
			print()
			print("In a panic you attempt to fire the beam at the group of Gothons. \n\
			\rRight as you bring your other arm up to initiate the release, the \n\
			\rGothons have no choice but to attempt to save their own lives and \n\
			\rstart blasting you. You succeed in killing 2 and ripping the ship's \n\
			\rbridge to shreds before dying.")
			return 'death'
		elif action == 'PLACE' or action == 'place':
			print()
			print("You point your blaster at the laser under your arm, hoping that \n\
			\rthe Gothons are not knowledgeable about human weaponry and especially \n\
			\rabout what you have under your arm. Like shooting it would do anything... \n\
			\rThe Gothons see the charged laser, and a gun pointed right at the source. \n\
			\rYou see their hands slowly rising and beads of sweat run down their skin. \n\
			\rYou inch backwards towards the door, open it, and then carefully place \n\
			\rthe laser on the floor, making sure to point it towards the glass separating \n\
			\rthe air-less space from the inside of the bridge. You then jump back through \n\
			\rthe door, punch the close button so hard it breaks, and blast the lock \n\
			\rso the Gothons can't get out. \n\
			\rNow that the bomb is placed you run to the escape pods to get off this tin can.")
			input()
			return 'escape_pod'
		else:
			print("What?")
			return 'the_bridge'

class EscapePod(Scene):
	
	def enter(self):
		print("You rush through the ship desperately trying to make it to \n\
		\rthe escape pod before the whole ship explodes. It seems like \n\
		\rhardly any Gothons are on the ship, so your run is clear of \n\
		\rinterference. You get to the chamber with the escape pods, and \n\
		\rnow need to pick one to take. Some of them could be damaged \n\
		\rbut you don't have time to look at them all! There's 5 pods, and you \n\
		\rdecide to check three. Which one do you check first?")
		guess = input("#> ")
		good_pod = randint(1, 5)
		guesses = 0
		
		while guess != good_pod and guesses < 2:
			guess = input("#> ")
			guesses += 1
		
		if int(guess) != good_pod:
			print()
			print("You don't have any more time.")
			print("You jump into pod %s and hit the Emergency Eject button." % guess)
			print("The pod escapes out into the void of space, then implodes \n\
			\ras the hull ruptures, crushing your body into jam jelly.")
			return 'death'
		else:
			print()
			print("You jump into pod %s and hit the Emergency Eject button." % guess)
			print("The pod escapes out into the void of space, accelerating \n\
			\rtowards the planet below. As it rockets off, you look back and see \n\
			\ra blue beam of light shoot out of the bridge. Before your eyes, \n\
			\ryour ship implodes then explodes like a bright star. Debris is flying \n\
			\revery which way, but none come into contact with your pod. The laser \n\
			\rcuts off after the explosion, but the segment of light that was emitted \n\
			\rcontinues out, catching up with the Gothon ship that is attempting to warp \n\
			\raway. The laser annihilates its charging thrusters, and tears right through \n\
			\rthe entire hull. As you watch the obliteration of the Gothon ship, you feel \n\
			\rthe warm heat of the explosion on your face and smile. You escaped alive. \n\
			\rYou won!")
			return 'finished'


class Map(object):
	
	scenes = {
		'central_corridor': CentralCorridor(),
		'laser_weapon_armory': LaserWeaponArmory(),
		'the_bridge': TheBridge(),
		'escape_pod': EscapePod(),
		'death': Death()
	}
	
	# Creates a local variable "start_scene" equal to the scene we want to start in
	def __init__(self, start_scene):
		self.start_scene = start_scene
	
	# Getter method to return the scene's corresponding method (value) based on the name (key)
	def get_scene(self, scene_name):
		return Map.scenes.get(scene_name)
	
	def opening_scene(self):
		return self.get_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()