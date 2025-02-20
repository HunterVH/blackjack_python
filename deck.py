'''
The definition of the deck class.
'''

import card
import random

'''
This class can be used to create a deck object that can hold cards
'''
class deck:
    '''
    This is the initial creation of the deck
    '''
    def __init__(self, size):
        ACEVALUE = 11
        self.cards = []
        self.size = size*52
        for j in range(self.size):
            suit = j//(13*size)
            value = j%13+1
            match suit:
                case 0:
                    match value:
                        case 1:
                            self.cards.append(card.card('A♥','Hearts', ACEVALUE))
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
                            self.cards.append(card.card('A♦','Diamonds', ACEVALUE))
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
                            self.cards.append(card.card('A♣','Clubs', ACEVALUE))
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
                            self.cards.append(card.card('A♠','Spades', ACEVALUE))
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
    
    '''
    Prints all cards that are inside the deck
    '''
    def __str__(self):
        deck = self.cards[0].name
        for j in range(1,(self.size)):
            deck = deck+', '+(self.cards[j].name)
        return deck
    
    '''
    Randomly shuffles the deck
    '''
    def shuffle(self):
        random.shuffle(self.cards)

    '''
    Simulates an intial blackjack deal, two cards to the player, two cards to 
    the dealer
    '''
    def blackjackFirstDeal(self):
        # Add a new shuffled deck if the deck runs out of cards
        if(self.size < 4):
            newDeck = deck(1)
            newDeck.shuffle()
            self.cards = newDeck.cards + self.cards
            self.size = newDeck.size + self.size
            pass

        dealerHand = []
        playerHand = []
        dealerHand.append(self.cards.pop())
        playerHand.append(self.cards.pop())
        dealerHand.append(self.cards.pop())
        playerHand.append(self.cards.pop())

        self.size -= 4

        return dealerHand, playerHand
    
    '''
    Returns the next card in the deck
    '''
    def hit(self):
        # Add a new shuffled deck if the deck runs out of cards
        if(self.size < 1):
            newDeck = deck(1)
            newDeck.shuffle()
            self.cards = newDeck.cards + self.cards
            self.size = newDeck.size + self.size
            
        self.size -= 1
        
        return self.cards.pop()

def test():
    deck1 = deck(5)
    print('Created')
    print(deck1)
    deck1.shuffle()
    print(deck1)
    pass

if __name__ == "__main__":
    test()