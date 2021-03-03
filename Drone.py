import math

class Drone:
    def __init__(self, capacité, position):
        self.capacité = capacité
        self.position = position
        self.items = []

    def get_distance_to(self, next_position):
        distance = math.sqrt(self.position ** 2 + (next_position) ** 2)
        return math.ceil(distance)

    def max_load(self, product_type_id):

    def load(self, product_type_id, number_of_items):
        self.items.append({
            "product_type_id": product_type_id,
            "number_of_items": number_of_items
        })
