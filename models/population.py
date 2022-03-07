class Population:
    """ Represents population
        individuals - list of individuals in population ([Individual])
        print_population() - prints population to console
    """
    def __init__(self, individuals):
        self.individuals = individuals

    def print_population(self):
        for individual in self.individuals:
            print(individual.__str__())
            print()
