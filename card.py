'''Card Class
Created 12/3/17
Final Project
@author: Charles Kornoelje (cek26).
'''

class Card:
    '''Class that creates a card object.'''
    
    # Helpful list of suits.
    SUITS = ['S', 'C', 'H', 'D']                    
    
    def __init__(self, num = 10, suit = 'D'):
        '''Constructor'''
        
        # Assigns the card number, making sure that it is valid.
        if num < 1 or num > 13:
            raise ValueError('Please enter a number between 1-13 inclusivly.')
        else:
            self._num = num
        
        if suit not in Card.SUITS:
            raise ValueError('Please enter a valid suit: S, C, H, D.')
        else:
            self._suit = suit
            
    def get_num(self):
        '''Accessor: Returns the number of the card.'''
        return self._num
    
    def get_suit(self):
        '''Accessor: Returns the suit of the card.'''
        return self._suit
    
    def get_card(self):
        '''Accessor: Returns the number and suit of the card.'''
        return str(self._num) + self._suit
                
    def __str__(self):
        '''Printing method for the card.'''
        return str(self._num) + self._suit
    
    def __repr__(self):        
        '''Prints the object when in a list'''
        return str(self)