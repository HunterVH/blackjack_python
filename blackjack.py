"""
This Program will simulate a game of blackjack
"""

import deck
import player

# def firstDeal(playerHand, dealerHand, shoe):
#     playerTotal = 0
#     dealerTotal = 0
#     for j in range(4):
#         card = shoe.pop()
#         cardValue = int(card[1:])
#         if(cardValue > 10):
#             if(j%2 == 1):
#                 playerTotal += 10
#                 playerHand.append(card)
#             else:
#                 dealerTotal += 10
#                 dealerHand.append(card)
#         elif(cardValue == 1):
#             if(j%2 == 1):
#                 playerTotal += 11
#                 playerHand.append(card)
#             else:
#                 dealerTotal += 11
#                 dealerHand.append(card)
#         else:
#             if(j%2 == 1):
#                 playerTotal += cardValue
#                 playerHand.append(card)
#             else:
#                 dealerTotal += cardValue
#                 dealerHand.append(card)

#     return playerTotal, dealerTotal


def main():
    shoe = deck.deck(5)
    print(shoe)
    player1 = player.player('Hunter')
    dealer = player.player('Dealer')
    playing = True

    

    while(playing):
        
        dealer.hand, player1.hand = shoe.blackjackFirstDeal()
        dealer.update()
        player1.update()

        userIn = ''
        while(userIn[:1] != 'S' and userIn[:1] != 'Q'):
            userIn = (input("(H)it, (S)tay, or (Q)uit: ")).upper()
            print(userIn)
            print(userIn[:1])
            if(userIn[:1] == 'H'):
                print('Hit!')
            elif(userIn[:1] == 'S'):
                print('Stay!')
            elif(userIn[:1] == 'Q'):
                print('Quitter!')
            else:
                print('That was not a valid input.')

        while(userIn != 'D' and userIn != 'Q'):
            userIn = input('(D)eal or (Q)uit: ').upper()
            if(userIn[:1] == 'Q'):
                playing = False
            elif(userIn[:1] != 'D'):
                pass
            else:
                print('That was not a valid input')


if __name__ == "__main__":
    main()