from abilities.base import TriggerAbility
from cards.pokemon_card import PokemonCard
from core.game import Game
from core.player import Player


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


class PreventKnockOutTriggerAbility(TriggerAbility):
    names: list[str] = ["Resolute Heart", "Sturdy"]
    descriptions: list[str] = [
        "If this Pokémon has full HP and would be Knocked Out by damage from an attack, it is not Knocked Out, and its remaining HP becomes 10."]
    incoming_damage: int = 0

    def __init__(self, health_remaining: int):
        self.health_remaining = health_remaining

    def can_activate(self, ability_owner: PokemonCard) -> bool:
        return ability_owner.damage_counters_attached == 0 and self.incoming_damage >= ability_owner.health_points

    def activate(self, ability_owner: PokemonCard):
        if self.can_activate(ability_owner):
            ability_owner.prevent_damage = True
            ability_owner.health_points = self.health_remaining
