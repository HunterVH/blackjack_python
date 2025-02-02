"""
This Program will simulate a game of blackjack
"""

import deck
import player

def printHandContent(player1, dealer):
        print(f'{player1.name}: {player1.handContent()}\n\tTotal: {player1.handValue()}\n')
        print(f'{dealer.name}: {dealer.dealerContent()}, *')

def playerPlays(player1, dealer, shoe):
    playing = True

    while(playing):
        
        dealer.playerHand, player1.playerHand = shoe.blackjackFirstDeal()

        printHandContent(player1, dealer)

        userIn = ''
        while(userIn[:1] != 'S' and userIn[:1] != 'Q' and not player1.checkBust()):
            userIn = (input("(H)it, (S)tay, or (Q)uit: ")).upper()
            if(userIn[:1] == 'H'):
                print('Hit!')
                player1.hit(shoe.hit())
                printHandContent()
                if(player1.checkBust()):
                    print('You Busted!')
            elif(userIn[:1] == 'S'):
                print('Stay!')
            elif(userIn[:1] == 'Q'):
                print('Quitter!')
                playing = False
            else:
                print('That was not a valid input.')

        while(userIn[:1] != 'D' and userIn[:1] != 'Q'):
            userIn = input('(D)eal or (Q)uit: ').upper()
            if(userIn[:1] == 'Q'):
                playing = False
            elif(userIn[:1] == 'D'):
                player1.clearHand()
                dealer.clearHand()
            else:
                print('That was not a valid input')

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