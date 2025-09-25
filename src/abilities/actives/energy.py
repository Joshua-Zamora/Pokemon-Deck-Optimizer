from abc import ABC

from cards.energy_card import EnergyCard
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


class AttachEnergyFromHandActiveAbility(ActiveAbility, ABC):
    def __init__(self, name: str, description: str, energy_type: str, amount: int = 1, pokemon_restriction: str = None):
        super().__init__(name, description)
        self.energy_type = energy_type
        self.amount = amount
        self.pokemon_restriction = pokemon_restriction

    def can_activate(self, player: Player, source: int = 0, target: int = 1) -> bool:
        if self.pokemon_restriction and self.pokemon_restriction not in player.pokemon[target].name:
            return False

        for card in player.hand:
            if type(card) is EnergyCard and card.energy_type == self.energy_type:
                return True

        return False

    def activate(self, player: Player, source: int = 0, target: int = 1):
        player.attach_energy_to_pokemon_from_hand(target, self.energy_type, self.amount)


class AttachEnergyFromDiscardPileActiveAbility(ActiveAbility, ABC):
    def __init__(self, name: str, description: str, energy_type: str, amount: int = 1):
        super().__init__(name, description)
        self.energy_type = energy_type
        self.amount = amount

    def can_activate(self, player: Player) -> bool:
        for card in player.discard_pile:
            if type(card) is EnergyCard and card.energy_type == self.energy_type:
                return True

        return False

    def activate(self, player: Player, source: int = 0, target: int = 1):
        player.attach_energy_to_pokemon_from_discard_pile(target, self.energy_type, self.amount)


class AttachEnergyFromDiscardPileWithDamageActiveAbility(ActiveAbility, ABC):
    def __init__(self, name: str, description: str, energy_type: str, amount: int = 1, damage_counters: int = 1):
        super().__init__(name, description)
        self.energy_type = energy_type
        self.amount = amount
        self.damage_counters = damage_counters

    def can_activate(self, player: Player, target: int = 0) -> bool:
        energy_type_available, pokemon_would_live = False, False

        for card in player.discard_pile:
            if type(card) is EnergyCard and card.energy_type == self.energy_type:
                energy_type_available = True
                break

        if player.pokemon[target].health_points - (self.damage_counters * 10) > 0:  # Multiply by 10 to convert to hp
            pokemon_would_live = True

        return energy_type_available and pokemon_would_live

    def activate(self, player: Player, source: int = 0, target: int = 0):
        player.attach_energy_to_pokemon_from_discard_pile(target, self.energy_type, self.amount)
        player.attach_damage_counter(target, self.damage_counters)


class AttachEnergyFromDeckActiveAbility(ActiveAbility, ABC):
    def __init__(self, name: str, description: str, energy_type: str, amount: int = 1):
        super().__init__(name, description)
        self.energy_type = energy_type
        self.amount = amount

    def can_activate(self, player: Player) -> bool:
        for card in player.deck:
            if type(card) is EnergyCard and card.energy_type == self.energy_type:
                return True

        return False

    def activate(self, player: Player, source: int = 0, target: int = 1):
        player.attach_energy_to_pokemon_from_deck(target, self.energy_type, self.amount)
