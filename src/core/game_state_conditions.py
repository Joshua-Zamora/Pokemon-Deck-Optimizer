from core.game import Game
from core.player import Player
from cards.card_state_conditions import *


def are_any_pokemon_ex_in_play_for_player(player: Player):
    for pokemon in player.pokemon:
        if is_pokemon_ex(pokemon):
            return True

    return False


def are_any_pokemon_v_in_play_for_player(player: Player):
    for pokemon in player.pokemon:
        if is_pokemon_v(pokemon):
            return True

    return False


def are_any_pokemon_tera_in_play_for_player(player: Player):
    for pokemon in player.pokemon:
        if is_pokemon_tera(pokemon):
            return True

    return False


def is_pokemon_checkup(game: Game):
    return game.in_pokemon_checkup


def is_players_first_turn(player: Player):
    return player.is_first_turn


def is_card_in_discard_pile(card: Card, player: Player):
    return card in player.discard_pile


def which_pokemon_in_play_have_energy_attached(player: Player):
    pokemon_list = []

    for pokemon in player.pokemon:
        if pokemon.energy_cards_attached:
            pokemon_list.append(pokemon)

    return pokemon_list


def which_pokemon_in_hand_have_abilities(player: Player):
    pokemon_list = []

    for pokemon in player.hand:
        if pokemon.abilities:
            pokemon_list.append(pokemon)

    return pokemon_list


def has_supporter_card_been_played_by_opponent(opponent: Player):
    return opponent.supporter_card_played


def has_energy_card_been_attached_to_any_pokemon(player: Player):
    for pokemon in player.pokemon:
        if pokemon.energy_cards_attached:
            return True

    return False


def has_item_card_been_played_by_opponent(opponent: Player):
    return opponent.item_card_played


def get_number_of_benched_pokemon(player: Player):
    return len(player.pokemon[1:])


def get_cards_in_discard_pile(player: Player):
    return player.discard_pile


def get_number_cards_in_discard_pile_by_name(player: Player, name: str):
    count = 0
    for card in player.discard_pile:
        if name in card.name:
            count += 1

    return count


def get_pokemon_that_had_energy_attached_to_it(player: Player):
    return


def get_pokemon_that_just_evolved(player: Player):
    pokemon_list = []
    for pokemon in player.pokemon:
        if pokemon.energy_cards_attached:
            pokemon_list.append(pokemon)

    return pokemon_list


def get_number_of_cards_in_play_by_team_type(player: Player, team_type: str):
    count = 0
    for pokemon in player.pokemon:
        if get_pokemon_team(pokemon) == team_type:
            count += 1

    return count


def get_pokemon_that_is_now_active(player: Player):
    return player.pokemon[0]


def get_number_of_prize_cards_taken(player: Player):
    return abs(len(player.prize_cards) - 6)


def get_number_of_prize_cards_remaining(player: Player):
    return len(player.prize_cards)


def get_number_of_cards_in_hand(player: Player):
    return len(player.hand)


def has_player_turn_ended(player: Player):
    return player.has_turn_ended


def does_player_go_first(game: Game):
    return game.first_player_to_move
