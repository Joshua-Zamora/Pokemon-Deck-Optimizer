from abilities.base import TriggerAbility, ActiveAbility, PassiveAbility
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

    def __init__(self, name: str, card_id: str, regulation_mark: str, energy_type: str, pokemon_category: str,
                 health_points: int, stage: int, evolves_from: str, attacks: list,
                 abilities: list[TriggerAbility | ActiveAbility | PassiveAbility],
                 weakness: tuple[str, int] | None, resistance: tuple[str, int] | None, retreat_cost: int | None,
                 suffix: str | None):
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
        self.suffix = suffix
