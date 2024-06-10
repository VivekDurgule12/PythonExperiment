class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def assign_department(self, new_department):
        self.emp_department = new_department

    def calculate_emp_salary(self, hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = overtime * (self.emp_salary / 50)
            return self.emp_salary + overtime_amount
        else:
            return self.emp_salary

    def print_employee_details(self):
        print(f"ID: {self.emp_id}, Name: {self.emp_name}, Salary: ${self.emp_salary}, Department: {self.emp_department}")

# Sample Employee Data
employees = [
    Employee("E7876", "ADAMS", 50000, "ACCOUNTING"),
    Employee("E7499", "JONES", 45000, "RESEARCH"),
    Employee("E7900", "MARTIN", 50000, "SALES"),
    Employee("E7698", "SMITH", 55000, "OPERATIONS")
]

# Demonstration
for emp in employees:
    emp.print_employee_details()

print("\nAfter changing department and calculating salary with overtime:")

for emp in employees:
    emp.assign_department("NEW_DEPARTMENT")
    new_salary = emp.calculate_emp_salary(55)  # Example: 55 hours worked
    emp.print_employee_details()
    print(f"New Salary with Overtime: ${new_salary:.2f}")
    print()
