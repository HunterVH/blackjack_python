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

def firstDeal(playerHand, dealerHand, shoe):
    playerTotal = 0
    dealerTotal = 0
    for j in range(4):
        card = shoe.pop()
        cardValue = int(card[1:])
        if(cardValue > 10):
            if(j%2 == 1):
                playerTotal += 10
                playerHand.append(card)
            else:
                dealerTotal += 10
                dealerHand.append(card)
        elif(cardValue == 1):
            if(j%2 == 1):
                playerTotal += 11
                playerHand.append(card)
            else:
                dealerTotal += 11
                dealerHand.append(card)
        else:
            if(j%2 == 1):
                playerTotal += cardValue
                playerHand.append(card)
            else:
                dealerTotal += cardValue
                dealerHand.append(card)

    return playerTotal, dealerTotal


def main():
    shoeSize = 2
    playerHand = []
    playerTotal = 0
    dealerHand = []
    dealerTotal = 0
    playing = True

    shoe = createShoe(shoeSize)
    #print(shoe)

    while(playing):
        playerTotal, dealerTotal = firstDeal(playerHand, dealerHand, shoe)
        print('Your Hand:', playerHand,'\nTotal:',playerTotal)
        print('Dealer Hand:', dealerHand[0], '\nTotal:',dealerTotal)

        #print('\nHit or Stay?')
        #Get User Input
        userIn = ''
        while(userIn != 'Stay'):
            userIn = input("Hit or Stay: ")
            if(userIn == 'Hit'):
                print('Hit!')
            elif(userIn == 'Stay'):
                print('Stay!')
            else:
                print('That was not a valid input.')

        while(userIn != 'Deal' and userIn != 'Leave'):
            userIn = input('Deal or Leave: ')
            if(userIn == 'Leave'):
                playing = False
            elif(userIn != 'Deal'):
                print('That was not a valid input')
            else:
                playerHand.clear()
                dealerHand.clear()


if __name__ == "__main__":
    main()
