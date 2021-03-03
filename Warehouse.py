import fileFormatting

class Warehouse:
    def __init__(self, position, items, id):
        self.position = position
        self.items = items
        self.ordre_commande = []
        self.id = id
    
    def mes_commandes(self):pass

liste_warehouse = []
id = 0
for i in fileFormatting.read_file()["warehouses"]:
    liste_warehouse.append(Warehouse((i["row"], i["column"]), i["items"], id))
    id += 1