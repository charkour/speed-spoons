'''Hand Class.
Created 12/3/17
Final Project
@author: Charles Kornoelje (cek26)
'''

# Each player will have a hand with their deck of 4 cards and also an additional card that they will have picked up.

from deck import *

class Hand:
    '''Creates a hand object.'''
    
    def __init__(self, deck = [ ]):
        '''Constructor'''
        
        self._personal_deck = Deck()
        self._personal_deck.set_deck(deck)
        self._received_card = ''
        self._card_to_pass = ''
        
    def get_hand_contents(self):
        '''Accessor: Returns the hand as a list of lists.'''
        return [str(self._personal_deck), str(self._received_card), str(self._card_to_pass)]
    
    def get_deck(self):
        '''Accessor: Returns the deck of the hand'''
        return self._personal_deck.get_deck()
    
    def get_received_card(self):
        '''Accessor: Returns the received card of the hand'''
        return self._received_card
    
    def get_card_to_pass(self):
        '''Accessor: Returns the card to be passed on.'''
        return self._card_to_pass
    
    def set_received_card_hand(self, card_from_player):
        '''Mutator: Sets the received card in hand to new card.'''
        '''CALLS set_card_to_pass()'''
        self.set_card_to_pass(self._received_card)
        self._received_card = card_from_player
        
    def set_received_card_when_swapping(self, new_received_card): 
        '''Mutator: Sets the received card when two are swapped'''
        self._received_card = new_received_card   

    def set_card_to_pass(self, card_to_pass_on):
        '''Mutator: Sets card to be passed to next player.'''
        self._card_to_pass = card_to_pass_on
        
    def set_personal_deck(self, new_deck):
        '''Mutator: Sets the personal deck of the Player.'''
        self._personal_deck.set_deck(new_deck)
        
    def set_card_in_deck(self, new_card, idx):
        '''Mutator: Changes a card in the deck of four for the Player.'''
        self._personal_deck.set_specific_card(new_card, idx)
        
    def __str__(self):
        '''Printing method for the hand.'''
        return str(['Personal Deck:', str(self._personal_deck), 'Card Recieved:' ,self._received_card, 'Card to pass:', self._card_to_pass])
        
    def __reper__(self):
        '''When get fn is called, get the objects representation'''
        return str(self)
    
    
    
if __name__ == '__main__':
    hand1 = Hand()
    print('The hand of the player', hand1.get_hand_contents())
    
    from main import *
    game = Game()
    print(game.get_deck())
    print(game.get_human().get_hand())