import json

def merge_orders(orders):
    merged = {}
    for order in orders:
        address = order["address"]
        if address not in merged:
            merged[address] = []
        merged[address].append(order)

    return merged

def load_from_json_file(file_path:str):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

