from nose.tools import *
from ex47.game import Room



def setup():
    print("SETUP!")

def test_room():
	gold = Room("GoldRoom",
				""" This room has gold in it you can grab. There's a
				door to the north. """)
	assertEqual(gold.name, "GoldRoom")
	assertEqual(gold.paths, {})
	
def test_room_paths():
	center = Room("Center", "Test room in the center.")
	north = Room("North", "Test room in the north.")
	south = Room("South", "Test room in the south.")
	
	center.add_paths({'north': north, 'south': south})
	assertEqual(center.go('north'), north)
	assertEqual(center.go('south'), south)

def test_map():
	start = Room("Start", "You can go west and down a hole")
	west = Room("Trees", "There are trees here. You can go east.")
	down = Room("Dungeon", "It's dark down here. You can go up.")
	
	start.add_paths({'west': west, 'down': down})
	west.add_paths({'east': start})
	down.add_paths({'up': start})
	
	assertEqual(start.go('west'), west)
	assertEqual(start.go('west').go('east'), start)
	assertEqual(start.go('down').go('up'), start)

def teardown():
    print("TEAR DOWN!")

def test_basic():
    print("I RAN!")
