import datetime
import os

# print(os.getcwd())


class LMS:
    def __init__(self, book_list, library_name):
        self.book_list = book_list
        self.library_name = library_name
        self.book_dic = {}
        id = 101
        with open(self.book_list) as book:
            content = book.readlines()
        for line in content:
            self.book_dic.update({str(id): {"book_title": line.replace("\n", ""), "lender": "", "issue_data": "",
                                            "status": "available"}})
            id = id+1

    def display_books(self):
        print("----------------List of Books----------------")
        print("Book ID\t\tTitle\t\t\tStatus")
        print("---------------------------------------------")
        for key, value in self.book_dic.items():
            print(key, "\t\t", value.get("book_title"), "\t", value.get("status"))



book_list = "book_list.txt"
lib1 = "First Library"
obj = LMS(book_list, lib1)
obj.display_books()
