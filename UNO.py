
from UNO_Deck import Deck
from UNO_Player import Player
from random import random, choice
from colorama import Fore, Style, init
from UNO_Cards import Card
init()

deck = Deck()
uno_deck = deck.create_a_deck()

class Game():
    def __init__(self):
        self.players_number = 0
        self.players = []
        self.winner = None
        self.card_to_match = choice(uno_deck)

    #The first function of the game print the three avaible options of how many players can play uno
    def ask_players_number(self):
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
                else:
                    if election.upper() == 'B':
                        self.players_number = 3
                    else:
                        if election.upper() == 'C':
                            self.players_number = 4
                        else:
                            print('Oh, it looks like you are trying to select an unplayable number of players. Try again with one of the options.')
            except:
                print('Oh, it looks like you are trying to select an unplayable number of players. Try again with one of the options.')               
              
            for i in range(1, self.players_number + 1):
                player = Player(i)
                self.players.append(player)
        return self.players_number

    #this function give cards to the players deppending of the number of the input
    def assign_player_cards(self, player, number_of_cards):
        count = 0
        while count < number_of_cards:
            card = choice(uno_deck)
            player.cards.append(card)
            count += 1
        return player.cards
    #this function revise if the player doesn't have any card
    #if that is true, the player is the winner
    def looking_for_winner(self, participant):
        if len(participant.cards) == 0:
            self.winner = participant
        else:
            self.winner = None
    
        return self.winner
    
    #this function give the first 7 cards to all the players
    def first_cards(self):
        for player in self.players:
            self.assign_player_cards(player, 7)
    #this function makes 
    def first_card_to_match(self):
        while self.card_to_match.category != 'Normal':
            self.card_to_match = choice(uno_deck)
    
    def change_color(self, player):
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
        if len(player.cards) == 1:
            if player.UNO == True:
                print(Fore.GREEN + "You are doing well, you are about to win. Unless somebody decide to drop a 4..." + Style.RESET_ALL)
            else:
                print(Fore.RED + "You didn't shout UNO and you have one card. You are going to receive two cards so you won't worry about shouting UNO." + Style.RESET_ALL)
                self.assign_player_cards(player, 2)

    def player_system(self):
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
                                    self.card_to_match = dropped_card
                                    current_player.cards.remove(dropped_card)
                                    counter += 1

                                elif dropped_card.category == 'Block':
                                    if current_player == self.players[-1]:
                                        print(Fore.GREEN + "{} can sit down and take a rest. {} blocked your next move".format(self.players[0].name, current_player.name) + Style.RESET_ALL)
                                        self.card_to_match = dropped_card
                                        current_player.cards.remove(dropped_card)
                                        counter = 1
                                    else:
                                        print(Fore.GREEN + '{} can sit down and take a rest. {} blocked your next move'.format(self.players[counter + 1].name, current_player.name) + Style.RESET_ALL)
                                        self.card_to_match = dropped_card
                                        current_player.cards.remove(dropped_card)
                                        counter += 2
                                            
                                elif dropped_card.category == 'Drag_2':
                                    if current_player == self.players[-1]:
                                        print(Fore.GREEN + '{} is going to receive a beatiful gift! {} dropped a Drag 2 card, now {} have two more cards. What a good friend'.format(self.players[0].name, current_player.name, self.players[0].name) + Style.RESET_ALL)
                                        self.card_to_match = dropped_card
                                        current_player.cards.remove(dropped_card)
                                        self.assign_player_cards(self.players[0], 2)
                                        counter += 1
                                    else:
                                        print(Fore.GREEN + '{} is going to receive a beatiful gift! {} dropped a Drag 2 card, now {} have two more cards. What a good friend'.format(self.players[counter + 1].name, current_player.name, self.players[counter + 1].name) + Style.RESET_ALL)
                                        self.card_to_match = dropped_card
                                        current_player.cards.remove(dropped_card)
                                        self.assign_player_cards(self.players[counter + 1], 2)
                                        counter += 1

                                elif dropped_card.category == 'Reverse':
                                    print(Fore.GREEN + '{} dropped a reverse card. The order of the game is going to change.'.format(current_player.name) + Style.RESET_ALL)
                                    i = self.players_number - 1
                                    new_order = []
                                    while i > -1:
                                        new_order.append(self.players[i])
                                        i -= 1
                                    self.players = new_order
                                    self.card_to_match = dropped_card
                                    current_player.cards.remove(dropped_card)
                                    counter += 1

                            else:                              
                                if dropped_card.category == 'Normal':
                                    if dropped_card.character == self.card_to_match.character:
                                        print( Fore.GREEN +'{} dropped: {}'.format(current_player.name, dropped_card.show_card()))
                                        self.card_to_match = dropped_card
                                        current_player.cards.remove(dropped_card)
                                        counter += 1
                                    else:
                                        print(Fore.RED + "This cards dosen't match. Try again" + Style.RESET_ALL)
                                elif dropped_card.color == 'Black':
                                    if dropped_card.category == 'Drag_4':
                
                                        if current_player == self.players[-1]:
                                            print(Fore.GREEN + "The world is shaking because of {}'s evil. This player dropped a Drag 4 card, {} must receive four cards".format(current_player.name, self.players[0].name) + Style.RESET_ALL)
                                            self.assign_player_cards(self.players[0], 4)
                                            self.change_color(current_player)
                                            current_player.cards.remove(dropped_card)
                                            counter += 2        
                                        else:
                                            print(Fore.GREEN + "The world is shaking because of {}'s evil. This player dropped a Drag 4 card, {} must receive four cards".format(current_player.name, self.players[counter + 1].name) + Style.RESET_ALL)
                                            self.assign_player_cards(self.players[counter + 1], 4)
                                            self.change_color(current_player)
                                        
                                            current_player.cards.remove(dropped_card)
                                            counter += 1
                                    else:
                                        print(Fore.GREEN + '{} drop a card to change the color'.format(current_player.name) + Style.RESET_ALL)
                                                            
                                        self.card_to_match = dropped_card
                                        current_player.cards.remove(dropped_card)
                                        self.change_color(current_player)
                                        counter += 1
                                else:
                                    print(Fore.RED + "This cards dosen't match. Try again" + Style.RESET_ALL)
                                                                     
                        except:
                            print(Fore.RED + "What are you trying to drop? Don't be a cheater and try again" + Style.RESET_ALL)       

                    elif action.capitalize() == 'Drag':
                        dragged_card = choice(uno_deck)
                        current_player.cards.append(dragged_card)
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
    
                self.looking_for_winner(current_player)  
                if current_player == self.winner:
                    break

    def show_points(self):
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
            


uno = Game()
uno.ask_players_number()
uno.first_card_to_match()
uno.player_system()
uno.show_points()

