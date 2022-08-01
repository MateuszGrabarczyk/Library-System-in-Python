def check_if_has_letters(id):
    """ Checks if particular string has any letter in it """
    for i in id:
        if i in "qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM,./!@#$%^&*()-_=+|\'\":;`[]{}<>?":
            return True
    return False

def check_if_bookid_exists(id, book_list):
    """ Checks if the given id exists in book_list"""
    for book in book_list:
        if id == book.id:
            return True
    return False

def check_bookid_of_issued_books(student_list, book_list):
    """ This function checks at the beginning of the program if students have valid
        id in their issued books """
    for student in student_list:
        for book_id in student.issued_books:
            if not check_if_bookid_exists(book_id, book_list):
                student.issued_books.remove(book_id)

def check_if_studentid_exists(id, student_list):
    """ Checks if the given id exists in student_list"""
    for student in student_list:
        if id == student.id:
            return True
    return False


def clear():
    """ Function to make the program look better"""
    print(100 * "\n")


def admin_menu_description(admin):
    """ Admin menu """
    clear()
    admin.welcome()
    print("1. Search for a book")
    print("2. Add a book")
    print("3. Delete a book")
    print("4. Add a user")
    print("5. Delete user")
    print("6. See the statistics about the system")
    print("7. Exit")


def user_menu_description(student):
    """ Student menu """
    clear()
    print("Welcome {} {}!".format(student.name, student.lastname))
    print("1. Issue a book")
    print("2. Return a book")
    print("3. Search for a book")
    print("4. View issued books")
    print("5. Exit")


def check_rating_range(rating):
    """ Checks if the range of book rating is valid"""
    if 1 <= rating <= 5:
        return True
    return False


def does_input_match_any_student(login, password, student_list):
    """ Checks when logging into program if parameters match any student """
    for student in student_list:
        if student.login == login and student.password == password:
            return True
    return False
