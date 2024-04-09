from tkinter import *
from utils import *

"""

Tkinter scrollbar for listing out books and members

grid_forget() removes button from grid

"""

class gui:

    def __init__(self):
        
        # List of all books and members in catalogue
        self.bookList = []
        self.memberList = []

        # Create root object
        self.root = Tk()

        # List to store all button objects
        b_list = []

        # Creates a button that adds a book to the catalogue when pressed
        # Will first prompt the user to fill out info about book using book_search
        ab = Button(self.root, command= lambda: self.book_fill_out(0))
        b_list.append(ab)

        # Creates a button that adds a member to the catalogue when pressed
        # Will first prompt the user to fill out information about member
        am = Button(self.root, command= lambda: self.member_fill_out(0))
        b_list.append(am)

        # Creates a button that removes a book when pressed
        # Will first prompt the user to type which book they wish to remove
        # Will use several 



    def main_menu(self):

        # Exact same thing as init, except it only sets up labels and buttons

        
        return

# For the two "fill out" functions below 
# mode = 0 is for adding
# mode = 1 is for removing
# Otherwise it goes into search mode

    def book_fill_out(self, mode):
    
        if mode == 0:

            return

        elif mode == 1:
            
            return

        else:

            return
        
        return
    
    def member_fill_out(self, mode):

        if mode == 0:

            return

        elif mode == 1:
            
            return

        else:

            return

        return
    
    def list_books(self):

        listBooks(self.bookList)
        return
    
    def list_members(self):

        listMembers(self.memberList)
        return

        