from abc import ABC
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
