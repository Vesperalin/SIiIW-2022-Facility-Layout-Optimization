import json

from models.cost_of_flow import CostOfFlow
from models.amount_of_flow import AmountOfFlow
from models.entity import Entity


"""
    read_data(problem_instance): 
        parameter - ProblemInstance object
        returns
            - cost_of_flow_results - list of CostOfFlow objects - read from file
            - amount_of_flow - list of AmountOfFlow objects - read from file
            - entities - list of entities id - based on all entity indexes from <problem instance name>_flow.json
"""


def read_data(problem_instance):
    with open("data/{}_cost.json".format(problem_instance.name)) as file:
        cost_of_flows_data = json.load(file)

    with open("data/{}_flow.json".format(problem_instance.name)) as file:
        amount_of_flows_data = json.load(file)

    cost_of_flows_results = []
    amount_of_flows_results = []
    entities_indexes = set()  # to collect all entities id without repetitions

    for record in cost_of_flows_data:
        result = CostOfFlow(record['source'], record['dest'], record['cost'])
        cost_of_flows_results.append(result)

    for record in amount_of_flows_data:
        result = AmountOfFlow(record['source'], record['dest'], record['amount'])
        amount_of_flows_results.append(result)

    for record in amount_of_flows_data:
        entities_indexes.add(record['source'])
        entities_indexes.add(record['dest'])

    return cost_of_flows_results, amount_of_flows_results, list(entities_indexes)
