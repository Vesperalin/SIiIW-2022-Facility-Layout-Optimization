import json.decoder
import matplotlib.pyplot as plt

from models.problem_instances import ProblemInstance
from utils.data_reader import read_data
from utils.random_method import random_method
from utils.statistics import show_statistics, count_statistics
from flo.tournament_selection import tournament_selection
from flo.roulette_selection import roulette_selection
from flo.crossover import crossover
from models.individual import Individual
from models.population import Population


# TODO refactor code

def generate_populations(amount_of_loop, initial_pop, tournament_size, probability, cost, flow):
    current_pop = initial_pop
    best = []
    worst = []
    avg = []

    for o in range(0, amount_of_loop):
        potential_parents = tournament_selection(current_pop, tournament_size)
        # potential_parents = roulette_selection(current_pop)
        temp_children = crossover(current_pop, potential_parents, probability)

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
        random_method(500, easy_problem_instance, easy_entities, easy_costs_of_flow, easy_amounts_of_flow)

    flat_starting_population = \
        random_method(500, flat_problem_instance, flat_entities, flat_costs_of_flow, flat_amounts_of_flow)

    hard_starting_population = \
        random_method(500, hard_problem_instance, hard_entities, hard_costs_of_flow, hard_amounts_of_flow)


    """count_statistics(easy_starting_population)
    generate_populations(10, easy_starting_population, 5, 0.70, easy_costs_of_flow, easy_amounts_of_flow)"""

    """count_statistics(flat_starting_population)
    generate_populations(10, flat_starting_population, 5, 0.70, flat_costs_of_flow, flat_amounts_of_flow)"""

    count_statistics(hard_starting_population)
    generate_populations(15, hard_starting_population, 5, 0.70, hard_costs_of_flow, hard_amounts_of_flow)
















    # parents = tournament_selection(hard_starting_population, 20)
    """for x in parents:
        print("{} and {}".format(x[0], x[1]))"""
    # probability = 0.70
    # children = crossover(hard_starting_population, parents, probability)

    # temp liczenie wskaznika - tworzenie populacji
    """l = []
    for x in children:
        a = Individual(x, hard_costs_of_flow, hard_amounts_of_flow)
        l.append(a)

    p = Population(l)
    count_statistics(p)"""

    """print("*********************************************")

    for i in range(0, 100):
        par = tournament_selection(p, 50)
        prob = 0.70
        chil = crossover(p, par, prob)
        f = []
        for e in children:
            h = Individual(e, hard_costs_of_flow, hard_amounts_of_flow)
            f.append(h)
        p = Population(f)
        count_statistics(p)

    show_statistics(p, p, p)

    show_graph()"""

    """for x in children:
        print(x)"""

    """a = 0
    for x in easy_starting_population.individuals:
        print(str(a) + ": " + str(x.adaptation_value))
        a += 1

    parents = roulette_selection(easy_starting_population)

    print("*******************************")

    for x in parents:
        print("{} and {}".format(x[0], x[1]))"""




    """flat_starting_population = \
        random_method(1000, flat_problem_instance, flat_entities, flat_costs_of_flow, flat_amounts_of_flow)

    hard_starting_population = \
        random_method(1000, hard_problem_instance, hard_entities, hard_costs_of_flow, hard_amounts_of_flow)

    show_statistics(easy_starting_population, flat_starting_population, hard_starting_population)"""
