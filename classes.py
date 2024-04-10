"""

Books must have an author, title, and bookId.

Added a bool to track if the book is being borrowed or not.

Decided not to implement a way to check how long a book is being borrowed (AKA: No late penalty).

"""

class Book():

    def __init__(self):
        
        self.author = ""
        self.title = ""
        self.bookId = ""
        self.available = True

    def printBook(self):

        print("Title: " + self.title)
        print("Author: " + self.author)
        print("Book Id: " + self.bookId)
        if self.available:
            print("Available: Yes")
        else:
            print("Available: No")

"""

Members must have a first and last name, memberId, and bookCount to track the number of books they've borrowed.

"""
    
class Member():

    def __init__(self):

        self.firstName = ""
        self.lastName = ""
        self.memberId = ""
        self.bookCount = 0

    def printMember(self):

        print("Name: " + self.firstName + " " + self.lastName)
        print("Member Id: " + self.memberId)
        print("Books Borrowed: " + str(self.bookCount))