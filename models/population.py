class Population:
    """ Represents population
        individuals - matrix of individuals in population
    """
    def __init__(self, individuals):
        self.individuals = individuals

    def __str__(self):
        result = ""
        for individual in self.individuals:
            result += individual.__str__() + '\n'
        return result
