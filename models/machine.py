class Machine:
    """ Class represents machine
        machine_id - identifier of machine (int)
    """
    def __init__(self, machine_id):
        self.machine_id = machine_id

    def __str__(self):
        return "Machine {}".format(self.machine_id)
