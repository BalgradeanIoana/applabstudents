from ro.ubb.applabstudents.domain.note import Nota


class NoteService:
    def __init__(self, nota_repository):
        self.__nota_repository = nota_repository

    def adaugare_nota(self,student_id, nr_lab, nr_problema, nota):
        nota = Nota(student_id, nr_lab, nr_problema, nota)
        self.__nota_repository.save(nota)


    def modifica_nota(self,student_id, nr_lab, nr_problema, nota):
        nota = Nota(student_id, nr_lab, nr_problema, nota)
        self.__nota_repository.update(nota)


    def stergere_nota(self, student_id, nr_lab, nr_problema):
        id = (student_id, nr_lab, nr_problema)
        self.__nota_repository.delete_by_id(id)


    def find_by_id(self, student_id, nr_lab, nr_problema):
        id = (student_id, nr_lab, nr_problema)
        return self.__nota_repository.find_by_id(id)


    def afisare_note(self):
        return self.__nota_repository.find_all()
