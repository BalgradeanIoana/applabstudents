from dataclasses import dataclass


class Converters:
    @staticmethod
    def create_studenti_nota_lab(student, nota):
        return NumeNotaDto(student.get_nume(), nota)


@dataclass
class NumeNotaDto:
    __nume: str
    __nota: int

    @property
    def nume(self):
        return self.__nume

    @property
    def nota(self):
        return self.__nota
    def __str__(self):
        return "Numele studentului: " + self.__nume + " nota: " + str(self.__nota)