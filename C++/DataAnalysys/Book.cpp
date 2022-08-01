#include "Book.h"
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

Book::Book(int _id, string _author, int _year_published, string _title, double _rating, string _is_issued) {
	id = _id;
	author = _author;
	year_published = _year_published;
	title = _title;
	rating = _rating;
	is_issued = _is_issued;
}
