class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("\n    Books present in this library are: ")
        for book in self.books:
            print("\t*",book)

    def issueBook(self, bookName):
        if bookName in self.books:
            print(f"    You issued {bookName}. Read and return it within 30 days.\n    Thank You!")
            self.books.remove(bookName)
            return True

        else:
            print("    This book is not available!!\n    Try after some days.")
            return False

    def returnBook(self, bookReturn):
        self.books.append(bookReturn)
        print("    Thanks for returning this book. we hope you come again.")


class Student:
    # def __init__(self, borrowBooksList):
    #     self.borowBooks = borrowBooksList

    def requestBook(self):
        self.book = input("    Enter the name of the Book you want to Borrow...: ")
        print()
        return self.book

    def returnBook(self):
        self.book = input("    Enter the name of the Book you want to Return...: ")
        print()
        return self.book


if __name__ == "__main__":
    centralLibrary = Library(["Python", "C", "C++", "Core java"])
    studentBook = Student()
    print("\n*************Central Library*************")
    while (True):
        showMenu = '''
------------------------------------    
    Please select your option:

    1. Show Available Books.
    2. Issue book.
    3. Return Book.
    4. Exit!
------------------------------------
    '''
        print(showMenu)

        option = int(input("    Enter your option: "))
        if option == 1:
            centralLibrary.displayAvailableBooks()
        elif option == 2:
            centralLibrary.issueBook(studentBook.requestBook())
        elif option == 3:
            centralLibrary.returnBook(studentBook.returnBook())
        elif option == 4:

            print('''  
        Thanks for using this app. Give some rating!!

                Do you want to give rating?
                        
                        * * * * *

            1. Yes                        2. Later!
            ''')
            rating  = int(input("           "))
            if rating == 1:
                print("  Thank You!!","\U0001F917")
            break
