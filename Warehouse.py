import fileFormatting

class Warehouse:
    def __init__(self, position, items):
        self.position = position
        self.items = items
        self.ordre_commande = []
    
    def mes_commandes(self):pass

liste_warehouse = []
for i in fileFormatting.read_file()["warehouses"]:
    liste_warehouse.append(Warehouse((i["row"], i["column"]), i["items"]))