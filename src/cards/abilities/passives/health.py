from cards.abilities.base import PassiveAbility
from src.cards.pokemon_card import PokemonCard
from src.core.player import Player


class IncreaseAllPokemonHealthPassiveAbility(PassiveAbility):
    names: list[str] = ["Vibrant Dance"]
    descriptions: list[str] = ["All of your Pokémon in play get +40 HP. The effect of Vibrant Dance doesn't stack."]

    def __init__(self, amount: int):
        self.amount = amount

    def can_activate(self, player: Player) -> bool:
        return True

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {'increase_all_pokemon_health': self.amount}


class IncreaseHealthIfEnergyAttachedPassiveAbility(PassiveAbility):
    names: str = ["Nutritional Iron", "Expanding Body", "Adrena-Power"]
    descriptions: str = ["If this Pokémon has 3 or more {M} Energy attached, it gets +100 HP.",
                         "If this Pokémon has any Special Energy attached, it gets +100 HP.",
                         "If this Pokémon has any {D} Energy attached, it gets +100 HP, and the attacks it uses do 100 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance)."]

    def __init__(self, energy_type: str, amount: int, health_increase: int, damage_increase: int = None):
        self.energy_type = energy_type
        self.amount = amount
        self.health_increase = health_increase
        self.damage_increase = damage_increase

    def can_activate(self, ability_owner: PokemonCard) -> bool:
        count = 0

        for energy in ability_owner.energy_cards_attached:
            if energy.energy_type == self.energy_type:
                count += 1

        return count >= self.amount

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        if self.damage_increase:
            return {"increase_health": self.health_increase,
                    "increase_damage": self.damage_increase} if self.can_activate(ability_owner) else {}

        return {"increase_health": self.health_increase} if self.can_activate(ability_owner) else {}
