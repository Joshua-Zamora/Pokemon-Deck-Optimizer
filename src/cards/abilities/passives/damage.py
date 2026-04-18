from cards.abilities.base import PassiveAbility
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


class DecreaseOpponentAttackDamageIfFullHPPassiveAbility(PassiveAbility):
    names: list[str] = ["Crimson Armor'"]
    descriptions: list[str] = [
        "If this Pokémon has full HP, it takes 80 less damage from attacks from your opponent's Pokémon (after applying Weakness and Resistance)."]

    def __init__(self, amount: int):
        self.amount = amount

    def can_activate(self, ability_owner: PokemonCard) -> bool:
        return ability_owner.damage_counters_attached == 0

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {"opponent_damage": -self.amount} if self.can_activate(ability_owner) else {}


class IncreaseDamageResistanceIfAnyEnergyAttachedPassiveAbility(PassiveAbility):
    names: list[str] = ["Rock Armor"]
    descriptions: list[str] = [
        "If this Pokémon has any Energy attached, it takes 30 less damage from attacks (after applying Weakness and Resistance)."]

    def __init__(self, amount: int):
        self.amount = amount

    def can_activate(self, ability_owner: PokemonCard) -> bool:
        return ability_owner.energy_cards_attached is not None and len(ability_owner.energy_cards_attached) > 0

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {"increase_damage_resistance": self.amount} if self.can_activate(ability_owner) else {}


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


class IncreasePokemonAttackDamageIfOpponentHasAbilityPassiveAbility(PassiveAbility):
    names: list[str] = ["Compound Eyes"]
    descriptions: list[str] = [
        "Attacks used by this Pokémon do 50 more damage to your opponent's Active Pokémon that has an Ability (before applying Weakness and Resistance)."]

    def __init__(self, amount: int):
        self.amount = amount

    def can_activate(self, player: Player) -> bool:
        return len(player.opponent.pokemon[0].abilities) != 0

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {"increase_damage_if_opponent_has_ability": self.amount} if self.can_activate(player) else {}


class IncreaseDamageOnNumDamageCountersAttachedPassiveAbility(PassiveAbility):
    names: list[str] = ["Lose Cool"]
    descriptions: list[str] = [
        "If this Pokémon has 2 or more damage counters on it, attacks used by this Pokémon do 120 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance)."]

    def __init__(self, damage_counters: int, amount: int):
        self.damage_counters = damage_counters
        self.amount = amount

    def can_activate(self, player: Player) -> bool:
        return player.pokemon[0].damage_counters_attached >= self.damage_counters

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {"increase_damage": self.amount} if self.can_activate(player) else {}


class IncreasePokemonAttackDamageForPokemonPassiveAbility(PassiveAbility):
    names: list[str] = ["Cheer On to Glory", "Cobalt Command", "Victory Cheer", "Cheering Bone", "Extra Helpings",
                        "Regal Cheer", "Primal Knowledge", "Sunny Day"]
    descriptions: list[str] = [
        "Attacks used by your Cynthia's Pokémon do 30 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
        "Attacks used by your Future Pokémon, except any Iron Crown ex, do 20 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
        "Attacks used by your Evolution {R} Pokémon do 10 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
        "As long as this Pokémon is on your Bench, attacks used by your Marowak do 30 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
        "Attacks used by your Hop's Pokémon do 30 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance). The effect of Extra Helpings doesn't stack.",
        "Attacks used by your Pokémon do 20 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
        "Attacks used by your Pokémon do 30 more damage to your opponent's Active Evolution Pokémon (before applying Weakness and Resistance).",
        "Attacks used by your {G} Pokémon and {R} Pokémon do 20 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance)."]

    def __init__(self, amount: int, energy_types: list[str] = None, pokemon_restriction: str = None,
                 pokemon_exception: str = None, must_be_on_bench: bool = False, doesnt_stack: bool = False,
                 against_evolved: bool = False, your_evolved: bool = False):
        if energy_types is None:
            energy_types = []
        self.amount = amount
        self.energy_types = energy_types
        self.pokemon_restriction = pokemon_restriction
        self.pokemon_exception = pokemon_exception
        self.must_be_on_bench = must_be_on_bench
        self.doesnt_stack = doesnt_stack
        self.against_evolved = against_evolved
        self.your_evolved = your_evolved

    def can_activate(self, player: Player, ability_owner: PokemonCard) -> bool:
        if self.pokemon_restriction:
            for poke in player.pokemon:
                if self.pokemon_restriction in poke.name:
                    return True
        elif self.your_evolved:
            for poke in player.pokemon:
                if poke.stage > 0 and poke.energy_type in self.energy_types:
                    return True
        elif self.must_be_on_bench:
            return ability_owner in player.pokemon[1:]
        elif self.pokemon_exception == "iron crown":
            for poke in player.pokemon:
                if "iron treads" in poke.name or "iron valiant" in poke.name:
                    return True
        elif self.against_evolved:
            for poke in player.opponent.pokemon:
                if poke.stage > 0:
                    return True
        elif self.energy_types:
            for poke in player.pokemon:
                if poke.energy_type in self.energy_types:
                    return True
        elif self.amount:
            return True

        return False

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        if self.your_evolved:
            return {"increase_pokemon_damage_if_evolved": self.amount} if self.can_activate(player,
                                                                                            ability_owner) else {}
        elif self.pokemon_exception:
            return {f"increase_pokemon_damage_for_future": self.amount} if self.can_activate(player,
                                                                                             ability_owner) else {}
        elif self.pokemon_restriction:
            return {f"increase_pokemon_damage_for_{self.pokemon_restriction}": self.amount} if self.can_activate(
                player, ability_owner) else {}
        elif self.energy_types:
            return {f"increase_pokemon_damage_for_{self.energy_types}": self.amount} if self.can_activate(player,
                                                                                                          ability_owner) else {}
        else:
            return {"increase_pokemon_damage": self.amount} if self.can_activate(player, ability_owner) else {}


class OpponentEffectsNegatedFromAttackDamagePassiveAbility(PassiveAbility):
    names: str = ["Azure Seas"]
    descriptions: str = [
        "Damage from attacks used by this Pokémon isn't affected by any effects on your opponent's Active Pokémon."]

    def can_activate(self) -> bool:
        return True

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {"negate_effects_to_attacks": True} if self.can_activate() else {}
