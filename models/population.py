class Population:
    """ Represents population
        individuals - list of individuals in population ([Individual])
    """
    def __init__(self, individuals):
        self.individuals = individuals

    def __str__(self):
        result = ""
        for individual in self.individuals:
            result += individual.__str__() + '\n'
        return result
