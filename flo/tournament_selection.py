import random

"""
    tournament_selection(population, N)
        parameters:
            population - Population object
            N - size of tournament
        returns:
            list of pairs (potential parents) of indexes of individuals in population eg. [[2, 3], [1, 3], [0, 1]]
"""


def tournament_selection(population, N):
    list_of_pairs_of_potential_parents = []
    amount_of_chosen_parents = 0
    amount_of_parents = 0

    if len(population.individuals) % 2 == 0:
        amount_of_parents = len(population.individuals)
    else:
        amount_of_parents = len(population.individuals) - 1

    for x in range(0, int(amount_of_parents / 2)):
        list_of_pairs_of_potential_parents.append([-1, -1])

    while amount_of_chosen_parents < amount_of_parents:
        list_of_randomly_chosen_individuals_indexes = set()

        while len(list_of_randomly_chosen_individuals_indexes) < N:
            list_of_randomly_chosen_individuals_indexes.add(random.randrange(0, len(population.individuals)))

        list_of_randomly_chosen_individuals_indexes = list(list_of_randomly_chosen_individuals_indexes)

        the_best_individual_index = None

        for x in list_of_randomly_chosen_individuals_indexes:
            if the_best_individual_index is None:
                the_best_individual_index = x
            elif population.individuals[x].adaptation_value < population.individuals[the_best_individual_index].adaptation_value:
                the_best_individual_index = x

        for pair in list_of_pairs_of_potential_parents:
            if pair[0] == -1:
                pair[0] = the_best_individual_index
                amount_of_chosen_parents += 1
                break
            elif pair[1] == -1:
                pair[1] = the_best_individual_index
                amount_of_chosen_parents += 1
                break

    return list_of_pairs_of_potential_parents
