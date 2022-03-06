class Individual:
    """ Represents an individual in population
        matrix - matrix of entities - genotype (2d list od Entity objects)
        costs_of_flow - list of costs of flow
        amounts_of_flow - list of costs of flow
        coordinates - dictionary of pairs: id of entity : (x coordinate, y coordinate)

        __generate_id_to_coordinates_collection() - method used to create coordinates dictionary
        get_entity_coordinates_by_id(id) - returns coordinates of entity is scheme (x position, y position)
                                            returns None, when entity was not found
        __get_cost(source_entity_id, destination_entity_id) - method returns cost of flow between given entities
                                                                returns None when connection between entities was not found
        __get_amount(source_entity_id, destination_entity_id) - method returns amount of flow between given entities
                                                                  returns None when connection between entities was not found
        __get_distance(source_entity_id, destination_entity_id) - calculates distance between entities
        count_adaptation_value() - returns adaptation value for individual
    """

    def __init__(self, matrix, costs_of_flow, amounts_of_flow):
        self.matrix = matrix
        self.costs_of_flow = costs_of_flow
        self.amounts_of_flow = amounts_of_flow
        self.coordinates = self.__generate_id_to_coordinates_collection()

    def __str__(self):
        result = ""
        for i in range(len(self.matrix)):
            result += "[ "
            for j in range(len(self.matrix[i])):
                result += str(self.matrix[i][j]) + " "
            result += "]"
        return result

    def __generate_id_to_coordinates_collection(self):
        coordinates = {}
        for i in range(len(self.matrix[0])):
            for j in range(len(self.matrix)):
                if self.matrix[j][i] is not None:
                    coordinates.update({self.matrix[j][i].entity_id: (i, j)})
        return coordinates

    def get_entity_coordinates_by_id(self, entity_id):
        coordinates = self.coordinates.get(entity_id)
        return coordinates

    def __get_cost(self, source_entity_id, destination_entity_id):
        result = list(filter(lambda c: c.source == source_entity_id and c.destination == destination_entity_id,
                             self.costs_of_flow))
        if not result:
            return None
        else:
            return result[0].cost

    def __get_amount(self, source_entity_id, destination_entity_id):
        result = list(filter(lambda c: c.source == source_entity_id and c.destination == destination_entity_id,
                             self.amounts_of_flow))
        if not result:
            return None
        else:
            return result[0].amount

    # no need to check for errors, because given ids are always correct - given from count_adaptation_value()
    def __get_distance(self, source_entity_id, destination_entity_id):
        source_entity_coordinates = self.get_entity_coordinates_by_id(source_entity_id)
        destination_entity_coordinates = self.get_entity_coordinates_by_id(destination_entity_id)
        return abs(source_entity_coordinates[0] - destination_entity_coordinates[0]) + \
               abs(source_entity_coordinates[1] - destination_entity_coordinates[1])

    def count_adaptation_value(self):
        result = 0
        for i in range(0, len(self.amounts_of_flow)):
            source_id = self.amounts_of_flow[i].source
            destination_id = self.amounts_of_flow[i].destination
            amount = self.amounts_of_flow[i].amount

            # because there is no need to check further if amount = 0, then the product is also 0
            if amount > 0:
                result += (self.amounts_of_flow[i].amount * self.costs_of_flow[i].cost * self.__get_distance(source_id, destination_id))

        return result
