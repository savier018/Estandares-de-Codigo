class Student:
    # Represents a student with grades and evaluation methods.
    def __init__(self, student_id: str, name: str):
        if not student_id.strip():
            raise ValueError("Student ID cannot be empty.")
        if not name.strip():
            raise ValueError("Student name cannot be empty.")
        self.student_id = student_id
        self.name = name
        self.grades: list[float] = []
        self.honor: bool = False
        self.is_passed: bool = False

    # Adds a grade to the student's record.
    def add_grade(self, grade):
        try:
            grade = float(grade)
        except (TypeError, ValueError):
            print(f"[Error] Grade must be a number (0–100). Got: {grade!r}")
            return
        if not (0 <= grade <= 100):
            print(f"[Error] Grade out of range 0–100. Got: {grade}")
            return
        self.grades.append(grade)

    # Calculates the average of the student's grades.
    def calculate_average(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    # Returns the letter grade based on the average.
    def get_letter_grade(self) -> str:
        avg = self.calculate_average()
        if avg >= 90:
            return 'A'
        if avg >= 80:
            return 'B'
        if avg >= 70:
            return 'C'
        if avg >= 60:
            return 'D'
        return 'F'

    # Evaluates the student's performance based on grades.
    def evaluate(self):
        avg = self.calculate_average()
        self.honor = (avg >= 90)
        self.is_passed = (avg >= 60)

    # Deletes a grade by index.
    def delete_grade(self, index: int):
        try:
            del self.grades[index]
        except IndexError:
            print(f"[Error] Cannot delete grade: index {index}")

    # Generates a report of the student's performance.
    def report(self):
        self.evaluate()
        print(f"--- Report for {self.student_id} ---")
        print(f"Name           : {self.name}")
        print(f"Grades Count   : {len(self.grades)}")
        print(f"Grades         : {self.grades}")
        print(f"Average        : {self.calculate_average():.2f}")
        print(f"Letter Grade   : {self.get_letter_grade()}")
        print(f"Honor Roll     : {'Yes' if self.honor else 'No'}")
        print(f"Pass/Fail      : {'Passed' if self.is_passed else 'Failed'}")
        print("------------------------------\n")
