from src.abilities.base import PassiveAbility
from src.cards.pokemon_card import PokemonCard
from src.core.player import Player


class DecreaseOpponentAttackDamageIfActivePassiveAbility(PassiveAbility):
    def __init__(self, name: str, description: str, amount: int):
        super().__init__(name, description)
        self.amount = amount

    def can_activate(self, player: Player, ability_owner: PokemonCard) -> bool:
        return player.pokemon[0] == ability_owner

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {'opponent_damage': -self.amount} if self.can_activate(player, ability_owner) else {}


class DecreaseOpponentAttackDamagePassiveAbility(PassiveAbility):
    def __init__(self, name: str, description: str, amount: int):
        super().__init__(name, description)
        self.amount = amount

    def can_activate(self) -> bool:
        return True

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {'opponent_damage': -self.amount}


class DecreaseOpponentAttackDamageOnEnergiesAttachedPassiveAbility(PassiveAbility):
    def __init__(self, name: str, description: str, energy_type: str, amount: int):
        super().__init__(name, description)
        self.energy_type = energy_type
        self.amount = amount

    def can_activate(self, player: Player) -> bool:
        for poke in player.pokemon:
            for energy in poke.energy_cards_attached:
                if energy.energy_type == self.energy_type:
                    return True

        return False

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {f'opponent_damage_on_{self.energy_type}': -self.amount} if self.can_activate(player) else {}


class MitigateAllBenchDamagePassiveAbility(PassiveAbility):
    def __init__(self, name: str, description: str):
        super().__init__(name, description)

    def can_activate(self, player: Player) -> bool:
        return len(player.pokemon) > 1

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {'damage_done_to_bench': 0} if self.can_activate(player) else {}


class IncreasePokemonAttackDamagePassiveAbility(PassiveAbility):
    def __init__(self, name: str, description: str, amount: int, pokemon: str = None):
        super().__init__(name, description)
        self.amount = amount
        self.pokemon = pokemon

    def can_activate(self, player: Player, ability_owner: PokemonCard) -> bool:
        return ability_owner in player.pokemon[1:]

    def get_modifiers(self, player: Player, owner: PokemonCard) -> dict:
        return {"increase_pokemon_damage": [self.pokemon, self.amount]} if self.can_activate(player, owner) else {}
