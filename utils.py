from classes import *

# Implement exception handling for functions

def addBook(gui, author, title, numBooks):

    book = Book()
    book.title = title
    book.author = author
    book.bookId = str(numBooks)
    gui.bookList.append(book) 


def addMember(gui, firstName, lastName, numMembers):

    member = Member()
    member.firstName = firstName
    member.lastName = lastName
    member.memberId = str(numMembers)
    gui.memberList.append(member)


def removeBook(gui):
    
    return


def removeMember(gui):

    return


def listBooks(gui):

    list = gui.bookList

    # IMPLEMENT label that says "List of Books" before loop

    # IMPLEMENT scrollbar so user can see all elements in longer lists
    for i in list:
        
        # IMPLEMENT label that uses "formattedBookInfo" function as text
        # i.formattedBookInfo()
        return


def listMembers(gui):

    list = gui.memberList
    
    # IMPLEMENT label that says "List of Members" before loop 

    # IMPLEMENT scrollbar so user can see all elements in longer lists
    for i in list:

        # IMPLEMENT label that uses "formattedMemberInfo" function as text
        # i.formattedMemberInfo()
        print("---------------------------------")


# Searching algorithm used to find a book in the book list
def findBook():

    # If found, return book

    # If not found, return false

    return 

# Searching algorithm used to find a member in the member list
def findMember():

    # If found, return member

    # If not found, return false

    return
