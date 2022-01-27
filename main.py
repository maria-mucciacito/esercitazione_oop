import csv

class Item:
    pay_rate = 0.8  #20% sconto
    all_items = []
    
    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"
    #Nota, in alternativa, si possono usare le exceptions
    #if price < 0:
    #   raise ValueError(f"Price {price} is not greater than or qaul to zero!")
    #if quantity < 0:
    #   raise ValueError(f"Quantity {quantity} is not greater than or equal to zero!")
        self.name = name
        self.price = price
        self.quantity = quantity
           
        Item.all_items.append(self)
    
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def calculate_total_price(self):
        return self.apply_discount(self.price) * self.quantity

    def apply_discount(self, price):
        return price * self.pay_rate
    
    @staticmethod
    def is_integer(num):
        try:
            int(num)
            return True
        except ValueError:
            return False

    
    @classmethod
    def read_from_csv(cls):
        input_file = csv.DictReader(open("esercitazione_oop/items.csv"))
        items = list(input_file)
        for item in items:
            if cls.is_integer(item.get('qunatity')):
                Item(name = item.get('name'), price=float(item.get('price')), quantity=int(item.get('quantity')))

    
     

item1 = Item("Phone", 100, 9.8)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all_items)
for i in Item.all_items: 
    print(i.name + " - " + str(i.calculate_total_price()))

print(Item.read_from_csv())