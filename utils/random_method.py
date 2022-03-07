import random
import numpy as np

from models.individual import Individual
from models.population import Population


"""
    random_method(population_size, problem_instance, entities, costs_of_flow, amounts_of_flow)
        generates and returns Population instance, which contains collection of population individuals
            
    assign_positions_to_entities_in_matrix(problem_instance, entities)
        returns matrix of randomly placed entities (numpy 2D list od entities)
"""


def random_method(population_size, problem_instance, entities, costs_of_flow, amounts_of_flow):
    population = []
    for i in range(population_size):
        individual = Individual(assign_positions_to_entities_in_matrix(problem_instance, entities),
                                costs_of_flow, amounts_of_flow)
        population.append(individual)

    return Population(population)


def assign_positions_to_entities_in_matrix(problem_instance, entities):
    matrix_of_individual = np.empty(shape=(problem_instance.height, problem_instance.width))
    matrix_of_individual.fill(-1)
    possible_indexes = []  # collection of all possible coordinates in matrix (indexing from 0, not 1)
    n = 0  # numerator for entities

    for i in range(problem_instance.height):  # creating empty matrix and gathering all coordinates
        for j in range(problem_instance.width):
            possible_indexes.append((i, j))

    random.shuffle(possible_indexes)  # shuffling collection of coordinates

    while n < len(entities):  # placing entities on random coordinates from shuffled collection
        matrix_of_individual[possible_indexes[entities[n]][0]][possible_indexes[entities[n]][1]] = entities[n]
        n += 1

    return matrix_of_individual
