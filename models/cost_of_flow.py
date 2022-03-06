class CostOfFlow:
    """ Class represents cost of flow between two machines
        source - source machine id (int)
        destination - destination machine id (int)
        cost - cost of flow from source machine to destination machine (int)
    """
    def __init__(self, source, destination, cost):
        self.source = source
        self.destination = destination
        self.cost = cost

    def __str__(self):
        return "Cost of flow {} - source: {}, destination: {}".format(self.cost, self.source, self.destination)
