from abilities.base import PassiveAbility
from cards.pokemon_card import PokemonCard
from core.player import Player


class LimitNumberOfOpponentBenchedPokemonPassiveAbility(PassiveAbility):
    def __init__(self, name: str, description: str, amount: int):
        super().__init__(name, description)
        self.amount = amount

    def can_activate(self, player: Player, ability_owner: PokemonCard) -> bool:
        return player.pokemon[0] == ability_owner

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {"opponent_bench_limit": self.amount} if self.can_activate(player, ability_owner) else {}