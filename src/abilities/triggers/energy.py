from cards.pokemon_card import PokemonCard
from src.abilities.base import TriggerAbility
from src.core.player import Player


class MoveEnergyOnKnockoutTriggerAbility(TriggerAbility):
    names: list[str] = []
    descriptions: list[str] = []

    def __init__(self, energy_type: str, amount: int = 1):
        self.energy_type = energy_type
        self.amount = amount

    def can_activate(self, player: Player) -> bool:
        ko = player.recently_knocked_out_pokemon
        return bool(ko and any(e.energy_type == self.energy_type for e in ko.energy_cards_attached))

    def activate(self, player: Player, source: int = 0, target: int = 1):
        for i in range(self.amount):
            player.move_your_energy(source, target, self.energy_type)


class MaySwitchOnEnergyAttachedTriggerAbility(TriggerAbility):
    names: list[str] = ["Far-Flying Meteor"]
    descriptions: list[str] = [
        "During your turn, if this Pokémon is on your Bench, whenever you attach an Energy card from your hand to this Pokémon, you may switch it with your Active Pokémon."]
    energy_has_been_attached: bool = False

    def can_activate(self, player: Player, ability_owner: PokemonCard) -> bool:
        return ability_owner in player.pokemon[1:] and self.energy_has_been_attached

    def activate(self, player: Player, ability_owner: PokemonCard, source: int):
        if self.can_activate(player, ability_owner):
            player.swap_benched_pokemon_with_active_pokemon(source, True)
