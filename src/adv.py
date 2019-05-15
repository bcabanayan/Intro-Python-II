from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together
# DRAW A MAP USING THIS SCHEMATIC!

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Can currently use the string "outside"
# But eventually, wanna use the dictionary to actually get the room name

player1 = Player("Player 1", "outside")

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# check if it's the correct type of input
# if it's the correct type of input, check if there's a room in that direction
# if there's a room in that direction, then update player's current room to new room

selection = ""
directionList = ('n', 's', 'e', 'w')
# test if selection is correct type of input
while str(selection).lower() not in directionList:
    currentRoomName = room[player1.current_room].name
    print('LOCATION: ' + currentRoomName)
    currentRoomDescription = room[player1.current_room].description
    print('DESCRIPTION: ' + currentRoomDescription)
    selection = input("WHICH DIRECTION? TYPE n, s, e, OR w: ")
    selection = str(selection).lower()
    if selection in directionList:
        print('Thanks for providing a direction.')
    else:
        print('Please provide a direction.')

# print('New location: ' + room[room[player1.current_room].n_to])