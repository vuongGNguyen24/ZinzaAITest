import time
import os

import OOPSolution, DictionarySolution

TEST_DIR = "TestCases"

def find_files(dir):
    return [os.path.join(".", dir, file_name) for file_name in os.listdir(os.path.join(".", dir))]

def test_oop_solution(file_dir:str):
    orders = OOPSolution.Order.from_json_file(file_dir)

    print("All orders:")
    for order in orders:
        print(f"{order.order_id}: {order.address} -> {order.products}")
    print()

    order_gropups = OOPSolution.merge_orders(orders)
    
    print("Result from oop solution:")
    for item in order_gropups:
        print(item)

def test_default_dict_solution(file_dir:str):
    orders = DictionarySolution.load_from_json_file(file_dir)
    order_gropups = DictionarySolution.merge_orders(orders)

    print("Result from dictionary solution:")
    for address, orders in order_gropups.items():
        print(f"Address: {address}")
        for item in orders:
            print(f"Id: {item['order_id']}, ", end="")
            print(f"products: {item['products']}")

def main():
    file_dirs = find_files(TEST_DIR)

    for dir in file_dirs:
        test_oop_solution(dir)
        test_default_dict_solution(dir)
        print()


main()