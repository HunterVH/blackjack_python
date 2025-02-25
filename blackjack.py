"""
This Program will simulate a game of blackjack
"""

import deck
import player
import time
import os

'''
player1 - player object representing the user
dealer - player object representing the computer
seeDealer - Boolean that determines if the dealers cards are to be displayed
Prints the contents of the player's and dealer's (conditionally) hand to the screen
'''
def printHandValues(player1, dealer, seeDealer=False):
    if(seeDealer):
        playerHandContent = f'{player1.name}: {player1.handContent()}\n\tTotal: {'BUSTED' if player1.checkBust() else player1.handValue()}'

        dealerHandContent = f'{dealer.name}: {dealer.handContent()}\n\tTotal: {'BUSTED' if dealer.checkBust() else dealer.handValue()}'
    else:
        playerHandContent = f'{player1.name}: {player1.handContent()}\n\tTotal: {'BUSTED' if player1.checkBust() else player1.handValue()}'

        dealerHandContent = f'{dealer.name}: {dealer.dealerContent()}, *\n'
    
    print(f'{playerHandContent}\n\n{dealerHandContent}')

'''
player1 - player object representing the user
dealer - player object representing the computer
waittime - number that represents how long to wait before clearing the screen and displaying the player/dealer hands
seeDealer - Boolean that determines if the dealers cards are to be displayed
Forces a wait in the program for the player to view the cards/decisions before updating the terminal output
'''
def refresh(player1, dealer, waittime, seeDealer=False):
    time.sleep(waittime)
    os.system('cls')
    printHandValues(player1, dealer, seeDealer)

'''
player1 - player object representing the user
dealer - player object representing the computer
Print the winner of the game to the player
'''
def displayWinner(player1, dealer):
    # refresh(player1, dealer, 2, True)
    print()
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
player1 - player object representing the user
dealer - player object representing the computer
shoe - represents the deck that cards are being drawn from
The functionality for the dealer's turn
'''
def dealerPlays(player1, dealer, shoe):
    SOFTHIT = 17
    value = dealer.handValue()
    
    while(not dealer.checkBust()):
        refresh(player1, dealer, 1, True)
        time.sleep(1)
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
    
    
'''
player1 - player object representing the user
dealer - player object representing the computer
shoe - represents the deck that cards are being drawn from
The functionality for a player taking their turn
'''
def playerPlays(player1, dealer, shoe):
    playing = True

    while(playing):
        
        dealer.playerHand, player1.playerHand = shoe.blackjackFirstDeal()

        # Functionality for hitting and staying
        userIn = ''
        while(userIn[:1] != 'S' and userIn[:1] != 'Q' and not player1.checkBust()):
            refresh(player1, dealer, 1)
            userIn = (input("\n(H)it, (S)tay, or (Q)uit: ")).upper()
            if(userIn[:1] == 'H'):
                print('Hit!')
                player1.hit(shoe.hit())
                if(player1.checkBust()):
                    refresh(player1, dealer, 1)
                    print('You Busted!')
            elif(userIn[:1] == 'S'):
                print('Stay!')
            elif(userIn[:1] == 'Q'):
                print('Quitter!')
                playing = False
            else:
                print('That was not a valid input.')

        if(userIn[:1] != 'Q'):
            dealerPlays(player1, dealer, shoe)
            refresh(player1, dealer, 1, True)
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
def playBlackjack():
    # Create the shoe
    shoe = deck.deck(1)
    shoe.shuffle()
    # Create the players
    player1 = player.player('Hunter')
    dealer = player.player('Dealer')

    playerPlays(player1, dealer, shoe)

if __name__ == "__main__":
    playBlackjack()