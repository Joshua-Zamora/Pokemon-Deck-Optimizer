from cards.abilities.base import ActiveAbility, PassiveAbility
from src.cards.card import Card
from src.cards.energy_card import EnergyCard
from src.cards.trainer_card import TrainerCard


class PokemonCard(Card):
    energy_cards_attached: list[EnergyCard] = []
    pokemon_tool_attached: TrainerCard | None = None
    damage_counters_attached: int = 0
    afflictions: dict = {
        "asleep": False,
        "burned": False,
        "confused": False,
        "paralyzed": False,
        "poisoned": False,
    }
    prevent_damage: bool = False
    pokemon_that_attacked = None
    received_damage_this_turn: bool = False

    def __init__(self, name: str, card_id: str, regulation_mark: str, energy_type: str, pokemon_category: str,
                 health_points: int, stage: int, evolves_from: str, attacks: list,
                 abilities: list[ActiveAbility | PassiveAbility],
                 weakness: tuple[str, int] | None, resistance: tuple[str, int] | None, retreat_cost: int | None,
                 suffix: str | None, worth_number_of_prize_cards: int = 1):
        super().__init__(name, card_id, regulation_mark)
        self.energy_type = energy_type
        self.pokemon_category = pokemon_category
        self.max_health_points = health_points
        self.current_health_points = health_points
        self.stage = stage
        self.evolves_from = evolves_from
        self.attacks = attacks
        self.abilities = abilities
        self.weakness = weakness
        self.resistance = resistance
        self.retreat_cost = retreat_cost
        self.suffix = suffix
        self.worth_number_of_prize_cards = worth_number_of_prize_cards


    def damaged(self, amount_of_damage_counters: int, pokemon):
        self.damage_counters_attached += amount_of_damage_counters
        self.current_health_points -= (amount_of_damage_counters * 10)
        self.pokemon_that_attacked = pokemon
        self.received_damage_this_turn = True

    def proceed_to_next_turn(self):
        self.received_damage_this_turn = False
