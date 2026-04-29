class Employee:
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
emp1 = Employee("Sneha", 25000)
emp2 = Employee("Anu", 30000)
emp1.display()
print()   
emp2.display()