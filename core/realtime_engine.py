import random


class RealTimeEngine:

    def __init__(self, cars):

        self.cars = cars
        self.tick = 0

    def step(self):

        for name, car in self.cars.items():

            speed_variation = random.uniform(0.95, 1.05)

            tire_factor = max(
                0.5,
                car["tire"] / 100
            )

            movement = (
                car["speed"]
                * speed_variation
                * tire_factor
            ) * 0.02

            car["position"] += movement

            tire_loss = random.uniform(
                0.1,
                0.4
            )

            car["tire"] = max(
                0,
                car["tire"] - tire_loss
            )

            if car["tire"] < 30:
                car["speed"] *= 0.99

        self.tick += 1

        return self.cars