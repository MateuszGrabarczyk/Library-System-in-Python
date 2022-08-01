from Library import *
from functions import *
from time import *
from Admin import *

library = Library()
admin = Admin()

while True:
    print("Welcome to the library system")
    print("1. Log in")
    print("2. Exit programme")
    choice = input("Choose one of the options: ")
    if choice == "1":
        clear()
        login = input("Login: ")
        password = input("Password: ")
        if login == admin.login and password == admin.password:
            while True:
                admin_menu_description(admin)
                choice = input("Choose one of the options: ")
                # Write all options here from 1 to 6
                if choice == "1":
                    library.search_for_a_book()
                elif choice == "2":
                    library.add_book()
                elif choice == "3":
                    library.delete_book()
                elif choice == "4":
                    library.add_student()
                elif choice == "5":
                    library.delete_student()
                elif choice == "6":
                    library.show_stats()
                elif choice == "7":
                    print("Quitting...")
                    sleep(1.5)
                    clear()
                    break
                else:
                    print("Wrong input, try again")
                    sleep(2)
        elif does_input_match_any_student(login, password, library.student_list):
            for student in library.student_list:
                if student.login == login and student.password == password:
                    while True:
                        user_menu_description(student)
                        choice = input("Choose one of the options: ")
                        if choice == "1":
                            library.issue_book(student)
                        elif choice == "2":
                            library.return_book(student)
                        elif choice == "3":
                            library.search_for_a_book()
                        elif choice == "4":
                            library.view_issued_books(student)
                        elif choice == "5":
                            print("Quitting...")
                            sleep(1.5)
                            clear()
                            break
                        else:
                            print("Wrong input, try again")
                            sleep(2)
                    break
        else:
            print("User was not found, try again.")
            sleep(2.5)
            clear()
    elif choice == "2":
        print("Quitting programme...")
        sleep(1.5)
        break
    else:
        print("Wrong choice, try again.")
        sleep(1.5)
        clear()

library.overwrite_files()
