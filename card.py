'''
This is a class definition for the card class.
'''

'''
An object to represent playing cards
'''
class card:
    '''
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