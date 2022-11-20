from deck import Deck


class Player:
    deck: Deck
    name: str

    def __init__(self, name):
        self.name = name
        self.deck = Deck()

    @property
    def points(self):
        return sum([card.primary_value for card in self.deck.cards])

    @property
    def secondary_points(self):
        return sum([card.secondary_value for card in self.deck.cards])

    def __str__(self):
        return f"""
        name: {self.name}
        points: {self.points}/{self.secondary_points}
        deck: {str(self.deck)}
        """

    def print_fake(self):
        print(f"""
        name: {self.name}
        deck: {str(self.deck.cards[0])}
        """)

    def take_card(self, deck: Deck):
        card = deck.pop()
        self.deck.append(card)

    def get_best_points(self):
        if self.points > 21:
            return self.secondary_points
        elif self.secondary_points > 21:
            return self.points
        else:
            return max([self.points, self.secondary_points])