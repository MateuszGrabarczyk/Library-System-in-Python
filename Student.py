from User import *


class Student(User):
    """ Class representing a student in the system"""

    def __init__(self, id, name, lastname, login, password):
        super().__init__(name, lastname, login, password)
        self.issued_books = []
        self.id = id

    def welcome(self):
        """ Method to welcome the student in the system"""
        print("Welcome {} {}, right now you have {} issued books.".format(self.name, self.lastname,
                                                                          len(self.issued_books)))
