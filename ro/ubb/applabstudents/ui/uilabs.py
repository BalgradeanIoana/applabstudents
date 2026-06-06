from ro.ubb.applabstudents.domain.exceptions import IdDuplicat, EntitateInexistenta, ValidatorException


class ConsolaLaborator():
    def __init__(self, laborator_service):
        self.__laborator_service = laborator_service

    def ui_adauga_laborator(self, nr_lab, nr_problema, descriere, deadline):
        try:
            nr_lab = int(nr_lab)
            nr_problema = int(nr_problema)
            deadline =  int(deadline)
            self.__laborator_service.adaugare_laborator(nr_lab, nr_problema, descriere, deadline)
        except ValueError:
            print("Date incorecte. Asigurativa ca nr laboratorului, nr problemei si deadline-ul sunt numere!!")
        except IdDuplicat as nld:
            print(nld)
        except ValidatorException as ve:
            print(ve)


    def ui_modifica_laborator(self, nr_lab, nr_problema, descriere, deadline):
        try:
            nr_lab = int(nr_lab)
            nr_problema = int(nr_problema)
            deadline = int(deadline)
            self.__laborator_service.modifica_laborator(nr_lab, nr_problema, descriere,deadline)
        except ValueError:
            print("Date incorecte. Asigurativa ca nr laboratorului, nr problemei si deadline-ul sunt numere!!")
        except EntitateInexistenta as li:
            print(li)
        except ValidatorException as ve:
            print(ve)


    def ui_sterge_laborator(self, nr_lab, nr_problema):
        try:
            nr_lab = int(nr_lab)
            nr_problema = int(nr_problema)
            self.__laborator_service.stergere_lab(nr_lab, nr_problema)
        except ValueError:
            print("Date incorecte. Asigurativa ca nr laboratorului este numar!!")
        except EntitateInexistenta as li:
            print(li)


    def ui_afisare_laboratoare(self):
        all_labs = self.__laborator_service.afisare_laboratoare()
        for laborator in all_labs:
            print(laborator)
