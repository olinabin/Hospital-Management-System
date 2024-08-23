class Person:
    last_id = 0

    def __init__(self, first_name, surname):
        self.id = Person.last_id + 1
        Person.last_id += 1
        self.__first_name = first_name
        self.__surname = surname

    def get_unique_hospital_id(self):
        return self.id

    def full_name(self):
        return f'{self.__first_name} {self.__surname}'
    
    def get_first_name(self):
        return self.__first_name

    
    def set_first_name(self, new_first_name):
        self.__first_name = new_first_name 

    def get_surname(self):
        return self.__surname
    
    def set_surname(self, new_surname):
        self.__surname = new_surname