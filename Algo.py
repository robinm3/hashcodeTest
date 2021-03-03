import Commande, Drone


def algo(warehouses, params, weights, number_of_products, number_of_warehouses, number_of_rows, number_of_columns, number_of_drones, number_of_customer_orders, deadline, maximum_load, customer_orders):
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

    drone = Drone(params[4], position_base_drone)

    for i, product in enumerate(order1.product_types):
        total_time += drone.load(i, product, 1, warehouse_chosen.position)
        commands.append({
            "drone_id": 0,
            "tag": "L",
            "warehouse_id": warehouse_chosen.id,
            "product_type_id": i,
            "number_of_items": 1
        })
        total_time += drone.deliver(i, product, 1, order_position)
        commands.append({
            "drone_id": 0,
            "tag": "U",
            "warehouse_id": warehouse_chosen.id,
            "product_type_id": i,
            "number_of_items": 1
        })
    return commands
