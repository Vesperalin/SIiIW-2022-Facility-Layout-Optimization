import numpy as np


"""
    roulette_selection(population)
        parameters:
            population - Population object
        returns:
            list of pairs (potential parents) of indexes of individuals in population eg. [[2, 3], [1, 3], [0, 1]]
"""


def roulette_selection(population):
    list_of_pairs_of_potential_parents = []
    amount_of_parents = 0
    n = 0

    if len(population.individuals) % 2 == 0:
        amount_of_parents = len(population.individuals)
    else:
        amount_of_parents = len(population.individuals) - 1

    population_fitness = sum([individual.adaptation_value for individual in population.individuals])
    probabilities = [individual.adaptation_value / population_fitness for individual in population.individuals]
    inverse_probabilities = [(1 - x) for x in probabilities]
    inverse_probabilities = [x / sum(inverse_probabilities) for x in inverse_probabilities]
    result = np.random.choice(a=len(population.individuals), size=amount_of_parents, p=inverse_probabilities)
    print(result)

    while n < amount_of_parents - 1:
        list_of_pairs_of_potential_parents.append([result[n], result[n + 1]])
        n += 2

    return list_of_pairs_of_potential_parents

