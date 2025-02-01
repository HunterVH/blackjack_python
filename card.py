'''
This is a class definition for the card class.
'''

class card:
    def __init__(self, name, suit, value):
        self.name = name
        self.suit = suit
        self.value = value

    # Returns the name of the card as a string with a letter/number and suit
    def __str__(self):
        return self.name