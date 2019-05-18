from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item('Sword', 'A weapon for a warrior'), Item('Wand', 'A weapon for a mage')]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("Shield", "It's flimsy, but it'll do")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("Fool's gold nugget", "A useless stone...maybe!")])}

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

player1 = Player('Player 1', room['outside'], [Item('Bag', 'A patched up sack'), Item('Apple', 'Keeps the doctor away')])

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
# check if it';s the quit input
# if it's the correct type of input, check if there's a room in that direction
# if there's a room in that direction, then update player's current room to new room

selection = ''
# Test for quit input
while selection != 'q':
    # Print current room name
    currentRoomName = player1.current_room.name
    print("\n" + "**********" + "\n\n" + 'LOCATION: ' + currentRoomName + "\n")
    # Print current room description
    currentRoomDescription = player1.current_room.description
    print('DESCRIPTION: ' + currentRoomDescription + "\n")
    # Print inventory, if room contains items
    currentRoomInventory = player1.current_room.inventory
    if len(currentRoomInventory) > 0:
        print("ITEMS IN ROOM:" + "\n")
        for item in currentRoomInventory:
            print(item)
        print("\n")
    # Prints player's inventory, if player has items
    playerInventory = player1.inventory
    if len(playerInventory) > 0:
        print("YOUR ITEMS:" + "\n")
        for item in playerInventory:
            print(item)
        print("\n")
    # Prompt for input
    selection = input("WHICH DIRECTION? TYPE n, s, e, OR w TO MOVE. TYPE q TO QUIT: ")
    selection = selection.lower().strip()
    # Determine is correct directional input is provided
    if selection == 'n':
    # Determine if room exists to the north, and then update current room if it exists
        if player1.current_room.n_to != 'No room there.':
            player1.current_room = player1.current_room.n_to
        else:
            print ('NO ROOM TO THE NORTH!')
    # Determine if room exists to the south, and then update current room if it exists
    elif selection == 's':
        if player1.current_room.s_to != 'No room there.':
            player1.current_room = player1.current_room.s_to
        else:
            print ('NO ROOM TO THE SOUTH!')
    # Determine if room exists to the east, and then update current room if it exists
    elif selection == 'e':
        if player1.current_room.e_to != 'No room there.':
            player1.current_room = player1.current_room.e_to
        else:
            print ('NO ROOM TO THE EAST!')
    # Determine if room exists to the west, and then update current room if it exists
    elif selection == 'w':
        if player1.current_room.w_to != 'No room there.':
            player1.current_room = player1.current_room.w_to
        else:
            print ('NO ROOM TO THE WEST!')
    # Quit condition
    elif selection == 'q':
        print('Thanks for playing.')
    elif len(selection) > 1:
        selection = selection.split(' ')
        # Check if command is to get or take an item
        if selection[0] == 'get' or selection[0] == 'take':
            selection.pop(0)
            itemCheck = ' '.join(selection)
            roomItemNames = []
            # Create list of all items in room by name
            for item in player1.current_room.inventory:
                roomItemNames.append(item.name.lower())
            # Check if item input is in list of room items; if so, add to the player inventory and remove from room inventory
            if itemCheck in roomItemNames:
                itemIndex = roomItemNames.index(itemCheck)
                player1.current_room.inventory[itemIndex].on_take()
                player1.inventory.append(player1.current_room.inventory[itemIndex])
                del player1.current_room.inventory[itemIndex]
            else:
                print("No such item in here!")
    # Prompt to type correct input
    else: 
        print('Please select a direction.')