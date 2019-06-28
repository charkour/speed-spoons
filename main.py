'''Speed Spoons! The Game setup and execution.
Created 12/3/17
Final Project
@author: Charles Kornoelje (cek26).
'''

debug = False

from random import shuffle
from player import *   
        
class Game:
    '''Creates a game object.'''
    def __init__(self):
        '''Constructor'''
        
        # Program waits for the Human to input if wait_state is True. 
        self._wait_state = True
        
        # Create the deck
        self._game_deck = Deck()
        self._game_deck.create_deck_of_52()
        self._game_deck_cards = self._game_deck.get_deck()
        
        # Sets up the number of players, spoons, and AI counts.
        self._players = 4
        self._list_of_AI = [ ]
        self._list_of_players = [ ]
        self._AI = self._spoons = self._players - 1
        
        # From the cards picked by the players, the start pile is created.
        start_point = self._players * 4
        self._start_pile = self._game_deck_cards[start_point:]
        if debug:
            print('Start Pile:', self._start_pile)
        
        # Container to hold all the cards passed by final player.
        self._end_pile = [ ]
        
        # Create the Human and add to the list of Players.
        self._human = Human('Human', deck = self._game_deck_cards)
        self._list_of_players.append(self._human)
        
        # Crate the AI, appends then to a list of AI.
        for AI_player in range(self._AI):
            tmp_player = AI(AI_player)
            self._list_of_AI.append(tmp_player)
            self._list_of_players.append(tmp_player)
        if debug:
            print('List of the players:', self._list_of_players)

        # Set the inital hand for each of the players in the list.
        for player in self._list_of_players:
            player.set_initial_personal_deck(self._game_deck_cards, self._list_of_players.index(player)) # Passes the idx of the player in the list as an argument.
            
        # Sets the initial recieved card of the human from the start_pile.
        self._human.set_received_card(self._start_pile)
        
    def get_deck(self):
        '''Accessor: Returns the deck used in the game.'''
        return self._game_deck_cards
    
    def get_start_pile(self):
        '''Accessor: Returns the start pile'''
        return self._start_pile
    
    def get_end_pile(self):
        '''Accessor: Returns the end pile'''
        return self._end_pile
    
    def get_AI_list(self):
        '''Accessor: Returns the list of the AI'''
        return self._list_of_AI
    
    def get_player_list(self):
        '''Accessor: Returns the list of the Players'''
        return self._list_of_players
    
    def get_human(self):
        '''Accessor: Returns human object'''
        return self._human
    
    def get_human_name(self):
        '''Accessor: Returns human name.'''
        return self._human.get_name()
    
    def get_human_deck(self):
        '''Accessor: Returns the deck of the human'''
        return self._human.get_hand().get_deck()
    
    def get_human_hand(self):
        '''Accessor: Returns the human hand'''
        return self._human.get_hand().get_hand_contents()
    
    def get_human_received_card(self):
        '''Accessor: Returns the received card of the Human:'''
        return self._human.get_hand().get_received_card()
    
    def get_spoons(self):
        '''Accessor: Returns the spoon number'''
        return self._spoons
    
    def get_wait_state(self):
        '''Accessor: Returns the wait state.'''
        return self._wait_state
    
    def change_wait_state_true(self):
        '''Mutator: Sets wait_state to True'''
        self._wait_state = True
        
    def change_wait_state_false(self):
        '''Mutator: Sets wait_state to False'''
        self._wait_state = False
        
#     def AI_pass_card(self):
#         '''Actions of the AI to pass a card on without swapping any.'''
        
    def add_to_end_pile(self):
        '''Takes the card from the last player and adds it to the end pile.'''
        self._end_card = self._list_of_players[-1].get_hand().get_card_to_pass()
        self._end_pile.append(self._end_card)
        
        # If the length of the pile is 0, the end pile is shuffled and a copy is passed to the start_pile.
        if len(self._start_pile) == 0:
            shuffle(self._end_pile)
            self._start_pile = self._end_pile[:]
            self._end_pile = [ ]
        if debug:
            print('End Pile:', len(self._end_pile), self._end_pile)
            print('Type of card added:', type(self._end_card), self._end_card)
            
    def check_if_four_match(self, player):
        '''After every player's turn, checks to see if Player can grab the spoon.
        If Player can grab the spoon, sets their spoon ability to True, and False if otherwise.'''
        self._four_deck = player.get_hand().get_deck()
        if self._four_deck[0].get_num() == self._four_deck[1].get_num() == self._four_deck[2].get_num() == self._four_deck[3].get_num():    # Checks if all numbers are the same.
            player.set_grab_spoon_ability_true()
            if debug:
                print('Match!')
        else:
            player.set_grab_spoon_ability_false()


        
if __name__ == '__main__':
    
    # Random testing. I apologize for the messy blocks of code.
    print('Default Card:', Card())
    deck = Deck()
    deck.create_deck_of_52()
    game_deck = deck.get_deck()
    for card in game_deck:
        print(card, end = ' ')
    print('The deck of cards', deck)
    
    print('Initailizaing game class.')
    game = Game()
    print(game._game_deck)
    print(game.get_deck())
    
    print('List of AI')
    print(game.get_AI_list())
    print(game.get_human_name())
    
    print("Player's hand")
    print(game._human.get_hand())       # Uses Private Variable
    
    print('Testing the number of things in game creation:')
    print(game._AI)
    print(game._spoons)
    
    print('The Human\'s hand:')
    print(game.get_human().get_hand())
    
    print(game.get_human().get_received_card())