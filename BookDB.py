from Book import *


class BookDB:
    """ Books database where all the information
        about the books will be stored """
    book_list = []

    def readFromBooksTxt(self):
        """ Method to read from the txt file containing books data """
        try:
            with open("books.txt", "r", encoding="windows-1250") as f:
                for line in f:
                    data = line.strip().split(';')
                    try:
                        book = Book(data[0], data[1], float(data[2]), data[3], data[4],data[5])
                        self.book_list.append(book)
                    except:
                        pass
        except FileNotFoundError:
            print("File that is necessary to start the program wasn't found, the program will stop here.")
            exit(0)

    def writeToBooksTxt(self):
        """ Method to write to the txt file containing books data """
        with open("books.txt", "w", encoding="windows-1250") as f:
            for b in self.book_list:
                f.write("{};{};{};{};{};{}".format(b.id, b.author, int(b.publication_year), b.title, b.rating, b.is_issued))
                f.write("\n")

    def print_books(self):
        for book in self.book_list:
            print("{} by {}".format(book.title, book.author))
