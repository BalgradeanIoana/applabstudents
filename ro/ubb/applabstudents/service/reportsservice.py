from functools import reduce

from ro.ubb.applabstudents.service.dto import Converters, NumeNotaDto
from ubb.applabstudents.domain.exceptions import EntitateInexistenta


class ReportsService:
    def __init__(self, student_repository, lab_repository, nota_repository):
        self.__student_repository = student_repository
        self.__lab_repository = lab_repository
        self.__nota_repository = nota_repository
    def get_studenti_nota_lab(self, nr_lab, nr_problema):
        """
        :return: Returneaza toti studentii (care au nota) si nota de la o anumita problema de laborator,
         sortati in ordine descrescatoare dupa nota si in ordine alfabetica dupa nume(in cazul in care doi studenti au acesi nota)
        Return DTOs (student_name, nota).
        """
        nr_lab = int(nr_lab)
        nr_problema = int(nr_problema)
        dtos = []
        note = self.__nota_repository.find_all()
        for nota in note:
            if nota.get_id()[1] == nr_lab and nota.get_id()[2] == nr_problema:
                student = self.__student_repository.find_by_id(nota.get_id()[0])
                dto = Converters.create_studenti_nota_lab(student, nota.get_nota())
                dtos.append(dto)
        dtos = self.__get_sorted_studenti_nota_lab(dtos)
        if len(dtos) == 0:
            raise EntitateInexistenta("Nu exista studenti cu note la acest laborator")
        return dtos

    def get_studenti_nota_sub_5(self):
        dtos = []
        studenti = self.__student_repository.find_all()
        for student in studenti:
            medie = self.__calculeaza_media(student)
            if medie < 5:
                dto = Converters.create_studenti_nota_lab(student, medie)
                dtos.append(dto)
        if len(dtos) == 0:
            raise EntitateInexistenta("Nu exista studenti cu media sub 5")
        dtos = self.__get_sorted_studenti_nota_lab(dtos)
        return dtos

    def __calculeaza_media(self, student):
        all_grades = self.__nota_repository.find_all()
        note_student = list(filter(lambda x: x.get_id()[0] == student.get_id(), all_grades))
        n = len(note_student)
        if n == 0:
            return 0
        medie = reduce(lambda x, y: x + y.get_nota() / n, note_student, 0)
        return medie


    @staticmethod
    def __get_sorted_studenti_nota_lab(dtos):
        def less_than(dto1, dto2):
            if dto1.nota < dto2.nota:
                return False
            if dto1.nota == dto2.nota:
                return dto1.get_nume < dto2.get_nume
            return True

        NumeNotaDto.__lt__ = less_than
        dtos = sorted(dtos)
        NumeNotaDto.__lt__ = object.__lt__
        return dtos
