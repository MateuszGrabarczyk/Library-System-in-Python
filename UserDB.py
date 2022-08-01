from Student import *


class UserDatabase:
    """ User database where all the information
        about the students will be stored """
    student_list = []

    def readFromUserTxt(self):
        """ Method to read from the txt file containing students data """
        try:
            with open("users.txt", "r") as f:
                for line in f:
                    data = line.strip().split(';')
                    try:
                        student = Student(data[0], data[1], data[2], data[3], data[4])
                        if len(data) > 5:
                            for i in range(5, len(data)):
                                student.issued_books.append(data[i])
                        self.student_list.append(student)
                    except:
                        pass
        except FileNotFoundError:
            print("File that is necessary to start the program wasn't found, the program will stop here.")
            exit(0)

    def writeToUserTxt(self):
        """ Method to write to the txt file containing students data """
        with open("users.txt", "w") as f:
            for s in self.student_list:
                f.write("{};{};{};{};{}".format(s.id, s.name, s.lastname, s.login, s.password))
                if len(s.issued_books) > 0:
                    for book_id in s.issued_books:
                        f.write(";" + book_id)
                f.write("\n")

    def print_users(self):
        """ Method to print all the students to the console"""
        for user in self.student_list:
            print("{} - {} {}".format(user.id, user.name, user.lastname))