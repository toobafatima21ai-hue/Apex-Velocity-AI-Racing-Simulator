import random


def create_car(name):

    return {

        "name": name,

        "position": random.uniform(
            0,
            5
        ),

        "speed": random.randint(
            60,
            90
        ),

        "tire": random.randint(
            80,
            100
        )
    }