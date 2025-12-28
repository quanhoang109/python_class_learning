"""
Exercise 3: Student Class

Create a `Student` class with:
- Attributes: name, student_id, grades (list)
- Methods:
  - add_grade(grade) - add grade to list (0-100 validation)
  - get_average() - return average of all grades
  - get_letter_grade() - convert average to letter (A/B/C/D/F)
  - display_report_card() - show all info
"""

# TODO: Write your Student class here
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print("Grade must be between 0 and 100.")

    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def get_letter_grade(self):
        average = self.get_average()
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

    def display_report_card(self):
        print(f"Student Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {self.get_average():.2f}")
        print(f"Letter Grade: {self.get_letter_grade()}")


# Test code (uncomment when ready)
student = Student("Alice", "S12345")
student.add_grade(85)
student.add_grade(92)
student.add_grade(88)
student.display_report_card()
