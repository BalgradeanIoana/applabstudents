from ro.ubb.applabstudents.domain.lab import Laborator


class LaboratorService:
    def __init__(self, lab_repository):
        self.__lab_repository = lab_repository

    def adaugare_laborator(self, nr_lab, nr_problema, descriere, deadline):
        laborator = Laborator(nr_lab, nr_problema, descriere,deadline)
        self.__lab_repository.save(laborator)


    def modifica_laborator(self, nr_lab, nr_problema, descriere, deadline):
        lab = Laborator(nr_lab, nr_problema, descriere, deadline)
        self.__lab_repository.update(lab)


    def stergere_lab(self, nr_lab, nr_problema):
        id = (nr_lab, nr_problema)
        self.__lab_repository.delete_by_id(id)


    def find_by_id(self, nr_lab, nr_problema):
        id = (nr_lab, nr_problema)
        return self.__lab_repository.find_by_id(id)


    def afisare_laboratoare(self):
        return self.__lab_repository.find_all()

