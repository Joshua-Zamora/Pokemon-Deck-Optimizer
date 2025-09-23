from abc import ABC, abstractmethod
from abilities.ability import Ability


class ActiveAbility(Ability, ABC):
    @abstractmethod
    def can_activate(self, game_state):
        pass

    @abstractmethod
    def activate(self, game_state):
        pass
