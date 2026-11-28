class StoreItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
    
    def print_name_and_price(self):
        print(self.name)
        print(self.price)


chips = StoreItem("Chips", 1.99) # Don't modify this line

# TODO: Access the attributes of the chips object and display them

chips.print_name_and_price()