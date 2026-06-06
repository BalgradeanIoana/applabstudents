from ro.ubb.applabstudents.domain.exceptions import IdDuplicat, EntitateInexistenta


class NoteRepository:
    def __init__(self, validator):
        self.__validator = validator
        self.__all_grades = []

    def find_all(self):
        return self.__all_grades

    def save(self, nota):
        self.__validator.validate(nota)
        if self.find_by_id(nota.get_id()) is not None:
            raise IdDuplicat("Aceasta problema a fost notata deja")
        self.__all_grades.append(nota)

    def update(self, nota_modificata):
        self.__validator.validate(nota_modificata)
        if self.find_by_id(nota_modificata.get_id()) is None:
            raise EntitateInexistenta("Acesta nota nu exista")
        self.__all_grades[:] = [nota_modificata if nota.get_id() == nota_modificata.get_id() else nota for nota in self.__all_grades]

    def delete_by_id(self, id):
        if self.find_by_id(id) is None:
            raise EntitateInexistenta("Acesta nota nu exista")
        self.__all_grades[:] = [nota for nota in self.__all_grades if nota.get_id() != id]

    def find_by_id(self, id):
        for nota in self.__all_grades:
            if nota.get_id() == id:
                return nota
        return None



