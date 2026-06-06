from ro.ubb.applabstudents.domain.exceptions import IdDuplicat, EntitateInexistenta


class ConsolaStudent():
    def __init__(self, student_service):
        self.__student_service = student_service

    def ui_adauga_student(self, id, nume, grupa):
        try:
            id = int(id)
            grupa = int(grupa)
            self.__student_service.adaugare_student(id, nume, grupa)
        except ValueError:
            print("Date incorecte. Asigurativa ca Id-ul si grupa sunt numere!!")
        except IdDuplicat as i:
            print(i)


    def ui_modificare_student(self, id,  nume, grupa):
        try:
            id = int(id)
            grupa = int(grupa)
            self.__student_service.modifica_student(id, nume, grupa)
        except ValueError:
            print("Date incorecte. Asigurativa ca Id-ul si grupa sunt numere!!")
        except EntitateInexistenta as si:
            print(si)


    def ui_stergere_student(self, id):
        try:
            id = int(id)
            self.__student_service.stergere_student(id)
        except ValueError:
            print("Date incorecte. Asigurativa ca Id-ul este numar!!")
        except EntitateInexistenta as si:
            print(si)


    def ui_afisare_studenti(self):
        all_students = self.__student_service.afisare_studenti()
        for student in all_students:
            print(student)