'''
This is the class definition for a black jack player.
'''

import hand

class player:
    def __init__(self, name):
        self.name = name
        self.__dict__['hand'] = hand.hand()

    def __setattr__(self, name, value):
        if(name == 'hand'):
            if(type(value) is list):
                self.hand.setHand(value)
            else:
                print('Must assign using a list')
        elif(name == 'name'):
            self.__dict__[name] = value
        else:
            print('You cannot set this attribute')

    def handContent(self):
        contents = ''
        for j in self.hand:
            contents += j.name + ', '
        return contents[:-2]
    
    def dealerContent(self):
        return self.hand[0].name
    
if __name__ == "__main__":
    pass