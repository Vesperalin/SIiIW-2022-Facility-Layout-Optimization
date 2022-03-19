import json.decoder
import matplotlib.pyplot as plt
from math import sqrt

from models.problem_instances import ProblemInstance
from models.individual import Individual
from models.population import Population
from utils.data_reader import read_data
from utils.random_method import random_method
from utils.statistics import count_statistics
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
        
    generate_statistics_for_genetic_algorithm(amount_of_generations, tournament_size, prob_of_crossover, 
            prob_of_mutation, cost, flow, problem_instance, entities,population_size)
        method generates populations (genetic algorithm) and counts adaptation values for it's individuals
        then determines and returns values needed for comparing random method and genetic algorithm 
        returns: the best adaptation value found, the worst adaptation value found, 
            avg of the best adaptation values in each lap, standard deviation between the best and avg values
            
    generate_statistics_for_random_method(amount_of_loops, cost, flow, problem_instance, entities, population_size)
        method generates random populations and counts adaptation values for it's individuals
        then determines and returns values needed for comparing random method and genetic algorithm 
        returns: the best adaptation value found, the worst adaptation value found, 
            avg of the best adaptation values in each lap, standard deviation between the best and avg values
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

    print(min(best))
    show_graph(best, worst, avg)


def generate_statistics_for_genetic_algorithm(amount_of_generations, tournament_size, prob_of_crossover,
                                              prob_of_mutation, cost, flow, problem_instance, entities,
                                              population_size):
    best_of_all_tours = -1
    worst_of_all_tours = 0
    bests_of_all_tours = []
    avg_of_all_best = 0
    standard_deviation = 0

    for i in range(0, 10):
        starting_population = random_method(population_size, problem_instance, entities, cost, flow)
        count_statistics(starting_population)
        current_pop = starting_population

        best = []
        worst = []

        for o in range(0, amount_of_generations):
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

            current_pop = new_population

        if best_of_all_tours == -1 or min(best) < best_of_all_tours:
            best_of_all_tours = min(best)

        if max(worst) > worst_of_all_tours:
            worst_of_all_tours = max(worst)

        bests_of_all_tours.append(min(best))

    sum_of_best = 0
    for x in bests_of_all_tours:
        sum_of_best += x

    avg_of_all_best = sum_of_best / len(bests_of_all_tours)

    for x in bests_of_all_tours:
        standard_deviation += ((x - avg_of_all_best) ** 2)

    standard_deviation = standard_deviation / (len(bests_of_all_tours) - 1)
    standard_deviation = sqrt(standard_deviation)

    return best_of_all_tours, worst_of_all_tours, avg_of_all_best, standard_deviation


def generate_statistics_for_random_method(amount_of_loops, cost, flow, problem_instance, entities, population_size):
    best_of_all_tours = -1
    worst_of_all_tours = 0
    bests_of_all_tours = []
    avg_of_all_best = 0
    standard_deviation = 0

    for a in range(0, 10):
        for i in range(0, amount_of_loops):
            random_population = random_method(population_size, problem_instance, entities, cost, flow)
            count_statistics(random_population)

            best_of_tour = -1
            worst_of_tour = 0

            for individual in random_population.individuals:
                if best_of_tour == -1 or individual.adaptation_value < best_of_tour:
                    best_of_tour = individual.adaptation_value

                if individual.adaptation_value > worst_of_tour:
                    worst_of_tour = individual.adaptation_value

            bests_of_all_tours.append(best_of_tour)

            if best_of_all_tours == -1 or best_of_tour < best_of_all_tours:
                best_of_all_tours = best_of_tour

            if worst_of_tour > worst_of_all_tours:
                worst_of_all_tours = worst_of_tour

    sum_of_best = 0
    for x in bests_of_all_tours:
        sum_of_best += x

    avg_of_all_best = sum_of_best / len(bests_of_all_tours)

    for x in bests_of_all_tours:
        standard_deviation += ((x - avg_of_all_best) ** 2)

    standard_deviation = standard_deviation / (len(bests_of_all_tours) - 1)
    standard_deviation = sqrt(standard_deviation)

    return best_of_all_tours, worst_of_all_tours, avg_of_all_best, standard_deviation


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

    """flat_starting_population = \
        random_method(50, flat_problem_instance, flat_entities, flat_costs_of_flow, flat_amounts_of_flow)"""

    """hard_starting_population = \
        random_method(500, hard_problem_instance, hard_entities, hard_costs_of_flow, hard_amounts_of_flow)"""

    """count_statistics(easy_starting_population)
    generate_populations(50, easy_starting_population, 20, 0.75, 0.05, easy_costs_of_flow, easy_amounts_of_flow)"""

    """count_statistics(flat_starting_population)
    generate_populations(60, flat_starting_population, 20, 0.75, 0.05, flat_costs_of_flow, flat_amounts_of_flow)"""

    """count_statistics(hard_starting_population)
    generate_populations(200, hard_starting_population, 20, 0.85, 0.95, hard_costs_of_flow, hard_amounts_of_flow)"""
