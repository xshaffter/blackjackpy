from deck import Deck


class DeckBuilder:

    @staticmethod
    def build_main_deck():
        total_cards_per_deck = [i + 1 for i in range(13)]
        diamonds = DeckBuilder.build_cards_by_type(total_cards_per_deck, "♦️")
        hearts = DeckBuilder.build_cards_by_type(total_cards_per_deck, "♥️")
        picks = DeckBuilder.build_cards_by_type(total_cards_per_deck, "♣️")
        spades = DeckBuilder.build_cards_by_type(total_cards_per_deck, "♠️")

        total_cards = diamonds + hearts + picks + spades
        deck = Deck(total_cards)
        return deck

    @staticmethod
    def build_cards_by_type(total_cards_per_deck, card_type):
        return [(card_number, card_type) for card_number in total_cards_per_deck]
