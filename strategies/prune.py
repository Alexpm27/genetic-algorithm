def select_best_individuals(population, max_individuals, maximize):
    sorted_population = sorted(population, key=lambda ind: ind.y, reverse=maximize)

    best_individuals = []
    seen_chromosomes = set()

    for individual in sorted_population:
        if individual.chromosome not in seen_chromosomes:
            best_individuals.append(individual)
            seen_chromosomes.add(individual.chromosome)

        if len(best_individuals) == max_individuals:
            break

    return best_individuals
