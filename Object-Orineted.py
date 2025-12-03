import re

class Student:
    def __init__(self, name, email, grades):
        self.name = name
        self.email = email
        self.grades = grades

    def addGrades(self, grade):
        self.grades.append(grade)

    def aveGrades(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def displayInfo(self):
        print("Student Name:", self.name)
        print("Email:", self.email)
        print("Grades:", self.grades)
        print("Average:", self.aveGrades())

    def grades_tuple(self):
        return tuple(self.grades)

    def add_grade(self, grade):
        self.addGrades(grade)

    def average_grade(self):
        return self.aveGrades()

    def display_info(self):
        self.displayInfo()


student1 = Student("Alice Johnson", "alice@email.com", [90, 85])
student1.addGrades(95)
student1.addGrades(100)
student1.displayInfo()

student2 = Student("Bob Smith", "bob@email.com", [88, 92, 79])
student2.addGrades(85)
student2.addGrades(90)
student2.displayInfo()

student3 = Student("Carla Diaz", "carla@email.com", [75, 83])
student3.addGrades(95)
student3.addGrades(89)
student3.displayInfo()

student_dict = {
    "alice@email.com": student1,
    "bob@email.com": student2,
    "carla@email.com": student3
}

def get_student_by_email(email):
    return student_dict.get(email)

students = [student1, student2, student3]
unique_grades = {grade for s in students for grade in s.grades}
print("Unique grades across all students:", unique_grades)

print("\n--- Demonstrating Tuple Immutability ---")
alice_tuple = student1.grades_tuple()
print("Grades as tuple for Alice:", alice_tuple)
try:
    alice_tuple[0] = 999
except TypeError:
    print("Tuples are immutable — you cannot change their contents once created.")

print("\n--- Part 5: List Operations ---")
for s in students:
    removed = s.grades.pop()
    print(f"Removed last grade ({removed}) from {s.name}'s list.")
    if s.grades:
        first = s.grades[0]
        last = s.grades[-1]
        print(f"First grade: {first}, Last grade: {last}")
    else:
        print("No grades left in the list!")
    print(f"{s.name} now has {len(s.grades)} grades remaining.")
    print("-" * 40)

print("\n--- Bonus ---")
def is_valid_email(email):
    return re.fullmatch(r"^[\w\.-]+@[\w\.-]+\.com$", email) is not None

for s in students:
    print(f"{s.email} valid? {is_valid_email(s.email)}")

above_90 = sum(1 for s in students for g in s.grades if g > 90)
print("Count of grades > 90 across all students:", above_90)
