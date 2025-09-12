import random
from Player import Player
from src.Card import Card


class Game:
    winner: Player | None = None
    sudden_death: bool = False


    def __init__(self, player_one: Player, player_two: Player):
        self.player_one = player_one
        self.player_two = player_two
        self.player_one.opponent = self.player_two
        self.player_two.opponent = self.player_one


    def play(self):
        """Houses the main gameplay logic."""
        player_at_play = self.determine_first_player_to_move()
        self.set_up_board()
        
        while True:
            self.take_turn(player_at_play, player_at_play.opponent)

            if self.win_condition_met():
                break
            elif self.sudden_death:
                break
            else:
                self.enter_checkup_period()

            if self.win_condition_met():
                break
            elif self.sudden_death:
                break
            else:
                player_at_play = self.player_one if player_at_play == self.player_two else self.player_two

        if self.sudden_death:
            self.reset_game_state()
            return self.play()
        else:
            return self.winner


    def reset_game_state(self):
        """Resets the game state for a new game."""
        self.player_one.reset_player_state()
        self.player_two.reset_player_state()


    def take_turn(self, player: Player, opponent: Player):
        # Draw card
        player.draw_card()

        """ To do:
            A. Put Basic Pokémon cards from your hand onto your Bench (as many as you want).
            B. Evolve your Pokémon (as many as you want).
            C. Attach an Energy card from your hand to one of your Pokémon (once per turn).
            D. Play Trainer cards (as many as you want, but only one Supporter card and one Stadium card per turn).
            E. Retreat your Active Pokémon (only once per turn).
            F. Use Abilities (as many as you want).
        """

        # Attack
        player.attack(player.opponent)


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
            self.sudden_death = True

        return self.winner is not None


    def move_first(self, player: Player) -> bool:
        pass


    def determine_first_player_to_move(self) -> Player:
        coin_toss = random.choice([self.player_one, self.player_two])

        take_first_turn = self.move_first(self.player_one) if coin_toss == self.player_one else self.move_first(self.player_two)

        return self.player_one if coin_toss == self.player_one and take_first_turn else self.player_two


    def set_up_board(self):
        """Initializes the board for play."""
        # Shuffle each deck
        random.shuffle(self.player_one.deck)
        random.shuffle(self.player_two.deck)

        # Draw the top seven cards from each deck
        for i in range (7):
            self.player_one.draw_card()
            self.player_two.draw_card()

        # To do: Check to see if you have any Basic Pokémon in your hand

        # To do: Put one of your Basic Pokémon face down as your Active Pokémon

        # To do: Put up to 5 more Basic Pokémon face down on your Bench

        # Set prize cards for each player
        if self.sudden_death:
            self.player_one.prepare_for_sudden_death()
            self.player_two.prepare_for_sudden_death()
            self.sudden_death = False
        else:
            self.player_one.set_prize_cards()
            self.player_two.set_prize_cards()

        # To do: Both players flip their Active and Benched Pokémon face up and start the game!


    def enter_checkup_period(self):
        pass
