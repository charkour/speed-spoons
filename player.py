'''Player class, including Human and AI.
Created 12/3/17
Final Project
@author: Charles Kornoelje (cek26).
'''

'''Make sure to turn debug to false when I turn it in'''

debug = False

from random import randint
from hand import *

class Player:
    '''Creates a player object'''
    
    NAMES = ['Bob', 'Greg', 'Jerry']
    
    def __init__(self, name = None, color = None, deck = ['0D', '0H', '0C', '0S']):
        '''Constructor'''
        # Ints are assigned to CPUs. They return True and get named.
        if str(name).isdigit():
            self._name = 'CPU: ' + self.NAMES[name]
        else:
            self._name = name
        
        # Creates a random hex color.
        if color is None:
            self._color = '#' + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9))
        
        # Adds the cards to the player's hand.
        self._hand = Hand(deck)
        
        # No player starts with having a spoon.
        self._grab_spoon_ability = False                #FIXME: Set the spoon state.
        self._have_spoon = False
        
        # Sets the received card to getting the first one of the pile. 
        self._recieved_card = self.get_received_card()
        
    def get_name(self):
        '''Accessor: Returns the name of the Player'''
        return self._name
    
    def get_color(self):
        '''Accessor: Returns the color identifer of the Player.'''
        return self._color
    
    def get_hand(self):
        '''Accessor: Returns the current hand of Player.'''
        return self._hand
    
    def get_received_card(self):
        '''Accessor: Returns the current card the Player is looking at, potentially will swap.'''
        return self._hand.get_received_card()
    
    def get_grab_spoon_ability(self):
        '''Accessor: Returns the Player's ability to grab a spoon. True if they have a match of four numbers'''
        return self._grab_spoon_ability
    
    def set_grab_spoon_ability_true(self):
        '''Mutator: Sets the Player's spoon ability to True'''
        self._grab_spoon_ability = True
        
    def set_grab_spoon_ability_false(self):
        '''Mutator: Sets the Player's spoon ability to False'''
        self._grab_spoon_ability = False
    
    def set_initial_personal_deck(self, deck, idx):
        '''Mutator: Sets the intial hand of the Player.
        Gets the cards from the ititial deck and makes sure no players overlap.'''
        if debug:
            print('This is the initial deck', deck)
        self._hand.set_personal_deck(deck[idx * 4:idx * 4 + 4])
        
    def swap_card(self, idx, start_pile):
        '''Swaps card in personal deck with the received card, and then puts the card in the to be passed on spot in the hand.'''
        
        #Gets the card from the hand that is being taken out of the deck and also changes it to the card to be passed.
        tmp_card = self.get_received_card()
        card_taken_out = self._hand.get_deck()[idx]        
        self._hand.set_card_to_pass(card_taken_out)     
        if debug:
            print('Card to pass:', self._hand.get_card_to_pass())
            print('Card_taken out:', card_taken_out)
        
        # Sets a new card in the personal text.
        self.set_card_in_personal_deck(tmp_card, idx)
        self._hand.set_received_card_when_swapping(card_taken_out)
        self.set_received_card(start_pile)
        
    
    def set_card_in_personal_deck(self, new_card, idx):
        '''Mutator: Changes the card in the hand at a certain index.'''
        self._hand.set_card_in_deck(new_card, idx)
    
    def get_spoon_state(self):
        '''Accessor: Returns the state of the spoon for the Player.
        False if they don't have a spoon, True of they do.'''
        return self._have_spoon
    
    def set_spoon_state(self):
        '''Mutator: changes the state of the spoon'''
        if self._have_spoon == False:
            self._have_spoon = True
    
    def grab_spoon(self):
        '''Mutator: Changes the state of the spoon to True and calls a function'''
        self.set_spoon_state() 
    
    def __str__(self):
        '''Printing method'''
        return str(self._name)
    
    def __repr__(self):                          # I learned about __repr__ from here: https://stackoverflow.com/questions/12933964/printing-a-list-of-objects-of-user-defined-class
        '''Prints the object when in a list'''
        return str(self)      
        
class Human(Player):
    '''Object for the user'''
    
    def __init__(self, name = 'No-Name', deck = None):
        '''Constructor'''
        Player.__init__(self, name, deck = deck)
        
