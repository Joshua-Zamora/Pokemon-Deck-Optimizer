from abc import ABC
from src.abilities.actives.active_ability import ActiveAbility


class MoveEnergyActiveAbility(ActiveAbility, ABC):
    def __init__(self, name: str, description: str, source: str = "", target: str = "", amount: int = 1):
        super().__init__(name, description)
        self.source = source
        self.target = target
        self.amount = amount

    def activate(self, game_state):
        game_state.player_one.move_energy(self.source, self.target, "energy", self.amount)


class AttachEnergyActiveAbility(ActiveAbility, ABC):
    def __init__(self, name: str, description: str):
        super().__init__(name, description)

    def activate(self, game_state):
        pass
