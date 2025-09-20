from abc import ABC, abstractmethod


class Ability(ABC):
    has_activated: bool = False

    def __init__(self, name: str, description: str, is_passive: bool = False):
        self.name = name
        self.description = description
        self.is_passive = is_passive

    @abstractmethod
    def activate(self):
        pass
