class Card:
    card_type: str
    value: int
    name: str

    def __init__(self, card_number, card_type):
        card_dict = {
            11: ("J", 10),
            12: ("Q", 10),
            13: ("K", 10),
            1: ("A", (1, 11)),
        }
        if card_number not in card_dict.keys():
            self.card_type = card_type
            self.value = card_number
            self.name = str(card_number)
        else:
            self.card_type = card_type
            data = card_dict[card_number]
            self.name = data[0]
            self.value = data[1]

    @property
    def primary_value(self):
        return 1 if self.name == "A" else self.value

    @property
    def secondary_value(self):
        return 11 if self.name == "A" else self.value

    def __str__(self):
        return f"{self.name}-{self.card_type}"
