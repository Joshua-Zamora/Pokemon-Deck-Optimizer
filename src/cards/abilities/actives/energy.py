from src.cards.energy_card import EnergyCard
from cards.abilities.base import ActiveAbility
from src.core.player import Player


class MoveEnergyActiveAbility(ActiveAbility):
    names: list[str] = []
    descriptions: list[str] = []

    def __init__(self, energy_type: str, your_own: bool, amount: int = 1):
        self.energy_type = energy_type
        self.your_own = your_own
        self.amount = amount

    def activate(self, player, source: int = 0, target: int = 1):
        for i in range(self.amount):
            if self.your_own:
                player.move_your_energy(source, target, self.energy_type)
            else:
                player.move_opponents_energy(source, target, self.energy_type)


class MoveEnergyFromBenchToActiveActiveAbility(ActiveAbility):
    names: list[str] = ["Fire Off"]
    descriptions: list[str] = [
        "As often as you like during your turn, you may move a {R} Energy from 1 of your Benched Pokémon to your Active Pokémon."]

    def __init__(self, energy_type: str, amount: int = 1):
        self.energy_type = energy_type
        self.amount = amount

    def can_activate(self, player: Player, source: int = 0, target: int = 1) -> bool:
        available = 0

        for poke in player.pokemon[1:]:
            for energy in poke.energy_cards_attached:
                if energy.energy_type == self.energy_type:
                    available += 1

        return available >= self.amount

    def activate(self, player: Player, source: int = 0, target: int = 1):
        if self.can_activate(player):
            for i in range(self.amount):
                player.move_your_energy(source, 0, self.energy_type)


class AttachEnergyFromHandActiveAbility(ActiveAbility):
    names: list[str] = ["Electric Streamer", "Inferno Fandango", "Super Cold"]
    descriptions: list[str] = [
        "As often as you like during your turn, you may attach a Basic {L} Energy card from your hand to 1 of your Iono's Pokémon.",
        "As often as you like during your turn, you may attach a Basic {R} Energy card from your hand to 1 of your Pokémon.",
        "As often as you like during your turn, you may attach a Basic {W} Energy card from your hand to 1 of your Pokémon."
        ]

    def __init__(self, energy_type: str, amount: int = 1, pokemon_restriction: str = None):
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


class AttachEnergyFromDiscardPileActiveAbility(ActiveAbility):
    names: list[str] = []
    descriptions: list[str] = []

    def __init__(self, energy_type: str, amount: int = 1):
        self.energy_type = energy_type
        self.amount = amount

    def can_activate(self, player: Player) -> bool:
        for card in player.discard_pile:
            if type(card) is EnergyCard and card.energy_type == self.energy_type:
                return True

        return False

    def activate(self, player: Player, source: int = 0, target: int = 1):
        player.attach_energy_to_pokemon_from_discard_pile(target, self.energy_type, self.amount)


class AttachEnergyFromDiscardPileWithDamageActiveAbility(ActiveAbility):
    names: list[str] = ["Psychic Embrace"]
    descriptions: list[str] = [
        "As often as you like during your turn, you may attach a Basic {P} Energy card from your discard pile to 1 of your {P} Pokémon. If you attached Energy to a Pokémon in this way, put 2 damage counters on that Pokémon. You can't use this Ability on a Pokémon that would be Knocked Out."]

    def __init__(self, energy_type: str, amount: int = 1, damage_counters: int = 1):
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


class AttachEnergyFromDeckActiveAbility(ActiveAbility):
    names: list[str] = []
    descriptions: list[str] = []

    def __init__(self, energy_type: str, amount: int = 1):
        self.energy_type = energy_type
        self.amount = amount

    def can_activate(self, player: Player) -> bool:
        for card in player.deck:
            if type(card) is EnergyCard and card.energy_type == self.energy_type:
                return True

        return False

    def activate(self, player: Player, source: int = 0, target: int = 1):
        player.attach_energy_to_pokemon_from_deck(target, self.energy_type, self.amount)
