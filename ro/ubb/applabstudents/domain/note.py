from ro.ubb.applabstudents.domain.base_entity import BaseEntity


class Nota(BaseEntity):
    def __init__(self, student_id, nr_lab, nr_problema, nota):
        super().__init__((student_id, nr_lab, nr_problema))
        self.__student_id = student_id
        self.__nr_lab = nr_lab
        self.__nr_problema = nr_problema
        self.__nota = nota

    def get_student_id(self):
        return self.__student_id

    def get_nr_lab(self):
        return self.__nr_lab

    def get_nr_problema(self):
        return self.__nr_problema

    def get_nota(self):
        return self.__nota

    def set_nota(self, nota):
        self.__nota = nota
    def __str__(self):
        return "Id-ul studentului" + str(self.__student_id) + "Numar laborator: " + str(self.__nr_lab) + " Numar problema: " + str(self.__nr_problema) + " Nota: " + str(self.__nota)
