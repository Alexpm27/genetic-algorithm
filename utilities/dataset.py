import csv
import os


def save_statistic(average_fitness, best_fitness, worst_fitness):
    output_csv = '../graphics/fitness/statistics.csv'
    with open(output_csv, 'a', newline='') as csvfile:
        fieldnames = ['Average Fitness', 'Best Fitness', 'Worst Fitness']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if os.stat(output_csv).st_size == 0:
            writer.writeheader()

        writer.writerow(
            {'Average Fitness': average_fitness, 'Best Fitness': best_fitness, 'Worst Fitness': worst_fitness})


def save_population(generation, x_values, y_values):
    output_csv = '../graphics/generations/population_data.csv'
    with open(output_csv, 'a', newline='') as csvfile:
        fieldnames = ['Generation', 'X', 'Y']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if os.stat(output_csv).st_size == 0:
            writer.writeheader()

        for x, y in zip(x_values, y_values):
            writer.writerow({'Generation': generation + 1, 'X': x, 'Y': y})
