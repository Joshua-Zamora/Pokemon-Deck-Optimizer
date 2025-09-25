from abc import ABC, abstractmethod
from src.cards.pokemon_card import PokemonCard
from src.core.player import Player


class Ability(ABC):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description


class ActiveAbility(Ability, ABC):
    @abstractmethod
    def can_activate(self, player: Player, source: int = 0, target: int = 1) -> bool:
        pass

    @abstractmethod
    def activate(self, player: Player, source: int = 0, target: int = 1):
        pass


class PassiveAbility(Ability, ABC):
    """Always-on effects; no activation, but apply via hooks in game loop."""

    def apply(self, player: Player, owner: PokemonCard, context: dict):
        """e.g., Context: {'damage_amount': 100, 'attacker': ...} for damage prevention."""
        pass


class TriggerAbility(Ability, ABC):
    """Event-based; no manual activation."""

    @property
    @abstractmethod
    def trigger_event(self) -> str:  # e.g., 'on_ko', 'on_damage', 'end_turn'
        pass
