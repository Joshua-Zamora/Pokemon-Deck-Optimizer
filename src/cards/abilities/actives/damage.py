from cards.abilities.base import ActiveAbility
from src.core.player import Player


class MoveDamageCounterToPokemonActiveAbility(ActiveAbility):
    names: list[str] = ["Rocket Brain"]
    descriptions: list[str] = [
        "As often as you like during your turn, you may move 1 damage counter from 1 of your Team Rocket's Pokémon to another of your Pokémon."]

    def __init__(self, amount: int = 1, pokemon_restriction: str = None):
        self.amount = amount
        self.pokemon_restriction = pokemon_restriction

    def can_activate(self, player: Player, source: int = 0, target: int = 1) -> bool:
        if self.pokemon_restriction and self.pokemon_restriction not in player.pokemon[source].name:
            return False

        return True if player.pokemon[source].damage_counters_attached >= self.amount else False

    def activate(self, player: Player, source: int = 0, target: int = 1):
        player.move_damage_counter_to_pokemon(source, target, self.amount)


class GetDamageCounterFromPokemonActiveAbility(ActiveAbility):
    names: list[str] = ["Strange Behavior"]
    descriptions: list[str] = [
        "As often as you like during your turn, you may move 1 damage counter from 1 of your other Pokémon to this Pokémon."]

    def __init__(self, amount: int = 1):
        self.amount = amount

    def can_activate(self, player: Player, source: int = 0, target: int = 1) -> bool:
        return True if player.pokemon[target].damage_counters_attached >= self.amount else False

    def activate(self, player: Player, source: int = 0, target: int = 1):
        player.get_damage_counter_from_pokemon(source, target, self.amount)
