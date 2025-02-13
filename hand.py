'''
This is the definition for the hand class
'''

class hand:
    def __init__(self):
        self.cards = []
        self.totalValue = 0
        self.numberOfAces = 0

    '''
    This function dictates what happens when setting the attributes of the class
    '''
    def __setattr__(self, name, value):
        if(name == 'cards'):
            self.__dict__[name] = value
            for iter in self.cards:
                self.totalValue += iter.value
                if iter.value == 11:
                    self.numberOfAces += 1
        elif(name == 'numberOfAces'):
            self.__dict__[name] = value
        elif(name == 'totalValue'):
            self.__dict__[name] = value
        else:
            print(f'{name} is not a valid attribute')
    
    '''
    This function resets the hand to have no cards
    '''
    def fold(self):
        self.cards.clear()
        self.totalValue = 0
        self.numberOfAces = 0

    '''
    Sets the hand equal to the given dealt card(s)
    '''
    def setHand(self, dealtCards):
        self.cards = dealtCards

    '''
    This function returns the value of the hand, and calculates Aces as 1 or 11
    '''
    def getHandValue(self):
        if self.numberOfAces > 0:
            if (self.totalValue-((self.numberOfAces-1)*10)) <= 21:
                return [self.totalValue-(self.numberOfAces*10),self.totalValue-((self.numberOfAces-1)*10)]
            else:
                return self.totalValue-(self.numberOfAces*10)
        else:
            return self.totalValue

    '''
    This function adds a given card to the hand
    '''
    def hit(self, newCard):
        self.cards.append(newCard)
        self.totalValue += newCard.value
        if newCard.value == 11:
            self.numberOfAces += 1