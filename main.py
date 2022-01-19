# How to create a class:
class Item:
    price = None
    name = ''
    quantity = None

    def __init__(self,name:str, price:float, quantity=0):
        #Check price e quantity
        assert price >= 0, f"Price {price} è minore di 10"
        assert quantity >= 0, f"La quantità {quantity} è minore di 10"
        
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculate_total_price(self):
        return self.price * self.quantity

# How to create an instance of a class
item1 = Item('Phone',100,5)
# Calling methods from instances of a class:
print(item1.calculate_total_price())

# How to create an instance of a class (We could create as much as instances we'd like to)
item2 = Item("Laptop",1000,3)
# Calling methods from instances of a class: 
print(item2.calculate_total_price())