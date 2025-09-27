from abc import ABC
from abilities.base import TriggerAbility
from core.player import Player


class MoveEnergyOnKnockoutTriggerAbility(TriggerAbility):
    def __init__(self, name: str, description: str, energy_type: str, amount: int = 1):
        super().__init__(name, description)
        self.energy_type = energy_type
        self.amount = amount

    def can_activate(self, player: Player) -> bool:
        ko = player.recently_knocked_out_pokemon
        return bool(ko and any(e.energy_type == self.energy_type for e in ko.energy_cards_attached))

    def activate(self, player: Player, source: int = 0, target: int = 1):
        for i in range(self.amount):
            player.move_your_energy(source, target, self.energy_type)
