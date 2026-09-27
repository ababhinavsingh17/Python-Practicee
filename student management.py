class Student:
    def __init__(self, name, rollno, marks1, marks2):
        self.name = name
        self.rollno = rollno
        self.m1 = marks1
        self.m2 = marks2
students = []
def add_student():
    name = input("Enter name: ")
    rollno = input("Enter roll number: ")
    m1 = int(input("Enter marks1: "))
    m2 = int(input("Enter marks2: "))
    students.append(Student(name, rollno, m1, m2))
def display_students():
    for s in students:
        print(f"Name: {s.name}, RollNo: {s.rollno}, Marks1: {s.m1}, Marks2: {s.m2}")
def search_student(rollno):
    for s in students:
        if s.rollno == rollno:
            return s
    return None
def delete_student(rollno):
    s = search_student(rollno)
    if s:
        students.remove(s)
