import random

from cards.trainer_card import TrainerCard
from player import Player


class Game:
    winner: Player | None = None
    enter_sudden_death: bool = False
    in_pokemon_checkup: bool = False
    all_abilities: dict = {}
    all_attacks: dict = {}
    stadium_in_play: TrainerCard = None

    def __init__(self, player_one: Player, player_two: Player):
        self.player_one = player_one
        self.player_two = player_two
        self.player_one.opponent = self.player_two
        self.player_two.opponent = self.player_one

    def determine_first_player_to_move(self) -> Player:
        coin_toss = random.choice([self.player_one, self.player_two])

        if coin_toss == self.player_one:
            return self.player_one if self.player_one.will_move_first() else self.player_two
        else:
            return self.player_two if self.player_two.will_move_first() else self.player_one

    def set_up_board(self):
        """Initializes the board for play."""
        self.player_one.set_up(self.enter_sudden_death)
        self.player_two.set_up(self.enter_sudden_death)
        self.enter_sudden_death = False

    def win_condition_met(self) -> bool:
        """Checks if the game should end or enter sudden death."""
        ways_won_player_one = 0
        ways_won_player_two = 0

        if len(self.player_one.prize_cards) == 0:
            ways_won_player_one += 1

        if len(self.player_two.bench) == 0 and self.player_two.active_spot is None:
            ways_won_player_one += 1

        if len(self.player_two.deck) == 0:
            ways_won_player_one += 1

        if len(self.player_two.prize_cards) == 0:
            ways_won_player_two += 1

        if len(self.player_one.bench) == 0 and self.player_one.active_spot is None:
            ways_won_player_two += 1

        if len(self.player_one.deck) == 0:
            ways_won_player_two += 1

        if ways_won_player_one > ways_won_player_two:
            self.winner = self.player_one
        elif ways_won_player_two > ways_won_player_one:
            self.winner = self.player_two
        elif ways_won_player_one == ways_won_player_two:
            self.enter_sudden_death = True

        return self.winner is not None

    def enter_checkup_period(self):
        pass

    def reset_game_state(self):
        """Resets the game state for a new game."""
        self.player_one.reset_player_state()
        self.player_two.reset_player_state()

    def play(self):
        """Houses the main gameplay logic."""
        player_at_play = self.determine_first_player_to_move()
        self.set_up_board()

        while True:
            player_at_play.take_turn()

            if self.win_condition_met():
                break
            elif self.enter_sudden_death:
                break
            else:
                self.enter_checkup_period()

            if self.win_condition_met():
                break
            elif self.enter_sudden_death:
                break
            else:
                player_at_play = self.player_one if player_at_play == self.player_two else self.player_two

        if self.enter_sudden_death:
            self.reset_game_state()
            return self.play()
        else:
            return self.winner
