import asyncio
import pickle
import urllib.error
from dataclasses import asdict
from pprint import pprint

from scipy.linalg import svd
from tcgdexsdk import TCGdex, Query
import numpy as np
import scipy.spatial.distance as dist
from scipy.cluster import hierarchy
import pandas as pd  # Optional for nicer output

sdk = TCGdex('en')


async def get_all_card_resumes_by_mark(mark):
    all_cards = []
    page = 1
    has_more = True
    max_retries = 15  # Adjustable; number of retry attempts

    while has_more:
        retries = 0
        success = False
        cards = []
        while retries < max_retries and not success:
            try:
                cards = await sdk.card.list(
                    Query().equal("regulationMark", mark).paginate(page=page, itemsPerPage=250)
                )  # API maximum per page
                success = True
            except (TimeoutError,
                    ConnectionError) as e:  # Catch relevant exceptions; add more if needed (e.g., from tcgdexsdk)
                retries += 1
                delay = 2 ** retries  # Exponential backoff (2s, 4s, 8s, etc.)
                print(f"Error fetching page {page}: {e}. Retrying {retries}/{max_retries} after {delay}s...")
                await asyncio.sleep(delay)

        if not success:
            raise RuntimeError(f"Failed to fetch page {page} after {max_retries} retries.")

        all_cards.extend(cards)
        has_more = len(cards) == 250
        print(f"Fetched page {page} with {len(cards)} cards")
        page += 1

    return all_cards


async def save_cards(file, cards):
    with open(file, 'wb') as f:
        pickle.dump(cards, f)

    print(f"Saved {len(cards)} cards to {file}")


def read_cards(file):
    with open(file, 'rb') as f:
        cards = pickle.load(f)

    return cards


def sort_cards_into_pickle_files(all_cards):
    card_dict = {}

    for card in all_cards:
        if card.regulationMark not in card_dict:
            print(card.regulationMark)
            card_dict[card.regulationMark] = [card]
        else:
            card_dict[card.regulationMark].append(card)

    for reg_mark, cards in card_dict.items():
        with open(f"{reg_mark}.pkl", 'wb') as f:
            pickle.dump(cards, f)


async def get_actual_card_data_from_resumes(resumes):
    batch_size = 50  # Optimal batch size for API performance; adjust based on rate limits
    max_retries = 15  # Same as above
    full_cards = []

    for i in range(0, len(resumes), batch_size):
        batch = resumes[i:i + batch_size]
        batch_results = []
        for resume in batch:  # Per-ID retry loop (since gather doesn't handle individual failures well)
            retries = 0
            success = False
            while retries < max_retries and not success:
                try:
                    card = await sdk.card.get(resume.id)
                    batch_results.append(card)
                    success = True
                except (TimeoutError, ConnectionError, urllib.error.HTTPError, urllib.error.URLError) as e:
                    if isinstance(e, urllib.error.HTTPError) and e.code == 404:
                        print(f"Card {resume.id} not found (404)—skipping.")
                        print(resume.name)
                        success = True  # Exit retry loop without appending or raising
                        break  # Optional: Immediately skip to the next card
                    else:
                        retries += 1
                        delay = 2 ** retries
                        print(
                            f"Error fetching card {resume.id}: {e}. Retrying {retries}/{max_retries} after {delay}s...")
                        await asyncio.sleep(delay)
            if not success:
                print(f"Failed to fetch card {resume.id} after {max_retries} retries—skipping.")

        full_cards.extend(batch_results)
        print(f"Fetched batch {i // batch_size + 1} with {len(batch_results)} full cards")

    return full_cards


def print_card_info(card):
    card_dict = asdict(card)
    pprint(card_dict, indent=4, width=80, sort_dicts=False)


