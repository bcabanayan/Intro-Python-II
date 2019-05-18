# Implement a class to hold room information. This should have name and
# description attributes.

class Room:

    def __init__(self, name, description, inventory = [], n_to = "No room there.", s_to = "No room there.", e_to = "No room there.", w_to = "No room there."):
        self.name = name
        self.description = description
        self.inventory = inventory
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

    def __repr__(self):
        output = ""
        output += self.name + "\n" + self.description + "\n"
        return output

    # def take_item(item):
        # loop through inventory
        # return item if found and able to be taken
        # return none if not in this room