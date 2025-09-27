from src.abilities.base import PassiveAbility
from src.cards.pokemon_card import PokemonCard
from src.core.player import Player


class IncreaseAllPokemonHealthPassiveAbility(PassiveAbility):
    def __init__(self, name: str, description: str, amount: int):
        super().__init__(name, description)
        self.amount = amount

    def can_activate(self, player: Player) -> bool:
        return True

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {'increase_all_pokemon_health': self.amount}