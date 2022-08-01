class User:
    def __init__(self, name, lastname, login, password):
        self.name = name
        self.lastname = lastname
        self.login = login
        self.password = password

    def welcome(self):
        print("Welcome {}{}".format(self.name, self.lastname))