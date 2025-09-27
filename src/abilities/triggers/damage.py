from src.abilities.base import TriggerAbility, Ability
from src.cards.pokemon_card import PokemonCard
from src.core.game import Game
from src.core.player import Player


class HealWhenAttachingEnergyTriggerAbility(TriggerAbility):
    def __init__(self, name: str, description: str, damage_counters: int):
        super().__init__(name, description)
        self.damage_counters = damage_counters

    def can_activate(self, player: Player, ability_owner: PokemonCard) -> bool:
        return ability_owner == player.pokemon[0]

    def activate(self, player: Player, ability_owner: PokemonCard, target_pokemon: PokemonCard):
        if self.can_activate(player, ability_owner):
            target_pokemon.damage_counters_attached -= self.damage_counters