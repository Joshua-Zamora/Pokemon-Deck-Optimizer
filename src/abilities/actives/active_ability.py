from abc import ABC
from src.core.ability import Ability


class ActiveAbility(Ability, ABC):
    def can_activate(self, game_state):
        return True

    def activate(self, game_state, source: str, target: str = "", amount: int = 0):
        pass
