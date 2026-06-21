class CameraSystem:

    def __init__(self):
        self.mode = "BROADCAST"

    def set_mode(self, mode):
        self.mode = mode

    def get_view(self, cars):
        sorted_cars = sorted(cars.items(), key=lambda x: -x[1]["position"])

        if self.mode == "LEADER":
            return sorted_cars[:2]

        elif self.mode == "PLAYER":
            return [c for c in sorted_cars if c[0] == "PLAYER"]

        return sorted_cars