from math import sqrt


"""
    show_statistics(easy_starting_population, flat_starting_population, hard_starting_population)
        shows results from count_statistics(starting_population) function
        
    count_statistics(starting_population)
        calculates and returns:
            the best adaptation score, the worst adaptation score, average adaptation score and standard deviation
        for individuals in population
"""


def show_statistics(easy_starting_population, flat_starting_population, hard_starting_population):
    easy_statistics = count_statistics(easy_starting_population)
    flat_statistics = count_statistics(flat_starting_population)
    hard_statistics = count_statistics(hard_starting_population)
    results = [easy_statistics, flat_statistics, hard_statistics]

    for i in range(len(results)):
        if i == 0:
            print("Easy data for 1000 individuals")
        elif i == 1:
            print("Flat data for 1000 individuals")
        else:
            print("Hard data for 1000 individuals")
        print("Best score: " + str(results[i][0]))
        print("Worst score: " + str(results[i][1]))
        print("Average score: " + str(results[i][2]))
        print("Standard deviation: " + str(results[i][3]))
        print("*****************************************************************************************")


def count_statistics(starting_population):
    best_score = -1
    worst_score = 0
    sum_of_scores = 0
    scores = []
    standard_deviation = 0

    for individual in starting_population.individuals:
        result = individual.count_adaptation_value()
        if result < best_score or best_score == -1:
            best_score = result
        if result > worst_score:
            worst_score = result
        sum_of_scores += result
        scores.append(result)

    average = sum_of_scores / len(starting_population.individuals)

    for score in scores:
        standard_deviation += ((score - average) ** 2)

    standard_deviation = standard_deviation / (len(starting_population.individuals) - 1)
    standard_deviation = sqrt(standard_deviation)

    return best_score, worst_score, round(average, 2), round(standard_deviation, 2)
