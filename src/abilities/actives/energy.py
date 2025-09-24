from abc import ABC
from src.abilities.base import ActiveAbility
from src.core.player import Player


class MoveEnergyActiveAbility(ActiveAbility, ABC):
    def __init__(self, name: str, description: str, energy_type: str, your_own: bool, amount: int = 1):
        super().__init__(name, description)
        self.energy_type = energy_type
        self.your_own = your_own
        self.amount = amount

    def activate(self, player, source: int = 0, target: int = 1):
        for i in range(self.amount):
            if self.your_own:
                player.move_your_energy(source, target, self.energy_type)
            else:
                player.move_opponents_energy(source, target, self.energy_type)


class MoveEnergyOnKnockoutActiveAbility(ActiveAbility, ABC):
    def __init__(self, name: str, description: str, energy_type: str, amount: int = 1):
        super().__init__(name, description)
        self.energy_type = energy_type
        self.amount = amount

    def activate(self, player: Player, source: int = 0, target: int = 1):
        for i in range(self.amount):
            player.move_your_energy(source, target, self.energy_type)



class AttachEnergyActiveAbility(ActiveAbility, ABC):
    def __init__(self, name: str, description: str):
        super().__init__(name, description)

    def activate(self, game_state):
        pass
