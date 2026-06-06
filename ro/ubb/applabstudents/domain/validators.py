from ro.ubb.applabstudents.domain.exceptions import ValidatorException


class StudentValidator:
    def validate(self, student):
        id = int(student.get_id())
        if id < 1:
            raise ValidatorException("Id-ul trebuie sa fie un numar pozitiv")
        grupa = int(student.get_grupa())
        if grupa < 100 or grupa > 5000:
            raise ValidatorException("Grupa trebuie sa fie un numar intre 100 si 5000")


class LabValidator:
    def validate(self, lab):
        id = (int(lab.get_id()[0]), int(lab.get_id()[1]))
        if id[0] < 1 or id[1] < 1:
            raise ValidatorException("Numarul laboratorului si al problemei trebuie sa fie numere pozitive")
        deadline = int(lab.get_deadline())
        if deadline < 1 or deadline > 14:
            raise ValidatorException("Deadline-ul trebuie sa fi ecuprins intre 1 si 14")


class NotaValidator:
    def validate(self, nota):
        id = (int(nota.get_id()[0]), int(nota.get_id()[1]), int(nota.get_id()[2]))
        if id[0] < 1 or id[1] < 1 or id[2] < 1:
            raise ValidatorException("Numarul laboratorului, al problemei si id-ul studentului trebuie sa fie numere pozitive")
        nota = int(nota.get_nota())
        if nota < 1 or nota > 10:
            raise ValidatorException("Nota trebuie sa fie cuprinsa intre 1 si 10")
