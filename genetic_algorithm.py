import math
import os
import random

import numpy as np
from matplotlib import pyplot as plt
import numexpr as ne
from models.individual import Individual
from strategies.couples import all_with_all
from strategies.crosses import crossover_random_point
from strategies.mutations import mutate_random_position
from strategies.prune import select_best_individuals
from utilities.statistic import calculate_statistics, plot_evolution
from utilities.media import create_video


class GeneticAlgorithm:
    population_init = []
    population = []
    population_generated = []
    average_fitness = []
    best_fitness = []
    worst_fitness = []

    def __init__(self, principal_function, original_population, generations,
                 probability_of_gen, probability_of_ind, maximum_population,
                 a, b, resolution, min_or_max):
        self.principal_function = principal_function
        self.original_population = original_population
        self.generations = generations
        self.probability_of_gen = probability_of_gen
        self.probability_of_ind = probability_of_ind
        self.maximum_population = maximum_population
        self.a = a
        self.b = b
        self.resolution = resolution
        self.min_or_max = min_or_max

    def start(self):
        self.population = self.generate_population()
        for i in range(self.generations):
            pairs = all_with_all(self.population)
            crossovers = crossover_random_point(pairs)
            descendants = mutate_random_position(crossovers, self.probability_of_ind, self.probability_of_gen)
            new_individuals = self.decode_chromosomes(descendants)
            self.population = self.population + new_individuals

            average, best, worst = calculate_statistics(self.population, self.min_or_max)
            self.save_statistics(average, best, worst)
            self.population_generated.append(self.population)
            self.population = select_best_individuals(self.population, self.maximum_population, self.min_or_max)
            self.print_population()
        print(self.average_fitness, self.best_fitness, self.worst_fitness)
        self.create_generation_graphic(self.population_generated, i)
        plot_evolution(self.generations, self.average_fitness, self.best_fitness, self.worst_fitness)
        create_video()

    def decode_chromosomes(self, chromosomes):
        individuals = []
        for chromosome in chromosomes:
            decimal = self.binary_to_decimal(chromosome)
            x = self.calculate_x(decimal)
            y = round(self.calculate_y(x), 4)
            individuals.append(Individual(chromosome, decimal, x, y))
        return individuals

    def generate_population(self):
        chromosomes = [self.generate_chromosomes() for _ in range(self.original_population)]
        population = self.decode_chromosomes(chromosomes)
        self.population_init = population
        self.print_population_init()
        return population

    def ranges(self):
        return self.b - self.a

    def points(self):
        return int(self.ranges() / self.resolution + 1)

    def calculate_bits(self):
        return math.ceil(math.log2(self.points()))

    def new_resolution(self):
        bits = self.calculate_bits()
        deltax = round(self.ranges() / (2 ** bits - 1), 4)
        if self.resolution > deltax:
            return deltax
        else:
            return self.resolution

    def calculate_y(self, x):
        return np.log(1 + abs(x ** 3)) * np.cos(x) - np.sin(x) * np.log(2 + abs(2 + x ** 5))
        #6 * np.log(0.1 + abs(x ** 3)) + np.cos(x ** 2)
        #return round(eval(self.principal_function), 4)

    def calculate_fx(self, x):
        result_array = ne.evaluate(self.principal_function.replace('x', 'x_range'))
        return result_array

    def generate_chromosomes(self):
        binary_number = ''.join(random.choice('01') for _ in range(self.calculate_bits()))
        return binary_number

    def binary_to_decimal(self, binary_number):
        decimal_number = int(binary_number, 2)
        return decimal_number

    def calculate_x(self, decimal_value):
        x = round(self.a + decimal_value * self.new_resolution(), 4)
        return x

    def save_statistics(self, average, best, worst):
        self.average_fitness.append(average)
        self.best_fitness.append(best)
        self.worst_fitness.append(worst)

    def create_generation_graphic(self, population_generated, i):
        num_points = 100
        output_folder = '../graphics/generations/img'
        os.makedirs(output_folder, exist_ok=True)

        x_range = np.linspace(self.a, self.b, num_points)
        y_range = self.calculate_y(x_range)

        for population in population_generated:
            fig, ax = plt.subplots()

            ax.plot(x_range, y_range, label='Función', color='black', linestyle='--')

            x_values = [ind.x for ind in population]
            y_values = [ind.y for ind in population]

            idx_max = np.argmax(y_values)
            idx_min = np.argmin(y_values)

            ax.scatter(x_values, y_values, label=f'Demás individuos')

            if self.min_or_max:
                ax.scatter(x_values[idx_max], y_values[idx_max], color='green', label='Mejor individuo')
                ax.scatter(x_values[idx_min], y_values[idx_min], color='red', label='Peor individuo')
            else:
                ax.scatter(x_values[idx_max], y_values[idx_max], color='red', label='Peor individuo')
                ax.scatter(x_values[idx_min], y_values[idx_min], color='green', label='Mejor individuo')

            ax.set_xlim(self.a, self.b)

            ax.set_title(f'Generación {i + 1}')
            ax.set_xlabel('Rango')
            ax.set_ylabel('f(x)')
            ax.legend()
            ax.grid(True)

            filename = os.path.join(output_folder, f'Grafica_generacion_{i + 1}.png')
            plt.savefig(filename)
            print("Lista hecha: ", filename)
            ax.clear()
            plt.close()

    def print_population_init(self):
        for individual in self.population_init:
            print(individual)

    def print_population(self):
        for individual in self.population:
            print(individual)
