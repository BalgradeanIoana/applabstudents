class BaseEntity:
    def __init__(self, id):
        self.__id = id
    def get_id(self):
        return self.__id
    def set_id(self, id):
        self.__id = id