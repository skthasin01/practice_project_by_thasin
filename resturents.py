from menu import Menu
class Resturent:
    def __init__(self,name):
        self.name = name
        self.employees = [] # this is data-base
        self.menu = Menu()
           
    def add_employee(self,employee):
        self.employees.append(employee)
    
    def view_employee(self):
        print("Employee List!!")
        for emp in self.employees:
            print(emp.name,emp.email,emp.phone,emp.address)
