import Commande
import Drone


def algo(warehouses, weights, maximum_load, deadline, customer_orders, number_of_drones):
    total_time = 0
    commands = []

    for index, order in enumerate(customer_orders):
        customer_id = index
        for i, product in enumerate(order.items):
            total_time = deliver_most_items_from_product(customer_id, product, maximum_load, i, weights, order,
                                                         warehouses,
                                                         commands, total_time,
                                                         deadline, number_of_drones)
    return commands


def deliver_most_items_from_product(customer_id, product, maximum_load, i, weights, order, warehouses, commands,
                                    total_time,
                                    deadline, number_of_drones):
    last_drone_id = 0
    number_of_items_left = int(product)
    drone = Drone.Drone(last_drone_id, maximum_load, warehouses[0].position)
    warehouse_chosen = order.find_next_best_warehouse(drone, warehouses, i)
    if not warehouse_chosen:
        pass
    while number_of_items_left != 0 and warehouse_chosen:
        next_drone_id = get_next_drone_number(last_drone_id, number_of_drones)
        drone = Drone.Drone(next_drone_id, maximum_load, warehouses[0].position)

        loaded = load_product_from_warehouse_to_drone(i, weights, number_of_items_left,
                                                      warehouse_chosen, drone, order,
                                                      warehouses, total_time, commands, product)
        if not loaded:
            break
        number_of_items_loaded, total_time = loaded
        total_time = deliver_product_to_location_with_drone(customer_id, i, weights, number_of_items_loaded, drone,
                                                            order,
                                                            order.position, total_time, commands, product)
        if total_time > deadline:
            break
        last_drone_id = drone.drone_id
    return total_time


def load_product_from_warehouse_to_drone(i, weights, number_of_items_left, warehouse_chosen, drone, order,
                                         warehouses, total_time, commands, product):
    loaded = drone.load(i, int(weights[i]), number_of_items_left, warehouse_chosen)
    if not loaded:
        warehouse_chosen = order.find_next_best_warehouse(drone, warehouses, i)
        if not warehouse_chosen:
            return False

        loaded = drone.load(i, int(weights[i]), number_of_items_left, warehouse_chosen)

    if not loaded:
        return False

    total_time += loaded["distance"]
    number_of_items_loaded = loaded["number_of_items_loaded"]
    number_of_items_left -= number_of_items_loaded
    commands.append({
        "drone_id": str(drone.drone_id),
        "tag": "L",
        "warehouse_id": warehouse_chosen.id,
        "product_type_id": i,
        "number_of_items": number_of_items_loaded
    })
    print("loading from drone " + str(drone.drone_id) + " at warehouse " + str(warehouse_chosen.id) + " with " + str(
        number_of_items_loaded) + " of product " + str(i))
    print("location: " + str(warehouse_chosen.position))
    return number_of_items_loaded, total_time


def deliver_product_to_location_with_drone(customer_id, i, weights, number_of_items_loaded, drone, order,
                                           location, total_time, commands, product):
    total_time += drone.deliver(i, int(weights[i]), int(product), location)
    commands.append({
        "drone_id": str(drone.drone_id),
        "tag": "D",
        "customer_id": customer_id,
        "product_type_id": i,
        "number_of_items": number_of_items_loaded
    })
    order.item_delivered(i, number_of_items_loaded)
    print("delivering from drone " + str(drone.drone_id) + " to customer " + str(customer_id) + " with " + str(
        number_of_items_loaded) + " of product " + str(i))
    print("location: " + str(location))
    return total_time


def get_next_drone_number(last_drone_id, number_of_drones):
    if last_drone_id < number_of_drones:
        return last_drone_id + 1
    else:
        return 0
