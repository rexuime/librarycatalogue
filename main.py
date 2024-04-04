from classes import *
from utils import *

options = ["ab", "am", "rb", "rm", "lb", "lm", "fb", "fm"]

if __name__ == "__main__":

    bookList = []
    memberList = []

    choose(options)
    
    match options:

        case "ab":

            addBook(bookList)

        case "am":

            addMember(memberList)

        case "rb":

            removeBook(bookList)

        case "rm":

            removeMember(memberList)

        case "lb":

            

        case "lm":

        case "fb":


        case "fm":

            break

    book = Book()
    member = Member()
    bookList.append(book)
    memberList.append(member)

    listBooks(bookList)
    listMembers(memberList)