import numpy as np
import random


def crossover(pair):
    crossover_point = random.randint(1, len(pair[0]) - 1)
    descendant1 = pair[0][:crossover_point] + pair[1][crossover_point:]
    descendant2 = pair[1][:crossover_point] + pair[0][crossover_point:]

    return descendant1, descendant2


def crossover_random_point(all_pairs):
    descendants = []
    for pair in all_pairs:
        descendant1, descendant2 = crossover(pair)
        descendants.append(descendant1)
        descendants.append(descendant2)
    print_crosses(descendants)
    return np.array(descendants)


def print_crosses(descendants):
    for descendant in descendants:
        print(f"Crosses: {descendant}")
