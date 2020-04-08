
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

    #this function assign the player's first cards
    def assign_player_cards(self):
        for player in self.players:
            count = 0
            while count < 7:
                card = choice(uno_deck)
                player.cards.append(card)
                uno_deck.remove(card)
                count += 1
        return self.players
    #this function revise if the player doesn't have any card
    #if that is true, the player is the winner
    def looking_for_winner(self, participant):
        if len(participant.cards) == 0:
            self.winner = participant
        else:
            self.winner = None
    
        return self.winner
    #this function makes 
    def first_card_to_match(self):
        while self.card_to_match.category != 'Normal':
            self.card_to_match = choice(uno_deck)
        

    def player_system(self):
        
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
                    if len(current_player.cards) == 1:
                        print(Fore.RED + "Oh, i see a distracted player with just one card. You are going to receive two more cards so you don't need to worry about shouting UNO" + Style.RESET_ALL)
                        first_card = choice(uno_deck)
                        second_card = choice(uno_deck)
                        current_player.cards.append(first_card)
                        current_player.cards.append(second_card)
                    
                    action = input('Drop, drag or UNO: ')

                    if action.capitalize() == 'Drop':
                        try:
                            card_number = int(input('Write the number of the card to drop: '))
                            dropped_card = current_player.cards[card_number]
                            if dropped_card.color == self.card_to_match.color:

                                if dropped_card.category == 'Normal':
                                    print('{} dropped: {}'.format(current_player.name, dropped_card.show_card()))
                                    self.card_to_match = dropped_card
                                    current_player.cards.remove(dropped_card)
                                    self.looking_for_winner(current_player)
                                    counter += 1
                                elif dropped_card.category == 'Block':
                                    if current_player == self.players[-1]:

                                        print("{} can sit down and take a rest. {} blocked your next move".format(self.players[0].name, current_player.name))
                                        self.card_to_match = dropped_card
                                        current_player.cards.remove(dropped_card)

                                        self.looking_for_winner(current_player)
                                        counter = 1
                                    else:
                                        print('{} can sit down and take a rest. {} blocked your next move'.format(self.players[counter + 1].name, current_player.name))
                                        self.card_to_match = dropped_card
                                        current_player.cards.remove(dropped_card)
                                        self.looking_for_winner(current_player)
                                        counter += 2
                                        
                                elif dropped_card.category == 'Drag_2':
                                    if current_player == self.players[-1]:
                                        print('{} is going to receive a beatiful gift! {} dropped a Drag 2 card, now {} have two more cards. What a good friend'.format(self.players[0].name, current_player.name, self.players[0].name))
                                        first_card = choice(uno_deck)
                                        second_card = choice(uno_deck)
                                        
                                        self.players[0].cards.append(first_card)
                                        self.players[0].cards.append(second_card)
                                        
                                        self.card_to_match = dropped_card
                                        
                                        current_player.cards.remove(dropped_card)
                                        
                                        uno_deck.remove(first_card)
                                        uno_deck.remove(second_card)
                                        self.looking_for_winner(current_player)
                                        counter += 1
                                    else:
                                        
                                        print('{} is going to receive a beatiful gift! {} dropped a Drag 2 card, now {} have two more cards. What a good friend'.format(self.players[counter + 1].name, current_player.name, self.players[counter + 1].name))
                                        
                                        first_card = choice(uno_deck)
                                        second_card = choice(uno_deck)
                                        
                                        self.players[counter + 1].cards.append(first_card)
                                        self.players[counter + 1].cards.append(second_card)
                                        
                                        uno_deck.remove(first_card)
                                        uno_deck.remove(second_card)

                                        self.card_to_match = dropped_card
                                        
                                        current_player.cards.remove(dropped_card)
                                        
                                        self.looking_for_winner(current_player)
                                        counter += 1
                            
                                else:
                                    print('{} dropped a reverse card. The order of the game is going to change.'.format(current_player.name))
                                    i = self.players_number - 1
                                    new_order = []
                                    while i > -1:
                                        new_order.append(self.players[i])
                                        i -= 1
                                    self.players = new_order
                                    self.card_to_match = dropped_card
                                    current_player.cards.remove(dropped_card)

                                    self.looking_for_winner(current_player)
                                    counter += 1


                            else:
                                
                                if dropped_card.category == 'Normal':
                                    if dropped_card.character == self.card_to_match.character:
                                        print('{} dropped: {}'.format(current_player.name, dropped_card.show_card()))
                                        self.card_to_match = dropped_card
                                        current_player.cards.remove(dropped_card)
                                        self.looking_for_winner(current_player)
                                        counter += 1
                            
                                elif dropped_card.color == 'Black':
                                    if dropped_card.category == 'Drag_4':
                
                                        if current_player == self.players[-1]:
                                            print("The world is shaking because of {}'s evil. This player dropped a Drag 4 card, {} must receive four cards".format(current_player.name, self.players[0].name))
                                            
                                            i = 0
                                            while i < 4:
                                                card = choice(uno_deck)
                                                self.players[0].cards.append(card)
                                                uno_deck.remove(card)
                                                i += 1

                                            try:
                                                new_color = input('Write the new color: ')
                                                if new_color.capitalize() not in deck.colours:
                                                    print('The color that you are trying to put is unavaible')          
                                                else:
                                                    self.card_to_match = Card(" ", " ", " ", 'Colour')       
                                                    self.card_to_match.color = new_color.capitalize()
                                                    current_player.cards.remove(dropped_card)
                                                    print('{} changed the color to {}'.format(current_player.name, self.card_to_match.color))
                                                    self.looking_for_winner(current_player)
                                                    counter += 2
                                            except:
                                                print('The color that you are trying to put is unavaible')
                                        else:
                                            print("The world is shaking because of {}'s evil. This player dropped a Drag 4 card, {} must receive four cards".format(current_player.name, self.players[counter + 1].name))
                                            
                                            i = 0
                                            while i < 4:
                                                card = choice(uno_deck)
                                                self.players[counter + 1].cards.append(card)
                                                uno_deck.remove(card)
                                                i += 1

                                            current_player.cards.remove(dropped_card)
                                            try:
                                                new_color = input('Write the new color: ')
                                                if new_color.capitalize() not in deck.colours:
                                                    print('The color that you are trying to put is unavaible')          
                                                else:
                                                    self.card_to_match = Card(" ", " ", " ", 'Colour')       
                                                    self.card_to_match.color = new_color.capitalize()
                                                    print('{} changed the color to {}'.format(current_player.name, self.card_to_match.color))
                                                    self.looking_for_winner(current_player)
                                                    counter += 1
                                            except:
                                                print('The color that you are trying to put is unavaible')
                                            
                                            
                                    else:
                                        print('{} drop a card to change the color'.format(current_player.name))
                                    
                                        try:
                                            new_color = input('Write the new color: ')
                                            if new_color.capitalize() not in deck.colours:
                                                print("The color that you are trying to put is unavaible")
                                            else:
                                                self.card_to_match = Card(" ", " ", " ", 'Colour')
                                                current_player.cards.remove(dropped_card)
                                                self.card_to_match.color = new_color.capitalize()
                                                print('{} changed the color to {}'.format(current_player.name, self.card_to_match.color))
                                                
                                                self.looking_for_winner(current_player)
                                                counter += 1
                                        except:
                                            print("The color that you are trying to put is unavaible")                
                        except:
                            print("What are you trying to drop? Don't be a cheater and try again")    

                    elif action.capitalize() == 'Drag':
                        dragged_card = choice(uno_deck)
                        current_player.cards.append(dragged_card)
                        print('You took: {}'.format(dragged_card.show_card()))
                        counter += 1
                    elif action.upper() == 'UNO':
                        if len(current_player.cards) == 1:
                            print(Fore.GREEN + "{} just have one card! UNO".format(current_player.name) + Style.RESET_ALL)
                        else:
                            print("{} shouted UNO, but doesn't have one card. {} is going to receive two cards for being a clown".format(current_player.name, current_player.name))
                            first_card = choice(uno_deck)
                            second_card = choice(uno_deck)
                            current_player.cards.append(first_card)
                            current_player.cards.append(second_card)
                except:
                    print("Select one of the avaible options")
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
uno.assign_player_cards()
uno.first_card_to_match()
uno.player_system()
uno.show_points()

