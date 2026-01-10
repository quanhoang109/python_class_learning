"""
Exercise 9: Employee System

Create an employee management system:

Base class `Employee`:
- Attributes: name, employee_id, base_salary
- Methods: calculate_salary(), display_info()

Child classes:
- FullTimeEmployee(Employee) - gets full salary + benefits ($500)
- PartTimeEmployee(Employee) - hours_worked * hourly_rate
- Contractor(Employee) - project_fee (fixed amount)

Override calculate_salary() in each child class.
"""

# TODO: Write your Employee, FullTimeEmployee, PartTimeEmployee, and Contractor classes here
class Employee:
    def __init__(self, name, employee_id, base_salary):
        self.name = name
        self.employee_id = employee_id
        self.base_salary = base_salary

    def calculate_salary(self):
        pass
    def display_info(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, Salary: ${self.calculate_salary():.2f}")
class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, base_salary):
        super().__init__(name, employee_id, base_salary)
    def calculate_salary(self):
        benefits = 500
        return self.base_salary + benefits
    
class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id, 0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked
    
class Contractor(Employee):
    def __init__(self, name, employee_id, project_fee):
        super().__init__(name, employee_id, 0)
        self.project_fee = project_fee
    def calculate_salary(self):
        return self.project_fee 

# Test code (uncomment when ready)
employees = [
    FullTimeEmployee("Alice", "E001", 5000),
    PartTimeEmployee("Bob", "E002", 25, 80),
    Contractor("Charlie", "E003", 8000)
]

for emp in employees:
    emp.display_info()
