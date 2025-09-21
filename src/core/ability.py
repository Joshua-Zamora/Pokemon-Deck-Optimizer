from abc import ABC, abstractmethod


class Ability(ABC):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    def can_activate(self, game_state):
        pass

    @abstractmethod
    def activate(self, game_state, source: str, target: str = "", amount: int = 0):
        pass
