class Commande:
    def __init__(self, position, items, Num):
        self.position = position
        self.items = items
        self.num = Num

    def find_wearhouse(self, liste_wearhouse):
        distance = []
        for wearhouse in liste_wearhouse:
            distance.append([(self.position[0] - wearhouse.position[0])**2 + (self.position[1] - wearhouse.position[1])**2, liste_wearhouse.index(wearhouse)])
        for j in range(0, lst-i-1):  
            if (tup[j][1] > tup[j + 1][1]):  
                temp = tup[j]  
                tup[j]= tup[j + 1]  
                tup[j + 1]= temp