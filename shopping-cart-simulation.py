class ShoppingCart:

  def __init__(self):
    self.cart = {}
    self.total = 0
    self.values = 0

  def add_item(self,item_name,price,quantity):
    self.cart[item_name] = {"price":price,"quantity":quantity}
    self.total += price*quantity

  def remove_item(self,item_name):
    item = self.cart.pop(item_name,None)
    if item is not None:
      self.total -= item["price"]*item["quantity"]

  def get_total(self):
    return self.total

  def calculate_total(self):
    total = 0
    for item in self.cart.values():
      total += item["price"]*item["quantity"]
    return total

  def display_cart(self):
    for item_name,item in self.cart.items():
      print(f"{item_name} : price :{item['price']}$ x quantity: {item['quantity']}")
    print(f"Total: {self.get_total()}$")

cart = ShoppingCart()
cart.add_item("oranges",10,2)
cart.add_item("apples",20,3)
cart.display_cart()