#     def get_score(self):
#         '''Accessor: Returns the score of the Human.'''
#         return self._score
#         
#     def set_score(self, points = 0):
#         '''Mutator: Changes the score of the Human.'''
#         self._score += points
        
    def pass_card_on(self, start_pile):   
        '''Pass card without swapping:'''
        self.set_received_card(start_pile) 
        
    def set_received_card(self, start_pile):
        '''Mutator: Changes the card the Human is holding.'''
        if debug:
            print('THIS IS THE STARTING PILE RECEIVED:', start_pile)
        self._hand.set_received_card_hand(start_pile[0])
        start_pile.pop(0)
        
#     def take_turn(self, start_pile):
#         '''One turn for the human player'''
#         self._is_turn = True
#         #self.set_received_card(start_pile)
        
class AI(Player):
    '''Creates AI object'''
    
    def __init__(self, name):
        '''Constructor'''
        Player.__init__(self, name)
        self._bail_counter = 0
        self._reation_time = 300        # These two instance variables are unused but were intened to be implemented in the creation of the AI.
        
    def set_received_card(self, list_of_players):
        '''Mutator: Changes the card that the AI will pick-up'''
        
        # Finds the index of the player before.
        self._idx_player_before = list_of_players.index(self) - 1
        if debug:
            print('Idx of player before', self._idx_player_before)
            
        # Retreives the cards from the player before.
        self._player_before = list_of_players[self._idx_player_before]
        self._card_from_player_before = self._player_before.get_hand().get_card_to_pass()
        self._hand.set_received_card_hand(self._card_from_player_before)
        if debug:
            print('New hand of AI', self.get_hand())
        
    def pass_card_on(self):
        '''Passes card without swapping any'''
        self._hand.set_card_to_pass(self._hand.get_received_card())
        if debug:
            print('New hand of AI', self.get_hand())
        
    def AI_turn(self, list_of_players):
        '''Calculates best action.'''
        '''FIXME: The AI was intended to use the pass_card and swap_card methods; however they only use the pass method.
        I was hoping to use If statements to calculate best card to match with, but I found the logic would be much harder than originally thought.
        Currently, the computers hold the cards in their hand and pass them on. They aren't the smartest guys but they sure are cute.
        They are like cute, little pet rocks who are so kind and do what they are told and pass their cards without messing up.
        I tried several times to implement and trouble-shoot my swap_cards method with the AI but I couldn't solve the errors.'''
        
        # Bail increments, would be used by AI logic. 
        self._bail_counter += 1
        
        # Sets the receives card and passes it on.
        self.set_received_card(list_of_players)
        self.pass_card_on()
        if debug:
            print('AI %s Took turn' % self.get_name())

      
        
if __name__ == '__main__':
    # More random testing code.
    
    # Testing human and changing the hand.
    human = Human()
    print('Human and their hand:', human.get_name(), human.get_hand())
    
    # Changing the hand
    print('Chaning hand: Placing 2D into idx 1 (Second pos)')
    from card import *
    from deck import *
    test_deck = ['0D', '0H', '0C', '0S']
    test_card = Card(2,'D')
    human.set_initial_personal_deck(test_deck, 0)
    human.set_card_in_personal_deck(test_card, 1)
    print('Human hand after changing 2nd pos', human.get_hand())        #FIXME: The new card in the deck is not a string. Not sure if that is an issure.
    
    ai= AI(1)
    print('AI 1 hand:', ai.get_hand())
    
    # Setting up a game and testing the ability of set_ititial_hand()
    from main import *
    game = Game()
    print(game.get_deck())
    print(game.get_human().get_hand(), end = '')
    
    # Try getting the hand of the AI
    for AI in game.get_AI_list():               #FIXME: Needs to be fixed. I think this works.
        print('\nThe AI\'s hand', AI.get_hand(), end = '')
        
    # The starting card of the human.
    print('\nStarting Picked Up Card of the Human: ', game.get_human().get_received_card())
    
    #Have human pick up new card, and get another.        THIS WORKS!
    game.get_human().set_received_card(game.get_start_pile())
    print('New human hand:', game.get_human().get_hand())
    game.get_human().set_received_card(game.get_start_pile())
    print('New human hand:', game.get_human().get_hand())
    
    ai1 = game.get_AI_list()[0]
    print('ai1', ai1, ai1.get_hand())
    
    ai1.set_received_card(game.get_player_list())
    ai1.pass_card_on()