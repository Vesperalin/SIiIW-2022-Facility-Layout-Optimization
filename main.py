import json.decoder
import matplotlib.pyplot as plt

from models.problem_instances import ProblemInstance
from models.individual import Individual
from models.population import Population
from utils.data_reader import read_data
from utils.random_method import random_method
from utils.statistics import show_statistics, count_statistics
from flo.tournament_selection import tournament_selection
from flo.roulette_selection import roulette_selection
from flo.crossover import crossover
from flo.mutation import mutation


"""
    generate_populations(amount_of_loop, initial_pop, tournament_size, prob_of_crossover, prob_of_mutation, cost, flow)
        parameters
            amount_of_loop - amount of generations
            initial_pop - initial population (Population object)
            tournament_size - size ot tournament
            prob_of_crossover - probability of crossover
            prob_of_mutation - probability of mutation
            cost - list of costs of flow between entities
            flow - list of amount of flow between entities
        method generates populations and counts adaptation values for it's individuals
        after calculations shows results on graph
"""


def generate_populations(amount_of_loop, initial_pop, tournament_size, prob_of_crossover, prob_of_mutation, cost, flow):
    current_pop = initial_pop
    best = []
    worst = []
    avg = []

    for o in range(0, amount_of_loop):
        potential_parents = tournament_selection(current_pop, tournament_size)
        # potential_parents = roulette_selection(current_pop)
        temp_children = crossover(current_pop, potential_parents, prob_of_crossover)
        mutation(temp_children, prob_of_mutation)

        individuals = []
        for x in temp_children:
            a = Individual(x, cost, flow)
            individuals.append(a)

        new_population = Population(individuals)
        stats = count_statistics(new_population)

        best.append(stats[0])
        worst.append(stats[1])
        avg.append(stats[2])

        current_pop = new_population

    show_graph(best, worst, avg)


def show_graph(best, worst, avg):
    plt.plot(best, label="best")
    plt.plot(worst, label="worst")
    plt.plot(avg, label="avg")
    plt.ylabel("fitness")
    plt.xlabel("generation")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    easy_problem_instance = ProblemInstance("easy", 3, 3, 9)
    flat_problem_instance = ProblemInstance("flat", 1, 12, 12)
    hard_problem_instance = ProblemInstance("hard", 5, 6, 24)

    easy_costs_of_flow = []
    flat_costs_of_flow = []
    hard_costs_of_flow = []

    easy_amounts_of_flow = []
    flat_amounts_of_flow = []
    hard_amounts_of_flow = []

    easy_entities = []
    flat_entities = []
    hard_entities = []

    try:
        easy_costs_of_flow, easy_amounts_of_flow, easy_entities = read_data(easy_problem_instance)
        flat_costs_of_flow, flat_amounts_of_flow, flat_entities = read_data(flat_problem_instance)
        hard_costs_of_flow, hard_amounts_of_flow, hard_entities = read_data(hard_problem_instance)

    except FileNotFoundError:
        print("Couldn't find the files")
    except json.decoder.JSONDecodeError:
        print("Error while reading a files")

    easy_starting_population = \
        random_method(200, easy_problem_instance, easy_entities, easy_costs_of_flow, easy_amounts_of_flow)

    flat_starting_population = \
        random_method(200, flat_problem_instance, flat_entities, flat_costs_of_flow, flat_amounts_of_flow)

    hard_starting_population = \
        random_method(200, hard_problem_instance, hard_entities, hard_costs_of_flow, hard_amounts_of_flow)

    """count_statistics(easy_starting_population)
    generate_populations(50, easy_starting_population, 20, 0.80, 0.05, easy_costs_of_flow, easy_amounts_of_flow)"""

    """count_statistics(flat_starting_population)
    generate_populations(60, flat_starting_population, 20, 0.75, 0.05, flat_costs_of_flow, flat_amounts_of_flow)"""

    count_statistics(hard_starting_population)
    generate_populations(100, hard_starting_population, 20, 0.75, 0.05, hard_costs_of_flow, hard_amounts_of_flow)
