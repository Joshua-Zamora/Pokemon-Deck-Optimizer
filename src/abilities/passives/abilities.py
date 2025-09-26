from src.abilities.base import PassiveAbility
from src.core.player import Player


class BasicPokemonInPlayHaveNoAbilities(PassiveAbility):
    def __init__(self, name: str, description: str):
        super().__init__(name, description)

    def can_activate(self, player: Player):
        for poke in player.pokemon:
            if poke.pokemon_category == "basic":
                return True

        for poke in player.opponent.pokemon:
            if poke.pokemon_category == "basic":
                return True

        return False

    def activate(self, player: Player):
        return {'basic_pokemon_no_abilities': True} if self.can_activate(player) else {} # except for Mischievous Lock.




