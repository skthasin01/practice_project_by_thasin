from fooditem import FoodItem
from menu import Menu
from user_up_v2 import Customers,Admin,Employee
from resturents import Resturent
from orders import Order

mama_vagne = Resturent("MAMA VAGNE Resturent")

def customer_menu():
    name = input("Enter your name: ")
    email = input("Enter your email address: ")
    phone = input("Enter your phone number: ")
    address = input("Enter your present address: ")
    customer = Customers(name=name,phone=phone,email=email,address=address)
    
    while True:
        print(f"Welcome {customer.name}")
        print("1. View Menu")
        print("2. Add item to cart")
        print("3. View cart")
        print("4. PayBill")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1 :
            customer.view_menu_item(mama_vagne)
        elif choice == 2:
            item_name = input("Enter item name:")
            item_quantity = int(input("Enter item quantity: "))
            customer.add_to_cart(mama_vagne,item_name,item_quantity)

        elif choice == 3 :
            customer.view_cart()
        elif choice == 4 :
            customer.pay_bill()
        elif choice == 5:
            break
        else:
            print("Invalid Choice")


def admin_menu():
    name = input("Enter your name: ")
    email = input("Enter your email address: ")
    phone = input("Enter your phone number: ")
    address = input("Enter your present address: ")
    admin = Admin(name=name,phone=phone,email=email,address=address)
    
    while True:
        print(f"Welcome {admin.name}")
        print("1. Add new item")
        print("2. Add new Employee")
        print("3. View Employee")
        print("4. View Item")
        print("5. Delete Item")
        print("6. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1 :
            item_name = input("Enter item name: ")
            item_price = int(input("Enter item price: "))
            item_quantity = int(input("Enter item quantity: "))
            item = FoodItem(item_name,item_price,item_quantity)
            admin.add_new_item(mama_vagne,item)
            
        elif choice == 2:
            name = input("Enter Employee name: ")
            phone = input("Enter Employee phone number: ")
            email = input("Enter Employee email address: ")
            address = input("Enter Employee present address: ")
            age = int(input("Enter Employee age: "))
            designation = input("Enter Employee designation: ")
            salary = int(input("Enter Employee salary: "))
            
            employee = Employee(name,phone,email,address,age,designation,salary)
            admin.add_employee(mama_vagne,employee)

        elif choice == 3 :
            admin.view_employee(mama_vagne)
        elif choice == 4 :
            admin.view_menu(mama_vagne)
        elif choice == 5:
            item_name = input("Enter item name: ")
            admin.remove_item(mama_vagne,item_name)
            print(f"{item_name} deleted!!")
        elif choice == 6:
            break
        else:
            print("Invalid Choice")

while True:
    print("Welcome!!")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    choice = int(input('Enter your choice: '))
    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid input")


