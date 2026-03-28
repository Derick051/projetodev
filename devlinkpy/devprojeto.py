# Classe Cliente
class Customer:
    def __init__(self, name, customer_type, balance):
        self.name = name
        self.customer_type = customer_type  # NORMAL ou VIP
        self.balance = balance
# Classe Item
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
# Classe Pedido
class Order:
    def __init__(self, order_id, customer, items):
        self.order_id = order_id
        self.customer = customer
        self.items = items
        self.status = None

    def total(self):
        total = 0
        for item in self.items:
            total += item.price * item.quantity
        return total
    
def process_order(order):
    if len(order.items) == 0:
        order.status = "REJECTED"
        return order
    total = order.total()

    # Saldo insuficiente
    if order.customer.balance < total:
        order.status = "REJECTED"
        return order
    
    # Cliente VIP
    if order.customer.customer_type == "VIP" and total <= 2000:
        order.status = "APPROVED"
        return order
    
    # Pedido alto
    if total > 1000:
        order.status = "PENDING"

        return order
    order.status = "APPROVED"
    return order

customer = Customer("Derick", "VIP", 2500)

item1 = Item("Notebook", 1200, 1)
item2 = Item("Mouse", 100, 2)

order = Order(1, customer, [item1, item2])

processed = process_order(order)

print("ID:", processed.order_id)
print("Cliente:", processed.customer.name)
print("Total:", processed.total())
print("Status:", processed.status)