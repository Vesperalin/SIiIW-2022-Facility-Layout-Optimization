class AmountOfFlow:
    """
        source - source machine id
        destination - destination machine id
        amount - amount of flow from source machine to destination machine
    """
    def __init__(self, source, destination, amount):
        self.source = source
        self.destination = destination
        self.amount = amount

    def __str__(self):
        return "Amount of flow {} - source: {}, destination: {}".format(self.amount, self.source, self.destination)
