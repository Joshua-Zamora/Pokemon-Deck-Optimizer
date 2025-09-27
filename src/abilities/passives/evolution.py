from src.abilities.base import PassiveAbility
from src.cards.pokemon_card import PokemonCard
from src.core.player import Player


class PokemonCanEvolveImmediatelyPassiveAbility(PassiveAbility):
    def __init__(self, name: str, description: str):
        super().__init__(name, description)

    def can_activate(self, player: Player, ability_owner: PokemonCard) -> bool:
        return ability_owner == player.pokemon[0]

    def activate(self, player: Player, ability_owner: PokemonCard):
        return {"can_evolve_immediately": True} if self.can_activate(player, ability_owner) else {}

