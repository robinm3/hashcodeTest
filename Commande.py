import fileFormatting


class Commande:
    def __init__(self, position, nombre, items):
        self.position = position
        self.items = items
        self.nombre = nombre

    def find_warehouse_stock(self, liste_warehouse):
        valide_warehouse = []
        for warehouse in liste_warehouse:
            compteur = 0
            for i in range(len(self.items)):
                if self.items[i] <= warehouse.items[i]:
                    compteur += 1
            if compteur == len(warehouse.items):
                valide_warehouse.append(warehouse)
        return valide_warehouse
                

    def find_warehouse(self, liste_warehouse):
        distance = []
        valide = self.find_warehouse_stock(liste_warehouse)
        for warehouse in valide:            
            distance.append([(self.position[0] - warehouse.position[0])**2 + (self.position[1] - warehouse.position[1])**2, warehouse])
        for j in range(len(distance)):  
            if (distance[j][0] > distance[j + 1][0]):  
                temp = distance[j]  
                distance[j] = distance[j + 1]  
                distance[j + 1] = temp
        return distance[1]



