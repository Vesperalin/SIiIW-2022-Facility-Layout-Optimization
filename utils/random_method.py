import random


from models.individual import Individual


def random_method(population_size, problem_instance, machines):
    population = []
    for i in range(population_size):
        individual = Individual(assign_positions_to_machines_in_matrix(problem_instance, machines))
        population.append(individual)

    return population


def assign_positions_to_machines_in_matrix(problem_instance, machines):
    matrix_of_individual = []
    possible_indexes = []
    k = 0

    for i in range(problem_instance.height):
        inner = []
        for j in range(problem_instance.width):
            inner.append(None)
            possible_indexes.append((i, j))
        matrix_of_individual.append(inner)

    random.shuffle(possible_indexes)

    while k < len(machines):
        matrix_of_individual[possible_indexes[k][0]][possible_indexes[k][1]] = machines[k]
        k += 1

    return matrix_of_individual
