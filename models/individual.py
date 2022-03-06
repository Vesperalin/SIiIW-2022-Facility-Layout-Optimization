class Individual:
    """ Represents an individual in population
        matrix - matrix of machines - genotype
    """
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result = ""
        for i in range(len(self.matrix)):
            result += "[ "
            for j in range(len(self.matrix[i])):
                result += str(self.matrix[i][j]) + " "
            result += "]"
        return result
