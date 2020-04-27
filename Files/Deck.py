from .Cards import Card

class UNO_Deck():
    def __init__(self):
        self.characters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        self.symbols = ['#', '⊘', '⇎', '⊕', '+']
        self.categories = ['Normal', 'Block', 'Reverse', 'Change_color', 'Drag_4', 'Drag_2']
        self.colours = ['Red', 'Green', 'Yellow', 'Blue']
        self.deck = []

    def create_a_deck(self):
        """Create a deck creating cards
        with the class Cards 
        """
        black_cards_qty = 4
        colored_cards_qty = 2
        for category in self.categories:
            for i in range(black_cards_qty):
                if category == 'Change_color':
                    change_color_card = Card(' ', '©', 'Black', category)
                    self.deck.append(change_color_card)
                elif category == 'Drag_4':
                    drag_4_card = Card('4', '+', 'Black', category)
                    self.deck.append(drag_4_card)
            for color in self.colours:
                for i in range(colored_cards_qty):
                    if category == 'Normal':
                        for character in self.characters:
                            normal_card = Card(character, '#', color, category)
                            self.deck.append(normal_card)
                    elif category == 'Block':
                        block_card = Card(' ', 'Ø', color, category)
                        self.deck.append(block_card)
                    elif category == 'Reverse':
                        reverse_card = Card(' ', '«-»', color, category)
                        self.deck.append(reverse_card)
                    elif category == 'Drag_2':
                        drag_2_card = Card('2', '+', color, category)
                        self.deck.append(drag_2_card)
        return self.deck
