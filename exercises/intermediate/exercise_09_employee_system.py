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


# Test code (uncomment when ready)
# employees = [
#     FullTimeEmployee("Alice", "E001", 5000),
#     PartTimeEmployee("Bob", "E002", 25, 80),
#     Contractor("Charlie", "E003", 8000)
# ]
#
# for emp in employees:
#     emp.display_info()
