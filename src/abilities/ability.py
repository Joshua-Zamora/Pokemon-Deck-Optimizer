from abc import ABC, abstractmethod


class Ability(ABC):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
