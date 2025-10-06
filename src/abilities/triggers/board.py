import random

from abilities.base import TriggerAbility
from cards.pokemon_card import PokemonCard
from core.player import Player


class TakeOneFewerPrizeCardOnKnockoutTriggerAbility(TriggerAbility):
    names: list[str] = ["Oh No You Don't"]
    descriptions: list[str] = [
        "If this Pokémon is Knocked Out by damage from an attack from your opponent's Pokémon, and if you have any Pecharunt ex in play, your opponent takes 1 fewer Prize card."]

    def __init__(self, pokemon_restriction: str = None):
        self.pokemon_restriction = pokemon_restriction

    def can_activate(self, player: Player, ability_owner: PokemonCard):
        for poke in player.pokemon:
            if self.pokemon_restriction in poke.name:
                return ability_owner.damage_counters_attached * 10 > ability_owner.health_points

        return False

    def activate(self, player: Player, ability_owner: PokemonCard):
        if self.can_activate(player, ability_owner):
            ability_owner.worth_number_of_prize_cards -= 1


class DiscardFromHandOnKnockoutTriggerAbility(TriggerAbility):
    names: list[str] = ["Startling Pumpkin"]
    descriptions: list[str] = [
        "If this Pokémon is Knocked Out by damage from an attack from your opponent's Pokémon, discard 2 random cards from your opponent's hand."]

    def __init__(self, num_cards: int = 1):
        self.num_cards = num_cards

    def can_activate(self, ability_owner: PokemonCard):
        return ability_owner.damage_counters_attached * 10 > ability_owner.health_points

    def activate(self, player: Player, ability_owner: PokemonCard):
        if self.can_activate(ability_owner):
            for i in range(self.num_cards):
                player.opponent.discard_card_from_hand(random.randint(0, len(player.hand) - 1))


class SearchDeckForCardOnKnockoutTriggerAbility(TriggerAbility):
    names: list[str] = ["Gold Coffin"]
    descriptions: list[str] = [
        "If this Pokémon is Knocked Out by damage from an attack from your opponent's Pokémon, search your deck for a card and put it into your hand. Then, shuffle your deck."]

    def can_activate(self, ability_owner: PokemonCard):
        return ability_owner.damage_counters_attached * 10 > ability_owner.health_points

    def activate(self, player: Player, ability_owner: PokemonCard, index: int):
        if self.can_activate(ability_owner):
            player.get_card_from_deck(index)


class KnockoutAttackingPokemonIfKnockedOutTriggerAbility(TriggerAbility):
    names: list[str] = ["Oh No You Don't"]
    descriptions: list[str] = []

    def can_activate(self, player: Player, ability_owner: PokemonCard):
        return ability_owner == player.pokemon[0] and ability_owner.damage_counters_attached * 10 > ability_owner.health_points

    def activate(self, player: Player, ability_owner: PokemonCard, ):
        if self.can_activate(player, ability_owner):
            coin_fip = random.choice
            player.opponent