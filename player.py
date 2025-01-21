'''
This is the class definition for a black jack player.
'''

class player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.handValue = 0
        self.hasAce = False

    def update(self):
        for j in self.hand:
            self.handValue = self.handValue+j.value