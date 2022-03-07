class AmountOfFlow:
    """ Class represents amount of flow between two entities
        source - source entity (int)
        destination - destination entity  (int)
        amount - amount of flow from source entity to destination entity (int)
    """
    def __init__(self, source, destination, amount):
        self.source = source
        self.destination = destination
        self.amount = amount

    def __str__(self):
        return "Amount of flow {} - source: {}, destination: {}".format(self.amount, self.source, self.destination)
