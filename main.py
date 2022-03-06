import json.decoder

from models.problem_instances import ProblemInstance
from utils.data_reader import read_data
from utils.random_method import random_method


if __name__ == '__main__':
    easy_problem_instance = ProblemInstance("easy", 3, 3, 9)
    flat_problem_instance = ProblemInstance("flat", 1, 12, 12)
    hard_problem_instance = ProblemInstance("hard", 5, 6, 24)

    costs_of_flow = []
    amounts_of_flow = []
    machines = []

    try:
        costs_of_flow, amounts_of_flow, machines = read_data(easy_problem_instance)

    except FileNotFoundError:
        print("Couldn't find the files")
    except json.decoder.JSONDecodeError:
        print("Error while reading a files")

    starting_population = random_method(3, easy_problem_instance, machines)

    print(starting_population.__str__())


# TODO: funkcja przystosowania

# Plan implementacji:
#   - potem funkcja przystosowania

# Pamiętać
#   - w funkcji przystosowania uwzględnić to, że nie ma połączenia każdy z każdym

# Pomysły
#   - getCost, getFlow, getDistance, f. przystosowania wydzieliś do osobnego pliku
#   - w pliku głównym porogramu mam listy: kosztów, przepływów oraz maszyn - one nigdy się nie zmieniają, żadne ich pole
#   - przyda się gdzieś metoda w stylu: getMachineCoordinatesById(id)
#   - co jak 2 macierze mają to samo ułożenie? - metoda losowa
#   - zmina z listy na array lub definiowanie wymiarów

