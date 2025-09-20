import pickle
from src.core.game import Game
from src.core.tcg_card import Card
from src.core.player import Player
from src.core.deck_builder import DeckBuilder


def main():
    card_regulations_allowed = ["G", "H", "I"]

    deck_builder = DeckBuilder(card_regulations_allowed,
                               games_per_evaluation=20,
                               population_size=50,
                               generations=30,
                               mutation_rate=0.1,
                               crossover_rate=0.7,
                               deck_size=60
                               )

    best_deck = deck_builder.optimize()

    print(best_deck)


if __name__ == "__main__":
    main()
