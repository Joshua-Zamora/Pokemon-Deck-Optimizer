from src.abilities.base import PassiveAbility
from src.cards.pokemon_card import PokemonCard
from src.core.player import Player


class DecreaseOpponentAttackDamageIfActivePassiveAbility(PassiveAbility):
    names: list[str] = ["Pressure"]
    descriptions: list[str] = [
        "As long as this Pokémon is in the Active Spot, attacks used by your opponent's Active Pokémon do 20 less damage (before applying Weakness and Resistance)."]

    def __init__(self, amount: int):
        self.amount = amount

    def can_activate(self, player: Player, ability_owner: PokemonCard) -> bool:
        return player.pokemon[0] == ability_owner

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {'opponent_damage': -self.amount} if self.can_activate(player, ability_owner) else {}


class DecreaseOpponentAttackDamagePassiveAbility(PassiveAbility):
    names: list[str] = ["Protective Bell", "Arm Thrust Practice"]
    descriptions: list[str] = [
        "All of your Pokémon take 10 less damage from attacks from your opponent's Pokémon (after applying Weakness and Resistance)."]

    def __init__(self, amount: int):
        self.amount = amount

    def can_activate(self) -> bool:
        return True

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {'opponent_damage': -self.amount}


class DecreaseOpponentAttackDamageIfOnBenchPassiveAbility(PassiveAbility):
    names: list[str] = ["Stone Palace"]
    descriptions: list[str] = [
        "As long as this Pokémon is on your Bench, all of your Steven's Pokémon take 30 less damage from attacks from your opponent's Pokémon (after applying Weakness and Resistance). The effect of Stone Palace doesn't stack."]

    def __init__(self, amount: int, pokemon_restriction: str):
        self.amount = amount
        self.pokemon_restriction = pokemon_restriction

    def can_activate(self, player: Player, ability_owner: PokemonCard) -> bool:
        return ability_owner in player.pokemon[1:]

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {f"opponent_damage_on_{self.pokemon_restriction}": -self.amount} if self.can_activate(player,
                                                                                                     ability_owner) else {}


class DecreaseOpponentAttackDamageOnEnergiesAttachedPassiveAbility(PassiveAbility):
    names: list[str] = ["Gear Coating"]
    descriptions: list[str] = [
        "All of your Pokémon that have any {M} Energy attached take 20 less damage from attacks from your opponent's Pokémon (after applying Weakness and Resistance)."]

    def __init__(self, energy_type: str, amount: int):
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


class DecreaseOpponentAttackDamageOnBasicPokemonIfPokemonInPlayPassiveAbility(PassiveAbility):
    names: list[str] = ["Curly Wall"]
    descriptions: list[str] = [
        "As long as you have at least 1 other Bouffalant in play, all of your Basic {C} Pokémon take 60 less damage from attacks from your opponent's Pokémon (after applying Weakness and Resistance). The effect of Curly Wall doesn't stack."]

    def __init__(self, amount: int, pokemon_restriction: str):
        self.amount = amount
        self.pokemon_restriction = pokemon_restriction

    def can_activate(self, player: Player) -> bool:
        count = 0

        for poke in player.pokemon:
            if self.pokemon_restriction in poke.name:
                count += 1

        return count > 1

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {f"opponent_damage_on_basic_pokemon_if_{self.pokemon_restriction}": -self.amount} if self.can_activate(
            player) else {}


class MitigateAllBenchDamagePassiveAbility(PassiveAbility):
    names: list[str] = ["Adverse Weather"]
    descriptions: list[str] = [
        "As long as this Pokémon is in the Active Spot, prevent all damage done to your Benched Pokémon by attacks from your opponent's Pokémon."]

    def can_activate(self, player: Player) -> bool:
        return len(player.pokemon) > 1

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {'mitigate_all_damage_to_bench': True} if self.can_activate(player) else {}


class MitigateAllDamageToPokemonPassiveAbility(PassiveAbility):
    names: list[str] = ["Plume Protection"]
    descriptions: list[str] = [
        "As long as this Pokémon is on your Bench, prevent all damage done to this Pokémon by attacks from your opponent's Pokémon."]

    def can_activate(self, player: Player, ability_owner: PokemonCard) -> bool:
        return ability_owner in player.pokemon[1:]

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {'mitigate_all_damage_to_this_pokemon': True} if self.can_activate(player, ability_owner) else {}


class MitigateAllDamageAndEffectsToPokemonPassiveAbility(PassiveAbility):
    class MitigateAllDamageToPokemonPassiveAbility(PassiveAbility):
        names: list[str] = ["Storehouse Hideaway", "So Submerged"]
        descriptions: list[str] = [
            "As long as this Pokémon is on your Bench, prevent all damage from and effects of attacks from your opponent's Pokémon done to this Pokémon."]

        def can_activate(self, player: Player, ability_owner: PokemonCard) -> bool:
            return ability_owner in player.pokemon[1:]

        def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
            return {'mitigate_all_damage_and_effects_to_this_pokemon': True} if self.can_activate(player,
                                                                                                  ability_owner) else {}


class IncreasePokemonAttackDamageForPokemonPassiveAbility(PassiveAbility):
    names: list[str] = ["Cheering Bone"]
    descriptions: list[str] = [
        "As long as this Pokémon is on your Bench, attacks used by your Marowak do 30 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance)."]

    def __init__(self, amount: int, pokemon: str = None):
        self.amount = amount
        self.pokemon = pokemon

    def can_activate(self, player: Player, ability_owner: PokemonCard) -> bool:
        return ability_owner in player.pokemon[1:]

    def get_modifiers(self, player: Player, owner: PokemonCard) -> dict:
        return {f"increase_pokemon_damage_for_{self.pokemon}": self.amount} if self.can_activate(player, owner) else {}
