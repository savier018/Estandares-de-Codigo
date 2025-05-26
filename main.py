from student_manager import StudentManager


def main():
    mgr = StudentManager()

    # 1. Create students
    mgr.add_student("x123", "Alice")
    mgr.add_student("y456", "")
    mgr.add_student("x123", "Bob")

    # 2. Add notes
    mgr.add_grade("x123", 95)
    mgr.add_grade("x123", 87.5)
    mgr.add_grade("x123", "nota")
    mgr.add_grade("x123", 105)
    mgr.add_grade("z999", 70)

    # 3. Eliminar nota inválida
    mgr.delete_grade("x123", 5)

    # 4. Informes
    mgr.report_student("x123")
    mgr.report_all()


if __name__ == "__main__":
    main()
