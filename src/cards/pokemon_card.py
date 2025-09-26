from src.cards.card import Card
from src.cards.energy_card import EnergyCard
from src.cards.trainer_card import TrainerCard
from src.abilities.base import ActiveAbility


class PokemonCard(Card):
    energy_cards_attached: list[EnergyCard]
    pokemon_tool_attached: TrainerCard
    damage_counters_attached: int

    def __init__(self, name: str, card_id: str, regulation_mark: str, energy_type: str, pokemon_category: str,
                 health_points: int, stage: int, evolves_from: str, attacks: list, abilities: list[ActiveAbility],
                 weakness: tuple[str, int], resistance: tuple[str, int], retreat_cost: int):
        super().__init__(name, card_id, regulation_mark)
        self.energy_type = energy_type
        self.pokemon_category = pokemon_category
        self.health_points = health_points
        self.stage = stage
        self.evolves_from = evolves_from
        self.attacks = attacks
        self.abilities = abilities
        self.weakness = weakness
        self.resistance = resistance
        self.retreat_cost = retreat_cost

    def use_ability(self, game_state, index: int):
        self.abilities[index].activate(game_state)
