from ro.ubb.applabstudents.domain.exceptions import IdDuplicat, EntitateInexistenta, ValidatorException


class ConsolaNota():
    def __init__(self, nota_service):
        self.__nota_service = nota_service

    def ui_adauga_nota(self, student_id, nr_lab, nr_problema, nota):
        try:
            student_id = int(student_id)
            nr_lab = int(nr_lab)
            nr_problema = int(nr_problema)
            nota =  int(nota)
            self.__nota_service.adaugare_nota(student_id, nr_lab, nr_problema, nota)
        except ValueError:
            print("Date incorecte. Asigurativa ca nr laboratorului, nr problemei si id-ul studentului sunt numere!!")
        except IdDuplicat as nld:
            print(nld)
        except ValidatorException as ve:
            print(ve)


    def ui_modifica_nota(self, student_id, nr_lab, nr_problema, nota):
        try:
            student_id = int(student_id)
            nr_lab = int(nr_lab)
            nr_problema = int(nr_problema)
            nota = int(nota)
            self.__nota_service.modifica_nota(student_id, nr_lab, nr_problema, nota)
        except ValueError:
            print("Date incorecte. Asigurativa ca nr laboratorului, nr problemei si deadline-ul sunt numere!!")
        except EntitateInexistenta as li:
            print(li)
        except ValidatorException as ve:
            print(ve)


    def ui_sterge_nota(self, student_id, nr_lab, nr_problema):
        try:
            student_id = int(student_id)
            nr_lab = int(nr_lab)
            nr_problema = int(nr_problema)
            self.__nota_service.stergere_nota(student_id, nr_lab, nr_problema)
        except ValueError:
            print("Date incorecte. Asigurativa ca nr laboratorului, nr problemei si id-ul studentului sunt numere!!")
        except EntitateInexistenta as li:
            print(li)



    def ui_afisare_note(self):
        all_grades = self.__nota_service.afisare_note()
        for laborator in all_grades:
            print(laborator)
