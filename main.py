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
            self.book_dic.update({str(id): {"book_title": line.replace("\n", ""), "lender": "", "issue_date": "",
                                            "status": "available"}})
            id = id+1

    def display_books(self):
        print("-------------------------List of Books--------------------------")
        print("Book ID\t\t Title\t Lender\t issue_date\t Status\t")
        print("----------------------------------------------------------------")
        for key, value in self.book_dic.items():
            print(key, "\t\t", value.get("book_title"), "\t", value.get("lender"), "\t", value.get("issue_date"), "\t", value.get("status"))

    def issue_books(self):
        books_id = input("Enter books id: ")
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if books_id in self.book_dic.keys():
            if self.book_dic[books_id]["status"] == "available":
                lender_name = input("Enter your Name: ")
                self.book_dic[books_id]["lender"] = lender_name
                self.book_dic[books_id]["issue_date"] = current_date
                self.book_dic[books_id]["status"] = "issued"
                print("Books Issued Successfully !!!")
            elif self.book_dic[books_id]["status"] == "issued":
                #print("This book is already issued to {0} on {1}".format(self.book_dic[books_id]["lender"], self.books_dic[books_id]["issue_date"]))
                print("This book is already issued to someone else.")
                return self.issue_books()
            else:
                print("Wrong Book ID")
                return self.issue_books()

    def add_books(self):
        new_book = input("Enter New Book Title: ")
        if new_book == "":
            return self.add_books()
        else:
            with open(self.book_list, "a") as book:
                book.writelines("{0} \n".format(new_book) )
                self.book_dic.update({str(int(max(self.book_dic))+1): {"book_title": new_book, "lender": "", "issue_date": "",
                                                "status": "available"}})
                print("{0} has been added successfully to the database!".format(new_book))

    def return_books(self):
        book_id = input("Enter Book ID: ")
        if book_id in self.book_dic.keys():
            if self.book_dic[book_id]["status"] == "issued":
                self.book_dic[book_id]["lender"] = ""
                self.book_dic[book_id]["status"] = "available"
                self.book_dic[book_id]["issue_date"] = ""
                print("\"{0}\" returned successfully!")
            else:
                print("Wrong book id")
                return return_books()

    """def remove_books(self):
        book_id = input("Enter Book ID: ")
        if book_id in self.book_dic.keys():
            book_name = self.book_dic[book_id]["title"]
            with open(self.book_list, "r") as book:
                book.truncate(int(book_id)-100)"""


try:
    book_list = "book_list.txt"
    lib1 = "First Library"
    obj = LMS(book_list, lib1)
    key_list = {"D": "Display Books", "I": "Issue a Book", "A": "Add a New Book", "R": "Return a Book", "T": "Remove a Book", "Q": "Quit"}
    key_press = False
    while key_press != "Q":
        print("Welcome to {0}".format(obj.library_name))
        for key, value in key_list.items():
            print("Press ", key, "To ", value)
        key_press = input("Press key: ").upper()
        if key_press == "D":
            print("Current Selection: Display Books")
            obj.display_books()
        elif key_press == "I":
            print("Current Selection: Issue a Book")
            obj.issue_books()
        elif key_press == "A":
            print("Current Selection: Add a Book")
            obj.add_books()
        elif key_press == "R":
            print("Current Selection: Return a Book")
            obj.return_books()
        # elif key_press == "T":
        # print("Current Selection: Remove a Book")
        # obj.remove_books()
        elif key_press == "Q":
            print("Current Selection: Quit")
            break
        else:
            continue
except Exception as e:
    print("Something went wrong. Please check your input.")
