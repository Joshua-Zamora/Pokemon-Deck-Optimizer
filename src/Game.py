import random
from Player import Player


class Game:
    def __init__(self, player_one: Player, player_two: Player):
        self.player_one = player_one
        self.player_two = player_two
        self.deck_one = player_one.get_deck()
        self.deck_two = player_two.get_deck()
        self.winner = None


    def play(self):
        player_at_play = self.determine_first_player_to_move()
        self.set_up_board()
        
        while True:
            self.take_turn(player_at_play)

            if self.win_condition_met():
                break
            else:
                self.enter_checkup_period()

            if self.win_condition_met():
                break
            else:
                player_at_play = self.player_one if player_at_play == self.player_two else self.player_two

        return self.winner


    def take_turn(self, player: Player) -> Player:
        pass


    def win_condition_met(self) -> bool:
        pass


    def move_first(self, player: Player) -> bool:
        pass


    def determine_first_player_to_move(self) -> Player:
        coin_toss = random.choice([self.player_one, self.player_two])

        take_first_turn = self.move_first(self.player_one) if coin_toss == self.player_one else self.move_first(self.player_two)

        return self.player_one if coin_toss == self.player_one and take_first_turn else self.player_two


    def set_up_board(self):
        pass


    def enter_checkup_period(self):
        pass
