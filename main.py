# This is a sample Python script.
import fileFormatting
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def test():
    command1 = {
        "drone_id": 1234,
        "tag": "L",
        "warehouse_id": 123,
        "product_type_id": 456,
        "number_of_items": 4
    }
    command2 = {
        "drone_id": 456,
        "tag": "U",
        "warehouse_id": 456,
        "product_type_id": 456,
        "number_of_items": 2
    }
    command3 = {
        "drone_id": 456,
        "tag": "D",
        "customer_id": 456,
        "product_type_id": 456,
        "number_of_items": 2
    }
    command4 = {
        "drone_id": 789,
        "tag": "W",
        "number_of_turns": 3
    }
    fileFormatting.read_file()
    fileFormatting.write_file(4, [command1, command2, command3, command4])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
