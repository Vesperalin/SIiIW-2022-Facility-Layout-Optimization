import json


from models.cost_of_flow import CostOfFlow
from models.amount_of_flow import AmountOfFlow
from models.machine import Machine


"""
    read_data(problem_instance): 
        parameter - ProblemInstance object
        returns
            - cost_of_flow_results - array of CostOfFlow objects - read from file
            - amount_of_flow - array of AmountOfFlow objects - read from file
            - machine - array of machine objects - based on all machine indexes from easy_flow.json
"""


def read_data(problem_instance):
    with open("data/{}_cost.json".format(problem_instance.name)) as file:
        cost_of_flow_data = json.load(file)

    with open("data/{}_flow.json".format(problem_instance.name)) as file:
        amount_of_flow_data = json.load(file)

    cost_of_flow_results = []
    amount_of_flow_results = []
    machines = []
    machines_indexes = set()

    for record in cost_of_flow_data:
        result = CostOfFlow(record['source'], record['dest'], record['cost'])
        cost_of_flow_results.append(result)

    for record in amount_of_flow_data:
        result = AmountOfFlow(record['source'], record['dest'], record['amount'])
        amount_of_flow_results.append(result)

    for record in amount_of_flow_data:
        machines_indexes.add(record['source'])
        machines_indexes.add(record['dest'])

    for machine_index in machines_indexes:
        machines.append(Machine(machine_index))

    return cost_of_flow_results, amount_of_flow_results, machines

