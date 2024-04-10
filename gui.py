from tkinter import *
from utils import *

"""

Tkinter scrollbar for listing out books and members

grid_forget() removes button from grid

"""

# Class for all GUI data and functions
class gui:

    def __init__(self):
        
        # List of all books and members in catalogue
        self.bookList = []
        self.memberList = []

        # Create root object
        self.root = Tk()
        self.root.geometry("1200x800")
        self.root.configure(bg="black")

        # Create main menu
        self.main_menu()

        # Start loop
        self.root.mainloop()

        return

    # Function to change to main_menu
    def main_menu(self):

        # Title for catalogue
        title = Label(self.root, text="Library Catalogue", height=4, width=30, fg="white", bg="black", font=("Arial", 50))
        title.place(x=10, y=30)

        # With width at 30, 220 pixels long, 1 width = 7.333 pixels
        # With height at 4, 70 pixels height, 1 height = 17.5 pixels

        # Add label
        al = Label(self.root, text="----------------------------------\nADD\n----------------------------------", height=4, width=30, fg="white", bg="black", font=("Arial", 14))
        al.place(x=22, y=300)

        # Creates a button that adds a book to the catalogue when pressed
        # Will first prompt the user to fill out info about book using book_search
        ab = Button(self.root, text="Add Book", command= lambda: self.book_fill_out(0), height=4, width=30)
        ab.place(x=80, y=400)

        # Creates a button that adds a member to the catalogue when pressed
        # Will first prompt the user to fill out information about member
        am = Button(self.root, text="Add Member", command= lambda: self.member_fill_out(0), height=4, width=30)
        am.place(x=80, y=480)

        # Remove label
        rl = Label(self.root, text="----------------------------------\nREMOVE\n----------------------------------", height=4, width=30, fg="white", bg="black", font=("Arial", 14))
        rl.place(x=290, y=300)

        # Creates a button that removes a book when pressed
        # Will first prompt the user to type which book they wish to remove
        rb = Button(self.root, text="Remove Book", command= lambda: self.book_fill_out(1), height=4, width=30)
        rb.place(x=350, y=400)

        # Creates a button that removes a member when pressed
        # Will first prompt the user to type which user they wish to remove
        rm = Button(self.root, text="Remove Member", command= lambda: self.member_fill_out(1), height=4, width=30)
        rm.place(x=350, y=480)

        # Search label
        rl = Label(self.root, text="----------------------------------\nSEARCH\n----------------------------------", height=4, width=30, fg="white", bg="black", font=("Arial", 14))
        rl.place(x=560, y=300)

        # Creates a button for the user to find a book
        # Will first prompt the user to type which book they wish to find
        fb = Button(self.root, text="Find Book", command= lambda: self.book_fill_out(2), height=4, width=30)
        fb.place(x=620, y=400)

        # Creates a button for the user to find a member
        # Will first prompt the user to type which member they wish to find
        fm = Button(self.root, text="Find Member", command= lambda: self.member_fill_out(2), height=4, width=30)
        fm.place(x=620, y=480)

        # List label
        rl = Label(self.root, text="----------------------------------\nLIST\n----------------------------------", height=4, width=30, fg="white", bg="black", font=("Arial", 14))
        rl.place(x=830, y=300)

        # Creates a button that lists all books in the catalogue
        lb = Button(self.root, text="List Books",command=self.list_books, height=4, width=30)
        lb.place(x=890, y=400)

        # Creates a button that lists all members in the catalogue
        lm = Button(self.root, text="List Members", command=self.list_members, height=4, width=30)
        lm.place(x=890, y=480)

        # Creates a button to exit the app
        exit = Button(self.root, text="Exit", command=self.root.quit, height=2, width=12)
        exit.place(x=1100, y=750)
        
        return
    

    # Function to clear the GUI of all widgets to change to a different GUI
    def clear_gui(self):

        list = self.root.grid_slaves()
        for i in list:
            i.destroy()
            del i


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

        