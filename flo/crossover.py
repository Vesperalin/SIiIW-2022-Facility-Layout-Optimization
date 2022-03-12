import random
import numpy as np

"""
    crossover(population, parents)
        parameters:
            population - Population object
            parents - list of pairs (potential parents) of indexes of individuals in population eg. [[2, 3], [1, 3], [0, 1]]
            probability - probability of crossover
            costs_of_flow - list of costs of flow
            amounts_of_flow - list of costs of flow
        returns:
            list of children genotype (2d numpy arrays with entities ids)
"""

# TODO refactor code


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
            # print("weszło " + str(random_num))
            result = order_one_crossover(population, pair[0], pair[1])
            children.append(result[0])
            children.append(result[1])

        """if random_num <= probability * 100:
            # print("weszło " + str(random_num))
            result = order_one_crossover(population, pair[0], pair[1])
            children.append(result[0])
            children.append(result[1])
        else:
            a = np.empty_like(population.individuals[pair[0]].matrix)
            a[:] = population.individuals[pair[0]].matrix
            children.append(a)

            c = np.empty_like(population.individuals[pair[1]].matrix)
            c[:] = population.individuals[pair[1]].matrix
            children.append(c)"""

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

    amount_of_elements_to_copy = int(fields_amount / n)  # będę kopiować 1/3 elementow z jednego rodzica

    """****************************************** 1 dziecko"""
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

    """**************************************************2 dziecko"""
    amount_of_empty = 0
    for i in range(0, amount_of_elements_to_copy):
        ch2_flatten_matrix[i] = p2_flatten_matrix[i]
        if p2_flatten_matrix[i] == -1:
            amount_of_empty += 1

    n = amount_of_elements_to_copy

    for i in range(0, len(p1_flatten_matrix)):
        if p1_flatten_matrix[i] != -1 and p1_flatten_matrix[i] not in ch2_flatten_matrix:
            ch2_flatten_matrix[n] = p1_flatten_matrix[i]
            n += 1
        elif p1_flatten_matrix[i] == -1 and amount_of_empty > 0:
            amount_of_empty -= 1
        elif p1_flatten_matrix[i] == -1 and amount_of_empty == 0:
            ch2_flatten_matrix[n] = p1_flatten_matrix[i]
            n += 1

    ch1_flatten_matrix = ch1_flatten_matrix.reshape((len(population.individuals[parent1_index].matrix),
                                                     len(population.individuals[parent1_index].matrix[0])))
    ch2_flatten_matrix = ch2_flatten_matrix.reshape((len(population.individuals[parent1_index].matrix),
                                                     len(population.individuals[parent1_index].matrix[0])))

    return ch1_flatten_matrix, ch2_flatten_matrix

    """print(p1_flatten_matrix)
    print(p2_flatten_matrix)
    print(ch1_flatten_matrix)
    # print(ch2_flatten_matrix)
    print("************")"""

    """amount_of_elements_to_copy = int(fields_amount / 3)  # będę kopiować 1/3 elementow z jednego rodzica
    n = 0
    amount_of_empty = 0
    save_i = 0
    save_j = 0

    for i in range(len(p1_matrix)):
        for j in range(len(p1_matrix[0])):
            if n < amount_of_elements_to_copy:
                ch1_flatten_matrix[i][j] = p1_matrix[i][j]
                n += 1
                if p1_matrix[i][j] == -1:
                    amount_of_empty += 1
            else:
                break
        if n >= amount_of_elements_to_copy:
            save_i = i
            save_j = j
            break

    save_i += 1
    save_j = 0
    print(save_i)
    print(save_j)

    for i in range(len(p2_matrix)):
        for j in range(len(p2_matrix[0])):
            pass

    print(p1_matrix)
    print()
    print(ch1_flatten_matrix)"""

    """print(p1_matrix)
    print(p2_matrix)
    print(ch1_flatten_matrix)
    print(ch2_flatten_matrix)"""


