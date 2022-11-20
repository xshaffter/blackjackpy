import time
from enum import Enum, auto

from deck import Deck
from deck_builder import DeckBuilder
from player import Player


class TurnType(Enum):
    WIN = auto()
    LOSE = auto()
    PASSED = auto()


class Game:
    deck: Deck
    player: Player
    computer: Player

    def __init__(self):
        self.deck = DeckBuilder.build_main_deck()
        self.player = Player("You")
        self.computer = Player("Computer")
        self.deck.shuffle()

    def start(self):
        self.computer.take_card(self.deck)
        self.player.take_card(self.deck)
        self.computer.take_card(self.deck)
        self.player.take_card(self.deck)
        self.computer.print_fake()

        pre_win = self.validate_player_win(self.player)
        if pre_win:
            print(f"{self.player.name} won! :D")
            result = TurnType.WIN
        else:
            result = self.do_player_turn(self.player)
        if result == TurnType.PASSED:
            pre_win = self.validate_player_win(self.computer)
            if pre_win:
                print(f"{self.computer.name} won! :D")
                computer_result = TurnType.WIN
            else:
                computer_result = self.do_player_turn(self.computer)

            if computer_result == TurnType.PASSED:
                print(f"{self.computer.name} won! :D")


    def do_player_turn(self, player) -> TurnType:
        print(player)
        while True:
            if player.name != "Computer":
                inpu = self.ask_input()
            else:
                inpu = self.computer_input()
                time.sleep(1)

            if inpu.upper() == 'Y':
                card = self.deck.pop()
                player.deck.append(card)
            else:
                return TurnType.PASSED

            print(player)

            if player.points > 21 and player.secondary_points > 21:
                print("You lose :(")
                return TurnType.LOSE
            elif self.validate_player_win(player):
                print(f"{player.name} won! :D")
                return TurnType.WIN

    # noinspection PyMethodMayBeStatic
    def ask_input(self) -> str:
        while True:
            inpu = input("¿quieres otra carta? (Y/N)")  # andalu' para "input", pero es una palabra reservada, srry

            if inpu.upper() in ("Y", "N"):  # Lo mismo que if inpu == "Y" || inpu == "N"
                break
        return inpu

    def computer_input(self) -> str:
        this_player = self.computer
        if this_player.get_best_points() > self.player.get_best_points():
            return "N"

        return "Y"

    def validate_player_win(self, player) -> bool:
        return 21 in (player.points, player.secondary_points)
