import os

import numpy as np
import matplotlib.pyplot as plt


def calculate_statistics(population, min_or_max):
    fitness_values = [ind.y for ind in population]

    if min_or_max:
        best_fitness = max(fitness_values)
        worst_fitness = min(fitness_values)
    else:
        worst_fitness = max(fitness_values)
        best_fitness = min(fitness_values)
    average_fitness = np.mean(fitness_values)
    print(average_fitness, best_fitness, worst_fitness)
    return average_fitness, best_fitness, worst_fitness


def plot_evolution(iterations, average_fitness_list, best_fitness_list, worst_fitness_list):
    output_folder = '../graphics/fitness/'
    os.makedirs(output_folder, exist_ok=True)
    plt.figure(figsize=(10, 6))
    generations = range(1, iterations + 1)

    plt.plot(generations, average_fitness_list, label='Promedio de Aptitud')
    plt.plot(generations, best_fitness_list, label='Mejor Aptitud', linestyle='--', color='green')
    plt.plot(generations, worst_fitness_list, label='Peor Aptitud', linestyle='--', color='red')

    plt.title('Evolución de Estadísticas en Varias Iteraciones')
    plt.xlabel('Iteración')
    plt.ylabel('Fitness')
    plt.legend()
    plt.grid(True)
    filename = os.path.join(output_folder, 'statistic-fitness-graphic.png')
    plt.savefig(filename)
    plt.show()
    plt.close()

