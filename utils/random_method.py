import random

from models.individual import Individual
from models.population import Population


"""
    random_method(population_size, problem_instance, machines)
        parameters - population size, problem instance and list of machines
        returns
            - population - returns Population instance, which contains collection of population individuals
            
    assign_positions_to_machines_in_matrix(problem_instance, machines)
        parameters - problem instance and list of machines
        returns - matrix of randomly placed machines - for individual
"""


def random_method(population_size, problem_instance, machines):
    population = []
    for i in range(population_size):
        individual = Individual(assign_positions_to_machines_in_matrix(problem_instance, machines))
        population.append(individual)

    return Population(population)


def assign_positions_to_machines_in_matrix(problem_instance, machines):
    matrix_of_individual = []  # matrix with machines that will be then assigned to individual
    possible_indexes = []  # collection of all possible coordinates in matrix (indexing from 0, not 1)
    m = 0  # numerator for machines

    for i in range(problem_instance.height):  # creating empty matrix and gathering all coordinates
        inner = []
        for j in range(problem_instance.width):
            inner.append(None)
            possible_indexes.append((i, j))
        matrix_of_individual.append(inner)

    random.shuffle(possible_indexes)  # shuffling collection of coordinates

    while m < len(machines):  # placing machines on random coordinates from shuffled collection
        matrix_of_individual[possible_indexes[m][0]][possible_indexes[m][1]] = machines[m]
        m += 1

    return matrix_of_individual
