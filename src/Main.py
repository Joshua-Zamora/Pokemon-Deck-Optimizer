import pickle
from Game import Game
from Card import Card
from Player import Player


def main():
    cards = pickle.load(open('all_pokemon_cards.pkl', 'rb'))

    for i, (card_name, card) in enumerate(cards.items()):
        if i >= 5:
            break

        print(f"{card_name}: {card}")

    deck_one = construct_deck(cards)
    deck_two = construct_deck(cards)

    player_one = Player('Player One', deck_one)
    player_two = Player('Player Two', deck_two)

    game = Game(player_one, player_two)
    game.play()



def construct_deck(cards: dict[str, Card]) -> list[Card]:
    deck = []
    return deck


if __name__ == "__main__":
    main()