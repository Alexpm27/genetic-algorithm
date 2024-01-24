import numpy as np
import random


def mutate(descendant, ind_mutation_rate, gen_mutation_rate):
    descendant_list = list(descendant)
    msg = f"Descendant: {descendant} "
    if round(random.random(), 2) < ind_mutation_rate:
        msg += " mutated to "

        for i in range(len(descendant_list)):
            if round(random.random(), 2) < gen_mutation_rate:
                mutation_position = random.randint(0, len(descendant_list) - 1)
                descendant_list[mutation_position] = str(1 - int(descendant_list[i]))
    descendant_list = ''.join(descendant_list)
    return descendant_list


def mutate_random_position(descendants, ind_mutation_rate, gen_mutation_rate):
    individuals = []

    for descendant in descendants:
        individual = mutate(descendant, ind_mutation_rate, gen_mutation_rate)
        individuals.append(individual)
    print_descendants(descendants)
    return np.array(descendants)


def print_descendants(mutated_population):
    for descendant in mutated_population:
        print(f"New individual: {descendant}")


