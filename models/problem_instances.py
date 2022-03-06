class ProblemInstance:
    """ Class represents given problem parameters: amount of entities, matrix size and name - prefix of data file
        name - name of the problem (easy, flat, hard) (string)
        width - width of matrix (int)
        height - height of matrix (int)
        entities_amount - amount of entities on matrix (int)
    """

    def __init__(self, name, width, height, entities_amount):
        self.name = name
        self.width = width
        self.height = height
        self.entities_amount = entities_amount

    def __str__(self):
        return "Problem instance {} - width: {}, height: {}, entities amount: {}"\
            .format(self.name, self.width, self.height, self.entities_amount)
