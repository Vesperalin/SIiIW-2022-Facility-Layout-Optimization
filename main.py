import json.decoder

from models.problem_instances import ProblemInstance
from utils.data_reader import read_data
from utils.random_method import random_method
from utils.statistics import show_statistics, count_statistics
from flo.tournament_selection import tournament_selection
from flo.roulette_selection import roulette_selection


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
        random_method(10, easy_problem_instance, easy_entities, easy_costs_of_flow, easy_amounts_of_flow)

    """flat_starting_population = \
        random_method(100, flat_problem_instance, flat_entities, flat_costs_of_flow, flat_amounts_of_flow)

    hard_starting_population = \
        random_method(100, hard_problem_instance, hard_entities, hard_costs_of_flow, hard_amounts_of_flow)"""

    count_statistics(easy_starting_population)

    a = 0
    for x in easy_starting_population.individuals:
        print(str(a) + ": " + str(x.adaptation_value))
        a += 1

    parents = roulette_selection(easy_starting_population)

    print("*******************************")

    for x in parents:
        print("{} and {}".format(x[0], x[1]))




    """flat_starting_population = \
        random_method(1000, flat_problem_instance, flat_entities, flat_costs_of_flow, flat_amounts_of_flow)

    hard_starting_population = \
        random_method(1000, hard_problem_instance, hard_entities, hard_costs_of_flow, hard_amounts_of_flow)

    show_statistics(easy_starting_population, flat_starting_population, hard_starting_population)"""
