class Player():
    def __init__(self, number):
        self.number = number
        self.name = input("Player {}: ".format(self.number))
        self.cards = []
        self.points = 0
    def show_all_cards(self):
        for i in range(0, len(self.cards)):
            print('{}: '.format(i) + self.cards[i].show_card())
        return self.cards