from src.abilities.base import PassiveAbility
from src.cards.pokemon_card import PokemonCard
from src.core.player import Player


class IncreaseAllPokemonHealthPassiveAbility(PassiveAbility):
    names: list[str] = ["Vibrant Dance"]
    descriptions: list[str] = ["All of your Pokémon in play get +40 HP. The effect of Vibrant Dance doesn't stack."]

    def __init__(self, amount: int):
        self.amount = amount

    def can_activate(self, player: Player) -> bool:
        return True

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {'increase_all_pokemon_health': self.amount}
