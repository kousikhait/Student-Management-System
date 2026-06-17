
import csv
from abc import ABC, abstractmethod


class Person(ABC):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def display(self):
        pass



class Student(Person):

    def __init__(self, student_id, name, age, course, marks):
        super().__init__(name, age)

        self.__student_id = student_id  
        self.course = course
        self.marks = marks

    def get_student_id(self):
        return self.__student_id

    def set_marks(self, marks):
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    
    def display(self):

        print("\n----------------------------")
        print(f"Student ID : {self.__student_id}")
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Course     : {self.course}")
        print(f"Marks      : {self.marks}")
        print(f"Average    : {self.average():.2f}")
        print("----------------------------")


# Student Manager Class
class StudentManager:

    def __init__(self):
        self.students = []

    # Add Student
    def add_student(self, student):
        self.students.append(student)
        print("Student Added Successfully!")

    # View All Students
    def view_students(self):

        if not self.students:
            print("No Students Found!")
            return

        for student in self.students:
            student.display()

    # Search Student
    def search_student(self, student_id):

        for student in self.students:
            if student.get_student_id() == student_id:
                return student

        return None

    # Update Marks
    def update_marks(self, student_id, marks):

        student = self.search_student(student_id)

        if student:
            student.set_marks(marks)
            print("Marks Updated Successfully!")
        else:
            print("Student Not Found!")

    # Delete Student
    def delete_student(self, student_id):

        student = self.search_student(student_id)

        if student:
            self.students.remove(student)
            print("Student Deleted Successfully!")
        else:
            print("Student Not Found!")

    # Export Report to CSV
    def export_to_csv(self):

        with open("students_report.csv", "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Student ID",
                "Name",
                "Age",
                "Course",
                "Marks",
                "Average"
            ])

            for student in self.students:

                writer.writerow([
                    student.get_student_id(),
                    student.name,
                    student.age,
                    student.course,
                    ",".join(map(str, student.marks)),
                    round(student.average(), 2)
                ])

        print("Report Exported Successfully!")
        print("File Name: students_report.csv")


# Main Function
def main():

    manager = StudentManager()

    while True:

        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Calculate Average")
        print("7. Export Report to CSV")
        print("8. Exit")

        choice = input("Enter Choice: ")

        # Add Student
        if choice == "1":

            sid = int(input("Student ID: "))
            name = input("Name: ")
            age = int(input("Age: "))
            course = input("Course: ")

            marks = []

            for i in range(3):
                mark = float(input(f"Subject {i+1} Marks: "))
                marks.append(mark)

            student = Student(
                sid,
                name,
                age,
                course,
                marks
            )

            manager.add_student(student)

        # View Students
        elif choice == "2":
            manager.view_students()

        # Search Student
        elif choice == "3":

            sid = int(input("Enter Student ID: "))

            student = manager.search_student(sid)

            if student:
                student.display()
            else:
                print("Student Not Found!")

        # Update Marks
        elif choice == "4":

            sid = int(input("Enter Student ID: "))

            marks = []

            for i in range(3):
                mark = float(input(f"New Subject {i+1} Marks: "))
                marks.append(mark)

            manager.update_marks(sid, marks)

        # Delete Student
        elif choice == "5":

            sid = int(input("Enter Student ID: "))
            manager.delete_student(sid)

        # Calculate Average
        elif choice == "6":

            sid = int(input("Enter Student ID: "))

            student = manager.search_student(sid)

            if student:
                print(f"Average Marks: {student.average():.2f}")
            else:
                print("Student Not Found!")

        # Export CSV
        elif choice == "7":
            manager.export_to_csv()

        # Exit
        elif choice == "8":
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    main()

