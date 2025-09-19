import random
from src.core.card import Card


class Player:
    prize_cards: list[Card] = []
    hand: list[Card] = []
    bench: list[Card] = []
    active_spot: Card | None = None
    discard_pile: list[Card] = []
    opponent = None

    def __init__(self, name, deck):
        self.name = name
        self.deck = deck
        self.__original_deck = deck[:]

    def set_up(self, sudden_death: bool = False):
        while True:
            random.shuffle(self.deck)
            self.draw_card(7)

            if self.has_basic_pokemon():
                break
            else:
                self.reset_player_state()
                self.opponent.draw_card(1)

        # To do: Put one of your Basic Pokémon face down as your Active Pokémon
        self.place_pokemon()

        # To do: Put up to 5 more Basic Pokémon face down on your Bench
        self.place_pokemon()

        # Set prize cards
        self.set_prize_cards(1) if sudden_death else self.set_prize_cards(6)

        # To do: Both players flip their Active and Benched Pokémon face up and start the game!

    def reset_player_state(self):
        self.prize_cards = []
        self.hand = []
        self.bench = []
        self.active_spot = None
        self.discard_pile = []
        self.deck = self.__original_deck[:]

    def draw_card(self, num_cards: int = 1):
        for i in range(num_cards):
            self.hand.append(self.deck.pop(0))

    def attack(self, opponent):
        pass

    def set_prize_cards(self, num_cards: int = 6):
        self.prize_cards = []

        for i in range(num_cards):
            self.prize_cards.append(self.deck.pop(0))

    def will_move_first(self) -> bool:
        pass

    def take_turn(self):
        # Draw card
        self.draw_card()

        """ To do:
            A. Put Basic Pokémon cards from your hand onto your Bench (as many as you want).
            B. Evolve your Pokémon (as many as you want).
            C. Attach an Energy card from your hand to one of your Pokémon (once per turn).
            D. Play Trainer cards (as many as you want, but only one Supporter card and one Stadium card per turn).
            E. Retreat your Active Pokémon (only once per turn).
            F. Use Abilities (as many as you want).
        """

        # Attack
        self.attack(self.opponent)

    def has_basic_pokemon(self) -> bool:
        pass

    def place_pokemon(self):
        pass

    def evolve_pokemon(self):
        pass

    def attach_energy(self):
        pass

    def play_pokemon_tool(self):
        pass

    def play_item(self):
        pass

    def play_supporter_card(self):
        pass

    def play_stadium_card(self):
        pass

    def retreat(self):
        pass

    def use_ability(self):
        pass
