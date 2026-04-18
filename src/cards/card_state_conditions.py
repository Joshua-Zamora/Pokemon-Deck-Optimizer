from cards.card import Card
from cards.pokemon_card import PokemonCard
from cards.trainer_card import TrainerCard
from core.player import Player

def is_pokemon_in_play(pokemon: PokemonCard, player: Player):
    return pokemon in player.pokemon

def is_pokemon_on_active_spot(player: Player, pokemon: PokemonCard):
    return player.pokemon[0] == pokemon


def is_pokemon_on_bench(player: Player, pokemon: PokemonCard):
    return True if pokemon in player.pokemon[1:] else False


def is_this_tool_attached(pokemon: PokemonCard, tool: str):
    return False if not pokemon.pokemon_tool_attached else pokemon.pokemon_tool_attached.name == tool


def is_this_energy_attached(pokemon: PokemonCard, energy: str):
    for energy_card in pokemon.energy_cards_attached:
        if energy_card.energy_type == energy:
            return True

    return False


def is_pokemon_ex(pokemon: PokemonCard):
    return False if not pokemon.suffix else pokemon.suffix.capitalize() == "EX"


def is_pokemon_v(pokemon: PokemonCard):
    return False if not pokemon.suffix else pokemon.suffix.capitalize() == "V"


def is_pokemon_basic(pokemon: PokemonCard):
    return pokemon.stage == 0


def is_pokemon_tera(pokemon: PokemonCard):
    return pokemon.suffix == "tera ex"


def is_card_trainer_type(card: Card):
    return type(card) == TrainerCard


def is_pokemon_evolved(pokemon: PokemonCard):
    return pokemon.stage > 0


def is_pokemon_poisoned(pokemon: PokemonCard):
    return pokemon.afflictions["poisoned"]


def is_pokemon_asleep(pokemon: PokemonCard):
    return pokemon.afflictions["asleep"]


def is_pokemon_burned(pokemon: PokemonCard):
    return pokemon.afflictions["burned"]


def is_pokemon_paralyzed(pokemon: PokemonCard):
    return pokemon.afflictions["paralyzed"]


def is_pokemon_confused(pokemon: PokemonCard):
    return pokemon.afflictions["confused"]


def is_ability_active(ability_name: str):
    return


def is_pokemon_full_health(pokemon: PokemonCard):
    return pokemon.damage_counters_attached == 0


def get_pokemon_team(pokemon: PokemonCard):
    if "TEAM ROCKET" in pokemon.name.capitalize():
        return "rocket"
    elif "GIOVANNI" in pokemon.name.capitalize():
        return "giovanni"
    elif "TEAM STAR" in pokemon.name.capitalize():
        return "star"
    else:
        return None


def get_amount_of_damage_inflicted(pokemon: PokemonCard):
    return pokemon.damage_counters_attached * 10


def get_number_of_damage_counters_attached(pokemon: PokemonCard):
    return pokemon.damage_counters_attached


def get_current_health_points(pokemon: PokemonCard):
    return pokemon.health_points - (pokemon.damage_counters_attached * 10)


def get_ability_name(pokemon: PokemonCard, ability_index: int = 0):
    return pokemon.abilities[ability_index].name


def get_pokemon_energy_type(pokemon: PokemonCard):
    return pokemon.energy_type


def get_number_of_energy_cards_attached(pokemon: PokemonCard):
    return len(pokemon.energy_cards_attached)


def get_energy_cards_attached(pokemon: PokemonCard):
    return pokemon.energy_cards_attached


def is_energy_type_attached(pokemon: PokemonCard, energy_type: str):
    for energy_card in pokemon.energy_cards_attached:
        if energy_card.energy_type == energy_type:
            return True

    return False


def get_number_of_energy_type_attached(pokemon: PokemonCard, energy_type: str):
    count = 0

    for energy_card in pokemon.energy_cards_attached:
        if energy_card.energy_type == energy_type:
            count += 1

    return count


def get_tool_attached(pokemon: PokemonCard):
    return pokemon.pokemon_tool_attached


def does_pokemon_card_have_an_ability(pokemon: PokemonCard):
    return True if pokemon.abilities else False


def does_pokemon_have_damage_counters(pokemon: PokemonCard):
    return pokemon.damage_counters_attached > 0


def does_pokemon_have_rule_box(pokemon: PokemonCard):
    return pokemon.suffix is not None


def did_pokemon_receive_damage(pokemon: PokemonCard):
    return pokemon.received_damage_this_turn


def which_pokemon_attacked_this_pokemon(pokemon: PokemonCard):
    return pokemon.pokemon_that_attacked


def would_pokemon_get_knocked_out_by_attack(pokemon: PokemonCard, damage_counters: int):
    return True if pokemon.current_health_points - (damage_counters * 10) <= 0 else False


def used_to_evolve_a_pokemon(pokemon: PokemonCard):
    return pokemon.stage > 0
