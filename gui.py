from tkinter import *
from utils import *

def main_menu(gui):

    # List to store all button objects
    gui.b_list = []

    # Creates a button that adds a book to the catalogue when pressed
    # Will first prompt the user to fill out info about book using book_search
    gui.b_list.append(Button(gui.root, command= lambda: gui.book_fill_out(0)))

    # Creates a button that adds a member to the catalogue when pressed
    # Will first prompt the user to fill out information about member
    gui.b_list.append(Button(gui.root, command= lambda: gui.member_fill_out(0)))

    # Creates a button that removes a book when pressed
    # Will first prompt the user to type which book they wish to remove
    gui.b_list.append(Button(gui.root, command= lambda: gui.book_fill_out(0)))

    # Creates a button that removes a member when pressed
    # Will first prompt the user to type which user they wish to remove
    gui.b_list.append(Button(gui.root, command= lambda: gui.member_fill_out(0)))

    # Creates a button for the user to find a book
    # Will first prompt the user to type which book they wish to find
    gui.b_list.append(Button(gui.root, command= lambda: gui.book_fill_out(2)))

    # Creates a button for the user to find a member
    # Will first prompt the user to type which member they wish to find
    gui.b_list.append(Button(gui.root, command= lambda: gui.member_fill_out(2)))

    # Creates a button that lists all books in the catalogue
    gui.b_list.append(Button(gui.root, command=gui.list_books))

    # Creates a button that lists all members in the catalogue
    gui.b_list.append(Button(gui.root, command=gui.list_members))

    # Creates a button to exit the app
    gui.b_list.append(Button(gui.root, command=gui.root.quit()))

def clear_gui(gui):

    for i in gui.b_list:
        i.grid_forget()
        gui.b_list.remove(i)

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

        # Start loop
        self.root.mainloop()



    def main_menu(self):

        # Exact same thing as init, except it only sets up labels and buttons
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
        rb = Button(self.root, command= lambda: self.book_fill_out(0))
        b_list.append(rb)

        # Creates a button that removes a member when pressed
        # Will first prompt the user to type which user they wish to remove
        am = Button(self.root, command= lambda: self.member_fill_out(0))
        b_list.append(am)

        # Creates a button for the user to find a book
        # Will first prompt the user to type which book they wish to find
        fb = Button(self.root, command= lambda: self.book_fill_out(2))
        b_list.append(fm)

        # Creates a button for the user to find a member
        # Will first prompt the user to type which member they wish to find
        fm = Button(self.root, command= lambda: self.member_fill_out(2))
        b_list.append(fb)

        # Creates a button that lists all books in the catalogue
        lb = Button(self.root, command=self.list_books)
        b_list.append(lb)

        # Creates a button that lists all members in the catalogue
        lm = Button(self.root, command=self.list_members)
        b_list.append(lm)

        # Creates a button to exit the app
        exit = Button(self.root, command=self.root.quit())
        b_list.append(exit)
        
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

        