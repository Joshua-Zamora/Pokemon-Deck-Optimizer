from src.abilities.base import PassiveAbility
from src.cards.pokemon_card import PokemonCard
from src.core.player import Player


class LimitNumberOfOpponentBenchedPokemonPassiveAbility(PassiveAbility):
    names: list[str] = ["Dust Field"]
    descriptions: list[str] = [
        "As long as this Pokémon is in the Active Spot, your opponent can't have more than 3 Benched Pokémon. If they have 4 or more Benched Pokémon, they discard Benched Pokémon until they have 3 Pokémon on the Bench. If more than one effect changes the number of Benched Pokémon allowed, use the smaller number."]

    def __init__(self, amount: int):
        self.amount = amount

    def can_activate(self, player: Player, ability_owner: PokemonCard) -> bool:
        return player.pokemon[0] == ability_owner

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {"opponent_bench_limit": self.amount} if self.can_activate(player, ability_owner) else {}


class OpponentCantPlayItemCardsPassiveAbility(PassiveAbility):
    names: list[str] = ["Daunting Gaze"]
    descriptions: list[str] = [
        "As long as this Pokémon is in the Active Spot, your opponent can't play any Item cards or Pokémon Tool cards from their hand."]

    def can_activate(self, player: Player, ability_owner) -> bool:
        return ability_owner == player.pokemon[0]

    def get_modifiers(self, player: Player, ability_owner: PokemonCard):
        return {"opponent_can_play_item_cards": False} if self.can_activate(player, ability_owner) else {}


class OpponentCantPlayItemCardsOrToolsPassiveAbility(PassiveAbility):
    names: list[str] = []
    descriptions: list[str] = []

    def can_activate(self, player: Player, ability_owner) -> bool:
        return ability_owner == player.pokemon[0]

    def get_modifiers(self, player: Player, ability_owner: PokemonCard):
        return {"opponent_can_play_item_cards": False, "opponent_can_play_tools": False} if self.can_activate(player,
                                                                                                              ability_owner) else {}


class OpponentCantPlayStadiumCardsPassiveAbility(PassiveAbility):
    names: list[str] = ["Massive Body", "Helical Swell"]
    descriptions: list[str] = [
        "As long as this Pokémon is in the Active Spot, your opponent can't play any Stadium cards from their hand."]

    def can_activate(self, player: Player, ability_owner: PokemonCard) -> bool:
        return ability_owner == player.pokemon[0]

    def get_modifiers(self, player: Player, ability_owner: PokemonCard):
        return {"opponent_can_play_stadium_cards": False} if self.can_activate(player, ability_owner) else {}


class CantPlayPokemonWithAbilityExceptForPassiveAbility(PassiveAbility):
    names: list[str] = ["Potent Glare"]
    descriptions: list[str] = [
        "As long as this Pokémon is in the Active Spot, your opponent can't play any Pokémon that has an Ability from their hand, except for Team Rocket's Pokémon."]

    def __init__(self, pokemon_restriction: str):
        self.pokemon_restriction = pokemon_restriction

    def can_activate(self, player: Player, ability_owner: PokemonCard) -> bool:
        return ability_owner == player.pokemon[0]

    def get_modifiers(self, player: Player, ability_owner: PokemonCard):
        return {"opponent_play_pokemon_with_ability_restriction": self.pokemon_restriction} if self.can_activate(player,
                                                                                                                 ability_owner) else {}
