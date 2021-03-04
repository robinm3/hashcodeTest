class Warehouse:
    def __init__(self, position, items, id):
        self.position = position
        self.items = items
        self.ordre_commande = []
        self.id = id

    def unload(self, product_type_id, number_of_items):
        print("before: "+ str(self.items[product_type_id]))
        if self.items[product_type_id] and int(self.items[product_type_id]) >= number_of_items:
            self.items[product_type_id] = int(self.items[product_type_id]) - number_of_items

            print("possible "+ str(number_of_items))
            return number_of_items
        elif self.items[product_type_id]:
            number_possible = self.items[product_type_id]
            print("possible "+ str(number_possible))
            self.items[product_type_id] = 0
            return number_possible
        else:
            return False

    def load(self, product_type_id, number_of_items):
        self.items[product_type_id] += number_of_items