def get_card_pool_specifics(cards):
    num_abilities = 0
    abilities = {}
    attacks = {}
    health_points = {}
    damages = {}
    stages = {}
    num_attacks = 0
    min_retreat_cost = 5
    max_retreat_cost = 0

    for card in cards:
        if card.abilities:
            num_abilities += len(card.abilities)

            for ability in card.abilities:
                if ability.effect not in abilities:
                    abilities[ability.effect] = 1
                else:
                    abilities[ability.effect] += 1
        if card.hp:
            if card.hp not in health_points:
                health_points[card.hp] = [card.hp, card.id, card.name]
            else:
                health_points[card.hp].append([card.hp, card.id, card.name])
        if card.stage:
            if card.stage not in stages:
                stages[card.stage] = 1
            else:
                stages[card.stage] += 1
        if card.attacks:
            num_attacks += len(card.attacks)

            for attack in card.attacks:
                if attack.effect not in attacks:
                    attacks[attack.effect] = 1
                else:
                    attacks[attack.effect] += 1

                if attack.damage:
                    if type(attack.damage) is not str:
                        if attack.damage not in damages:
                            damages[attack.damage] = [attack.damage, attack.cost, card.id, card.name]
                        else:
                            damages[attack.damage].append([attack.damage, attack.cost, card.id, card.name])

        if card.retreat:
            if int(card.retreat) < min_retreat_cost:
                min_retreat_cost = int(card.retreat)
            if int(card.retreat) > max_retreat_cost:
                max_retreat_cost = int(card.retreat)

    print(f"Number of abilities: {num_abilities}")
    print(f"Number of unique abilities: {len(abilities)}")
    print(f"Most common ability: {max(abilities, key=abilities.get)}, {abilities[max(abilities, key=abilities.get)]}")
    print(f"Least common ability: {min(abilities, key=abilities.get)}, {abilities[min(abilities, key=abilities.get)]}")
    print(f"Number of attacks: {num_attacks}")
    print(f"Number of unique attack effects: {len(attacks)}")
    print(f"Most common attack effect: {max(attacks, key=attacks.get)}, {attacks[max(attacks, key=attacks.get)]}")
    non_none_attacks = {k: v for k, v in attacks.items() if k is not None}
    if non_none_attacks:
        most_common = max(non_none_attacks, key=non_none_attacks.get)
        print(f"Most common attack effect (excluding None): {most_common}, {non_none_attacks[most_common]}")

    min_count = min(attacks.values())
    """
    least_common_effects = [effect for effect in attacks if attacks[effect] == min_count]
    if len(least_common_effects) == 1:
        print(f"Least common attack effect: {least_common_effects[0]}, {min_count}")
    else:
        print(f"Least common attack effects (tied at {min_count}):")
        for effect in least_common_effects:
            print(f"- {effect}")

    print(f"Minimum HP: {min(health_points.values())}")
    print(f"Maximum HP: {max(health_points.values())}")
    print(f"Minimum damage: {min(damages.values())}")
    print(f"Maximum damage: {max(damages.values())}")
    """
    print(f"Stages: {stages}")
    print(f"Minimum retreat cost: {min_retreat_cost}")
    print(f"Maximum retreat cost: {max_retreat_cost}")

    # Refined keywords (TCG-specific, synonyms)
    keywords = [
        'discard', 'draw', 'evolve', 'devolve', 'evolved', 'basic', 'stage', 'heal', 'recover', 'attach', 'search',
        'damage', 'prevent', 'switch', 'shuffle', 'retreat', 'play', 'flip', 'coin', 'put', 'move', 'look', 'reveal',
        'bench', 'active', 'energy', 'tool', 'stadium', 'supporter', 'prize', 'knock', 'counter', 'condition',
        'burn', 'poison', 'paralyze', 'asleep', 'confuse', 'weakness', 'resistance', 'attack', 'ability',
        'ex', 'v', 'tera', 'ancient', 'future', 'rule', 'hand', 'deck'
    ]

    ability_effects = [effect for effect in attacks if effect is not None]

    if ability_effects:
        # TF-IDF on full texts
        tfidf_vec, _ = tfidf_vectorize(ability_effects)

        # Keyword count matrix
        count_matrix = np.zeros((len(ability_effects), len(keywords)))
        for i, effect in enumerate(ability_effects):
            lower_effect = effect.lower()
            for j, kw in enumerate(keywords):
                count_matrix[i, j] = lower_effect.count(kw)

        # Normalize counts
        row_sums = count_matrix.sum(axis=1, keepdims=True)
        count_matrix = np.divide(count_matrix, row_sums, where=row_sums != 0)

        # Hybrid: Concatenate TF-IDF + keywords
        hybrid_matrix = np.hstack((tfidf_vec, count_matrix))

        # SVD reduction
        n_components = min(50, hybrid_matrix.shape[1] - 1)  # Avoid over-reduction
        U, S, Vt = svd(hybrid_matrix, full_matrices=False)
        reduced = U[:, :n_components] @ np.diag(S[:n_components])

        # Distance matrix (fix NaN)
        dist_matrix = dist.cdist(reduced, reduced, metric='cosine')
        dist_matrix[np.isnan(dist_matrix)] = 1.0

        condensed_dist = dist_matrix[np.triu_indices(len(ability_effects), k=1)]

        # Clustering
        linkage_matrix = hierarchy.linkage(condensed_dist, method='complete')
        threshold = 0.3  # Tune: 0.3-0.5 for 70-100 groups
        clusters = hierarchy.fcluster(linkage_matrix, threshold, criterion='distance')

        # Optional validation (if sklearn installed)
        # score = silhouette_score(reduced, clusters)
        # print(f"Silhouette Score: {score}")  # Aim >0.2

        # Group
        grouped = pd.DataFrame({'effect': ability_effects, 'cluster': clusters})
        unique_groups = grouped.groupby('cluster')['effect'].apply(list).to_dict()

        print(f"Number of unique effect groups: {len(unique_groups)}")
        for cluster_id, effects in sorted(unique_groups.items()):
            print(f"Group {cluster_id} (size: {len(effects)}):")
            for effect in effects:
                print(f"  - {effect}")
    else:
        print("No abilities to cluster")


def tfidf_vectorize(texts):
    words = [text.lower().split() for text in texts if text is not None]
    all_words = set(word for doc in words for word in doc)
    word_to_idx = {word: i for i, word in enumerate(all_words)}
    n_docs = len(words)
    tf = np.zeros((n_docs, len(all_words)))
    for i, doc in enumerate(words):
        for word in doc:
            tf[i, word_to_idx[word]] += 1
        tf[i] /= len(doc) if len(doc) > 0 else 1
    df = np.sum(tf > 0, axis=0)
    idf = np.log(n_docs / (df + 1))
    tfidf = tf * idf
    return tfidf, words

if __name__ == "__main__":
    file_name_resumes = "../../data/cards/all_legal_resumes.pkl"
    file_name_cards = "../data/cards/all_legal_cards.pkl"
    regs = ["G", "H", "I"]
    # all_pokemon_resumes = read_cards(file_name_resumes)
    # flattened = [item for sublist in all_pokemon_resumes for item in sublist]

    # all_pokemon_cards = asyncio.run(get_actual_card_data_from_resumes(flattened))
    all_legal_pokemon_cards = read_cards(file_name_cards)
    # print_card_info(all_legal_pokemon_cards[0])
    # asyncio.run(save_cards(file_name_cards, all_pokemon_cards))
    # sort_cards_into_pickle_files(all_legal_pokemon_cards)
    get_card_pool_specifics(all_legal_pokemon_cards)
