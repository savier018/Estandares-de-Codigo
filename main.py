class Student:

    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = []
        self.isPassed = False
        self.honor = False

    def addGrade(self, grade):
        if isinstance(grade, (int, float)):
            self.grades.append(grade)
        else:
            print(f"Invalid grade type: {grade} (must be numeric)")

    def calculateAverageGrade(self):
        if not self.grades:
            return 0.0
        total = sum(self.grades)
        return total / len(self.grades)

    def checkHonor(self):
        average = self.calculateAverageGrade()
        self.honor = average > 90

    def deleteGrade(self, index):
        try:
            del self.grades[index]
        except IndexError:
            print(f"Invalid index: {index}")

    def report(self):
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Grades Count: {len(self.grades)}")
        print(f"Average Grade: {self.calculateAverageGrade():.2f}")
        print(f"Honor Roll: {'Yes' if self.honor else 'No'}")


def main():
    student = Student("x123", "Alice")
    student.addGrade(100)
    student.addGrade("Fifty")
    student.checkHonor()
    student.deleteGrade(5)
    student.report()


if __name__ == "__main__":
    main()
