#pragma once
#include "Book.h"
#include <iostream>
#include <string>
#include <vector>
using namespace std;
/**
 * @brief Class which represents the books database in the system
*/
class BooksDatabase {
public:
	vector <Book> books_list;
};