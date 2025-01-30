'''
This is the definition for the hand class
'''

class hand:
    def __init__(self):
        cards = []
        totalValue = 0
        hasAce = False

    # def __setattr__(self, name, cards):
        
    #         if(type(cards) is list):
    #             self.cards = cards
    #             for j in self.cards:
    #                 self.totalValue = self.totalValue+j.value
    #         else:
    #             #Return an error message
    #             pass

    def fold(self):
        self.cards.clear()
        self.totalValue = 0
        self.hasAce = False

    def setHand(self, cards):
        self.cards = cards