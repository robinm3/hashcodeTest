class Commande:
    def __init__(self, position, nombre, items, id):
        self.position = position
        self.items = items
        self.nombre = nombre
        self.id = id

    def item_delivered(self, product_type_id, number_of_items):
        self.items[product_type_id] = int(self.items[product_type_id]) - number_of_items

    def find_warehouse_stock(self, liste_warehouse):
        next_best_warehouse = (liste_warehouse[0], 0)
        valide_warehouse = []
        for warehouse in liste_warehouse:
            compteur = 0
            for i in range(len(self.items)):
                if self.items[i] in warehouse.items:
                    compteur += int(warehouse.items[i])
            if compteur > 0 and compteur > next_best_warehouse[1]:
                next_best_warehouse = (warehouse, compteur)
                valide_warehouse.append(warehouse)

        return next_best_warehouse[0]

    def find_next_best_warehouse(self, liste_warehouse, product_id):
        next_best_warehouse = (False, 0)
        valide_warehouse = []
        for warehouse in liste_warehouse:
            compteur = 0
            if warehouse.items[product_id] and warehouse.items[product_id] != '0':
                compteur += int(warehouse.items[product_id])
            if compteur > 0 and compteur > next_best_warehouse[1]:
                next_best_warehouse = (warehouse, compteur)
                valide_warehouse.append(warehouse)
        return next_best_warehouse[0]


    def find_warehouse(self, liste_warehouse):
        distance = []
        valide = self.find_warehouse_stock(liste_warehouse)
        for warehouse in valide:
            distance.append([(self.position["x"] - warehouse.position["y"]) ** 2 + (
                        self.position["x"] - warehouse.position["y"]) ** 2, warehouse])

        # for j in range(len(distance)):
        #
        #     if distance[j][0] > distance[j + 1][0]:
        #         temp = distance[j]
        #         distance[j] = distance[j + 1]
        #         distance[j + 1] = temp
        return distance[1][1]
