"""
This Program will simulate a game of blackjack
"""

import deck
import player

def main():
    shoe = deck.deck(1)
    shoe.shuffle()
    print(shoe)
    player0 = player.player('Test')
    player1 = player.player('Hunter')
    dealer = player.player('Dealer')
    playing = True

    

    while(playing):
        
        dealer.hand, player1.hand = shoe.blackjackFirstDeal()

        print(player1.name, ": ", player1.handContent())
        print(dealer.name,": ", dealer.dealerContent())

        userIn = ''
        while(userIn[:1] != 'S' and userIn[:1] != 'Q'):
            userIn = (input("(H)it, (S)tay, or (Q)uit: ")).upper()
            if(userIn[:1] == 'H'):
                print('Hit!')
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
            elif(userIn[:1] != 'D'):
                pass
            else:
                print('That was not a valid input')


if __name__ == "__main__":
    main()