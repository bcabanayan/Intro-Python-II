class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        output = ""
        output += "> " + self.name + ": " + self.description
        return output

    def on_take(self):
        return print(F'You have picked up {self.name}!')

    def on_drop(self):
        return print(F'You have dropped {self.name}!')