from ro.ubb.applabstudents.domain.student import Student


class StudentService:
    def __init__(self, student_repository):
        self.__student_repository = student_repository

    def adaugare_student(self, id, nume, grupa):
        student = Student(id, nume, grupa)
        self.__student_repository.save(student)


    def modifica_student(self, id, nume, grupa):
        student = Student(id, nume, grupa)
        self.__student_repository.update(student)


    def stergere_student(self, id):
        self.__student_repository.delete_by_id(id)


    def find_by_id(self, id):
        return self.__student_repository.find_by_id(id)


    def afisare_studenti(self):
        return self.__student_repository.find_all()
