from ro.ubb.applabstudents.domain.exceptions import IdDuplicat, EntitateInexistenta


class StudentRepository:
    def __init__(self, validator):
        self.__validator = validator
        self.__all_students = []

    def find_all(self):
        return self.__all_students

    def save(self, student):
        self.__validator.validate(student)
        if self.find_by_id(student.get_id()) is not None:
            raise IdDuplicat("Acest id exista deja, incercati altul.")
        self.__all_students.append(student)

    def update(self, student_modificat):
        self.__validator.validate(student_modificat)
        if self.find_by_id(student_modificat.get_id()) is None:
            raise EntitateInexistenta("Nu exista nici un student cu acest Id")
        self.__all_students[:] = [student_modificat if student.get_id() == student_modificat.get_id() else student for student in self.__all_students]

    def delete_by_id(self, id):
        if self.find_by_id(id) is None:
            raise EntitateInexistenta("Nu exista nici un student cu acest Id")
        self.__all_students[:] = [student for student in self.__all_students if student.get_id() != id]

    def find_by_id(self, id):
        for student in self.__all_students:
            if student.get_id() == id:
                return student
        return None



