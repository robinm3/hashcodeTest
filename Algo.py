import Commande
import Drone


def algo(warehouses, weights, maximum_load, deadline, customer_orders):
    total_time = 0
    commands = []

    drone = Drone.Drone(maximum_load, warehouses[0].position)

    for index, order in enumerate(customer_orders):
        order1 = customer_orders[index]
        commande = order1
        for i, product in enumerate(order1.items):
            number_of_items_left = int(product)
            warehouse_chosen = commande.find_next_best_warehouse(warehouses, i)
            if not warehouse_chosen:
                pass
            while number_of_items_left != 0 and warehouse_chosen:
                loaded = drone.load(i, int(weights[i]), number_of_items_left, warehouse_chosen)
                if not loaded:
                    warehouse_chosen = commande.find_next_best_warehouse(warehouses, i)
                    if not warehouse_chosen:
                        break

                    loaded = drone.load(i, int(weights[i]), number_of_items_left, warehouse_chosen)

                if not loaded:
                    break

                total_time += loaded["distance"]
                number_of_items_loaded = loaded["number_of_items_loaded"]
                number_of_items_left -= number_of_items_loaded
                commands.append({
                    "drone_id": 0,
                    "tag": "L",
                    "warehouse_id": warehouse_chosen.id,
                    "product_type_id": i,
                    "number_of_items": int(product) - number_of_items_loaded
                })
                total_time += drone.deliver(i, int(weights[i]), int(product), order1.position)
                commands.append({
                    "drone_id": 0,
                    "tag": "U",
                    "warehouse_id": warehouse_chosen.id,
                    "product_type_id": i,
                    "number_of_items": number_of_items_loaded
                })
                commande.item_delivered(i, loaded["number_of_items_loaded"])
                if total_time > deadline:
                    break
    return commands
