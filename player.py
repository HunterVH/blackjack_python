'''
This is the class definition for a black jack player.
'''
import hand

class player:
    def __init__(self, name):
        self.name = name
        self.__dict__['playerHand'] = hand.hand()
        self.busted = False

    '''
    Defines the behavior when setting class attributes
    '''
    def __setattr__(self, name, value):
        if(name == 'playerHand'):
            if(type(value) is list):
                self.playerHand.setHand(value)
            else:
                print('Must assign using a list')
        elif(name == 'name'):
            self.__dict__[name] = value
        elif(name == 'busted'):
            self.__dict__[name] = value
        else:
            print('You cannot set this attribute')

    '''
    Returns the cards of the players hand as a comma seperated string
    '''
    def handContent(self):
        contents = ''
        for j in self.playerHand.cards:
            contents += j.name + ', '
        return contents[:-2]
    
    '''
    Returns the first card of the players hand as a string
    '''
    def dealerContent(self):
        return self.playerHand.cards[0].name
    
    '''
    Returns the total value of the player's hand
    '''
    def handValue(self):
        return self.playerHand.getHandValue()
    
    '''
    Adds a new card to the player's hand
    '''
    def hit(self, newCard):
        self.playerHand.hit(newCard)
        if self.playerHand.totalValue > 21:
            self.busted = True

    '''
    Empties the player's hand of cards and resets the value
    '''
    def clearHand(self):
        self.playerHand.fold()
        self.busted = False

    '''
    Returns a value that determines if the player has busted
    '''
    def checkBust(self):
        return self.busted
    
if __name__ == "__main__":
    pass