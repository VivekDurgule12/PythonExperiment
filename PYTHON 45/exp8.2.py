# Define the base class Person with attributes name and age
class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

# Define the derived class Employee that inherits from Person and adds employee_id
class Employee(Person):
    def _init_(self, name, age, employee_id):
        # Call the constructor of the base class with the given name and age
        super()._init_(name, age)
        self.employee_id = employee_id

# Create an instance of the Employee class
employee = Employee("John Doe", 30, 12345)

# Print out the name, age, and employee Id
print(f"Name: {employee.name}")
print(f"Age: {employee.age}")
print(f"Employee ID: {employee.employee_id}")
