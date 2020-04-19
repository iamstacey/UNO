from colorama import Fore, Back, Style, init
init()
class Card:
    def __init__(self, character, symbol, color, category):
        self.character = character
        self.symbol = symbol
        self.color = color
        self.category = category
    def __str__(self):
        return " {}{} ".format(self.character, self.symbol)
    def show_card(self):
        """Show the card with the 
        corresponding color
        """
        if self.color == 'Red':
            return  Fore.BLACK + Back.RED + self.__str__() + Style.RESET_ALL
        elif self.color == 'Green':
            return Fore.BLACK + Back.GREEN + self.__str__() + Style.RESET_ALL
        elif self.color == 'Yellow':
            return Fore.BLACK + Back.YELLOW + self.__str__() + Style.RESET_ALL
        elif self.color == 'Blue':
            return Fore.BLACK + Back.BLUE + self.__str__() + Style.RESET_ALL
        else:
            return self.__str__()
    

