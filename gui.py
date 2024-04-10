from tkinter import *
from utils import *

# Class for all GUI data and functions
class gui:

    def __init__(self):
        
        # List of all books and members in catalogue
        self.bookList = []
        self.memberList = []
        self.numBooks = 0
        self.numMember = 0

        # Create root object
        self.root = Tk()
        self.root.geometry("1200x800")
        self.root.configure(bg="black")

        # State of enter/confirm button for entries
        self.confirm = 0

        # Create main menu
        self.main_menu()

        # Start loop
        self.root.mainloop()


    # Function to change to main_menu
    def main_menu(self):

        self.clear_gui()

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
        ab = Button(self.root, text="Add Book", command= lambda: self.book_fill_out(0, False), height=4, width=30)
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
        rb = Button(self.root, text="Remove Book", command= lambda: self.book_fill_out(1, False), height=4, width=30)
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
        fb = Button(self.root, text="Find Book", command= lambda: self.book_fill_out(2, False), height=4, width=30)
        fb.place(x=620, y=400)

        # Creates a button for the user to find a member
        # Will first prompt the user to type which member they wish to find
        fm = Button(self.root, text="Find Member", command= lambda: self.member_fill_out(2), height=4, width=30)
        fm.place(x=620, y=480)
        
        # List label
        ll = Label(self.root, text="----------------------------------\nLIST\n----------------------------------", height=4, width=30, fg="white", bg="black", font=("Arial", 14))
        ll.place(x=830, y=300)

        # Creates a button that lists all books in the catalogue
        lb = Button(self.root, text="List Books",command=self.list_books, height=4, width=30)
        lb.place(x=890, y=400)

        # Creates a button that lists all members in the catalogue
        lm = Button(self.root, text="List Members", command= self.list_members, height=4, width=30)
        lm.place(x=890, y=480)

        self.default_widgets()

        # Disable remove, search, and list buttons if list is empty
        if len(self.bookList) == 0:
            rb.configure(state=DISABLED)
            fb.configure(state=DISABLED)
            lb.configure(state=DISABLED)
        else:
            rb.configure(state=NORMAL)
            fb.configure(state=NORMAL)
            lb.configure(state=NORMAL)

        if len(self.memberList) == 0:
            rm.configure(state=DISABLED)
            fm.configure(state=DISABLED)
            lm.configure(state=DISABLED)
        else:
            rm.configure(state=NORMAL)
            fm.configure(state=NORMAL)
            lm.configure(state=NORMAL)


