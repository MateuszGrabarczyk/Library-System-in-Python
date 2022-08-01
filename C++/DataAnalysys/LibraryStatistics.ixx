#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <string>
#include <iterator>
#include <algorithm>
#include <map>
#include <ranges>
#include <filesystem>
#include "BookDatabase.h"

export module LibraryStatistics;
using namespace std;
namespace fs = filesystem;

export class LibraryStatistics : public BooksDatabase {
public:
	LibraryStatistics() {
		// Reading file and saving the information to vector 
		ifstream file("C:\\Users\\stepo\\Desktop\\PK4\\Projekt\\LibrarySystem\\Python\\books.txt");
		string line; // temp string to save the information of a book from txt file
		vector <string> all_lines;
		if (file) {
			while (getline(file, line)) {
				all_lines.push_back(line);
			}
		}
		else {
			cout << "Unable to open the file!" << endl;
		}
		file.close();
		
		for (auto w : all_lines) {
			string words[6]; // saves the information about the certain book
			stringstream  ss(w);
			string str;
			int i = 0;
			while (getline(ss, str, ';')) {
				words[i] = str;
				i++;
			}

			int id = stoi(words[0]); // index 0 is ID
			string a = words[1];// index 1 is the name of author
			int year_p = stoi(words[2]); // index 2 is a year published
			string t = words[3]; // index 3 is a title of the book
			double r = stod(words[4]); // index 4 is a rating of the book
			string if_is = words[5]; // index 5 is an info if a book is issued
			Book book(id, a, year_p, t, r, if_is); // creating a book object
			books_list.push_back(book); // adding a book to the vector of books

		}
		
	}
	
	double average_rating() {
		double sum = 0;
		for (auto i : books_list) {
			sum += i.rating;
		}
		return sum / books_list.size();
	}

	double median_rating() {
		vector<double> ratings;

		for (auto i : books_list) {
			ratings.push_back(i.rating);
		}
		int n = ratings.size();
		sort(ratings.begin(), ratings.end());

		if (n % 2 == 0) {
			return (ratings[(n - 1) / 2] + ratings[n / 2]) / 2.0;
		}
		else {
			return ratings[n / 2];
		}
	}

	double percent_of_the_books_issued() {
		int num_of_books_issued = 0;

		for (auto i : books_list) {
			if (i.is_issued == "True") {
				num_of_books_issued += 1;
			}
		}

		double returned_value = (double)num_of_books_issued / books_list.size();
		return round(returned_value * 10000.0) / 10000.0 * 100;

	}
	
	pair<string,int> most_popular_author() {
		map<string, int> author_and_num_of_books;

		
		for (auto i : books_list) {
			author_and_num_of_books[i.author]++;
		}
		int max = 0;
		string author_name;
		for (auto i : author_and_num_of_books)
			if (i.second > max) {
				max = i.second;
				author_name = i.first;
			}
		pair<string, int> returned_value(author_name, max);
		return returned_value;		
	}

	int num_of_books_XXI_century() {
		vector<int> years_published;
		for (auto i : books_list) {
			years_published.push_back(i.year_published);
		}
		auto temp = years_published | views::filter([](const int n) {return n > 2000; });
		
		int sum = 0;
		for (auto i : temp) {
			sum++;
		}
		
		return sum;
	}

	int num_of_books_XX_century() {
		vector<int> years_published;
		for (auto i : books_list) {
			years_published.push_back(i.year_published);
		}
		auto temp = years_published | views::filter([](const int n) {return n > 1900 and n < 2001; });

		int sum = 0;
		for (auto i : temp) {
			sum++;
		}

		return sum;
	}

	void create_directory_and_save_file() {

		fs::path p = "C:\\Users\\stepo\\Desktop\\PK4\\Projekt\\LibrarySystem\\Statistics\\";

		if (!fs::is_directory(p) || !fs::exists(p)) { // Check if folder exists
			fs::create_directory(p); // create folder
		}
		p /= "stats.txt"; // adding the name of the new txt file 

		pair<string, int> pair(most_popular_author());
		double books_percentage_XXI_century = ((double)num_of_books_XXI_century() / books_list.size()) * 100.0;
		double books_percentage_XX_century = ((double)num_of_books_XX_century() / books_list.size()) * 100.0;

		books_percentage_XXI_century = round(books_percentage_XXI_century * 100.0) / 100.0;
		books_percentage_XX_century = round(books_percentage_XX_century * 100.0) / 100.0;
		std::ofstream ofs(p);
		ofs << "--- STATS OF THE LIBRARY SYSTEM ---\n";
		ofs << "The most popular author in the library is " << pair.first << " with " << pair.second << " books\n";
		ofs << "The average book rating is " << average_rating() << "\n";
		ofs << "The median book rating is " << median_rating() << "\n";
		ofs << "The percantage of the books that are issued is " << percent_of_the_books_issued() << "\n";
		ofs << "The percantage of the books that were released in XXI century is " << books_percentage_XXI_century << "\n";
		ofs << "The percantage of the books that were released in XX century is " << books_percentage_XX_century << "\n";
		ofs.close();
	}

};