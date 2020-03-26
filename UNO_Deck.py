from UNO_Cards import Card

class Deck():
    def __init__(self):
        self.characters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        self.symbols = ['#', '⊘', '⇎', '⊕', '+']
        self.categories = ['Normal', 'Block', 'Reverse', 'Change_color', 'Drag_4', 'Drag_2']
        self.colours = ['Red', 'Green', 'Yellow', 'Blue']
        self.deck = []

    def create_a_deck(self):
        for category in self.categories:
            if category == 'Change_color':
                i = 0
                while i < 4:
                    change_color_card = Card(' ', '⊕', 'Black', category)
                    self.deck.append(change_color_card)
                    i += 1
            if category == 'Drag_4':
                i = 0
                while i < 4:
                    drag_4_card = Card('4', '+', 'Black', category)
                    self.deck.append(drag_4_card)
                    i += 1
            for color in self.colours:
                if category == 'Normal':
                    for character in self.characters:
                        normal_card = Card(character, '#', color, category)
                        self.deck.append(normal_card)
                        self.deck.append(normal_card)
                if category == 'Block':
                    block_card = Card(' ', '⊘', color, category)
                    self.deck.append(block_card)
                    self.deck.append(block_card)
                if category == 'Reverse':
                    reverse_card = Card(' ', '⇎', color, category)
                    self.deck.append(reverse_card)
                    self.deck.append(reverse_card)
                if category == 'Drag_2':
                    drag_2_card = Card('2', '+', color, category)
                    self.deck.append(drag_2_card)
                    self.deck.append(drag_2_card)
        return self.deck