# For the two "fill out" functions below 
# mode = 0 is for adding
# mode = 1 is for removing
# Otherwise it goes into search mode


    # Function for users to add, remove, and search for books
    def book_fill_out(self, mode):

        self.clear_gui()
        self.default_widgets()

        info = Label(self.root, text="Enter Info Below", fg="white", bg="black", font=("Arial", 40))
        title = Label(self.root, text="Title", fg="white", bg="black", font=("Arial", 18), height=2, width=10)
        title_entry = Entry(self.root, width=34, borderwidth=3, font=("Arial", 14))
        author = Label(self.root, text="Author", fg="white", bg="black", font=("Arial", 18), height=2, width=10)
        author_entry = Entry(self.root, width=34, borderwidth=3, font=("Arial", 14))
        enter = Button(self.root, text="Enter", height=3, width=20, command= lambda: self.book_add(enter, cancel))
        cancel = Button(self.root, text="Cancel", height=3, width=20, state=DISABLED)
    
        # Add
        if mode == 0:

            info.place(x=410, y=140)
            title.place(x=530, y=260)
            title_entry.place(x=410, y=330)
            author.place(x=530, y=410)
            author_entry.place(x=410, y=480)
            enter.place(x=650, y=600)
            cancel.place(x=410, y=600)

        # Remove/Search
        else:

            info.place(x=410, y=140)
            title.place(x=530, y=180)
            title_entry.place(x=410, y=250)
            author.place(x=530, y=330)
            author_entry.place(x=410, y=400)
            bookid = Label(self.root, text="Book ID", fg="white", bg="black", font=("Arial", 18), height=2, width=10)
            bookid.place(x=530, y=480)
            bookid_entry = Entry(self.root, width=34, borderwidth=3, font=("Arial", 14))
            bookid_entry.place(x=410, y=550)
            enter.place(x=650, y=600)
            cancel.place(x=410, y=600)
        
            if mode == 1:

                self.book_remove(enter, cancel)
        
            else:

                self.book_search(enter, cancel) 


    def book_add(self, enter, cancel):

        if self.confirm == 0:

            enter.configure(text="Enter")
            cancel.configure(state=DISABLED)

        elif self.confirm == 1:

            enter.configure(text="Confirm?")
            cancel.configure(state=NORMAL)

        else:

            return


    #def book_remove(self, enter, cancel):

        #return
    
    #def book_search(self, enter, cancel):

        #return
        
        
    # Function for users to add, remove, and search for members
    def member_fill_out(self, mode):

        self.clear_gui()
        self.default_widgets()

        info = Label(self.root, text="Enter Info Below", fg="white", bg="black", font=("Arial", 40))
        firstname = Label(self.root, text="First Name", fg="white", bg="black", font=("Arial", 18), height=2, width=10)
        firstname_entry = Entry(self.root, width=34, borderwidth=3, font=("Arial", 14))
        lastname = Label(self.root, text="Last Name", fg="white", bg="black", font=("Arial", 18), height=2, width=10)
        lastname_entry = Entry(self.root, width=34, borderwidth=3, font=("Arial", 14))
        enter = Button(self.root, text="Enter", height=3, width=20, command= lambda: self.book_add(enter, cancel))
        cancel = Button(self.root, text="Cancel", height=3, width=20, state=DISABLED)

        # Add
        if mode == 0:

            info.place(x=410, y=140)
            firstname.place(x=530, y=280)
            firstname_entry.place(x=410, y=350)
            lastname.place(x=530, y=430)
            lastname_entry.place(x=410, y=500)
            enter.place(x=650, y=600)
            cancel.place(x=410, y=600)

        # Remove/Search
        else:

            info.place(x=410, y=140)
            firstname.place(x=530, y=330)
            firstname_entry.place(x=410, y=400)
            lastname.place(x=530, y=180)
            lastname_entry.place(x=410, y=250)
            memberid = Label(self.root, text="Member ID", fg="white", bg="black", font=("Arial", 18), height=2, width=10)
            memberid.place(x=530, y=480)
            memberid_entry = Entry(self.root, width=34, borderwidth=3, font=("Arial", 14))
            memberid_entry.place(x=410, y=550)
            enter.place(x=650, y=600)
            cancel.place(x=410, y=600)

            if mode == 1:

                self.member_remove(enter, cancel)

            else:
                
                self.member_search(enter, cancel)
    """
    def member_add(self, enter, cancel):

    def member_remove(self, enter, cancel):

    def member_search(self, enter, cancel):
    """

    def cancel(self):

        self.confirm = self.confirm - 1
    
    def list_books(self):

        listBooks(self)
        return
    
    def list_members(self):

        listMembers(self)
        return
    
    # Function to clear the GUI of all widgets to change to a different GUI
    def clear_gui(self):

        for i in self.root.place_slaves():
            i.destroy()
            del i


    # Creates a button to exit the app
    def default_widgets(self):

        # Back to menu button
        self.back = Button(self.root, text="Back to Menu", command=self.main_menu, height=2, width=12)
        self.back.place(x=10, y=750)

        # Exit button
        self.exit = Button(self.root, text="Exit", command=self.root.quit, height=2, width=12)
        self.exit.place(x=1100, y=750)

        # Creates labels to show how many books and members are currently in the catalogue
        bks = Label(self.root, text="Number of Books: " + str(len(self.bookList)), height=2, width=18, fg="white", bg="black", font=("Arial", 10))
        bks.place(x=450, y=750)
        mems = Label(self.root, text="|   Number of Members: " + str(len(self.memberList)), height=2, width=18, fg="white", bg="black", font=("Arial", 10))
        mems.place(x=590, y=750)

        