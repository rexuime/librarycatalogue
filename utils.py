from classes import *

# Implement exception handling for functions

def addBook(gui, title, author):

    book = Book()
    book.title = title
    book.author = author
    gui.bookList.append(book) 
    return


def addMember(gui, firstName, lastName):

    member = Member()
    member.firstName = firstName
    member.lastName = lastName
    member.memberId = str()
    gui.memberList.append(member)
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

    return 

# Searching algorithm used to find a member in the member list
def findMember():

    return
