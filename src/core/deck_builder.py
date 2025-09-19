import pickle
import random
import numpy as np
from typing import List
from src.core.card import Card
from src.core.player import Player
from src.core.game import Game


class DeckBuilder:
    card_pool = []

    def __init__(self, regulations: list[str] = None, games_per_evaluation: int = 20, population_size: int = 50,
                 generations: int = 30, mutation_rate: float = 0.1, crossover_rate: float = 0.7, deck_size: int = 60):
        self.regulations = regulations
        self.games_per_evaluation = games_per_evaluation
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.deck_size = deck_size
        self.load_cards()
        self.pool_size = len(self.card_pool)

    def load_cards(self):
        for reg in self.regulations:
            with open(f"./data/cards/filtered_by_regulation/{reg.capitalize()}.pkl", 'rb') as f:
                self.card_pool.extend(pickle.load(f))

    def generate_random_deck(self) -> List[int]:
        """Generate a random valid deck."""
        deck = [0] * self.pool_size
        remaining = self.deck_size

        while remaining > 0:
            idx = random.randint(0, self.pool_size - 1)

            if deck[idx] < 4:
                deck[idx] += 1
                remaining -= 1

        # Enforce some validity: e.g., at least 1 basic Pokémon (simplified check)
        basics = sum(deck[i] for i in range(self.pool_size) if self.card_pool[i].is_basic_pokemon)

        if basics == 0:
            return self.generate_random_deck()  # Retry

        return deck

    def deck_to_card_list(self, deck: List[int]) -> List[Card]:
        """Convert count list to actual deck list for Player."""
        card_list = []

        for i, count in enumerate(deck):
            card_list.extend([self.card_pool[i]] * count)

        random.shuffle(card_list)

        return card_list

    def evaluate_deck(self, deck: List[int], opponent_deck: List[Card]) -> float:
        """"""
        wins = 0
        candidate_deck_list = self.deck_to_card_list(deck)

        for _ in range(self.games_per_evaluation):
            player_one = Player("Candidate", candidate_deck_list)
            player_two = Player("Opponent", opponent_deck)

            winner = Game(player_one, player_two).play()

            if winner == player_one:
                wins += 1

        return wins / self.games_per_evaluation

    def selection(self, population: List[List[int]], scores: List[float]) -> List[List[int]]:
        """Tournament selection: select parents."""
        selected = []

        for _ in range(self.population_size):
            candidates = random.sample(list(zip(population, scores)), 3)
            selected.append(max(candidates, key=lambda x: x[1])[0])

        return selected

    def crossover(self, parent1: List[int], parent2: List[int]) -> List[int]:
        """Single-point crossover, then normalize to DECK_SIZE."""
        point = random.randint(1, self.pool_size - 1)
        child = parent1[:point] + parent2[point:]
        total = sum(child)

        if total != self.deck_size:
            diff = self.deck_size - total

            while diff != 0:
                idx = random.randint(0, self.pool_size - 1)

                if diff > 0 and child[idx] < 4:
                    child[idx] += 1
                    diff -= 1
                elif diff < 0 < child[idx]:
                    child[idx] -= 1
                    diff += 1

        return child

    def mutate(self, deck: List[int]) -> List[int]:
        """Swap counts between cards."""
        if random.random() < self.mutation_rate:
            idx1, idx2 = random.sample(range(self.pool_size), 2)

            if deck[idx1] > 0 and deck[idx2] < 4:
                deck[idx1] -= 1
                deck[idx2] += 1

        return deck

    def optimize(self) -> List[int]:
        """Uses a Genetic Algorthm to find an optimal deck."""
        population_a = [self.generate_random_deck() for _ in range(self.population_size)]
        population_b = [self.generate_random_deck() for _ in range(self.population_size)]

        for gen in range(self.generations):
            fitness_scores = [self.evaluate_deck(deck_one, deck_two) for deck_one, deck_two in
                              (population_a, population_b)]
            print(f"Generation {gen}: Best fitness {max(fitness_scores)}")

            parents = self.selection(population_a, fitness_scores)
            next_pop = []

            for i in range(0, self.population_size, 2):
                parent_one, parent_two = parents[i], parents[i + 1] if i + 1 < self.population_size else parents[0]

                if random.random() < self.crossover_rate:
                    child_one = self.crossover(parent_one[:], parent_two[:])
                    child_two = self.crossover(parent_two[:], parent_one[:])
                else:
                    child_one, child_two = parent_one[:], parent_two[:]

                next_pop.extend([self.mutate(child_one), self.mutate(child_two)])

            population_a = next_pop[:self.population_size]  # Elitism optional: keep best

        best_idx = np.argmax(
            [self.evaluate_deck(deck_one, deck_two) for deck_one, deck_two in (population_a, population_b)])

        return population_a[best_idx]
