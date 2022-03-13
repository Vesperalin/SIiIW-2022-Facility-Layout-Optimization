import random
import numpy as np


"""
    crossover(population, parents, probability)
        parameters:
            population - Population object
            parents - list of pairs (potential parents) of indexes of individuals in population eg. [[2, 3], [1, 3], [0, 1]]
            probability - probability of crossover
        returns:
            list of children genotype (2d numpy arrays with entities ids)
            
    order_one_crossover(population, parent1_index, parent2_index)
        parameters:
            population - Population object
            parent1_index - index of individual in population (first parent)
            parent2_index - index of individual in population (second parent)
        returns:
            two children of given parents (without mutation yet)
"""


def crossover(population, parents, probability):
    children = []

    for pair in parents:
        random_num = random.randrange(0, 101)

        if pair[0] == pair[1] or random_num > probability * 100:
            a = np.empty_like(population.individuals[pair[0]].matrix)
            a[:] = population.individuals[pair[0]].matrix
            children.append(a)

            c = np.empty_like(population.individuals[pair[1]].matrix)
            c[:] = population.individuals[pair[1]].matrix
            children.append(c)
        else:
            result = order_one_crossover(population, pair[0], pair[1])
            children.append(result[0])
            children.append(result[1])

    return children


def order_one_crossover(population, parent1_index, parent2_index):
    p1_flatten_matrix = population.individuals[parent1_index].matrix.flatten()
    p2_flatten_matrix = population.individuals[parent2_index].matrix.flatten()
    fields_amount = len(p1_flatten_matrix)

    ch1_flatten_matrix = np.empty(len(p1_flatten_matrix))
    ch1_flatten_matrix.fill(-1)
    ch2_flatten_matrix = np.empty(len(p1_flatten_matrix))
    ch2_flatten_matrix.fill(-1)

    n = random.randrange(2, fields_amount)

    amount_of_elements_to_copy = int(fields_amount / n)

    for _ in range(0, 2):
        amount_of_empty = 0

        for i in range(0, amount_of_elements_to_copy):
            ch1_flatten_matrix[i] = p1_flatten_matrix[i]
            if p1_flatten_matrix[i] == -1:
                amount_of_empty += 1

        n = amount_of_elements_to_copy

        for i in range(0, len(p2_flatten_matrix)):
            if p2_flatten_matrix[i] != -1 and p2_flatten_matrix[i] not in ch1_flatten_matrix:
                ch1_flatten_matrix[n] = p2_flatten_matrix[i]
                n += 1
            elif p2_flatten_matrix[i] == -1 and amount_of_empty > 0:
                amount_of_empty -= 1
            elif p2_flatten_matrix[i] == -1 and amount_of_empty == 0:
                ch1_flatten_matrix[n] = p2_flatten_matrix[i]
                n += 1

        # change references
        p_temp = p1_flatten_matrix
        p1_flatten_matrix = p2_flatten_matrix
        p2_flatten_matrix = p_temp

        c_temp = ch1_flatten_matrix
        ch1_flatten_matrix = ch2_flatten_matrix
        ch2_flatten_matrix = c_temp

    ch1_flatten_matrix = ch1_flatten_matrix.reshape((len(population.individuals[parent1_index].matrix),
                                                     len(population.individuals[parent1_index].matrix[0])))
    ch2_flatten_matrix = ch2_flatten_matrix.reshape((len(population.individuals[parent1_index].matrix),
                                                     len(population.individuals[parent1_index].matrix[0])))

    return ch1_flatten_matrix, ch2_flatten_matrix
