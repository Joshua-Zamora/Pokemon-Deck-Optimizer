from __future__ import annotations
from abc import ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # These imports are only for type checking and won't run at runtime, avoiding circular imports.
    from src.cards.pokemon_card import PokemonCard
    from src.core.player import Player


class Ability(ABC):
    names: list[str] = []
    descriptions: list[str] = []


class ActiveAbility(Ability):
    def can_activate(self, player: Player, source: int = 0, target: int = 1) -> bool:
        pass

    def activate(self, player: Player, source: int = 0, target: int = 1):
        pass


class PassiveAbility(Ability):
    """Always-on effects; no activation, but apply via hooks in game loop."""

    def apply(self, player: Player, owner: PokemonCard, context: dict):
        """e.g., Context: {'damage_amount': 100, 'attacker': ...} for damage prevention."""
        pass

    def get_modifiers(self, player: Player, owner: PokemonCard) -> dict:
        """Return modifiers as a dict, e.g., {'attack_cost_opponent': {'colorless': 1}}."""
        pass


class TriggerAbility(Ability):
    """Event-based; no manual activation."""

    def trigger_event(self) -> str:  # e.g., 'on_ko', 'on_damage', 'end_turn'
        pass
