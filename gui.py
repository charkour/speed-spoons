'''GUI for Speed Spoons. Let's the user interact with the game code.
Created 12/3/17
Final Project
@author: Charles Kornoelje (cek26)
'''

# spoon img from https://media.istockphoto.com/photos/spoon-picture-id499224263?k=6&m=499224263&s=612x612&w=0&h=ZVjPCVsOUPkI4nOpP-dK7n6QE9YJaPjtwYuDMQIVI4c=

debug = False

from tkinter import *
from main import *

class GUI:
    '''Simple GUI Object'''
    
    # By having a constant width and height, I wanted everything on the GUI to be scaled off of them. But I didn't have enough time to finish all the calculations.
    W = 600
    H = 600
    
    def __init__(self, window):
        '''Constructor'''
        
        # Window widgets is created.
        self._window = window
        self._canvas = Canvas(window, width=GUI.W, height=GUI.H)
        self._canvas.grid()
        self._show_start_screen(1)
        
        # The timer is set to 0 at the beginning of each game.
        self._time = 0
        self.timer()

    def _show_start_screen(self, event):
        '''The title screen when the game starts up'''
        
        # Canvas is created and gridded.
        self._canvas.grid_forget()
        self._canvas = Canvas(self._window, width=GUI.W, height=GUI.H)
        self._canvas.grid()
        self._title = self._canvas.create_text(GUI.W/2, GUI.H/4, font=("Times", 54, 'bold'), text="SPEED SPOONS!") 
        
        # Note: I liked using the rectangle as a button rather than the Button widget because I could visually customize the rectangle.
        # This creates the begin button.
        self._start_button = self._canvas.create_rectangle(270, 300, 330, 340, fill ='red')  
        self._start_text = self._canvas.create_text((GUI.W/2, GUI.H/2+20), text="Begin!") 
        self._canvas.tag_bind(self._start_button, '<Button-1>', self._show_game_screen)
        self._canvas.tag_bind(self._start_text, '<Button-1>', self._show_game_screen)
        
        # The how-to text on the screen.
        self._title = self._canvas.create_text(310, 500, font=("Times", 12), 
                                               text='The GOAL of the game is to quickly get four cards of the same number or face value'
                                                '\nand then grab a spoon before the three computer opponents.'
                                                '\nThe computers will take their turn after you, the human, swaps a card.'
                                               '\nTo PLAY, click on one of the four cards on the left side of the screen to swap it with the card on the right.'
                                               '\nClick the card on the right to pass and get a new card.'
                                               '\nOnce four of a kind are in a hand, click one of the spoons to win the game!'
                                               '\nRemember, the goal is SPEED!') 
        
    
    def _show_game_screen(self, event):
        '''The game screen'''
        # Get rids of the canvas to make a new screen.
        self._canvas.grid_forget()

        # Game object initaited
        self._game = Game()
        
        # Time set to zero if game is played again.
        self._time = 0
        
        # Canvas is created and gridded.
        self._canvas = Canvas(self._window, width=GUI.W, height=GUI.H)
        self._canvas.grid()
        
        # line is created to divide game screen.
        self._canvas.create_line(0, GUI.W*4/11, GUI.W, GUI.H*4/11)
        
        # Creates PhotoImage objects for all the cards in the deck.
        self._photos = [ ]
        self._game_deck = self._game.get_deck()
        for card in self._game_deck:
            tmp_photo = PhotoImage(file = card.get_card() + '.gif')
            self._photos.append(tmp_photo)
        if debug:
            print(self._photos)
        
        # Finds the idx of the card held by Human in the game_deck. Adds idx to lsit.    
        self._photo_locs = [ ]    
        human_deck = self._game.get_human_deck() 
        for card in human_deck:
            tmp_idx = self._game_deck.index(card)
            self._photo_locs.append(tmp_idx)
        if debug:
            print('Human Deck:', human_deck)
            print('Human deck element type:', type(human_deck[0]))
        
        # For each card in the hand, the index position in the game_deck is used to pick the correct tkinter PhotoImage object.
        # Lambda is used to pass in arguments when the card is clicked.
        # I had to repeat this code because I was unable to update the images on click.
        if self._game.get_wait_state():
            self._id0 = self._canvas.create_image(100, 400, image=self._photos[self._photo_locs[0]])        #Note: The image center is placed at the coords.
            self._canvas.tag_bind(self._id0, '<Button-1>', lambda event, x=self._photo_locs[0]: self.swap_command(card_idx=self._photo_locs[0], button_number=0, id=self._id0))
                                  
            self._id1 = self._canvas.create_image(200, 400, image=self._photos[self._photo_locs[1]])        #Note: The image center is placed at the coords.
            self._canvas.tag_bind(self._id1, '<Button-1>', lambda event, x=self._photo_locs[1]: self.swap_command(card_idx=self._photo_locs[1], button_number=1, id=self._id1))
                                   
            self._id2 = self._canvas.create_image(300, 400, image=self._photos[self._photo_locs[2]])        #Note: The image center is placed at the coords.
            self._canvas.tag_bind(self._id2, '<Button-1>', lambda event, x=self._photo_locs[2]: self.swap_command(card_idx=self._photo_locs[2], button_number=2, id=self._id2))
                                   
            self._id3 = self._canvas.create_image(400, 400, image=self._photos[self._photo_locs[3]])        #Note: The image center is placed at the coords.
            self._canvas.tag_bind(self._id3, '<Button-1>', lambda event, x=self._photo_locs[3]: self.swap_command(card_idx=self._photo_locs[3], button_number=3, id=self._id3))
              
            if debug:
                print('Current Human Hand')
                print(self._game.get_human().get_hand())      #Currently the cards displayed are the first four in the deck. Like the human hand.
        
            # The card that is received from the start pile is displaced.
            self._human_card_received = self._game.get_human_received_card()
            if debug:
                print('Game Deck:', len(self._game_deck), self._game_deck)
                print('Human hand, received card:', self._game.get_human_received_card())
                print('Human received card:', type(self._human_card_received))
                
            # To display the card, the location of the card in the list of photos is found and then printed.
            self._photo_loc = self._game_deck.index(self._human_card_received)
            self._received_image = self._canvas.create_image(550, 400, image=self._photos[self._photo_loc])
            self._canvas.tag_bind(self._received_image, '<Button-1>', self.pass_command)

        # Creates text to display the players in the game.
        self._player_text = self._canvas.create_text((30, 10), text="Players:")
        self._player_list = self._game.get_player_list()
        for x in range(len(self._player_list)):
            self._player_name = self._canvas.create_text((30, 25 + (15 * x)), text=self._player_list[x], anchor='w')
        
        # Text to label the the hand and the received card.
        self._hand_text = self._canvas.create_text((260, 500), text="Hand of Four Cards")
        self._received_text = self._canvas.create_text((550, 500), text="Received Card")
        
        # Puts the spoons on the screen.
        self._spoon_img = PhotoImage(file = 'spoon_resized.gif')
        for spoon in range(self._game.get_spoons()):
            spoon = self._canvas.create_image(250 + 50 * spoon, 100, image=self._spoon_img)
            self._canvas.tag_bind(spoon, '<Button-1>', lambda event, x=spoon: self.spoon_command(x))
        
    def _end_screen(self):
        '''To display the high score after the game'''
        # Clear the screen of the game screen.
        self._canvas.grid_forget()
        
        # Creates a new canvas.
        self._canvas = Canvas(self._window, width=GUI.W, height=GUI.H)
        self._canvas.grid()
        
        # Prints the outcome of the game for the Human.
        if self._game.get_human().get_spoon_state():
            if debug:
                print('They have the spoon')
            self._title = self._canvas.create_text(GUI.W/2, GUI.H/4, font=("Times", 54, 'bold'), text="YOU WIN!\nYOU GOT A SPOON.") 
        else:
            self._title = self._canvas.create_text(GUI.W/2, GUI.H/4, font=("Times", 54, 'bold'), text="YOU LOST!\nCPU GOT A SPOON.")
        
        # Creates the retry button to return to the start screen.
        self._retry_button = self._canvas.create_rectangle(270, 480, 330, 520, fill ='red')  
        self._retry_text = self._canvas.create_text((GUI.W/2, GUI.H/2+200), text="Retry?") 
        self._canvas.tag_bind(self._retry_button, '<Button-1>', self._show_start_screen) 
        self._canvas.tag_bind(self._retry_text, '<Button-1>', self._show_start_screen)
        
        # Open the highscore file. Gets the highscore.
        with open('highscore.txt') as highscore:
            self._highscore = highscore.readline()
        if self._highscore == '':       #If file is empty for some reason, give a big score.
            self._highscore = str(900000)
        
        # The final score is the time from the timer when the spoon is grabbed.
        self._final_time = self._time
        
        # Compares the highscores and then overwrites the high score. Prints the outcome on the screen.
        if int(self._highscore) > self._final_time:
            print('NEW HIGH SCORE')
            f = open('highscore.txt', 'w')
            f.write(str(self._final_time))
            f.close()
            self._start_text = self._canvas.create_text((300, 260), text="NEW HIGH SCORE: %s" % self._final_time)
        else:
            self._start_text = self._canvas.create_text((300, 260), text="Not a new high score.\nYour Score: %s\nHigh Score: %s" % (self._final_time, self._highscore))
            if debug:
                print('Not a new high score', self._final_time)     
                print('Type of file score:', type(self._highscore))
                print('TYpe of timer score:', type(self._final_time))
        
    def timer(self):
        '''Timer for high scores'''
        # Repeats every second.
        root.after(1000, self.timer)
        self._time += 1
        if debug:
            print('TIme:', self._time)
        
    def spoon_command(self, spoon_num):
        '''Checks if the player is able to grab the spoon.'''    
        if debug:
            print(spoon_num, 'The button worked')
        if self._game.get_human().get_grab_spoon_ability() is False:
            if debug:
                print('Cannot grab spoon!')
        else:
            print('Able to grab spoon!')
            self._game.get_human().set_spoon_state()
            self._end_screen()

    def swap_command(self, card_idx, button_number, id):
        '''Swap card images'''
        # Change the wait state.
        self._game.change_wait_state_false()
        if debug:
            print(card_idx, 'The button worked')
        
        # Find the location of the picture and then display it.
        photo_loc = self._game_deck.index(self._game.get_human().get_hand().get_received_card())
        self._game.get_human().swap_card(card_idx, self._game.get_start_pile())
        self._canvas.itemconfig(id, image=self._photos[photo_loc])
        
        # Find the location of the next card in the deck and display it on the screen.
        photo_loc2 = self._game_deck.index(self._game.get_human().get_hand().get_received_card())
        self._canvas.itemconfig(self._received_image, image=self._photos[photo_loc2])
        
        # Checks to see if the human has a match of four.
        self._game.check_if_four_match(self._game.get_human())
        if debug:
            print('Human hand', self._game.get_human().get_hand())
        
        # Makes the AI take their turn, and finishes the rest of the game.
        self.AI_turn()
        self._game.add_to_end_pile() 
        self._game.change_wait_state_true()
        
    def pass_command(self, event):
        '''Pass card images.'''
        # Change the wait state.
        self._game.change_wait_state_false()
        
        # Changes the received card to the card to pass and find the photo location.
        self._game.get_human().pass_card_on(self._game.get_start_pile())
        photo_loc = self._game_deck.index(self._game.get_human().get_hand().get_received_card())
        self._canvas.itemconfig(self._received_image, image=self._photos[photo_loc])
        
        # Checks to see if the human has a match of four.
        self._game.check_if_four_match(self._game.get_human())
        if debug:
            print('Human hand:', self._game.get_human().get_hand())  
            
        # Makes the AI take their turn, and finishes the rest of the game.              
        self.AI_turn()
        self._game.add_to_end_pile()
        self._game.change_wait_state_true()
       
        
    def AI_turn(self):
        '''Make the AI take all their turns.'''
        for ai in self._game.get_AI_list():
            ai.AI_turn(self._game.get_player_list())
            self._game.check_if_four_match(ai)
        

if __name__ == '__main__':
    # Runs the GUI.
    root = Tk()
    root.title('Speed Spoons!')
    app = GUI(root)
    root.mainloop()