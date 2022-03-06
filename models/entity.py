class Entity:
    """ Class represents entity
        entity_id - identifier of entity (int)
    """
    def __init__(self, entity_id):
        self.entity_id = entity_id

    def __str__(self):
        return "Entity {}".format(self.entity_id)
