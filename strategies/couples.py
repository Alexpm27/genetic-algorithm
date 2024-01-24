import itertools
import numpy as np


def all_with_all(population):
    all_pairs_combinations = list(itertools.combinations(population, 2))

    combined_matrix = []

    for combination in all_pairs_combinations:
        combined_matrix.append(np.concatenate([ind.chromosome for ind in combination]))
    print_pairs(combined_matrix)
    return combined_matrix


def print_pairs(pairs):
    for pair in pairs:
        print(f"Pair: {pair}")
