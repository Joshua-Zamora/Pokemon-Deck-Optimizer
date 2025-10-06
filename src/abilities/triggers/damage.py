import random

from core.game import Game
from src.abilities.base import TriggerAbility
from src.cards.pokemon_card import PokemonCard
from src.core.player import Player


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
    names: list[str] = ["Expert Hider", "Drifting Dodge", "Adrena-Pheromone", "Tangled Feet"]
    descriptions: list[str] = [
        "If any damage is done to this Pokémon by attacks, flip a coin. If heads, prevent that damage.",
        "If this Pokémon has any {D} Energy attached and is damaged by an attack, flip a coin. If heads, prevent that damage.",
        "If this Pokémon is Confused and is damaged by an attack, flip a coin. If heads, prevent that damage."]
    damaged: bool = False

    def __init__(self, energy_type: str = None, affliction: str = None):
        self.energy_type = energy_type
        self.affliction = affliction

    def can_activate(self, ability_owner: PokemonCard) -> bool:
        if self.energy_type:
            for energy in ability_owner.energy_cards_attached:
                if energy.energy_type == self.energy_type:
                    return self.damaged

            return False
        elif self.affliction:
            return ability_owner.afflictions[self.affliction] and self.damaged

        return self.damaged

    def activate(self, ability_owner: PokemonCard):
        if self.can_activate(ability_owner) and random.choice([True, False]):
            ability_owner.prevent_damage = True


class PreventDamageIfSameEnergyAsOpponentTriggerAbility(TriggerAbility):
    names: list[str] = ["Mimic Barrier"]
    descriptions: list[str] = [
        "If this Pokémon and your opponent's Active Pokémon have the same amount of Energy attached, prevent all damage done to this Pokémon by attacks from your opponent's Pokémon."]

    def can_activate(self, player: Player) -> bool:
        return len(player.pokemon[0].energy_cards_attached) == len(player.opponent.pokemon[0].energy_cards_attached)

    def activate(self, player: Player):
        if self.can_activate(player):
            player.pokemon[0].prevent_damage = True


class DamageAttackingPokemonOnAttackedTriggerAbility(TriggerAbility):
    names: list[str] = ["Pummeling Payback"]
    descriptions: list[str] = [
        "If this Pokémon is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), put 2 damage counters on the Attacking Pokémon for each {M} Energy attached to this Pokémon."]

    def __init__(self, damage_counters: int, energy_type: str):
        self.damage_counters = damage_counters
        self.energy_type = energy_type

    def can_activate(self, player: Player, ability_owner: PokemonCard) -> bool:
        return player.get_number_of_energy_on_pokemon(self.energy_type, ability_owner)

    def activate(self, player: Player, ability_owner: PokemonCard):
        if self.can_activate(player, ability_owner):
            for i in range(player.get_number_of_energy_on_pokemon(self.energy_type, ability_owner)):
                player.opponent.pokemon[
                    0].damage_counters_attached += self.damage_counters  # To do: May need to expand beyond active for determining attacking Pokemon
