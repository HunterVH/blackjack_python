"""
This Program will simulate a game of blackjack
"""

import deck
import player

'''
The function prints the contents of a players hand and shows the first card of a
dealers hand
'''
def printHandContentPlayerView(player1, dealer):
    print(f'{player1.name}: {player1.handContent()}\n\tTotal: {player1.handValue()}\n')
    print(f'{dealer.name}: {dealer.dealerContent()}, *')

'''
Prints the full contents of a given player's hand
'''
def printHandContent(player):
    print(f'{player.name}: {player.handContent()}\n\tTotal: {player.handValue()}\n')

'''
Print the winner of the game to the player
'''
def displayWinner(player1, dealer):
    def playerWin():
        print(f'{player1.name} Wins!')

    def dealerWin():
        print('The Dealer Wins!')

    def push():
        print('No One Wins!')

    if(player1.checkBust()):
        if(dealer.checkBust()):
            push()
        else:
            dealerWin()
    elif(dealer.checkBust()):
        playerWin()
    else:
        playerValue = player1.handValue()
        dealerValue = dealer.handValue()

        # Sets the hand value to the highest value in case of an Ace in hand
        if(type(playerValue) is list):
            playerValue = playerValue[1]
        if(type(dealerValue) is list):
            dealerValue = dealerValue[1]

        if(playerValue < dealerValue):
            dealerWin()
        elif(dealerValue < playerValue):
            playerWin()
        else:
            push()

'''
The functionality for the dealer's turn
'''
def dealerPlays(dealer, shoe):
    SOFTHIT = 17
    value = dealer.handValue()

    printHandContent(dealer)
    
    while(True):
        # This will happen if the dealer has an ace
        if(type(value) is list):
            if(value[1] <= SOFTHIT):
                print('Dealer Hits!')
                dealer.hit(shoe.hit())
                value = dealer.handValue()
            else:
                print('Dealer Stays!')
                break
        else:
            if value <= (SOFTHIT-1):
                print('Dealer Hits!')
                dealer.hit(shoe.hit())
                value = dealer.handValue()
            else:
                print('Dealer Stays!')
                break
    printHandContent(dealer)
    
'''
The functionality for a player taking their turn
'''
def playerPlays(player1, dealer, shoe):
    playing = True

    while(playing):
        
        dealer.playerHand, player1.playerHand = shoe.blackjackFirstDeal()
        printHandContentPlayerView(player1, dealer)

        # Functionality for hitting and staying
        userIn = ''
        while(userIn[:1] != 'S' and userIn[:1] != 'Q' and not player1.checkBust()):
            userIn = (input("(H)it, (S)tay, or (Q)uit: ")).upper()
            if(userIn[:1] == 'H'):
                print('Hit!')
                player1.hit(shoe.hit())
                printHandContentPlayerView(player1, dealer)
                if(player1.checkBust()):
                    print('You Busted!')
            elif(userIn[:1] == 'S'):
                print('Stay!')
            elif(userIn[:1] == 'Q'):
                print('Quitter!')
                playing = False
            else:
                print('That was not a valid input.')

        dealerPlays(dealer, shoe)
        displayWinner(player1, dealer)

        # Allows the user to play again or quit
        while(userIn[:1] != 'D' and userIn[:1] != 'Q'):
            userIn = input('(D)eal or (Q)uit: ').upper()
            if(userIn[:1] == 'Q'):
                playing = False
            elif(userIn[:1] == 'D'):
                player1.clearHand()
                dealer.clearHand()
            else:
                print('That was not a valid input')

'''
This function creates the deck, shuffles it and begins the game
'''
def main():
    # Create the shoe
    shoe = deck.deck(1)
    shoe.shuffle()
    # Create the players
    player1 = player.player('Hunter')
    dealer = player.player('Dealer')

    playerPlays(player1, dealer, shoe)

if __name__ == "__main__":
    main()