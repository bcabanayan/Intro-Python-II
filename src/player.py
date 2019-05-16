# Write a class to hold player information, e.g. what room they are in
# currently.

# Here, can pass inventory as an empty list, because the player will start with no items.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []