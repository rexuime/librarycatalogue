"""

Books must have an author, title, and bookId.

Added a bool to track if the book is being borrowed or not.

Decided not to implement a way to check how long a book is being borrowed (AKA: No late penalty).

"""

class Book():

    def __init__(self):
        
        # Book info
        self.author = ""
        self.title = ""
        self.bookId = ""
        self.available = True

    def formattedBookInfo(self):

        # Simple string manipulation to format book info for GUI
        string = "-------------------------------------------------------------------------------------------------------------------\n"
        string += "Title: " + self.title + "\nAuthor: " + self.author + "\nBook ID: " + self.bookId + "\n"

        if self.available:

            string += "Available: Yes\n"

        else:

            string+= "Available: No\n"

        string += "-------------------------------------------------------------------------------------------------------------------"
        return string

"""

Members must have a first and last name, memberId, and bookCount to track the number of books they've borrowed.

"""
    
class Member():

    def __init__(self):

        # Member information
        self.firstName = ""
        self.lastName = ""
        self.memberId = ""
        self.username = ""
        self.password = ""
        self.bookCount = 0

    def formattedMemberInfo(self):

        # Simple string manipulation to format member info for GUI
        string = "-------------------------------------------------------------------------------------------------------------------\n"
        string += "Name: " + self.firstName + " " + self.lastName + "\nMember ID: " + self.memberId + "\nBooks Borrowed: " + str(self.bookCount) + "\n"
        string += "-------------------------------------------------------------------------------------------------------------------"
        return string