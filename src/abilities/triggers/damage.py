import random

from core.game import Game
from src.abilities.base import TriggerAbility
from src.cards.pokemon_card import PokemonCard
from src.core.player import Player


class HealWhenAttachingEnergyTriggerAbility(TriggerAbility):
    names: list[str] = ["Auto Heal"]
    descriptions: list[str] = [
        "As long as this Pokémon is in the Active Spot, whenever you attach an Energy card from your hand to 1 of your Pokémon, heal 90 damage from that Pokémon."]

    def __init__(self, damage_counters: int):
        self.damage_counters = damage_counters

    def can_activate(self, player: Player, ability_owner: PokemonCard) -> bool:
        return ability_owner == player.pokemon[0]

    def activate(self, player: Player, ability_owner: PokemonCard, target_pokemon: PokemonCard):
        if self.can_activate(player, ability_owner):
            target_pokemon.damage_counters_attached -= self.damage_counters


class HealDuringPokemonCheckupTriggerAbility(TriggerAbility):
    names: list[str] = ["Blessed Salt"]
    descriptions: list[str] = ["During Pokémon Checkup, heal 20 damage from each of your Pokémon."]

    def __init__(self, damage_counters: int):
        self.damage_counters = damage_counters

    def can_activate(self, game_state: Game) -> bool:
        return game_state.in_pokemon_checkup

    def activate(self, game_state: Game, player: Player):
        if self.can_activate(game_state):
            for poke in player.pokemon:
                poke.damage_counters_attached -= self.damage_counters


class ApplyDamageDuringPokemonCheckupTriggerAbility(TriggerAbility):
    names: list[str] = ["Forest Miasma"]
    descriptions: list[str] = [
        "During Pokémon Checkup, if this Pokémon is in the Active Spot, put 1 damage counter on your opponent's Active Pokémon."]

    def __init__(self, damage_counters: int):
        self.damage_counters = damage_counters

    def can_activate(self, game_state: Game, ability_owner: PokemonCard, player: Player) -> bool:
        return game_state.in_pokemon_checkup and ability_owner == player.pokemon[0]

    def activate(self, game_state: Game, player: Player, ability_owner: PokemonCard):
        if self.can_activate(game_state, ability_owner, player):
            player.opponent.pokemon[0].damage_counters_attached += self.damage_counters


class ApplyDamageToBasicPokemonDuringPokemonCheckupTriggerAbility(TriggerAbility):
    names: list[str] = ["Sand Stream"]
    descriptions: list[str] = [
        "During Pokémon Checkup, if this Pokémon is in the Active Spot, put 2 damage counters on each of your opponent's Basic Pokémon."]

    def __init__(self, damage_counters: int):
        self.damage_counters = damage_counters

    def can_activate(self, game_state: Game, ability_owner: PokemonCard, player: Player) -> bool:
        return game_state.in_pokemon_checkup and ability_owner == player.pokemon[0]

    def activate(self, game_state: Game, player: Player, ability_owner: PokemonCard):
        if self.can_activate(game_state, ability_owner, player):
            for poke in player.opponent.pokemon:
                if poke.pokemon_category == "basic":
                    poke.damage_counters_attached += self.damage_counters


class ApplyDamageToPokemonWithAbilityDuringPokemonCheckupTriggerAbility(TriggerAbility):
    names: list[str] = ["Freezing Shroud"]
    descriptions: list[str] = [
        "During Pokémon Checkup, put 1 damage counter on each Pokémon that has an Ability (both yours and your opponent's), except any Froslass."]

    def __init__(self, damage_counters: int, pokemon_exception: str = None):
        self.damage_counters = damage_counters
        self.pokemon_exception = pokemon_exception

    def can_activate(self, game_state: Game) -> bool:
        return game_state.in_pokemon_checkup

    def activate(self, game_state: Game, player: Player):
        if self.can_activate(game_state):
            for poke in player.pokemon:
                if len(poke.abilities) > 0 and self.pokemon_exception not in poke.name:
                    poke.damage_counters_attached += self.damage_counters

            for poke in player.opponent.pokemon:
                if len(poke.abilities) > 0 and self.pokemon_exception not in poke.name:
                    poke.damage_counters_attached += self.damage_counters


class ApplyDamageToBurnedPokemonDuringPokemonCheckupTriggerAbility(TriggerAbility):
    names: list[str] = ["Magma Surge"]
    descriptions: list[str] = ["During Pokémon Checkup, put 3 more damage counters on your opponent's Burned Pokémon."]

    def __init__(self, damage_counters: int):
        self.damage_counters = damage_counters

    def can_activate(self, game_state: Game, player: Player) -> bool:
        return game_state.in_pokemon_checkup and player.opponent.pokemon[0].afflictions["burned"]

    def activate(self, game_state: Game, player: Player):
        if self.can_activate(game_state, player):
            player.opponent.pokemon[0].damage_counters_attached += self.damage_counters


class PreventDamageOnAttackedTriggerAbility(TriggerAbility):
    names: list[str] = ["Expert Hider", "Drifting Dodge"]
    descriptions: list[str] = [
        "If any damage is done to this Pokémon by attacks, flip a coin. If heads, prevent that damage."]
    damaged: bool = False

    def can_activate(self) -> bool:
        return self.damaged

    def activate(self, player: Player):
        if self.can_activate() and random.choice([True, False]):
            player.pokemon[0].prevent_damage = True


class PreventDamageIfSameEnergyAsOpponentTriggerAbility(TriggerAbility):
    names: list[str] = ["Mimic Barrier"]
    descriptions: list[str] = [
        "If this Pokémon and your opponent's Active Pokémon have the same amount of Energy attached, prevent all damage done to this Pokémon by attacks from your opponent's Pokémon."]

    def can_activate(self, player: Player) -> bool:
        return len(player.pokemon[0].energy_cards_attached) == len(player.opponent.pokemon[0].energy_cards_attached)

    def activate(self, player: Player):
        if self.can_activate(player):
            player.pokemon[0].prevent_damage = True