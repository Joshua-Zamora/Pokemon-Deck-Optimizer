from src.abilities.base import PassiveAbility
from src.cards.pokemon_card import PokemonCard
from src.core.player import Player


class LimitNumberOfOpponentBenchedPokemonPassiveAbility(PassiveAbility):
    def __init__(self, name: str, description: str, amount: int):
        super().__init__(name, description)
        self.amount = amount

    def can_activate(self, player: Player, ability_owner: PokemonCard) -> bool:
        return player.pokemon[0] == ability_owner

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {"opponent_bench_limit": self.amount} if self.can_activate(player, ability_owner) else {}


class OpponentCantPlayItemCardsPassiveAbility(PassiveAbility):
    def __init__(self, name: str, description: str):
        super().__init__(name, description)

    def can_activate(self, player: Player, ability_owner) -> bool:
        return ability_owner == player.pokemon[0]

    def get_modifiers(self, player: Player, ability_owner: PokemonCard):
        return {"opponent_can_play_item_cards": False} if self.can_activate(player, ability_owner) else {}


class OpponentCantPlayItemCardsOrToolsPassiveAbility(PassiveAbility):
    def __init__(self, name: str, description: str):
        super().__init__(name, description)

    def can_activate(self, player: Player, ability_owner) -> bool:
        return ability_owner == player.pokemon[0]

    def get_modifiers(self, player: Player, ability_owner: PokemonCard):
        return {"opponent_can_play_item_cards": False, "opponent_can_play_tools": False} if self.can_activate(player,
                                                                                                              ability_owner) else {}


class CantPlayPokemonWithAbilityExceptForPassiveAbility(PassiveAbility):
    def __init__(self, name: str, description: str, pokemon_restriction: str):
        super().__init__(name, description)
        self.pokemon_restriction = pokemon_restriction

    def can_activate(self, player: Player, ability_owner: PokemonCard) -> bool:
        return ability_owner == player.pokemon[0]

    def get_modifiers(self, player: Player, ability_owner: PokemonCard):
        return {"opponent_play_pokemon_with_ability_restriction": self.pokemon_restriction} if self.can_activate(player,
                                                                                                                 ability_owner) else {}
