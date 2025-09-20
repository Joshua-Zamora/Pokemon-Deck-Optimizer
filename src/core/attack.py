from abc import ABC, abstractmethod


class Attack(ABC):
    def __init__(self, name: str, description: str, damage: int, cost: int):
        self.name = name
        self.description = description
        self.damage = damage
        self.cost = cost

    @abstractmethod
    def activate(self):
        pass