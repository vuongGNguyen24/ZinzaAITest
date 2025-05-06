from typing import List
import json

class Order:
    def __init__(self, order_id:int, address:str, products:List[str]):
        self.order_id = order_id
        self.address = address
        self.products = products
    @classmethod
    def from_json_file(cls, filepath:str):
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [cls(**item) for item in data]
        

class OrderGroup:
    def __init__(self, address:str):
        self.address = address
        self.all_orders = []

    def add_order(self, order:Order):
        self.all_orders.append(order)
    def __str__(self):
        res = f"Address: {self.address}\n"
        for item in self.all_orders:
            res += f"Id: {item.order_id}, products: {item.products}\n"
        return res

def merge_orders(orders:List[Order]):
    groups = {}
    for order in orders:
        if order.address not in groups:
            groups[order.address] = OrderGroup(order.address)
        groups[order.address].add_order(order)
    return list(groups.values())
