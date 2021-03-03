class Product:
    def __init__(self, type_id, weight):
        self.type_id = type_id
        self.weight = weight

    def get_weight(self):
        return self.weight

    def get_type_id(self):
        return self.type_id
