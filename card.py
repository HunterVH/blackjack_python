'''
This is a class definition for the card class.
'''

'''
A class to represent playing cards
'''
class card:
    '''
    name - string - The name that represents the card
    suit - string - the suit of the card
    Creates the card object
    '''
    def __init__(self, name, suit, value):
        self.name = name
        self.suit = suit
        self.value = value

    '''
    Returns the name of the card
    '''
    def __str__(self):
        return self.name