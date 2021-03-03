def read_file():
    file = open('busy_day.in')

    lines = file.readlines()
    file.close()

    number_of_products = 0
    weights = []
    warehouses = []
    number_of_warehouses = 0
    number_of_customer_orders = 0
    params = []
    customer_orders = []
    row = 0
    number = 0
    first = True

    for index, line in enumerate(lines):
        line = line.replace("\n", "")
        if index == 0:
            params += line.split(" ")
        elif index == 1:
            number_of_products = line
        elif index == 2:
            weights = line.split(" ")
        elif index == 3:
            number_of_warehouses = int(line)
        elif 4 <= index < 4 + number_of_warehouses*2:
            if first:
                warehouse_info = line.split(" ")
                row = warehouse_info[0]
                column = warehouse_info[1]
                first = False
            else:
                items = line.split(" ")
                warehouses.append({
                    "row": row,
                    "column": column,
                    "items": items
                })
                first = True

        elif index == 4 + number_of_warehouses*2:
            number_of_customer_orders = line
        elif line:
            line_value = (index - (5 + number_of_warehouses*2)) % 3

            if line_value == 0:
                line_infos = line.split(" ")
                row = line_infos[0]
                column = line_infos[1]
            elif line_value == 1:
                number = line
            elif line_value == 2:
                product_types = line.split(" ")
                customer_orders.append({
                    "row": row,
                    "column": column,
                    "number": number,
                    "product_types": product_types
                })

    infos = {
        "warehouses": warehouses,
        "params": params,
        "weights": weights,
        "number_of_products": number_of_products,
        "number_of_warehouses": number_of_warehouses,
        "number_of_rows": params[0],
        "number_of_columns": params[1],
        "number_of_drones": params[2],
        "number_of_customer_orders": number_of_customer_orders,
        "deadline": params[3],
        "maximum_load": params[4],
        "customer_orders": customer_orders
    }
    return infos
