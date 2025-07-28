class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.marks = {}

    def add_mark(self, subject, score):
        self.marks[subject] = score

    def average_score(self):
        if not self.marks:
            return 0
        return sum(self.marks.values()) / len(self.marks)

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print("Marks:")
        for subject, score in self.marks.items():
            print(f"  {subject}: {score}")
        print(f"Average Score: {self.average_score():.2f}")
        print("-" * 30)

student1 = Student("Alice", "S101")
student1.add_mark("Math", 85)
student1.add_mark("Physics", 90)

student2 = Student("Bob", "S102")
student2.add_mark("Math", 75)
student2.add_mark("Chemistry", 80)
student2.add_mark("Biology", 70)

student1.display_info()
student2.display_info()
