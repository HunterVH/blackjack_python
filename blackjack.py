"""
This Program will simulate a game of blackjack
"""

import random

def createShoe(shoeSize):
    deck = []
    for iter in range(13*shoeSize):
        deck.append('H'+str(iter%13+1))
        deck.append('S'+str(iter%13+1))
        deck.append('D'+str(iter%13+1))
        deck.append('C'+str(iter%13+1))

    random.shuffle(deck)

    return deck

def main():
    shoeSize = 2
    shoe = createShoe(shoeSize)
    print(shoe)

    pass

if __name__ == "__main__":
    main()
