import Commande, Drone


def algo(warehouses, weights, maximum_load, deadline, customer_orders):
    order1 = customer_orders[0]
    total_time = 0
    commands = []

    order_position = {
        "x": order1.row,
        "y": order1.column
    }
    position_base_drone = {
        "x": warehouses[0].row,
        "y": warehouses[1].column
    }

    commande = Commande(order_position, order1.product_types, order1.number)

    warehouse_chosen = commande.find_warehouse(warehouses)

    drone = Drone(maximum_load, position_base_drone)

    for i, product in enumerate(order1.product_types):
        total_time += drone.load(i, weights[i], product, warehouse_chosen.position)
        commands.append({
            "drone_id": 0,
            "tag": "L",
            "warehouse_id": warehouse_chosen.id,
            "product_type_id": i,
            "number_of_items": 1
        })
        total_time += drone.deliver(i, weights[i], product, order_position)
        commands.append({
            "drone_id": 0,
            "tag": "U",
            "warehouse_id": warehouse_chosen.id,
            "product_type_id": i,
            "number_of_items": 1
        })
        if total_time > deadline:
            break
    return commands
