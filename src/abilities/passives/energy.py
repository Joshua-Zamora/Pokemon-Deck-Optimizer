from src.abilities.base import PassiveAbility
from src.cards.pokemon_card import PokemonCard
from src.core.player import Player


class IncreaseOpponentAttackCostPassiveAbility(PassiveAbility):
    def __init__(self, name: str, description: str, extra_cost: list):
        super().__init__(name, description)
        self.extra_cost = extra_cost

    def can_activate(self, player: Player, ability_owner: PokemonCard) -> bool:
        return player.pokemon[0] == ability_owner

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {'attack_cost_opponent': self.extra_cost} if self.can_activate(player, ability_owner) else {}


class IncreaseOpponentAttackCostOfBasicPokemonPassiveAbility(PassiveAbility):
    def __init__(self, name: str, description: str, extra_cost: list):
        super().__init__(name, description)
        self.extra_cost = extra_cost

    def can_activate(self, player: Player, ability_owner: PokemonCard) -> bool:
        return player.pokemon[0] == ability_owner

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {'opponent_attack_cost_basic_pokemon': self.extra_cost} if self.can_activate(player,
                                                                                            ability_owner) else {}


class ChangePokemonEnergyTypePassiveAbility(PassiveAbility):
    def __init__(self, name: str, description: str, energy_types: list[str]):
        super().__init__(name, description)
        self.energy_types = energy_types

    def can_activate(self, player: Player, ability_owner: PokemonCard):
        return ability_owner in player.pokemon

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {'pokemon_energy_types': self.energy_types} if self.can_activate(player, ability_owner) else {}


class NoRetreatCostForEnergyTypePokemonPassiveAbility(PassiveAbility):
    def __init__(self, name: str, description: str, energy_type: str):
        super().__init__(name, description)
        self.energy_type = energy_type

    def can_activate(self, player: Player):
        for poke in player.pokemon:
            for energy in poke.energy_cards_attached:
                if energy.energy_type == self.energy_type:
                    return True

        return False

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {f"retreat_cost_for_pokemon_with_{self.energy_type}_attached": 0} if self.can_activate(player) else {}


class ChangePokemonEnergyTypeIfToolAttachedPassiveAbility(PassiveAbility):
    def __init__(self, name: str, description: str, energy_type: list[str], tool: str):
        super().__init__(name, description)
        self.energy_type = energy_type
        self.tool = tool

    def can_activate(self, ability_owner: PokemonCard):
        return self.tool in ability_owner.pokemon_tool_attached.name

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {"pokemon_energy_types": self.energy_type} if self.can_activate(ability_owner) else {}
