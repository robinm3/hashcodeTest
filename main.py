# This is a sample Python script.
import fileFormatting
import Algo
import Warehouse
import Commande


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def get_warehouses():
    liste_warehouse = []
    id = 0
    for i in fileFormatting.read_file()["warehouses"]:
        position = {
            "x": i["row"],
            "y": i["column"]
        }
        liste_warehouse.append(Warehouse(position, i["items"], id))
        id += 1


def get_liste_commande():
    liste_commande = []
    for i in fileFormatting.read_file()["customer_orders"]:
        position = {
            "x": i["row"],
            "y": i["column"]
        }
        liste_commande.append(Commande.Commande(position, i["number"], i["product_types"]))
    return liste_commande


def test():
    command1 = {
        "drone_id": 1234,
        "tag": "L",
        "warehouse_id": 123,
        "product_type_id": 456,
        "number_of_items": 4
    }
    command2 = {
        "drone_id": 456,
        "tag": "U",
        "warehouse_id": 456,
        "product_type_id": 456,
        "number_of_items": 2
    }
    command3 = {
        "drone_id": 456,
        "tag": "D",
        "customer_id": 456,
        "product_type_id": 456,
        "number_of_items": 2
    }
    command4 = {
        "drone_id": 789,
        "tag": "W",
        "number_of_turns": 3
    }

    listes_commandes = get_liste_commande()
    listes_warehouses = get_warehouses

    infos = fileFormatting.read_file()
    commandes = Algo.algo(listes_warehouses, infos["weights"], infos["maximum_load"], infos["deadline"], listes_commandes)

    fileFormatting.write_file(len(commandes), commandes)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
