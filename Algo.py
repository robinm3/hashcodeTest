import Commande
import Drone


def algo(warehouses, weights, maximum_load, deadline, customer_orders):
    total_time = 0
    commands = []

    drone = Drone.Drone(maximum_load, warehouses[0].position)

    for index, order in enumerate(customer_orders):
        customer_id = index
        for i, product in enumerate(order.items):
            total_time = deliver_most_items_from_product(customer_id, product, drone, i, weights, order, warehouses, commands, total_time,
                                            deadline)
    return commands


def deliver_most_items_from_product(customer_id, product, drone, i, weights, commande, warehouses, commands, total_time, deadline):
    number_of_items_left = int(product)
    warehouse_chosen = commande.find_next_best_warehouse(warehouses, i)
    if not warehouse_chosen:
        pass
    while number_of_items_left != 0 and warehouse_chosen:
        loaded = load_product_from_warehouse_to_drone(i, weights, number_of_items_left,
                                                                      warehouse_chosen, drone, commande,
                                                                      warehouses, total_time, commands, product)
        if not loaded:
            break
        number_of_items_loaded, total_time = loaded
        total_time = deliver_product_to_location_with_drone(customer_id, i, weights, number_of_items_loaded, drone, commande,
                                           commande.position, total_time, commands, product)
        if total_time > deadline:
            break
    return total_time


def load_product_from_warehouse_to_drone(i, weights, number_of_items_left, warehouse_chosen, drone, commande,
                                         warehouses, total_time, commands, product):
    loaded = drone.load(i, int(weights[i]), number_of_items_left, warehouse_chosen)
    if not loaded:
        warehouse_chosen = commande.find_next_best_warehouse(warehouses, i)
        if not warehouse_chosen:
            return False

        loaded = drone.load(i, int(weights[i]), number_of_items_left, warehouse_chosen)

    if not loaded:
        return False

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
    return number_of_items_loaded, total_time


def deliver_product_to_location_with_drone(customer_id, i, weights, number_of_items_loaded, drone, commande,
                                           location, total_time, commands, product):
    total_time += drone.deliver(i, int(weights[i]), int(product), location)
    commands.append({
        "drone_id": 0,
        "tag": "D",
        "customer_id": customer_id,
        "product_type_id": i,
        "number_of_items": number_of_items_loaded
    })
    commande.item_delivered(i, number_of_items_loaded)
    return total_time
