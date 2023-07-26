class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        if subject not in self.grades:
            self.grades[subject] = []
        self.grades[subject].append(grade)

    def average_grade(self, subject):
        if subject in self.grades:
            return sum(self.grades[subject]) / len(self.grades[subject])
        else:
            return 0

    def display_details(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        for subject, grades in self.grades.items():
            average = sum(grades) / len(grades) if grades else 0
            print(f"{subject} - Average Grade: {average:.2f}")


class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name):
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name)
            print(f"Student {name} with ID {student_id} has been added to the system.")
        else:
            print("Student with this ID already exists.")

    def show_student_details(self, student_id):
        if student_id in self.students:
            self.students[student_id].display_details()
        else:
            print("Student not found.")

    def show_student_average_grade(self, student_id, subject):
        if student_id in self.students:
            average_grade = self.students[student_id].average_grade(subject)
            print(f"Student {self.students[student_id].name}'s average grade for {subject}: {average_grade:.2f}")
        else:
            print("Student not found.")


# ტესტირება
system = StudentManagementSystem()
system.add_student(1, "John Doe")
system.add_student(2, "Jane Smith")

system.students[1].add_grade("Math", 95)
system.students[1].add_grade("Math", 88)
system.students[1].add_grade("History", 78)
system.students[1].add_grade("History", 85)

system.students[2].add_grade("Math", 92)
system.students[2].add_grade("History", 79)

system.show_student_details(1)
system.show_student_average_grade(1, "Math")
system.show_student_details(2)
system.show_student_average_grade(2, "History")