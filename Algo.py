import Commande
import Drone


def algo(warehouses, weights, maximum_load, deadline, customer_orders, number_of_drones):
    total_time = 0
    commands = []

    for index, order in enumerate(customer_orders):

        customer_id = index
        print(order.items)
        for i, product in enumerate(order.items):
            print("i: "+str(i)+ " product "+str(product))
            total_time = deliver_most_items_from_product(customer_id, int(product), maximum_load, weights, order,
                                                         warehouses,
                                                         commands, total_time,
                                                         deadline, number_of_drones)
            print(total_time)
            print(deadline)
            if total_time + 2000 > deadline:
                break
        if total_time + 2000 > deadline:
            break
    return commands


def deliver_most_items_from_product(customer_id, product_id, maximum_load, weights, order, warehouses, commands,
                                    total_time,
                                    deadline, number_of_drones):
    last_drone_id = 0
    number_of_items_left = 1
    drone = Drone.Drone(last_drone_id, maximum_load, warehouses[0].position)
    warehouse_chosen = order.find_next_best_warehouse(drone, warehouses, product_id)
    if not warehouse_chosen:
        pass
    while number_of_items_left != 0 and warehouse_chosen:
        next_drone_id = get_next_drone_number(last_drone_id, number_of_drones)
        drone = Drone.Drone(next_drone_id, maximum_load, warehouses[0].position)

        loaded = load_product_from_warehouse_to_drone(product_id, weights, number_of_items_left,
                                                      warehouse_chosen, drone, order,
                                                      warehouses, total_time, commands, 1)
        if not loaded:
            break
        number_of_items_loaded, total_time = loaded
        total_time = deliver_product_to_location_with_drone(customer_id, product_id, weights, number_of_items_loaded, drone,
                                                            order,
                                                            order.position, total_time, commands, 1)
        if total_time > deadline:
            break
        last_drone_id = drone.drone_id
        number_of_items_left = 0
    return total_time


def load_product_from_warehouse_to_drone(product_id, weights, number_of_items_left, warehouse_chosen, drone, order,
                                         warehouses, total_time, commands, product):
    loaded = drone.load(product_id, int(weights[product_id]), number_of_items_left, warehouse_chosen)
    if not loaded:
        warehouse_chosen = order.find_next_best_warehouse(drone, warehouses, product_id)
        if not warehouse_chosen:
            return False

        loaded = drone.load(product_id, int(weights[product_id]), number_of_items_left, warehouse_chosen)

    if not loaded:
        return False

    total_time += loaded["distance"]
    number_of_items_loaded = loaded["number_of_items_loaded"]
    number_of_items_left -= number_of_items_loaded
    commands.append({
        "drone_id": str(drone.drone_id),
        "tag": "L",
        "warehouse_id": warehouse_chosen.id,
        "product_type_id": product_id,
        "number_of_items": number_of_items_loaded
    })
    print("loading from drone " + str(drone.drone_id) + " at warehouse " + str(warehouse_chosen.id) + " with " + str(
        number_of_items_loaded) + " of product " + str(product_id))
    print("location: " + str(warehouse_chosen.position))

    print("after: " + str(warehouse_chosen.items[product_id]))
    return number_of_items_loaded, total_time


def deliver_product_to_location_with_drone(customer_id, product_id, weights, number_of_items_loaded, drone, order,
                                           location, total_time, commands, product):
    total_time += drone.deliver(product_id, int(weights[product_id]), int(product), location)
    commands.append({
        "drone_id": str(drone.drone_id),
        "tag": "D",
        "customer_id": customer_id,
        "product_type_id": product_id,
        "number_of_items": number_of_items_loaded
    })
    order.item_delivered(product_id, number_of_items_loaded)
    print("delivering from drone " + str(drone.drone_id) + " to customer " + str(customer_id) + " with " + str(
        number_of_items_loaded) + " of product " + str(product_id))
    print("location: " + str(location))
    return total_time


def get_next_drone_number(last_drone_id, number_of_drones):
    if last_drone_id + 1 < number_of_drones:
        return last_drone_id + 1
    else:
        return 0
