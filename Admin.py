from User import *


class Admin(User):
    """ Class representing admin in the system"""
    def __init__(self, name="Mateusz", lastname="Grabarczyk", login="admin", password="admin"):
        super().__init__(name, lastname, login, password)

    def welcome(self):
        """ Method that prints welcome sentence about the admin"""
        print("Welcome {} {}, our dear Admin!".format(self.name, self.lastname))
