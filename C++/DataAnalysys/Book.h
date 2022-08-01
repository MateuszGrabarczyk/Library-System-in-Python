#pragma once
#include <iostream>
#include <string>
using namespace std;

/**
 * @brief Class which represents a book in the system
*/

class Book {
public:
	int id;
	string author;
	int year_published;
	string title;
	double rating;
	string is_issued;
public:
	Book(int _id, string _author, int _year_published, string _title, double _rating, string _is_issued);
};