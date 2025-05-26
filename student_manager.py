from student import Student


class StudentManager:
    # Manages multiple students and their grades.
    def __init__(self):
        self._students: dict[str, Student] = {}

    # Adds a new student to the manager.
    # If the student ID already exists, it will not add the student.
    # If the name is empty, it will raise an error.
    def add_student(self, student_id: str, name: str):
        if student_id in self._students:
            print(f"[Error] Student ID '{student_id}' already exists.")
            return
        try:
            student = Student(student_id, name)
        except ValueError as e:
            print(f"[Error] {e}")
            return
        self._students[student_id] = student
        print(f"[Info] Added student: {student_id} – {name}")

    # Adds a grade to a student's record.
    def add_grade(self, student_id: str, grade):
        student = self._students.get(student_id)
        if not student:
            print(f"[Error] No student found with ID '{student_id}'.")
            return
        student.add_grade(grade)

    # Deletes a grade from a student's record by index.
    def delete_grade(self, student_id: str, index: int):
        student = self._students.get(student_id)
        if not student:
            print(f"[Error] No student found with ID '{student_id}'.")
            return
        student.delete_grade(index)

    # Generates a report for a specific student or all students.
    def report_student(self, student_id: str):
        student = self._students.get(student_id)
        if not student:
            print(f"[Error] No student found with ID '{student_id}'.")
            return
        student.report()

    # Generates reports for all students.
    def report_all(self):
        if not self._students:
            print("[Info] No students to report.")
            return
        for student in self._students.values():
            student.report()
