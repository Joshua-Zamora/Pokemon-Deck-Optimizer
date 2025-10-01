import random

from src.abilities.base import TriggerAbility
from src.cards.pokemon_card import PokemonCard
from src.core.game import Game
from src.core.player import Player


class AddDamageToPoisonedPokemonTriggerAbility(TriggerAbility):
    names: list[str] = ["Toxic Subjugation"]
    descriptions: list[str] = [
        "As long as this Pokémon is in the Active Spot, put 5 more damage counters on your opponent's Poisoned Pokémon during Pokémon Checkup."]

    def __init__(self, damage_counters: int):
        self.damage_counters = damage_counters

    def can_activate(self, game_state: Game, player: Player, ability_owner: PokemonCard) -> bool:
        return ability_owner == player.pokemon[0] and player.opponent.pokemon[0].afflictions[
            "poisoned"] and game_state.in_pokemon_checkup

    def activate(self, game_state: Game, player: Player, ability_owner: PokemonCard):
        if self.can_activate(game_state, player, ability_owner):
            player.opponent.pokemon[0].damage_counters_attached += self.damage_counters


class PreventAllEffectsOnSupportCardPlayedTriggerAbility(TriggerAbility):
    names: list[str] = ["Wide Wall"]
    descriptions: list[str] = [
        "As long as this Pokémon is in the Active Spot, whenever your opponent plays a Supporter card from their hand, prevent all effects of that card done to all of your Pokémon."]

    def can_activate(self, player: Player, ability_owner: PokemonCard) -> bool:
        return ability_owner == player.pokemon[0]

    def activate(self, player: Player, ability_owner: PokemonCard):
        if self.can_activate(player, ability_owner):
            player.opponent.supporter_effects_mitigated = True


class FlipExtraCoinIfAsleepTriggerAbility(TriggerAbility):
    names: list[str] = ["Stir and Snooze"]
    descriptions: list[str] = [
        "If this Pokémon is Asleep, flip 2 coins instead of 1 during Pokémon Checkup. If either of them is tails, this Pokémon is still Asleep."]

    def can_activate(self, ability_owner: PokemonCard) -> bool:
        return ability_owner.afflictions["asleep"]

    def activate(self, player: Player, ability_owner: PokemonCard):
        if self.can_activate(ability_owner):
            random.choice([True, False]) # To do: Implement afflictions functionality in Game.py