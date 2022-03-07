import random

from models.individual import Individual
from models.population import Population


"""
    random_method(population_size, problem_instance, entities, costs_of_flow, amounts_of_flow)
        generates and returns Population instance, which contains collection of population individuals
            
    assign_positions_to_entities_in_matrix(problem_instance, entities)
        returns matrix of randomly placed entities (2D list od Entity objects)
"""


def random_method(population_size, problem_instance, entities, costs_of_flow, amounts_of_flow):
    population = []
    for i in range(population_size):
        individual = Individual(assign_positions_to_entities_in_matrix(problem_instance, entities),
                                costs_of_flow, amounts_of_flow)
        population.append(individual)

    return Population(population)


def assign_positions_to_entities_in_matrix(problem_instance, entities):
    matrix_of_individual = []  # matrix with entities that will be then assigned to individual
    possible_indexes = []  # collection of all possible coordinates in matrix (indexing from 0, not 1)
    m = 0  # numerator for entities

    for i in range(problem_instance.height):  # creating empty matrix and gathering all coordinates
        inner = []
        for j in range(problem_instance.width):
            inner.append(None)
            possible_indexes.append((i, j))
        matrix_of_individual.append(inner)

    random.shuffle(possible_indexes)  # shuffling collection of coordinates

    while m < len(entities):  # placing entities on random coordinates from shuffled collection
        matrix_of_individual[possible_indexes[entities[m]][0]][possible_indexes[entities[m]][1]] = entities[m]
        m += 1

    return matrix_of_individual
