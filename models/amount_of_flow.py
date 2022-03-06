class AmountOfFlow:
    """ Class represents amount of flow between two machines
        source - source machine id (int)
        destination - destination machine id (int)
        amount - amount of flow from source machine to destination machine (int)
    """
    def __init__(self, source, destination, amount):
        self.source = source
        self.destination = destination
        self.amount = amount

    def __str__(self):
        return "Amount of flow {} - source: {}, destination: {}".format(self.amount, self.source, self.destination)
