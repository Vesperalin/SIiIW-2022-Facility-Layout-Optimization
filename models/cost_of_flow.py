class CostOfFlow:
    """ Class represents cost of flow between two entities
        source - source entity (int)
        destination - destination entity (int)
        cost - cost of flow from source entity to destination entity (int)
    """
    def __init__(self, source, destination, cost):
        self.source = source
        self.destination = destination
        self.cost = cost

    def __str__(self):
        return "Cost of flow {} - source: {}, destination: {}".format(self.cost, self.source, self.destination)
