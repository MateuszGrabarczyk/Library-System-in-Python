class Book:
    """ Class representing a book in the system"""
    def __init__(self, id, author, publication_year, title, rating, is_issued=False):
        self.id = id
        self.author = author
        self.publication_year = publication_year
        self.title = title
        self.rating = rating
        self.is_issued = is_issued

    def print_details(self):
        """ Method to print the details about the book"""
        print("{} {} {} {} {}".format(self.id, self.author, self.publication_year, self.title, self.rating))
