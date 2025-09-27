from src.abilities.base import PassiveAbility
from src.cards.pokemon_card import PokemonCard
from src.core.player import Player


class WeaknessStrengthModifierOnOpponentsActivePassiveAbility(PassiveAbility):
    def __init__(self, name:str, description:str, modifier: int):
        super().__init__(name, description)
        self.modifier = modifier

    def can_activate(self, player: Player) -> bool:
        return player.pokemon[0].weakness is not None

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {"opponent_weakness_increase": player.pokemon[0].weakness[1] * 4} if self.can_activate(player) else {}
