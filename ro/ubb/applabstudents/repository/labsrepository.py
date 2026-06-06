from ro.ubb.applabstudents.domain.exceptions import IdDuplicat, EntitateInexistenta


class LaboratorRepository:
    def __init__(self, validator):
        self.__validator = validator
        self.__all_labs = []

    def find_all(self):
        return self.__all_labs

    def save(self, laborator):
        self.__validator.validate(laborator)
        if self.find_by_id(laborator.get_id()) is not None:
            raise IdDuplicat("Acest numar de laborator exista deja, incercati altul.")
        self.__all_labs.append(laborator)

    def update(self, lab_modificat):
        self.__validator.validate(lab_modificat)
        if self.find_by_id(lab_modificat.get_id()) is None:
            raise EntitateInexistenta("Acest laborator nu exista")
        self.__all_labs[:] = [lab_modificat if lab.get_id() == lab_modificat.get_id() else lab for lab in self.__all_labs]

    def delete_by_id(self, id):
        if self.find_by_id(id) is None:
            raise EntitateInexistenta("Acest laborator nu exista")
        self.__all_labs[:] = [laborator for laborator in self.__all_labs if laborator.get_id() != id]

    def find_by_id(self, id):
        for laborator in self.__all_labs:
            if laborator.get_id() == id:
                return laborator
        return None



