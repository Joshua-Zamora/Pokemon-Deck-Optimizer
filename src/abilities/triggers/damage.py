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
