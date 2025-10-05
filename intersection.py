import random

class Intersection:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.options = ["Left", "Straight", "Right"]

    def suggest_direction(self, vehicle):
        if abs(vehicle.position - self.position) < 5:  # voiture proche du carrefour
            choice = random.choice(self.options)
            vehicle.choose_direction(choice)