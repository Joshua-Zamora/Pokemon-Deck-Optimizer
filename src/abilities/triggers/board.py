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