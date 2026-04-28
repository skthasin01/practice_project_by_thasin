from abc import ABC
from orders import Order
class User(ABC):
    def __init__(self,name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)

    def add_employee(self,resturent,employee):
        resturent.add_employee(employee)

    def view_employee(self,resturent):
        resturent.view_employee()

    def add_new_item(self,resturent,item):
        resturent.menu.add_menu_item(item)

    def remove_item(self,resturent,item):
        resturent.menu.remove_item(item)
    
    def view_menu(self,resturent):
        resturent.menu.show_menu()

class Employee(User):
    def __init__(self, name, phone, email, address,age, designation,salary):
        super().__init__(name, phone, email, address) 
        self.age = age
        self.designation = designation
        self.salary = salary

class Customers(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()

    def view_menu_item(self,resturent):
        resturent.menu.show_menu()
    
    def add_to_cart(self,resturent,item_name,quantity):
        item = resturent.menu.find_item(item_name)
        if item is not None:
            if quantity > item.quantity:
                print("Item quantity exceeded!!")
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print("Item Added to cart")
        else:
            print("Item not found")
    
    def view_cart(self):
        print("###View Cart###")
        print("Name\tPrice\tQuantity")
        for item,quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"Total price : {self.cart.total_price}")

    def pay_bill(self):
        print(f"Total {self.cart.total_price}")
        self.cart.clear()
