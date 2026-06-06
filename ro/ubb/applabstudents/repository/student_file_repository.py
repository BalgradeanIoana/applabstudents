from ro.ubb.applabstudents.domain.exceptions import ValidatorException, IdDuplicat
from ro.ubb.applabstudents.domain.student import Student
from ro.ubb.applabstudents.repository.studentsrepository import StudentRepository


class StudentFileRepository(StudentRepository):
    def __init__(self,validator, filename):
        super().__init__(validator)
        self.__filename = filename
        self.__load_data()

    def __load_data(self):
        with open(self.__filename) as f:
            for linie in f:
                lista_student = linie.split(",")
                try:
                    student = Student(int(lista_student[0]), lista_student[1], int(lista_student[2]))
                    super().save(student)
                except ValidatorException as ve:
                    print(ve)
                except IdDuplicat as id:
                    print(id)
                except ValueError:
                    print("Id-ul si grupa trebuie sa fie numere")

    def save(self, student):
        try:
            super().save(student)
            self.__add_to_file(student)
        except ValidatorException as ve:
            print(ve)

    def __add_to_file(self, student):
        with open(self.__filename, "a") as f:
            string_student = str(
                student.get_id()) + "," + student.get_nume() + "," + str(student.get_grupa()) + "\n"
            f.write(string_student)

    def update(self, student_modificat):
        super().update(student_modificat)
        self.__rewrite()

    def delete_by_id(self, id):
        super().delete_by_id(id)
        self.__rewrite()


    def __rewrite(self):
        all_students = self.find_all()
        with open(self.__filename, "w") as f:
            for student in all_students:
                string_student = str(
                    student.get_id()) + "," + student.get_nume() + "," + str(student.get_grupa()) + "\n"
                f.write(string_student)