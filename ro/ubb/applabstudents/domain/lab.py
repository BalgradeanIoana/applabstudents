from ro.ubb.applabstudents.domain.base_entity import BaseEntity


class Laborator(BaseEntity):
    def __init__(self, nr_lab, nr_problema, descriere, deadline):
        super().__init__((nr_lab, nr_problema))
        self.__nr_lab = nr_lab
        self.__nr_problema = nr_problema
        self.__descriere = descriere
        self.__deadline = deadline
    def get_nr_lab(self):
        return self.__nr_lab

    def get_nr_problema(self):
        return self.__nr_problema

    def get_descriere(self):
        return self.__descriere

    def get_deadline(self):
        return self.__deadline

    def set_nr_lab(self, nr_lab):
        self.__nr_lab = nr_lab

    def set_nr_problema(self, nr_problema):
        self.__nr_problema = nr_problema

    def set_descriere(self, descriere):
        self.__descriere = descriere

    def set_deadline(self,deadline):
        self.__deadline = deadline


    def __str__(self):
        return "Numar laborator: " + str(self.__nr_lab) + " Numar problema: " + str(self.__nr_problema) + " Descriere: " + self.__descriere +  " Deadline : saptamana " + str(self.__deadline)
