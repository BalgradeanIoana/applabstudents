from ro.ubb.applabstudents.domain.exceptions import ValidatorException, IdDuplicat
from ro.ubb.applabstudents.domain.lab import Laborator
from ro.ubb.applabstudents.repository.labsrepository import LaboratorRepository


class LaboratorFileRepository(LaboratorRepository):
    def __init__(self,validator, filename):
        super().__init__(validator)
        self.__filename = filename
        self.__load_data()

    def __load_data(self):
        with open(self.__filename) as f:
            for linie in f:
                lista_lab = linie.split(",")
                try:
                    lab = Laborator(int(lista_lab[0]), int(lista_lab[1]), lista_lab[2], int(lista_lab[3]))
                    super().save(lab)
                except ValidatorException as ve:
                    print(ve)
                except IdDuplicat as id:
                    print(id)
                except ValueError:
                    print("Numarul laboratorului, problemei si deadline-ul trebuie sa fie numere")

    def save(self, lab):
        super().save(lab)
        self.__add_to_file(lab)

    def __add_to_file(self, lab):

        with (open(self.__filename, "a") as f):
            string_lab = str(
                lab.get_nr_lab()) + "," + str(lab.get_nr_problema()) + "," + lab.get_descriere() + "," + str(
                lab.get_deadline()) + "\n"
            f.write(string_lab)

    def update(self, lab_modificat):
        super().update(lab_modificat)
        self.__rewrite()

    def delete_by_id(self, id):
        super().delete_by_id(id)
        self.__rewrite()


    def __rewrite(self):
        all_labs = self.find_all()
        with open(self.__filename, "w") as f:
            for lab in all_labs:
                string_lab = str(
                    lab.get_nr_lab()) + "," + str(lab.get_nr_problema()) + "," + lab.get_descriere() + "," + str(
                    lab.get_deadline()) + "\n"
                f.write(string_lab)