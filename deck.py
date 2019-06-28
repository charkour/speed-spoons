'''Deck class
Created 12/3/17
Final Project
@author: Charles Kornoelje (cek26)
'''

# The deck will keep track of the lists of cards. list of 52 for the game deck, and 4 for the hand.
# This deck class caused me a lot of trouble. Professor Norman explained how he used a deck class in his solitare game and the applications seemed very helpful;
# however, in my program, I found that this class was maybe not needed, but I kept it in because it would have taken too much time to remove the class after already integrating it.

from random import randint
from card import *

class Deck:
    '''Creates a deck object, which is a list of cards.'''
    
    def __init__(self):
        '''Constructor'''
        # Creates a placeholder list.
        self._deck = ['0D', '0H', '0C', '0S']

    def get_deck(self):
        '''Accessor: Returns the list of cards'''
        return self._deck

    def set_deck(self, new_deck):
        '''Mutator: to update the deck'''
        self._deck = new_deck
        
    def get_specific_card(self, idx):
        '''Accessor: Get the specific card in the deck'''
        card = self._deck[idx]
        return card.get_card()
    
    def set_specific_card(self, new_card, idx):
        '''Mutator: Changes the specific card.'''
        self._deck.pop(idx)
        self._deck.insert(idx, new_card)

    '''FIXME: Where should this function go. In Cards or in here?'''
    def create_deck_of_52(self, debug = False):
        '''Calls the card class and creates a deck of 52 cards'''
        
        suits = ['S', 'C', 'H', 'D']
        cards = [ ]
        
        # Creates a card 1-13 and makes the card for each suit.
        for nums in range(13):
            for suit in suits:
                tmp_card = Card(nums+1,suit)
                cards.append(tmp_card)
        
        if debug:
            print('Deck Before suffled', cards)
        
        self.shuffle(cards)           # Suffles the cards.
                
        if debug:
            print('Deck after shuffled', cards)
            
        self.set_deck(cards)
    
    def shuffle(self, deck):
        '''Shuffle Cards'''
        
        #Loops 5*7 times, research found it was the best randomness.           #https://www.dartmouth.edu/~chance/teaching_aids/Mann.pdf
        for i in range(364):        #Should this be a while loop?
        
            #Picks random location on the list, assigns value to char, removes the char from list.
            rand_loc = randint(0, len(deck) - 1)
            card = deck[rand_loc]
            deck.remove(card)
            
            #Picks new random location list, inserts char back into list.
            rand_loc = randint(0, len(deck) - 1)
            deck.insert(rand_loc, card)    
            
        # Doesn't need to return anything because the method is changing a mutable object.
     
    def __str__(self):
        '''Printing method for the deck.'''
        return str(self._deck)
        
    def __reper__(self):
        '''When get fn is called, get the objects representation'''
        return str(self)
        
if __name__ == '__main__':
    game_deck = Deck()
    game_deck.create_deck_of_52()
    print(game_deck)
    print(type(game_deck.get_deck()), game_deck.get_deck())