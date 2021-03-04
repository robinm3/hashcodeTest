import Commande
import Drone


def algo(warehouses, weights, maximum_load, deadline, customer_orders):
    order1 = customer_orders[0]
    total_time = 0
    commands = []

    commande = Commande(customer_orders[0]["position"], order1["product_types"], order1["number"])

    warehouse_chosen = commande.find_warehouse(warehouses)

    drone = Drone(maximum_load, warehouses[0].position)

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
