'''
The definition of the deck class.
'''

import card
import random

class deck:
    # This is the initial creation of the deck 52 objects of the card class
    def __init__(self, size):
        self.cards = []
        self.size = size
        for j in range(52*self.size):
            suit = j//(13*self.size)
            value = j%13+1
            match suit:
                case 0:
                    match value:
                        case 1:
                            self.cards.append(card.card('A♥','Hearts', 11))
                            pass
                        case 11:
                            self.cards.append(card.card('J♥', 'Hearts', 10))
                        case 12:
                            self.cards.append(card.card('Q♥', 'Hearts', 10))
                        case 13:
                            self.cards.append(card.card('K♥', 'Hearts', 10))
                        case _:
                            self.cards.append(card.card(str(value)+'♥', 'Hearts', value))
                            pass
                case 1:
                    match value:
                        case 1:
                            self.cards.append(card.card('A♦','Diamonds', 11))
                        case 11:
                            self.cards.append(card.card('J♦', 'Diamonds', 10))
                        case 12:
                            self.cards.append(card.card('Q♦', 'Diamonds', 10))
                        case 13:
                            self.cards.append(card.card('K♦', 'Diamonds', 10))
                        case _:
                            self.cards.append(card.card(str(value)+'♦', 'Diamonds', value))
                case 2:
                    match value:
                        case 1:
                            self.cards.append(card.card('A♣','Clubs', 11))
                        case 11:
                            self.cards.append(card.card('J♣', 'Clubs', 10))
                        case 12:
                            self.cards.append(card.card('Q♣', 'Clubs', 10))
                        case 13:
                            self.cards.append(card.card('K♣', 'Clubs', 10))
                        case _:
                            self.cards.append(card.card(str(value)+'♣', 'Clubs', value))
                case 3:
                    match value:
                        case 1:
                            self.cards.append(card.card('A♠','Spades', 11))
                        case 11:
                            self.cards.append(card.card('J♠', 'Spades', 10))
                        case 12:
                            self.cards.append(card.card('Q♠', 'Spades', 10))
                        case 13:
                            self.cards.append(card.card('K♠', 'Spades', 10))
                        case _:
                            self.cards.append(card.card(str(value)+'♠', 'Spades', value))
                case _:
                    print("ERROR: deck.py match/case statement.")
                #♥/♦/♣/♠ alt 3/4/5/6
    # Calling a print to deck will print all values of the "cards" list
    def __str__(self):
        deck = self.cards[0].name
        for j in range(1,(52*self.size)):
            deck = deck+', '+(self.cards[j].name)
        return deck
    
    # This uses the random library to shuffle the "cards" list
    def shuffle(self):
        random.shuffle(self.cards)

    def blackjackFirstDeal(self):
        dealerHand = []
        playerHand = []
        dealerHand.append(self.cards.pop())
        playerHand.append(self.cards.pop())
        dealerHand.append(self.cards.pop())
        playerHand.append(self.cards.pop())

        return dealerHand, playerHand
        

def test():
    deck1 = deck(5)
    print('Created')
    print(deck1)
    deck1.shuffle()
    print(deck1)
    pass

if __name__ == "__main__":
    print('Entered')
    test()