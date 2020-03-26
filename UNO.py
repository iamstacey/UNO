from UNO_Deck import Deck
from UNO_Player import Player
from random import random, choice, shuffle

deck = Deck()
uno_deck = deck.create_a_deck()

class Game():
    def __init__(self):
        self.players_number = 0
        self.players = []
        self.winner = None

    #The first function of the game print the three avaible options of how many players can play uno
    def ask_players_number(self):
        print("Select the mode of the game".center(110, '='))
        print("A) Two players".center(100, ' '))
        print('B) Three players'.center(100, ' '))
        print('C) Four players'.center(100, ' '))

        #The users can write the letter correspondant to the option with the number of players they want to play
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
            #Then the program is going to ask the name of the players
            # and is going to save them at the array in self.players         
            for i in range(1, self.players_number + 1):
                player = Player(i)
                self.players.append(player)
        return self.players_number

    def assign_player_cards(self):
        #Here the program give the first seven random cards to every player in the game
        for player in self.players:
            count = 0
            while count < 7:
                card = choice(uno_deck)
                player.cards.append(card)
                uno_deck.remove(card)
                count += 1
        return self.players

    def looking_for_winner(self, participant):
        if len(participant.cards) == 0:
            self.winner = participant
        else:
            self.winner = None
    
        return self.winner
    def player_system(self):

        #The uno game is basically match your card with the current card on the table
        #to 
        card_to_match = choice(uno_deck)
        uno_deck.remove(card_to_match) 
        #This function only stops when the program find a winner
        while self.winner == None:

            if self.winner != None:
                break
            else:
                #Initialize a counter to assigns who is the current player playing
                #depending on their position at the array in self.players
                counter = 0
                while counter < self.players_number:
                    current_player = self.players[counter]
                    #Show who is playing
                    print("It's {} turn".format(current_player.name))
                    #Show the current player cards
                    current_player.show_all_cards()
                    #Print what is the current card the players need to match their cards with
                    print('Card to match:' + card_to_match.show_card())
                    

                    try:
                        #Ask the players if they want to drop a card or drag a card from the deck
                        action = input('Drop, drag or UNO: ')

                        if action.capitalize() == 'Drop':
                            #If the players selection is to drop a card, the program is going to ask the number of
                            #the card that they want to drop, the number is going to be show at the left of the card
                            try:
                                card_number = int(input('Write the number of the card to drop: '))
                                #From the cards of the player, the card dropped is going to be the card correspondent
                                #to the number that the player wrote
                                dropped_card = current_player.cards[card_number]
                                #The program is going to revise if the color of the dropped card match with the color of the 
                                #current card to match
                                if dropped_card.color == card_to_match.color:
                                    #Then is going to revise if the dropped card is normal
                                    if dropped_card.category == 'Normal':
                                        #If this is true, the card is going to be dropped. The program
                                        #is going to show who dropped the card and the card that was dropped
                                        print('{} dropped: {}'.format(current_player.name, dropped_card.show_card()))
                                        #Now the new card to match is the card that the player dropped
                                        card_to_match = dropped_card
                                        #Delete the droperd from the player cards
                                        current_player.cards.remove(dropped_card)
                                        self.looking_for_winner(current_player)
                                        if self.winner == current_player:
                                            break
                                        else:
                                            counter += 1
                                    #If the card dropped is not normal, the program is going to revise the other posibilities of cards
                                    #that can be dropped when the colors match
                                    #So, if the dropped card is a block card
                                    elif dropped_card.category == 'Block':
                                        #Revise if the number of the current number is equal to the number of players in the game
                                        #In other words revise if the current player is the last player of the round
                                        if current_player == self.players[-1]:
                                            #If this is true, the first player on the next round is going to be blocked
                                            print('{} blocked {} next move'.format(current_player.name, self.players[0].name))
                                            #Now the new card to match is the dropped card
                                            card_to_match = dropped_card
                                            #Delete the droperd from the player cards
                                            current_player.cards.remove(dropped_card)
                                            #The counter now is one, because the first player (when the counter is zero) move was blocked
                                            #Therefore, the next player to play is the second one
                                            self.looking_for_winner(current_player)
                                            if self.winner == current_player:
                                                break
                                            else:
                                                counter = 1
                                        else:
                                            #This happen whenever the current player is not the last one
                                            #This print: The current player blocked the next player next move
                                            print('{} blocked {} next move'.format(current_player.name, self.players[counter + 1].name))
                                            #The new card to match is the card that the current player dropped
                                            card_to_match = dropped_card
                                            #Delete the droperd from the player cards
                                            current_player.cards.remove(dropped_card)
                                            self.looking_for_winner(current_player)
                                            if self.winner == current_player:
                                               break
                                            else:
                                                counter += 2
                                    #If the card dropped is a drag 2 card        
                                    elif dropped_card.category == 'Drag_2':
                                        #Revise if the current player is the last player in the round
                                        if current_player == self.players[-1]:
                                            #Print a message announcing that the current player dropped a drag 2 card
                                            #and the next player is going to receive two cards
                                            print('{} drop a Drag 2 card, {} must receive two cards'.format(current_player.name, self.players[0].name))
                                            #Take two cards from the deck
                                            first_card = choice(uno_deck)
                                            second_card = choice(uno_deck)
                                            #Give the card to the next player, that is the first one in the next round
                                            self.players[0].cards.append(first_card)
                                            self.players[0].cards.append(second_card)
                                            #The new card to match is the card that the current player dropped
                                            card_to_match = dropped_card
                                            #Delete the droperd from the player cards
                                            current_player.cards.remove(dropped_card)
                                            #Delete the cards from the deck
                                            uno_deck.remove(first_card)
                                            uno_deck.remove(second_card)
                                            self.looking_for_winner(current_player)
                                            if self.winner == current_player:
                                               break
                                            else:
                                                counter += 1
                                        else:
                                            #Print the message announcing that the current player dropped a drag two
                                            print('{} drop a Drag 2 card, {} must receive two cards'.format(current_player.name, self.players[counter + 1].name))
                                            #Take thow cards from the deck
                                            first_card = choice(uno_deck)
                                            second_card = choice(uno_deck)
                                            #Give the cards to the next player
                                            self.players[counter + 1].cards.append(first_card)
                                            self.players[counter + 1].cards.append(second_card)
                                            #Delete the cards from the deck
                                            uno_deck.remove(first_card)
                                            uno_deck.remove(second_card)
                                            #The new card to match is the card that the current player dropped
                                            card_to_match = dropped_card
                                            #Delete the droperd from the player cards
                                            current_player.cards.remove(dropped_card)
                                            #The counter will increase by one to let the next player play
                                            self.looking_for_winner(current_player)
                                            if self.winner == current_player:
                                               break
                                            else:
                                                counter += 1
                                
                                    else:
                                        print('{} dropped a reverse card. The order of the game is going to change.'.format(current_player.name))
                                        i = self.players_number - 1
                                        new_order = []
                                        while i > -1:
                                            new_order.append(self.players[i])
                                            i -= 1
                                        self.players = new_order
                                        card_to_match = dropped_card
                                        current_player.cards.remove(dropped_card)

                                        self.looking_for_winner(current_player)
                                        if self.winner == current_player:
                                            break
                                        else:
                                            counter += 1


                                else:
                                    #If the colors are not the same, check the category of the card
                                    if dropped_card.category == 'Normal':
                                        if dropped_card.character == card_to_match.character:
                                            print('{} dropped: {}'.format(current_player.name, dropped_card.show_card()))
                                            card_to_match = dropped_card
                                            #Delete the dropped from the player cards
                                            current_player.cards.remove(dropped_card)
                                            self.looking_for_winner(current_player)
                                            if self.winner == current_player:
                                               break
                                            else:
                                                counter += 1
                                
                                    elif dropped_card.color == 'Black':
                                        if dropped_card.category == 'Drag_4':
                                            #Revise if the current player is the last player in the round
                                            if current_player == self.players[-1]:
                                                #Print a message announcing that the current player dropped a drag 2 card
                                                #and the next player is going to receive four cards
                                                print('{} drop a Drag 4 card, {} must receive four cards'.format(current_player.name, self.players[0].name))
                                                #Give the card to the next player, that is the first one in the next round
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
                                                        card_to_match = dropped_card       
                                                        card_to_match.color = new_color.capitalize()
                                                        current_player.cards.remove(dropped_card)
                                                        print('{} changed the color to {}'.format(current_player.name, card_to_match.color))
                                                        self.looking_for_winner(current_player)
                                                        if self.winner == current_player:
                                                            break
                                                        else:
                                                            counter += 2
                                                except:
                                                    print('The color that you are trying to put is unavaible')
                                            else:
                                                #Print the message announcing that the current player dropped a drag two
                                                print('{} drop a Drag 4 card, {} must receive two cards'.format(current_player.name, self.players[counter + 1].name))
                                                #Take thow cards from the deck
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
                                                        card_to_match = dropped_card       
                                                        card_to_match.color = new_color.capitalize()
                                                        print('{} changed the color to {}'.format(current_player.name, card_to_match.color))
                                                        self.looking_for_winner(current_player)
                                                        if self.winner == current_player:
                                                            break
                                                        else:
                                                            counter += 1
                                                except:
                                                    print('The color that you are trying to put is unavaible')
                                                #The counter will increase by one to let the next player play
                                                
                                        else:
                                            #Print the message announcing that the current player dropped a drag two
                                            print('{} drop a card to change the color'.format(current_player.name))
                                        
                                            try:
                                                new_color = input('Write the new color: ')
                                                if new_color.capitalize() not in deck.colours:
                                                    print("The color that you are trying to put is unavaible")
                                                else:
                                                    card_to_match = dropped_card
                                                    current_player.cards.remove(dropped_card)
                                                    card_to_match.color = new_color.capitalize()
                                                    print('{} changed the color to {}'.format(current_player.name, card_to_match.color))
                                                    #The counter will increase by one to let the next player play
                                                    self.looking_for_winner(current_player)
                                                    if self.winner == current_player:
                                                        break
                                                    else:
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
                                print("{} just have one card! UNO".format(current_player.name))
                            else:
                                print("{} shouted UNO, but doesn't have one card. {} is going to receive two cards for being a clown".format(current_player.name, current_player.name))
                                first_card = choice(uno_deck)
                                second_card = choice(uno_deck)
                                current_player.cards.append(first_card)
                                current_player.cards.append(second_card)

                        else:
                            print('Select one of the avaible options')
                    except:
                        print("Select one of the avaible options")

                    
         
           
                    
                    






uno = Game()
uno.ask_players_number()
uno.assign_player_cards()
uno.player_system()

