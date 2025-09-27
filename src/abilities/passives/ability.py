from src.abilities.base import PassiveAbility
from src.cards.pokemon_card import PokemonCard
from src.core.player import Player


class BasicPokemonInPlayHaveNoAbilities(PassiveAbility):
    def __init__(self, name: str, description: str):
        super().__init__(name, description)

    def can_activate(self, player: Player, ability_owner: PokemonCard):
        if ability_owner != player.pokemon[0]:
            return False

        for poke in player.pokemon:
            if poke.pokemon_category == "basic":
                return True

        for poke in player.opponent.pokemon:
            if poke.pokemon_category == "basic":
                return True

        return False

    def activate(self, player: Player, ability_owner: PokemonCard):
        return {'basic_pokemon_no_abilities': True} if self.can_activate(player,
                                                                         ability_owner) else {}  # except for Mischievous Lock.


class PokemonWIthRuleBoxHaveNoAbilitiesExceptFuture(PassiveAbility):
    def __init__(self, name: str, description: str):
        super().__init__(name, description)

    def can_activate(self, player: Player, ability_owner: PokemonCard):
        if ability_owner != player.pokemon[0]:
            return False

        for poke in player.pokemon:
            if poke.suffix:
                return True

        for poke in player.opponent.pokemon:
            if poke.suffix:
                return True

        return False

    def activate(self, player: Player, ability_owner: PokemonCard):
        return {'pokemon_with_rule_box_no_abilities_except_future': True} if self.can_activate(player,
                                                                                               ability_owner) else {}
