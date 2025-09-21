import random
from src.core.tcg_card import Card


class Player:
    prize_cards: list[Card] = []
    hand: list[Card] = []
    bench: list[Card] = []
    active_spot: Card | None = None
    discard_pile: list[Card] = []
    opponent = None
    modifiers = {}

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

    def attack(self, opponent, attack):
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
        attack_to_use = None

        # Attack
        self.attack(self.opponent, attack_to_use)

    def has_basic_pokemon_in_hand(self) -> bool:
        pass

    def card_location(self, card: Card) -> str:
        return "hand" if card in self.hand else "bench" if card in self.bench else "discard pile"

    def place_pokemon_on_bench(self, card: Card, index: int = 0):
        self.bench.insert(index, card)

    def place_pokemon_on_active_spot(self, card: Card):
        self.active_spot = card

    def move_pokemon_from_bench_to_active_spot(self, index: int):
        self.active_spot = self.bench.pop(index)

    def choose_active_pokemon_from_bench(self, index: int):
        self.active_spot = self.bench[index]

    def swap_benched_pokemon_with_active_pokemon(self, index: int, your_pokemon: bool):
        if your_pokemon:
            self.bench[index], self.active_spot = self.active_spot, self.bench[index]
        else:
            self.opponent.bench[index], self.opponent.active_spot = self.opponent.active_spot, self.opponent.bench[index]

    def swap_deck_card_with_benched_card(self, bench_index: int, deck_index: int):
        self.bench[bench_index], self.deck[deck_index] = self.deck[deck_index], self.bench[bench_index]

    def place_cards_into_hand(self, cards: list[Card] | Card):
        self.hand.extend(cards) if type(cards) == list else self.hand.append(cards)

    def place_cards_on_deck(self, card: list[Card] | Card, on_top: bool, your_deck: bool):
        if your_deck:
            if on_top:
                self.deck = card + self.deck
            else:
                self.deck.extend(card)
        else:
            if on_top:
                self.opponent.deck = card + self.opponent.deck
            else:
                self.opponent.deck.extend(card)

    def shuffle_cards_into_deck(self, cards: list[Card], your_deck: bool, also_shuffle_deck: bool, on_top: bool = False):
        random.shuffle(cards)
        if your_deck:
            if also_shuffle_deck:
                self.deck.extend(cards)
                random.shuffle(self.deck)
            elif on_top:
                self.deck = cards + self.deck
            else:
                self.deck.extend(cards)
        else:
            if also_shuffle_deck:
                self.opponent.deck.extend(cards)
                random.shuffle(self.opponent.deck)
            elif on_top:
                self.opponent.deck = cards + self.opponent.deck
            else:
                self.opponent.deck.extend(cards)

    def evolve_pokemon(self, evolved_pokemon: Card, target_pokemon: Card):
        pass

    def devolve_one_of_opponents_pokemon(self, target: str, index: int, number_of_stages_devolved: int, into_hand: bool):
        if target == "active":
            self.opponent.active_spot.devolve(number_of_stages_devolved, into_hand)
        elif target == "bench":
            self.opponent.bench[index].devolve(number_of_stages_devolved, into_hand)

    def attach_energy(self, source: str, target: str, energy_type: str, amount: int):
        pass

    def attach_energy_to_pokemon_from_deck(self, pokemon: Card, energy_type: str, amount: int):
        for i in range(len(self.deck)):
            current_card = self.deck[i]

            if current_card.type == "Energy" and current_card.energy_type == energy_type:
                pokemon.attach_energy(self.deck.pop(i))
                amount -= 1

            if amount == 0:
                break

    def attach_energy_to_pokemon_from_discard_pile(self, pokemon: Card, energy_type: str, amount: int):
        for i in range(len(self.discard_pile)):
            current_card = self.discard_pile[i]

            if current_card.type == "Energy" and current_card.energy_type == energy_type:
                pokemon.attach_energy(self.discard_pile.pop(i))
                amount -= 1

            if amount == 0:
                break

    def attach_energy_to_pokemon_from_hand(self, pokemon: Card, energy_type: str, amount: int):
        for i in range(len(self.hand)):
            current_card = self.hand[i]

            if current_card.type == "Energy" and current_card.energy_type == energy_type:
                pokemon.attach_energy(self.hand.pop(i))
                amount -= 1

            if amount == 0:
                break

    def move_energy(self, source: str, target: str, energy_type: str, amount: int):
        pass

    def remove_energy(self, source: str, energy_type: str, amount: int):
        pass

    def move_damage_counter(self, source: str, target: str, amount: int):
        pass

    def move_damage_counter_to_opponents_pokemon(self, active_pokemon: bool, index: int, amount: int):
        pass

    def attach_damage_counter(self, target: str, amount: int):
        pass

    def attach_damage_counter_to_opponents_pokemon(self, active_pokemon: bool, index: int, amount: int):
        pass

    def remove_damage_counter(self, target: str, amount: int):
        pass

    def inflict_poison(self, target: str):
        pass

    def inflict_sleep(self, target: str):
        pass

    def inflict_burn(self, target: str):
        pass

    def inflict_confused(self, target: str):
        pass

    def inflict_paralyzed(self, target: str):
        pass

    def recover_from_special_condition(self, target: str):
        pass

    def discard_benched_pokemon(self, index: int):
        self.discard_pile.append(self.bench.pop(index))

    def discard_all_cards_attached_to_a_benched_pokemon(self, index: int):
        self.discard_pile.append(self.bench[index].attached_cards)

    def discard_energy_card_from_hand(self, energy_type: str):
        for i in range(len(self.hand)):
            if self.hand[i].energy_type == energy_type:
                self.discard_pile.append(self.hand.pop(i))

    def discard_energy_card_from_pokemon(self):
        pass

    def discard_card_from_hand(self, index: int):
        self.discard_pile.append(self.hand.pop(index))

    def discard_x_number_of_cards_from_deck(self, from_top: bool, amount: int):
        for i in range(amount):
            self.discard_pile.append(self.deck.pop(0) if from_top else self.deck.pop())

    def discard_stadium_in_play(self):
        pass

    def attach_pokemon_tool(self):
        pass

    def play_item_card(self):
        pass

    def play_supporter_card(self):
        pass

    def play_stadium_card(self):
        pass

    def retreat(self, target: str):
        pass

    def take_prize_card(self, amount: int = 1):
        pass

    def use_ability(self):
        pass

    def get_card_from_deck(self, index: int):
        return self.deck.pop(index)

    def is_card_in_deck(self, name: str = "", card: Card = None) -> bool:
        if name:
            for card in self.deck:
                if name in card.name:
                    return True

        return card in self.deck

    def is_card_in_discard_pile(self, name: str = "", card: Card = None) -> bool:
        if name:
            for card in self.discard_pile:
                if name in card.name:
                    return True

        return card in self.discard_pile

    def get_card_from_discard_pile(self, index: int):
        return self.discard_pile.pop(index)

    def look_at_x_number_of_cards_from_the_top_of_a_deck(self, your_deck: bool, num_cards: int):
        return self.deck[:num_cards] if your_deck else self.opponent.deck[:num_cards]

    def reveal_cards_to_opponent(self, cards: list[Card]):
        pass

    def select_cards_from_deck(self, indexes: list[int]):
        cards = []
        for i in indexes:
            cards.append(self.deck.pop(i))

        return cards

    def search_deck_for_cards_by_energy_type(self, energy_type: str):
        card_locations = []
        for i in range(len(self.deck)):
            if self.deck[i].energy_type == energy_type:
                card_locations.append(i)

        return card_locations

    def search_deck_for_cards_by_card_type(self, card_type: str):
        card_locations = []
        for i in range(len(self.deck)):
            if self.deck[i].type == card_type:
                card_locations.append(i)

        return card_locations

    def search_deck_for_cards_by_health(self, health: int):
        card_locations = []
        for i in range(len(self.deck)):
            if  self.deck[i].hp <= health:
                card_locations.append(i)

        return card_locations

    def search_deck_for_cards_by_name(self, name: str):
        card_locations = []
        for i in range(len(self.deck)):
            if self.deck[i].name == name:
                card_locations.append(i)

        return card_locations

    def search_discard_pile_for_cards_by_energy_type(self, energy_type: str):
        card_locations = []
        for i in range(len(self.discard_pile)):
            if self.discard_pile[i].energy_type == energy_type:
                card_locations.append(i)

        return card_locations


    def search_discard_pile_for_cards_by_card_type(self, card_type: str):
        card_locations = []
        for i in range(len(self.discard_pile)):
            if self.discard_pile[i].type == card_type:
                card_locations.append(i)

        return card_locations

    def search_discard_pile_for_cards_by_health(self, health: int):
        card_locations = []
        for i in range(len(self.discard_pile)):
            if self.discard_pile[i].hp <= health:
                card_locations.append(i)

        return card_locations

    def search_discard_pile_for_cards_by_name(self, name: str):
        card_locations = []
        for i in range(len(self.discard_pile)):
            if self.discard_pile[i].name == name:
                card_locations.append(i)

        return card_locations
