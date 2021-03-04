import math


class Drone:
    def __init__(self, drone_id, capacité, position):
        self.drone_id = drone_id
        self.capacité = capacité
        self.position = position
        self.items = {}

    def get_distance_to(self, next_position):
        distance = math.sqrt((self.position["x"] - next_position["x"]) ** 2 + (self.position["y"] - next_position["y"]) ** 2)
        return math.ceil(distance)

    def max_load(self, product_weight):
        return self.capacité // product_weight

    def load(self, product_type_id, product_weight, number_of_items, warehouse):
        warehouse_position = warehouse.position
        new_number = number_of_items;
        if number_of_items >= self.max_load(product_weight):
            new_number = self.max_load(product_weight)
        items_loaded = int(warehouse.unload(product_type_id, new_number))
        if items_loaded:
            if self.items and product_type_id in self.items:
                self.items[product_type_id] += items_loaded
            else:
                self.items[product_type_id] = items_loaded
            self.capacité -= product_weight * items_loaded
            distance = self.get_distance_to(warehouse_position)
            self.position = warehouse_position

            return {"distance": distance, "number_of_items_loaded": items_loaded}

        return False

    def deliver(self, product_type_id, product_weight, number_of_items, destination_position):
        if product_type_id in self.items and self.items[product_type_id] <= number_of_items:
            self.items[product_type_id] -= number_of_items
            self.capacité += product_weight * number_of_items
            distance = self.get_distance_to(destination_position)
            self.position = destination_position
            return distance
        return False

    def unload(self, product_type_id, product_weight, number_of_items, warehouse):
        warehouse_position = warehouse.position
        if self.items[product_type_id] < number_of_items:
            warehouse.load(product_type_id, number_of_items)
            self.items[product_type_id] -= number_of_items
            self.capacité += product_weight * number_of_items
            distance = self.get_distance_to(warehouse_position)
            self.position = warehouse_position
            return distance
        return -1

    def wait(self, number_of_turns):
        return number_of_turns

