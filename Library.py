import builtins
import re
from os import *
from BookDB import *
from UserDB import *
from time import *
from functions import *


class Library(UserDatabase, BookDB):
    """ Class representing out library where all the actions
        will take place """

    def __init__(self):
        """ Constructor that reads from txt files necessary for
            library system and checks if book_ids from every
            student are valid and exist in book_list"""
        self.readFromUserTxt()
        self.readFromBooksTxt()
        check_bookid_of_issued_books(self.student_list, self.book_list)

    def overwrite_files(self):
        """ Method that overwrites the txt files that contain
            data from the system"""
        self.writeToUserTxt()
        self.writeToBooksTxt()

    # Methods for Admin in the library system
    def add_book(self):
        """ Method that allow admin to add a book to the system"""
        try:
            id = input("ID: ")
            title = input("Title: ")
            author = input("Author: ")
            rating = float(input("Rating: "))
            publication_year = int(input("Year of publishing: "))
            if check_if_has_letters(id) == False and check_if_bookid_exists(id, self.book_list) == False \
                    and check_rating_range(rating):
                book = Book(id, author, publication_year, title, round(rating, 2))
                print(book.rating)
                self.book_list.append(book)
            else:
                if check_if_has_letters(id):
                    print("Given ID has invalid characters, you will come back to main menu")
                    sleep(2)
                elif check_if_bookid_exists(id, self.book_list):
                    print("Given ID already exists, you will come back to main menu")
                    sleep(2)
                elif not check_rating_range(rating):
                    print("Rating has to be between 1 and 5, you will come back to main menu")
                    sleep(2)
        except ValueError:
            print("Your input is invalid, you will come back to the menu.")
            sleep(2)

    def delete_book(self):
        """ Method that allow admin to delete a book from the system"""
        id = input("ID of the book which will be deleted: ")
        exists = False
        for book in self.book_list:
            if id == book.id:
                exists = True
                if book.is_issued == "False":
                    print("{} by {} will be deleted.".format(book.title, book.author))
                    self.book_list.remove(book)
                    sleep(2)
                    break
                else:
                    print("This book is issued, so it cannot be deleted")
                    sleep(2)
                    break
        if not exists:
            print("Book which ID is {} was not found, you will come back to the menu.".format(id))
            sleep(2)

    def search_for_a_book(self):
        """
        Method that allow user to search for a book in the system
        User can search for author or title
        """
        clear()
        choice = input("1. Search for author\n2. Search for title\nChoice: ")
        matched = False
        if choice == "1":
            already_matched = []
            regex_author = input("Author: ").title()
            regex_author_exact = "^" + regex_author + "$"
            clear()
            for book in self.book_list:
                exact = re.search(regex_author_exact, book.author)
                if exact:
                    matched = True
                    print(book.id + " " + book.author + " - " + "\"" + book.title + "\"")
                    already_matched.append(book.author)
            for book in self.book_list:
                partially = re.search(regex_author, book.author)
                if partially and book.author not in already_matched:
                    matched = True
                    print(book.id + " " + book.author + " - " + "\"" + book.title + "\"")

            if not matched:
                print("No records like this were found, you will come back to main menu")
            system("pause")
        elif choice == "2":
            already_matched = []
            regex_title = input("Title: ").title()
            regex_title_exact = "^" + regex_title + "$"
            clear()
            for book in self.book_list:
                exact = re.search(regex_title_exact, book.title)
                if exact:
                    matched = True
                    print(book.id + " " + book.author + " - " + "\"" + book.title + "\"")
            for book in self.book_list:
                partially = re.search(regex_title, book.title)
                if partially and book.title not in already_matched:
                    matched = True
                    print(book.id + " " + book.author + " - " + "\"" + book.title + "\"")

            if not matched:
                print("No records like this were found, you will come back to main menu")
            system("pause")
        else:
            print("Wrong input, you will come back to the main menu")
            sleep(2)

    def add_student(self):
        """ Method that allow admin to add a student to the system"""
        id = input("ID: ")
        name = input("Name: ")
        lastname = input("Lastname: ")
        login = input("Login: ")
        password = input("Password: ")
        if not check_if_has_letters(id) and not check_if_studentid_exists(id, self.student_list):
            student = Student(id, name, lastname, login, password)
            print(student.id, student.name, student.lastname)
            self.student_list.append(student)
        else:
            if check_if_has_letters(id):
                print("Given ID has invalid characters, you will come back to main menu")
                sleep(2)
            elif check_if_studentid_exists(id, self.student_list):
                print("Given ID already exists, you will come back to main menu")
                sleep(2)

    def delete_student(self):
        """ Method that allow admin to delete a student from the system"""
        found = False
        clear()
        self.print_users()
        id = input("ID of the student which will be deleted: ")
        for student in self.student_list:
            if student.id == id:
                found = True
                if len(student.issued_books) > 0:
                    print("This student has {} issued books, so he/she cannot be deleted.".format(
                        len(student.issued_books)))
                    sleep(2)
                    break
                else:
                    print("{} {} will be deleted from the system".format(student.name, student.lastname))
                    self.student_list.remove(student)
                    sleep(2)
                    break

        if not found:
            print("Student whose id is {} was not found in the system.".format(id))
            sleep(2)

    def show_stats(self):
        """ Method that allow admin to see the statistics of the system"""
        clear()
        path = 'C:\\Users\\stepo\\Desktop\\PK4\\Projekt\\LibrarySystem\\Statistics\\stats.txt'
        try:
            with builtins.open(path) as file:
                found = True
                for line in file:
                    print(line.strip("\n"))
        except FileNotFoundError:
            print("The file with stats wasn't found.")
        system("pause")

    # Methods for a student in the library system
    def issue_book(self, student):
        """
        Method that allow student to issue a book
        Student issues a book by giving a title
        """
        clear()
        found = False
        id = input("ID of the book that you want to issue: ")
        for book in self.book_list:
            if book.id == id:
                if book.is_issued != "False":
                    print("This book is already issued, come back to main menu")
                    system("pause")
                    break
                found = True
                # 1. Add this book to the student's issued books
                student.issued_books.append(book.id)
                # 2. Set book's is_issued to True
                book.is_issued = True
                print("{} - {} will be issued.".format(book.author, book.title))
                break
        if not found:
            print("Book of ID {} was not found in the system".format(id))
        system("pause")

    def return_book(self, student):
        """ Method that allow student to return a book"""
        found = False
        if len(student.issued_books) == 0:
            clear()
            print("You don't have any books issued right now.")
            system("pause")
        else:
            self.view_issued_books(student)
            # The id is needed to return a book
            id = input("ID of the book which you want to return: ")
            for id_issued in student.issued_books:
                if id_issued == id:
                    found = True
                    print("The book has successfully been returned.")
                    student.issued_books.remove(id)
                    sleep(2)
                    for book in self.book_list:
                        if book.id == id:
                            book.is_issued = "False"
            if not found:
                print("Book of ID {} was not found in your issued books".format(id))
                sleep(2)

    def view_issued_books(self, student):
        """ Method that allow student to show his/her issued books"""
        clear()
        found = False
        counter = 1
        for book in self.book_list:
            if book.id in student.issued_books:
                found = True
                print("{}. {} - {} - {}".format(str(counter), book.id, book.author, book.title))
                counter += 1
        if not found:
            print("You don't have any books issued right now.")
        system("pause")
