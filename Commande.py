class Commande:
    def __init__(self, position, items, Num):
        self.position = position
        self.items = items
        self.num = Num

    def find_wearhouse(self, liste_wearhouse):
        distance = []
        for warehouse in liste_warehouse:
            for i in range(len(items)):
                if self.items <= warehouse.
            distance.append([(self.position[0] - warehouse.position[0])**2 + (self.position[1] - warehouse.position[1])**2, liste_warehouse.index(warehouse)])
        for j in range(len(distance)):  
            if (distance[j][0] > distance[j + 1][0]):  
                temp = distance[j]  
                distance[j]= distance[j + 1]  
                distance[j + 1]= temp