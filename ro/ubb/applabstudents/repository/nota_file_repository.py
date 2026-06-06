from ro.ubb.applabstudents.domain.exceptions import ValidatorException, IdDuplicat
from ro.ubb.applabstudents.domain.note import Nota
from ro.ubb.applabstudents.repository.noterepository import NoteRepository


class NotaFileRepository(NoteRepository):
    def __init__(self,validator, filename):
        super().__init__(validator)
        self.__filename = filename
        self.__load_data()

    def __load_data(self):
        with open(self.__filename) as f:
            for linie in f:
                lista_nota = linie.split(",")
                try:
                    nota = Nota(int(lista_nota[0]), int(lista_nota[1]), int(lista_nota[2]), int(lista_nota[3]))
                    super().save(nota)
                except ValidatorException as ve:
                    print(ve)
                except IdDuplicat as id:
                    print(id)
                except ValueError:
                    print("Numarul laboratorului, problemei si id-ul studentului trebuie sa fie numere")

    def save(self, nota):
        super().save(nota)
        self.__add_to_file(nota)

    def __add_to_file(self, nota):

        with (open(self.__filename, "a") as f):
            string_nota = str(
                nota.get_student_id()) + "," + str(nota.get_nr_lab()) + "," + str(nota.get_nr_problema()) + "," + str(
                nota.get_nota()) + "\n"
            f.write(string_nota)

    def update(self, nota_modificata):
        super().update(nota_modificata)
        self.__rewrite()

    def delete_by_id(self, id):
        super().delete_by_id(id)
        self.__rewrite()


    def __rewrite(self):
        all_grades = self.find_all()
        with open(self.__filename, "w") as f:
            for nota in all_grades:
                string_nota = str(
                    nota.get_student_id()) + "," + str(nota.get_nr_lab()) + "," + str(nota.get_nr_problema()) + "," + str(
                    nota.get_nota()) + "\n"
                f.write(string_nota)