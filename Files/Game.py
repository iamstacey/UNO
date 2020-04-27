
from .Deck import UNO_Deck
from .Players import Player
from random import random, choice
from colorama import Fore, Style, init
from .Cards import Card
init()

deck = UNO_Deck()


class UNO_Game():
    def __init__(self):
        self.deck = deck.create_a_deck()
        self.players_number = 0
        self.players = []
        self.winner = None
        self.card_to_match = choice(self.deck)
        self.discarded_cards = []

    
    def ask_players_number(self):
        """Ask how many players are going to be
        playing the game, then ask their names and save them 
        at the players attributte"""

        print(Fore.MAGENTA + """
                             
,--. ,--.,--.  ,--. ,-----.  
|  | |  ||  ,'.|  |'  .-.  ' 
|  | |  ||  |' '  ||  | |  | 
'  '-'  '|  | `   |'  '-'  ' 
 `-----' `--'  `--' `-----'  
                             
""" + Style.RESET_ALL)

        print(" Select the mode of the game ".center(110, '='))
        print("A) Two players".center(100, ' '))
        print('B) Three players'.center(100, ' '))
        print('C) Four players'.center(100, ' '))

        while self.players_number < 2:
            try:
                election = input('Election: ')

                if election.upper() == 'A':
                    self.players_number = 2
                elif election.upper() == 'B':
                    self.players_number = 3
                elif election.upper() == 'C':
                    self.players_number = 4
                else:
                    print(Fore.red+ 'Oh, it looks like you are trying to select an unplayable number of players. Try again with one of the options.' + Style.RESET_ALL)
            except:
                print(Fore.RED +'Oh, it looks like you are trying to select an unplayable number of players. Try again with one of the options.' + Style.RESET_ALL)               
              
            for i in range(1, self.players_number + 1):
                player = Player(i)
                self.players.append(player)
        return self.players_number

   
    def assign_player_cards(self, player, number_of_cards):
        """Assign cards to the player deppending of
        the number of the cards that the player
        is going to receive
        """
        for i in range(number_of_cards):
            card = choice(self.deck)
            player.cards.append(card)
            self.discarded_cards.append(card)
            self.deck.remove(card)
        return player.cards
   
    def looking_for_winner(self, player):
        """Check if the player has no cards
        if it's true then the player is the winner
        """
        if len(player.cards) == 0:
            self.winner = player
        else:
            self.winner = None
    
        return self.winner
    
    
    def first_cards(self):
        """ Assign the first 7 cards
        to all the players in the game
        """
        for player in self.players:
            self.assign_player_cards(player, 7)
   
    def first_card_to_match(self):
        """Makes sure that the game start
        with a normal card
        """
        while self.card_to_match.category != 'Normal':
            self.card_to_match = choice(self.deck)
    
    def change_color(self, player):
        """Change the current card to match
        to a color to match, the color is going
        to be selected by the user that dropped the card
        able to change the color
        """
        while self.card_to_match.category != 'Colour':
            try:
                new_color = input('Write the new color: ')
                if new_color.capitalize() in deck.colours:
                    self.card_to_match = Card(" ", " ", " ", 'Colour')       
                    self.card_to_match.color = new_color.capitalize()
                    print('{} changed the color to {}'.format(player.name, self.card_to_match.color))
                else:
                    print(Fore.RED + "The color that you are trying to put is unavaible" + Style.RESET_ALL)
            except:
                print(Fore.RED + "The color that you are trying to put is unavaible" + Style.RESET_ALL)
        return self.card_to_match
     
    def verify_uno(self, player):
        """Verify if the player only has one card
        """
        if len(player.cards) == 1:
            if player.UNO == True:
                print(Fore.GREEN + "Is this real? You are about to win." + Style.RESET_ALL)
            else:
                print(Fore.RED + "You didn't shout UNO and you have one card. You are going to receive two cards so you won't worry about shouting UNO." + Style.RESET_ALL)
                self.assign_player_cards(player, 2)
        elif len(player.cards) == 2:
            print(Fore.GREEN + 'You just have two cards, it means that you are about to win. Unless somebody decide to drop a drag 4 card...' + Style.RESET_ALL)
    def verify_deck(self):
        """If there are no enough cards
        at the deck, add the discarded cards
        back to the game
        """
        if len(self.deck) == 5:
            self.deck.extend(self.discarded_cards)
            self.discarded_cards = []
        else:
            pass
            
    def player_system(self):
        """Ask the card that the player wants to drop,
        execute the rule of the card and then it goes
        to the next player's turn until the game
        finds a winner
        """
        self.first_cards()
        while self.winner == None:
            counter = 0
            while counter < self.players_number:
                current_player = self.players[counter]

                print("It's {} turn".format(current_player.name))
                current_player.show_all_cards()

                if self.card_to_match.category == 'Colour':
                    print('Color to match: ' + self.card_to_match.show_card())
                else:
                    print('Card to match: ' + self.card_to_match.show_card())
                try:
                    action = input('Drop, drag or UNO: ')

                    if action.capitalize() == 'Drop':
                        self.verify_uno(current_player)
                        try: 
                            card_number = int(input('Write the number of the card to drop: '))
                            dropped_card = current_player.cards[card_number]
                            if dropped_card.color == self.card_to_match.color:
                                if dropped_card.category == 'Normal':
                                    print(Fore.GREEN + '{} dropped: {}'.format(current_player.name, dropped_card.show_card()) + Style.RESET_ALL)
                                    current_player.cards.remove(dropped_card)
                                    self.card_to_match = dropped_card
                                    counter += 1

                                elif dropped_card.category == 'Block':
                                    if current_player == self.players[-1]:
                                        print(Fore.GREEN + "{} can sit down and take a rest. {} blocked your next move".format(self.players[0].name, current_player.name) + Style.RESET_ALL)
                                        current_player.cards.remove(dropped_card)
                                        self.card_to_match = dropped_card
                                        counter = 1
                                    else:
                                        print(Fore.GREEN + '{} can sit down and take a rest. {} blocked your next move'.format(self.players[counter + 1].name, current_player.name) + Style.RESET_ALL)
                                        current_player.cards.remove(dropped_card)
                                        self.card_to_match = dropped_card
                                        counter += 2
                                            
                                elif dropped_card.category == 'Drag_2':
                                    if current_player == self.players[-1]:
                                        print(Fore.GREEN + '{} is going to receive a beatiful gift! {} dropped a Drag 2 card, now {} have two more cards. What a good friend'.format(self.players[0].name, current_player.name, self.players[0].name) + Style.RESET_ALL)
                                        current_player.cards.remove(dropped_card)
                                        self.assign_player_cards(self.players[0], 2)
                                        self.card_to_match = dropped_card
                                        counter += 1
                                    else:
                                        print(Fore.GREEN + '{} is going to receive a beatiful gift! {} dropped a Drag 2 card, now {} have two more cards. What a good friend'.format(self.players[counter + 1].name, current_player.name, self.players[counter + 1].name) + Style.RESET_ALL)
                                        current_player.cards.remove(dropped_card)
                                        self.assign_player_cards(self.players[counter + 1], 2)
                                        self.card_to_match = dropped_card
                                        counter += 1

                                elif dropped_card.category == 'Reverse':
                                    print(Fore.GREEN + '{} dropped a reverse card. The order of the game is going to change.'.format(current_player.name) + Style.RESET_ALL)
                                    i = self.players_number - 1
                                    new_order = []
                                    while i > -1:
                                        new_order.append(self.players[i])
                                        i -= 1
                                    self.players = new_order
                                    current_player.cards.remove(dropped_card)
                                    self.card_to_match = dropped_card
                                    counter += 1

                            else:                              
                                if dropped_card.category == 'Normal':
                                    if dropped_card.character == self.card_to_match.character:
                                        print( Fore.GREEN +'{} dropped: {}'.format(current_player.name, dropped_card.show_card()))
                                        current_player.cards.remove(dropped_card)
                                        self.card_to_match = dropped_card
                                        counter += 1
                                    else:
                                        print(Fore.RED + "This cards dosen't match. Try again" + Style.RESET_ALL)
                               
                                elif dropped_card.color == 'Black':
                                    if dropped_card.category == 'Drag_4':
                
                                        if current_player == self.players[-1]:
                                            print(Fore.GREEN + "The world is shaking because of {}'s evil. This player dropped a Drag 4 card, {} must receive four cards".format(current_player.name, self.players[0].name) + Style.RESET_ALL)
                                            self.assign_player_cards(self.players[0], 4)
                                            current_player.cards.remove(dropped_card)
                                            self.change_color(current_player)
                                            
                                            counter += 2        
                                        else:
                                            print(Fore.GREEN + "The world is shaking because of {}'s evil. This player dropped a Drag 4 card, {} must receive four cards".format(current_player.name, self.players[counter + 1].name) + Style.RESET_ALL)
                                            self.assign_player_cards(self.players[counter + 1], 4)
                                            current_player.cards.remove(dropped_card)
                                            self.change_color(current_player)
                                            counter += 1
                                    else:
                                        print(Fore.GREEN + '{} drop a card to change the color'.format(current_player.name) + Style.RESET_ALL)             
                                        self.change_color(current_player)
                                        current_player.cards.remove(dropped_card)
                                        counter += 1
                                else:
                                    print(Fore.RED + "This cards dosen't match. Try again" + Style.RESET_ALL)
                                                                     
                        except:
                            print(Fore.RED + "What are you trying to drop? Don't be a cheater and try again" + Style.RESET_ALL)       

                    elif action.capitalize() == 'Drag':
                        dragged_card = choice(self.deck)
                        current_player.cards.append(dragged_card)
                        self.deck.remove(dragged_card)
                        self.discarded_cards.append(dragged_card)
                        print('You took: {}'.format(dragged_card.show_card()))
                        counter += 1

                    elif action.upper() == 'UNO':
                        if len(current_player.cards) == 1:
                            current_player.UNO = True
                            print(Fore.YELLOW + "{} just have one card! UNO".format(current_player.name) + Style.RESET_ALL)
                        else:
                            print(Fore.YELLOW + "{} shouted UNO, but doesn't have one card. {} is going to receive two cards for being a clown".format(current_player.name, current_player.name) + Style.RESET_ALL)
                            self.assign_player_cards(current_player, 2)
                    else:
                        print(Fore.RED + "Select one of the avaible options" + Style.RESET_ALL)
                except:
                    print(Fore.RED + "Select one of the avaible options" + Style.RESET_ALL)

                self.verify_deck()
                self.looking_for_winner(current_player)  
                if current_player == self.winner:
                    break

    def show_points(self):
        """Show the point of all the players
        and give all the points to the winner
        """
        print(Fore.LIGHTMAGENTA_EX + """
        _____ _       _     _     
        |  ___(_)_ __ (_)___| |__  
        | |_  | | '_ \| / __| '_ \ 
        |  _| | | | | | \__ \ | | |
        |_|   |_|_| |_|_|___/_| |_|
                                    
        """ + Style.RESET_ALL )

        print(Fore.GREEN + "{} ".format(self.winner.name) + Style.RESET_ALL + "is the winner!")
        for player in self.players:
            for card in player.cards:
                if card.category == 'Normal':
                    player.points += int(card.character)
                    self.winner.points += int(card.character)
                elif card.category == 'Drag_2' or 'Block' or 'Reverse':
                    player.points += 20
                    self.winner.points += 20
                else:
                    player.points += 50
                    self.winner += 50 
            print('{}: {} points'.format(player.name, player.points))
        print("{} will receive everyone's points for being the winner".format(self.winner.name))
        print('{}: {} points'.format(self.winner.name, self.winner.points))
            

uno = UNO_Game()
