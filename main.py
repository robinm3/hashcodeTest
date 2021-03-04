# This is a sample Python script.
from input_output import parse_and_format
import Algo
import Warehouse
import Commande


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def get_warehouses():
    liste_warehouse = []
    id = 0
    for i in parse_and_format.read_file()["warehouses"]:
        position = {
            "x": int(i["row"]),
            "y": int(i["column"])
        }
        liste_warehouse.append(Warehouse.Warehouse(position, i["items"], id))
        id += 1
    return liste_warehouse


def get_liste_commande():
    liste_commande = []
    for i in parse_and_format.read_file()["customer_orders"]:
        position = {
            "x": int(i["row"]),
            "y": int(i["column"])
        }
        liste_commande.append(Commande.Commande(position, i["number"], i["product_types"], i))
    return liste_commande


def test():

    listes_commandes = get_liste_commande()
    listes_warehouses = get_warehouses()

    infos = parse_and_format.read_file()
    commandes = Algo.algo(listes_warehouses, infos["weights"], int(infos["maximum_load"]), int(infos["deadline"]), listes_commandes)

    parse_and_format.write_file(len(commandes), commandes)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# commandLoad = {
#         "drone_id": 1234,
#         "tag": "L",
#         "warehouse_id": 123,
#         "product_type_id": 456,
#         "number_of_items": 4
#     }
# commandUnload = {
#         "drone_id": 456,
#         "tag": "U",
#         "warehouse_id": 456,
#         "product_type_id": 456,
#         "number_of_items": 2
#     }
# commandDeliver = {
#         "drone_id": 456,
#         "tag": "D",
#         "customer_id": 456,
#         "product_type_id": 456,
#         "number_of_items": 2
#     }
# commandWait = {
#         "drone_id": 789,
#         "tag": "W",
#         "number_of_turns": 3
#     }