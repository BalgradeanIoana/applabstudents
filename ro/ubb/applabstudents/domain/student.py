from ro.ubb.applabstudents.domain.base_entity import BaseEntity


class Student(BaseEntity):
    def __init__(self, id, nume, grupa):
        super().__init__(id)
        self.__nume = nume
        self.__grupa = grupa

    def get_nume(self):
        return self.__nume

    def get_grupa(self):
        return self.__grupa

    def set_nume(self, nume):
        self.__nume = nume

    def set_grupa(self, grupa):
        self.__grupa = grupa

    def __str__(self):
        return "Id: " + str(self.get_id()) + " Nume: " + self.__nume + " Grupa: " + str(self.__grupa)