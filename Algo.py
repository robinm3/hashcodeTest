import Commande, Drone


def algo(warehouses, params, weights, number_of_products, number_of_warehouses, number_of_rows, number_of_columns, number_of_drones, number_of_customer_orders, deadline, maximum_load, customer_orders):
    order1 = customer_orders[0]

    order_position = {
        "x": order1.row,
        "y": order1.column
    }
    position_base_drone = {
        "x": warehouses[0].row,
        "y": warehouses[1].column
    }

    commande = Commande(order_position, order1.product_types, order1.number)

    warehouses_to_check = commande.find_warehouse_stock(warehouses)
    warehouse_chosen = commande.find_warehouse_distance(warehouses_to_check)

    drone = Drone(params[4], position_base_drone)

    for i, product in enumerate(order1.product_types):
        time = drone.load(i, product, 1, warehouse_chosen.position)