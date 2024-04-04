from classes import *

# Implement exception handling for functions

# Stand-In for GUI
def choose(options):

    input = ""

    if input not in options:
        print("--------------------------")
        print("What would you like to do?")
        print("--------------------------")
        print("Add Book: ab")
        print("--------------------------")
        print("Add Member: am")
        print("--------------------------")
        print("Remove Book: rb")
        print("--------------------------")
        print("Remove Member: rm")
        print("--------------------------")
        print("List Books: lb")
        print("--------------------------")
        print("List Members: lm")
        print("--------------------------")
        print("Find Book: fb")
        print("--------------------------")
        print("Find Member: fm")
        print("--------------------------")
        input = input("Enter choice: ")

def addBook(list):

    return

def addMember(list):

    book = Book()
    book.title = input("Enter title of book: ")
    book.author = input("Enter author of book: ")

    

    list.append(book)

def listBooks(list):

    for i in list:
        print("--------------------------------")
        print("List of Books")
        print("--------------------------------")
        i.printBook()
        print("--------------------------------")


def listMembers(list):

    for i in list:
        print("---------------------------------")
        print("List of Members")
        print("---------------------------------")
        i.printMember()
        print("---------------------------------")


#def findBook():


#d#ef findMember():


