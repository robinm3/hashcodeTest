import math


class Drone:
    def __init__(self, capacité, position):
        self.capacité = capacité
        self.position = position
        self.items = {}

    def get_distance_to(self, next_position):
        distance = math.sqrt((self.position.x - next_position.x) ** 2 + (self.position.y - next_position.y) ** 2)
        return math.ceil(distance)

    def max_load(self, product_weight):
        return self.capacité // product_weight

    def load(self, product_type_id, product_weight, number_of_items, warehouse_position):
        if self.max_load(product_weight) < number_of_items:
            if self.items[product_type_id]:
                self.items[product_type_id] += number_of_items
            else:
                self.items[product_type_id] = number_of_items
            self.capacité -= product_weight * number_of_items
            distance = self.get_distance_to(warehouse_position)
            self.position = warehouse_position
            return distance
        return -1

    def deliver(self, product_type_id, product_weight, number_of_items, destination_position):
        if self.items[product_type_id] < number_of_items:
            self.items[product_type_id] -= number_of_items
            self.capacité += product_weight * number_of_items
            distance = self.get_distance_to(destination_position)
            self.position = destination_position
            return distance
        return -1

    def unload(self, product_type_id, product_weight, number_of_items, warehouse_position):
        if self.items[product_type_id] < number_of_items:
            self.items[product_type_id] -= number_of_items
            self.capacité += product_weight * number_of_items
            distance = self.get_distance_to(warehouse_position)
            self.position = warehouse_position
            return distance
        return -1

    def wait(self, number_of_turns):
        return number_of_turns

