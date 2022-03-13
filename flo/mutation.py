import random


"""
    mutation(children, probability)
        parameters:
            children - list od 2D numpy arrays with ids of entities
            probability - probability of mutation
        changes two genes in individual's genotype (with given probability)
        doesn't return anything - makes changes in array (bc. it's passed by reference)
"""


def mutation(children, probability):
    for child in children:
        random_num = random.randrange(0, 101)

        if random_num <= probability * 100:
            height = len(children[0])
            width = len(children[0][0])

            random_y1 = random.randrange(0, height)
            random_x1 = random.randrange(0, width)

            random_y2 = random.randrange(0, height)
            random_x2 = random.randrange(0, width)

            temp = child[random_y1][random_x1]
            child[random_y1][random_x1] = child[random_y2][random_x2]
            child[random_y2][random_x2] = temp
