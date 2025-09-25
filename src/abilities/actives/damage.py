from abc import ABC

from abilities.base import ActiveAbility
from core.player import Player


class MoveDamageCounterToPokemonActiveAbility(ActiveAbility, ABC):
    def __init__(self, name: str, description: str, amount: int = 1, pokemon_restriction: str = None):
        super().__init__(name, description)
        self.amount = amount
        self.pokemon_restriction = pokemon_restriction

    def can_activate(self, player: Player, source: int = 0, target: int = 1) -> bool:
        if self.pokemon_restriction and self.pokemon_restriction not in player.pokemon[source].name:
            return False

        return True if player.pokemon[source].damage_counters_attached >= self.amount else False

    def activate(self, player: Player, source: int = 0, target: int = 1):
        player.move_damage_counter_to_pokemon(source, target, self.amount)


class GetDamageCounterFromPokemonActiveAbility(ActiveAbility, ABC):
    def __init__(self, name: str, description: str, amount: int = 1):
        super().__init__(name, description)
        self.amount = amount

    def can_activate(self, player: Player, source: int = 0, target: int = 1) -> bool:
        return True if player.pokemon[target].damage_counters_attached >= self.amount else False

    def activate(self, player: Player, source: int = 0, target: int = 1):
        player.get_damage_counter_from_pokemon(source, target, self.amount)