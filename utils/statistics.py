from math import sqrt


def show_statistics(easy_starting_population, flat_starting_population, hard_starting_population):
    easy_statistics = count_statistics(easy_starting_population)
    print("Easy data for 1000 individuals")
    print("Best score: " + str(easy_statistics[0]))
    print("Worst score: " + str(easy_statistics[1]))
    print("Average score: " + str(easy_statistics[2]))
    print("Standard deviation: " + str(easy_statistics[3]))
    print("*****************************************************************************************")
    flat_statistics = count_statistics(flat_starting_population)
    print("Flat data for 1000 individuals")
    print("Best score: " + str(flat_statistics[0]))
    print("Worst score: " + str(flat_statistics[1]))
    print("Average score: " + str(flat_statistics[2]))
    print("Standard deviation: " + str(flat_statistics[3]))
    print("*****************************************************************************************")
    hard_statistics = count_statistics(hard_starting_population)
    print("Hard data for 1000 individuals")
    print("Best score: " + str(hard_statistics[0]))
    print("Worst score: " + str(hard_statistics[1]))
    print("Average score: " + str(hard_statistics[2]))
    print("Standard deviation: " + str(hard_statistics[3]))


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
