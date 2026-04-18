from cards.abilities.base import PassiveAbility
from src.cards.pokemon_card import PokemonCard
from src.core.player import Player


class BasicPokemonInPlayHaveNoAbilities(PassiveAbility):
    names: list[str] = ["Mischievous Lock", "Fettered in Misfortune"]
    descriptions: list[str] = [
        "As long as this Pokémon is in the Active Spot, Basic Pokémon in play (both yours and your opponent's) have no Abilities, except for Mischievous Lock.",
        "Basic Pokémon V in play (both yours and your opponent's) have no Abilities."]

    def __init__(self, pokemon_exception: str = None, pokemon_restriction: str = None,
                 must_be_active: bool = False) -> None:
        self.pokemon_exception = pokemon_exception
        self.pokemon_restriction = pokemon_restriction
        self.must_be_active = must_be_active

    def can_activate(self, player: Player, ability_owner: PokemonCard):
        if self.must_be_active and ability_owner != player.pokemon[0]:
            return False

        if self.pokemon_restriction == "v":
            for poke in player.pokemon:
                if poke.pokemon_category == "basic" and poke.suffix == "v":
                    return True

            for poke in player.opponent.pokemon:
                if poke.pokemon_category == "basic" and poke.suffix == "v":
                    return True
        else:
            for poke in player.pokemon:
                if poke.pokemon_category == "basic":
                    return True

            for poke in player.opponent.pokemon:
                if poke.pokemon_category == "basic":
                    return True

        return False

    def activate(self, player: Player, ability_owner: PokemonCard):
        if self.pokemon_exception:
            return {f'basic_pokemon_no_abilities_except_{self.pokemon_exception}': True} if self.can_activate(player,
                                                                                                              ability_owner) else {}
        else:
            return {f"basic_pokemon_v_no_abilities": True} if self.can_activate(player, ability_owner) else {}


class PokemonWIthRuleBoxHaveNoAbilitiesExceptFuture(PassiveAbility):
    names: list[str] = ["Initialization"]
    descriptions: list[str] = [
        "As long as this Pokémon is in the Active Spot, Pokémon with a Rule Box in play (both yours and your opponent's) have no Abilities, except for Future Pokémon. (Pokémon ex, Pokémon V, etc. have Rule Boxes.)"]

    def can_activate(self, player: Player, ability_owner: PokemonCard):
        if ability_owner != player.pokemon[0]:
            return False

        for poke in player.pokemon:
            if poke.suffix:
                return True

        for poke in player.opponent.pokemon:
            if poke.suffix:
                return True

        return False

    def activate(self, player: Player, ability_owner: PokemonCard):
        return {'pokemon_with_rule_box_no_abilities_except_future': True} if self.can_activate(player,
                                                                                               ability_owner) else {}


class OpponentsActivePokemonHaveNoAbilitiesPassiveAbility(PassiveAbility):
    names: list[str] = ["Midnight Fluttering"]
    descriptions: list[str] = [
        "As long as this Pokémon is in the Active Spot, your opponent's Active Pokémon has no Abilities, except for Midnight Fluttering."]

    def __init__(self, pokemon_restriction: str):
        self.pokemon_restriction = pokemon_restriction

    def can_activate(self, player: Player, ability_owner: PokemonCard):
        return ability_owner == player.pokemon[0]

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {f"opponent_active_have_no_abilities_except_{self.pokemon_restriction}": True} if self.can_activate(
            player, ability_owner) else {}


class PokemonWithDamageHaveNoAbilitiesPassiveAbility(PassiveAbility):
    names: list[str] = ["Cursed Land"]
    descriptions: list[str] = [
        "As long as this Pokémon is in the Active Spot, your opponent's Pokémon in play that have any damage counters on them have no Abilities, except for Pokémon ex."]

    def __init__(self, pokemon_restriction: str):
        self.pokemon_restriction = pokemon_restriction

    def can_activate(self, player: Player, ability_owner: PokemonCard):
        return ability_owner == player.pokemon[0]

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {f"opponent_pokemon_no_abilities_except_{self.pokemon_restriction}": True} if self.can_activate(player,
                                                                                                               ability_owner) else {}


class BenchedStageTwoPokemonHaveNoAbilitiesPassiveAbility(PassiveAbility):
    names: list[str] = ["Sticky Bind"]
    descriptions: list[str] = [
        "As long as this Pokémon is on your Bench, Benched Stage 2 Pokémon (both yours and your opponent's) have no Abilities."]

    def can_activate(self, player: Player, ability_owner: PokemonCard):
        return ability_owner in player.pokemon[1:]

    def get_modifiers(self, player: Player, ability_owner: PokemonCard) -> dict:
        return {"bench_stage_two_no_abilities": True} if self.can_activate(player, ability_owner) else {}
