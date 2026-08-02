class StudentRecord:
    college_name = "MIT ADT University"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 75:
            return "A"
        elif self.marks >= 60:
            return "B"
        elif self.marks >= 40:
            return "C"
        else:
            return "Fail"

    def display_details(self):
        print(f"Name : {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.grade()}")      
        print("-" * 30)

    @staticmethod
    def check_pass(marks):
        return marks >= 40

    def __str__(self):
        return f"Student Name: {self.name} | Marks: {self.marks} | Grade: {self.grade()}"   


s1 = StudentRecord("Amit", 80)
s2 = StudentRecord("Jeetoom", 90)

print("College:", StudentRecord.college_name)
print()

s1.display_details()
s2.display_details()

print("Pass Status:")
print("30 Marks :", StudentRecord.check_pass(30))
print("85 Marks :", StudentRecord.check_pass(85))
print()

print(s1)
print(s2)


def result_decorator(func):
    def wrapper(*args, **kwargs):
        print("\n========== RESULT ==========")
        result = func(*args, **kwargs)
        print("============================")
        return result
    return wrapper


@result_decorator
def check_result(student):
    if StudentRecord.check_pass(student.marks):
        print(student.name, "PASSED")
    else:
        print(student.name, "FAILED")


check_result(s1)
check_result(s2)


class RollIterator:
    def __init__(self, max_roll):
        self.max_roll = max_roll

    def __iter__(self):
        self.current = 1
        return self

    def __next__(self):
        if self.current <= self.max_roll:
            roll = self.current
            self.current += 1
            return roll
        else:
            raise StopIteration


print("\nRoll Numbers using Iterator")
for roll in RollIterator(5):
    print("Roll No:", roll)


def generate_roll_numbers(max_roll):
    current = 1
    while current <= max_roll:
        yield current
        current += 1


print("\nRoll Numbers using Generator")
for roll in generate_roll_numbers(5):
    print("Roll No:", roll)