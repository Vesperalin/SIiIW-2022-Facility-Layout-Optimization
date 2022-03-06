class Individual:
    """ Represents an individual in population
        matrix - matrix of machines - genotype
    """

    def __init__(self, matrix, costs_of_flow, amounts_of_flow, amount_of_machines):
        self.matrix = matrix
        self.costs_of_flow = costs_of_flow
        self.amounts_of_flow = amounts_of_flow
        self.amount_of_machines = amount_of_machines

    def __str__(self):
        result = ""
        for i in range(len(self.matrix)):
            result += "[ "
            for j in range(len(self.matrix[i])):
                result += str(self.matrix[i][j]) + " "
            result += "]"
        return result

    def get_machine_coordinates_by_id(self, machine_id):
        for i in range(len(self.matrix[0])):
            for j in range(len(self.matrix)):
                if self.matrix[j][i] is not None:
                    if machine_id == self.matrix[j][i].machine_id:
                        return i, j
        return -1

    def __get_cost(self, source_machine_id, destination_machine_id):
        result = list(filter(lambda c: c.source == source_machine_id and c.destination == destination_machine_id,
                             self.costs_of_flow))
        if not result:
            return None
        else:
            return result[0].cost

    def __get_amount(self, source_machine_id, destination_machine_id):
        result = list(filter(lambda c: c.source == source_machine_id and c.destination == destination_machine_id,
                             self.amounts_of_flow))
        if not result:
            return None
        else:
            return result[0].amount

    def __get_distance(self, source_machine_id, destination_machine_id):
        source_machine_coordinates = self.get_machine_coordinates_by_id(source_machine_id)
        destination_machine_coordinates = self.get_machine_coordinates_by_id(destination_machine_id)
        return abs(source_machine_coordinates[0] - destination_machine_coordinates[0]) + \
               abs(source_machine_coordinates[1] - destination_machine_coordinates[1])

    def count_adaptation_value(self):  # uwzględniam brak połączenia każdy - każdy
        result = 0
        for i in range(0, len(self.amounts_of_flow)):
            source_id = self.amounts_of_flow[i].source
            destination_id = self.amounts_of_flow[i].destination
            amount = self.amounts_of_flow[i].amount

            if amount > 0:  # bo wtedy i tak to nie wpływa na wynik
                result += (self.amounts_of_flow[i].amount * self.costs_of_flow[i].cost * self.__get_distance(source_id, destination_id))

        return result


