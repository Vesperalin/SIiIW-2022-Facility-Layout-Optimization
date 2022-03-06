class ProblemInstance:
    """ Class represents given problem: amount of machines, matrix size and name - prefix of data file
        name - name of the problem (easy, flat, hard)
        width - width of matrix
        height - height of matrix
        machines_amount - amount of machines on matrix
    """

    def __init__(self, name, width, height, machines_amount):
        self.name = name
        self.width = width
        self.height = height
        self.machines_amount = machines_amount

    def __str__(self):
        return "Problem instance {} - width: {}, height: {}, machines amount: {}"\
            .format(self.name, self.width, self.height, self.machines_amount)
