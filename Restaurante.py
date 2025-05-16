class MenuItem():
    def __init__(self, name:str, price:float, is_vegan:bool=False):
        self.name = name
        self.price = price
    def is_vegan(self):
        return self.is_vegan
        
class Appetizer(MenuItem):
    def __init__(self, name:str, price:float):
        super().__init__(name, price)
    def __str__(self):
        return f"Appetizer: {self.name}, Price: {self.price}"
    
class MainCourse(MenuItem):
    def __init__(self, name:str, price:float, protein:str, grains:str, vegetables:str):
        super().__init__(name, price)
        self.protein = protein
        self.grains = grains
        self.vegetables = vegetables
    def __str__(self):
        return f"Main Course: {self.name}, Price: {self.price}, Protein: {self.protein}, Grains: {self.grains}, Vegetables: {self.vegetables}"
    
class Beverage(MenuItem):
    def __init__(self, name:str, price:float, size:str, type:str):
        super().__init__(name, price)
        self.size = size
        self.type = type
    def __str__(self):
        return f"Beverage: {self.name}, Price: {self.price}, Size: {self.size}, Type: {self.type}"

class Dessert(MenuItem):
    def __init__(self, name:str, price:float):
        super().__init__(name, price)
    def __str__(self):
        return f"Dessert: {self.name}, Price: {self.price}"
    
class Order():
    def __init__(self, items: list[MenuItem]):
        self.items = items

    def add_item(self, item: MenuItem):
        self.items.append(item)
    
    #Defining a discount method that applies a 10% to 30% discount, based on items in the order
    #10% after 15 items, then 0.5% extra, maxes out at 30%
    def discount(self) -> float:
        n = len(self.items)
        if n > 15:
            extra_items = n - 15
            discount_percent = 10 + (extra_items * 0.5)
            if discount_percent > 30:
                discount_percent = 30
            return discount_percent
        else:
            return 0.0

    def get_bill(self) -> float:
        total = sum(item.price for item in self.items)
        discount_percent = self.discount()
        if discount_percent > 0:
            total -= total * (discount_percent / 100)
        return total
        
    def __str__(self):
        order_str = "Order\n-------------------\n"
        for item in self.items:
            order_str += str(item) + "\n"
        order_str += f"-------------------\nTotal Items: {len(self.items)}\n"

        order_str += f"-------------------\nTotal: {sum(item.price for item in self.items)}\n"

        order_str += f"-------------------\nDiscount: {self.discount()}%\n"

        order_str += f"-------------------\nNet Total: {self.get_bill():.2f}\n-------------------"
        return order_str
    
if __name__ == "__main__":

    #Usage case
    order = Order([
        Appetizer("Empanadas", 3.50),
        Appetizer("Cheese Sticks", 4.00),
        Appetizer("Mini Burgers", 5.00),
        Appetizer("Mini Waffles", 2.50),
        Appetizer("Salchipapa", 5.00),
        MainCourse("Baby Beef", 10.00, "Beef", "Rice", "Salad"),
        MainCourse("Cordon Blue", 12.00, "Chicken", "Potatoes", "Salad"),
        MainCourse("Salmon", 15.00, "Fish", "Quinoa", "Lettuce"),
        MainCourse("Burger", 8.00, "Beef", "Bread", "Onion"),
        Beverage("Coca Cola", 2.00, "Medium", "Soda"),
        Beverage("Orange Juice", 3.00, "Large", "Juice"),
        Beverage("Quatro", 2.50, "Small", "Soda"),
        Beverage("Chocolate Milkshake", 4.00, "Large", "Milkshake"),
        Dessert("Chocolate Cake", 5.00),
        Dessert("Nutella Waffles", 6.00),
        Dessert("Flan", 4.00),
        Dessert("Lemon Cheesecake", 5.00)
    ])
    #17 items, should apply a 11% discount
    
    print(order)



