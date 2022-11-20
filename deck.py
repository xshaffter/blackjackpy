import random
from typing import List

from card import Card


class Deck:
    cards: List[Card]

    def __init__(self, cards=None):
        if not cards:
            self.cards = []
        else:
            self.cards = [Card(*card_data) for card_data in cards]

    def append(self, card: Card):
        self.cards.append(card)

    def pop(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)

    def __str__(self):
        result = ",".join([str(card) for card in self.cards])
        return result
