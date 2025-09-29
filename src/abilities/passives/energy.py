from src.abilities.base import PassiveAbility
from src.cards.pokemon_card import PokemonCard
from src.core.player import Player


class IncreaseOpponentAttackCostPassiveAbility(PassiveAbility):
    names: list[str] = ["Dazzling Gaze", "Quaking Zone"]
    descriptions: list[str] = [
        "As long as this Pokémon is in the Active Spot, attacks used by your opponent's Active Pokémon cost {C} more."]

    def __init__(self, extra_cost: list):
        self.extra_cost = extra_cost

    def can_activate(self, player: Player, ability_owner: PokemonCard) -> bool:
        return player.pokemon[0] == ability_owner

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {'attack_cost_opponent': self.extra_cost} if self.can_activate(player, ability_owner) else {}


class IncreaseOpponentAttackCostOfBasicPokemonPassiveAbility(PassiveAbility):
    names: list[str] = ["Primal Root"]
    descriptions: list[str] = [
        "As long as this Pokémon is in the Active Spot, attacks used by your opponent's Basic Pokémon cost {C} more."]

    def __init__(self, extra_cost: list):
        self.extra_cost = extra_cost

    def can_activate(self, player: Player, ability_owner: PokemonCard) -> bool:
        return player.pokemon[0] == ability_owner

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {'opponent_attack_cost_basic_pokemon': self.extra_cost} if self.can_activate(player,
                                                                                            ability_owner) else {}


class ChangePokemonEnergyTypePassiveAbility(PassiveAbility):
    names: list[str] = ["Double Type"]
    descriptions: list[str] = ["As long as this Pokémon is in play, it is {G} and {R} type."]

    def __init__(self, energy_types: list[str]):
        self.energy_types = energy_types

    def can_activate(self, player: Player, ability_owner: PokemonCard):
        return ability_owner in player.pokemon

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {'pokemon_energy_types': self.energy_types} if self.can_activate(player, ability_owner) else {}


class NoRetreatCostForEnergyTypePokemonPassiveAbility(PassiveAbility):
    names: list[str] = ["Metal Bridge", "Lunar Zone"]
    descriptions: list[str] = ["All of your Pokémon that have {M} Energy attached have no Retreat Cost.",
                               "All of your Pokémon that have {P} Energy attached have no Retreat Cost."]

    def __init__(self, energy_type: str):
        self.energy_type = energy_type

    def can_activate(self, player: Player):
        for poke in player.pokemon:
            for energy in poke.energy_cards_attached:
                if energy.energy_type == self.energy_type:
                    return True

        return False

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {f"retreat_cost_for_pokemon_with_{self.energy_type}_attached": 0} if self.can_activate(player) else {}


class DecreaseRetreatCostIfOnBenchPassiveAbility(PassiveAbility):
    names: list[str] = ["Secret Forest Path"]
    descriptions: list[str] = [
        "As long as this Pokémon is on your Bench, your Active Pokémon's Retreat Cost is {C}{C} less."]

    def __init__(self, amount: int, energy_type: str):
        self.amount = amount
        self.energy_type = energy_type

    def can_activate(self, player: Player, ability_owner: PokemonCard):
        return ability_owner in player.pokemon[1:]

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {f"decrease_retreat_cost_by_{self.energy_type}": self.amount} if self.can_activate(player,
                                                                                                  ability_owner) else {}


class OpponentsActivePokemonCantRetreatPassiveAbility(PassiveAbility):
    names: list[str] = ["Primordial Tentacles"]
    descriptions: list[str] = [
        "As long as this Pokémon is in the Active Spot, your opponent's Active Pokémon can't retreat."]

    def can_activate(self, player: Player, ability_owner: PokemonCard) -> bool:
        return ability_owner == player.pokemon[0]

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {"opponent_can_retreat": False} if self.can_activate(player, ability_owner) else {}


class ChangePokemonEnergyTypeIfToolAttachedPassiveAbility(PassiveAbility):
    names: list[str] = ["Dual Core"]
    descriptions: list[str] = [
        "As long as this Pokémon has a Future Booster Energy Capsule attached, it is {F} and {M} type."]

    def __init__(self, energy_type: list[str], tool: str):
        self.energy_type = energy_type
        self.tool = tool

    def can_activate(self, ability_owner: PokemonCard):
        return self.tool in ability_owner.pokemon_tool_attached.name

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {"pokemon_energy_types": self.energy_type} if self.can_activate(ability_owner) else {}


class AttacksCostLessForCardInDiscardPilePassiveAbility(PassiveAbility):
    names: list[str] = ["Food Prep"]
    descriptions: list[str] = ["Attacks used by this Pokémon cost {C} less for each Kofu card in your discard pile."]

    def __init__(self, energy_type: str, amount: int, pokemon_restriction: str):
        self.energy_type = energy_type
        self.amount = amount
        self.pokemon_restriction = pokemon_restriction

    def can_activate(self, player: Player) -> bool:
        for card in player.discard_pile:
            if self.pokemon_restriction in card.name:
                return True

        return False

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {
            f"attack_cost_of_this_card_is_{self.energy_type}_less_for_each{self.pokemon_restriction}": self.amount} if self.can_activate(
            player) else {}


class AttacksCostLessForEachOpponentBenchedPokemonPassiveAbility(PassiveAbility):
    names: list[str] = ["Hustle Play"]
    descriptions: list[str] = [
        "Attacks used by this Pokémon cost {C} less for each of your opponent's Benched Pokémon."]

    def __init__(self, energy_type: str, amount: int):
        self.energy_type = energy_type
        self.amount = amount

    def can_activate(self, player: Player) -> bool:
        return len(player.opponent.pokemon) > 1

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {
            f"attack_cost_of_this_card_is_{self.energy_type}_less_for_each_opponent_benched": self.amount} if self.can_activate(
            player) else {}


class AttackCostsLessForEachPrizeCardTakenPassiveAbility(PassiveAbility):
    names: list[str] = ["Seasoned Skill"]
    descriptions: list[str] = ["Blood Moon used by this Pokémon costs {C} less for each Prize card your opponent has taken."]

    def __init__(self, energy_type: str, amount: int, attack: str):
        self.energy_type = energy_type
        self.amount = amount
        self.attack = attack

    def can_activate(self, player: Player) -> bool:
        return len(player.prize_cards) < 6

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {f"attack_{self.attack}_cost_less": self.amount} if self.can_activate(player) else {}
