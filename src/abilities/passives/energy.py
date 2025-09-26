from src.abilities.base import PassiveAbility
from src.cards.pokemon_card import PokemonCard
from src.core.player import Player


class IncreaseOpponentAttackCostPassiveAbility(PassiveAbility):
    def __init__(self, name: str, description: str, extra_cost: dict):  # e.g., {'C': 1}
        super().__init__(name, description)
        self.extra_cost = extra_cost  # {'C': 1} for colorless

    def can_activate(self, player: Player, ability_owner: PokemonCard) -> bool:
        # For masking/visibility in RL state; not used for passive applying
        return player.pokemon[0] == ability_owner  # Only if the ability owner is in the active position

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {'attack_cost_opponent': self.extra_cost} if self.can_activate(player, ability_owner) else {}


class ChangePokemonEnergyTypePassiveAbility(PassiveAbility):
    def __init__(self, name: str, description: str, energy_types: list[str]):
        super().__init__(name, description)
        self.energy_types = energy_types

    def can_activate(self, player: Player, ability_owner: PokemonCard):
        return ability_owner in player.pokemon

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {'energy_types': self.energy_types} if self.can_activate(player, ability_owner) else {}