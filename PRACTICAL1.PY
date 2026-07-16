class Student:
    def __init__(self, name, roll_no, student_class, marks):
        self.name = name
        self.roll_no = roll_no
        self.student_class = student_class
        self.marks = marks

    def study(self):
        print(self.name, "is studying.")

    def score_good_marks(self):
        print(self.name, "scored",
              self.marks,"marks.")
        
student1 = Student("Ram", 1, "CSE", 85)
student2 = Student("Shyam", 2, "CSE", 90)
student3 = Student("Sita", 3, "CSE", 80)

student1.study()
student2.study()
student3.study()

student1.score_good_marks()
student2.score_good_marks()
student3.score_good_marks()
