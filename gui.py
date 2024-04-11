from tkinter import *
from utils import *

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

        # State of enter/confirm button for entries
        self.confirm = 0

        # Create main menu
        self.main_menu()

        # Start loop
        self.root.mainloop()


    """
    ----------------------------------------------------------------
    MAIN MENU FUNCTION: Menu for user to select what they wish to do
    ----------------------------------------------------------------
    """

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
        # Otherwise, enable them
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


    """
    --------------------------------------------------------------------------------------
    BOOK FUNCTIONS: For adding, removing, searching for, and listing catalogue members
    --------------------------------------------------------------------------------------
    """

    # Function for users to add, remove, and search for books
    def book_fill_out(self, mode):

        # Clear GUI and setup default widgets
        self.clear_gui()
        self.default_widgets()

        # Create widgets needed for add, remove, and search
        info = Label(self.root, text="Enter Info Below", fg="white", bg="black", font=("Arial", 40))
        title = Label(self.root, text="Title", fg="white", bg="black", font=("Arial", 18), height=2, width=10)
        title_entry = Entry(self.root, width=34, borderwidth=3, font=("Arial", 14))
        title_entry.bind('<KeyRelease>', lambda: self.book_entry_check(add_enter, title_entry, author_entry))
        author = Label(self.root, text="Author", fg="white", bg="black", font=("Arial", 18), height=2, width=10)
        author_entry = Entry(self.root, width=34, borderwidth=3, font=("Arial", 14))
        author_entry.bind('<KeyRelease>', lambda: self.book_entry_check(add_enter, title_entry, author_entry))
        add_enter = Button(self.root, text="Add", height=3, width=20, command= lambda: self.book_add(add_enter, cancel, author_entry, title_entry, info), state=DISABLED)
        remove_enter = Button(self.root, text="Remove", height=3, width=20, command= lambda: self.book_remove(remove_enter, cancel, author_entry, title_entry, info))
        search_enter = Button(self.root, text="Find", height=3, width=20, command= lambda: self.book_search(search_enter, cancel, author_entry, title_entry, info))
        cancel = Button(self.root, text="Cancel", height=3, width=20, state=DISABLED)

        # Setup entries for add, remove, and search

        # Setup
    
        # Add
        if mode == 0:

            # Place widgets for add screen
            info.place(x=410, y=140)
            title.place(x=530, y=260)
            title_entry.place(x=410, y=330)
            author.place(x=530, y=410)
            author_entry.place(x=410, y=480)
            add_enter.place(x=650, y=600)
            cancel.place(x=410, y=600)

        # Remove/Search
        else:

            # Place widgets for remove and search screens
            info.place(x=410, y=140)
            title.place(x=530, y=180)
            title_entry.place(x=410, y=250)
            author.place(x=530, y=330)
            author_entry.place(x=410, y=400)
            bookid = Label(self.root, text="Book ID", fg="white", bg="black", font=("Arial", 18), height=2, width=10)
            bookid.place(x=530, y=480)
            bookid_entry = Entry(self.root, width=34, borderwidth=3, font=("Arial", 14))
            #bookid_entry.bind('<KeyRelease>', lambda: self.book_entry_check(add_enter, title_entry, author_entry))
            bookid_entry.place(x=410, y=550)
            cancel.place(x=410, y=600)
        
            # Remove
            if mode == 1:

                self.book_remove(remove_enter, cancel)
        
            # Search
            else:

                self.book_search(search_enter, cancel) 


    # Determine whether adding or removing/searching, then go to that function
    def book_entry_check():

        return


    # Function for add book screen
    def book_add(self, enter, cancel, aute, tite, info):

        self.confirm += 1

        if self.confirm == 1:

            enter.configure(text="Confirm")
            cancel.configure(state=NORMAL)

        else:

            self.confirm = 0
            addBook(self, aute.get(), tite.get(), len(self.bookList))
            self.clear_gui()
            self.main_menu()


    # Function to check if add entries are blank or not
    def book_add_check(self, enter, tite, aute):

        if tite.get() == "" and aute.get() == "":

            enter.configure(state=DISABLED)

        else:

            enter.configure(state=NORMAL)


    # NEED TO FINISH
    # Function for remove book screen
    def book_remove(self, enter, cancel, info):

        # Place remove enter down
        enter.place(x=650, y=600)


    # NEED TO FINISH
    # Function for find book screen
    def book_search(self, enter, cancel, info):

        # Place search enter down
        enter.place(x=650, y=600)


    # NEED TO FINISH
    # Function to check if at least one remove or search entry is filled in
    def book_rs_check():

        return


    def list_books(self):

        listBooks(self)


    """
    ------------------------------------------------------------------------------------
    MEMBER FUNCTIONS: For adding, removing, searching for, and listing catalogue members
    ------------------------------------------------------------------------------------
    """
         
    # Function for users to add, remove, and search for members
    def member_fill_out(self, mode):

        # Clear GUI and setup default widgets
        self.clear_gui()
        self.default_widgets()

        # Create widgets for add, remove, and search
        info = Label(self.root, text="Enter Info Below", fg="white", bg="black", font=("Arial", 40))
        firstname = Label(self.root, text="First Name", fg="white", bg="black", font=("Arial", 18), height=2, width=10)
        firstname_entry = Entry(self.root, width=34, borderwidth=3, font=("Arial", 14))
        lastname = Label(self.root, text="Last Name", fg="white", bg="black", font=("Arial", 18), height=2, width=10)
        lastname_entry = Entry(self.root, width=34, borderwidth=3, font=("Arial", 14))
        memberid = Label(self.root, text="Member ID", fg="white", bg="black", font=("Arial", 18), height=2, width=10)
        memberid_entry = Entry(self.root, width=34, borderwidth=3, font=("Arial", 14))
        add_enter = Button(self.root, text="Add", height=3, width=20, command= lambda: self.member_add(add_enter, cancel, firstname_entry, lastname_entry, info))
        remove_enter = Button(self.root, text="Remove", height=3, width=20, command= lambda: self.member_remove(remove_enter, cancel, firstname_entry, lastname_entry, memberid_entry, info))
        search_enter = Button(self.root, text="Find", height=3, width=20, command= lambda: self.member_search(search_enter, cancel, firstname_entry, lastname_entry, memberid_entry, info))
        cancel = Button(self.root, text="Cancel", height=3, width=20, state=DISABLED, command= lambda: self.cancel(None, cancel))

        # Add
        if mode == 0:

            # Place widgets for add screen
            info.place(x=410, y=140)
            firstname.place(x=530, y=280)
            firstname_entry.place(x=410, y=350)
            lastname.place(x=530, y=430)
            lastname_entry.place(x=410, y=500)
            add_enter.place(x=650, y=600)
            cancel.place(x=410, y=600)
            cancel.configure(command= lambda: self.cancel(add_enter, cancel))

        # Remove/Search
        else:

            # Place widgets for remove and search screens
            info.place(x=410, y=140)
            firstname.place(x=530, y=330)
            firstname_entry.place(x=410, y=400)
            lastname.place(x=530, y=180)
            lastname_entry.place(x=410, y=250)
            memberid.place(x=530, y=480)
            memberid_entry.place(x=410, y=550)
            cancel.place(x=410, y=600)

            # Remove
            if mode == 1:

                cancel.configure(command= lambda: self.cancel(remove_enter, cancel))
                self.member_remove(remove_enter, cancel)

            # Search
            else:
                
                cancel.configure(command= lambda: self.cancel(search_enter, cancel))
                self.member_search(search_enter, cancel)


    def member_add(self, enter, cancel, fne, lne, info):

        self.confirm += 1

        if self.confirm == 1:

            enter.configure(text="Confirm")
            cancel.configure(state=NORMAL)

        else:

            self.confirm = 0

            addMember(self, fne.get(), lne.get(), len(self.memberList))
            self.clear_gui()
            self.main_menu()


    # Function to check if add entries are blank or not
    def member_add_check(self, enter, fne, lne):

        if fne.get() == "" and lne.get() == "":

            enter.configure(state=DISABLED)

        else:

            enter.configure(state=NORMAL)


    # NEED TO FINISH
    def member_remove(self, enter, cancel, fne, lne, mide, info):

        enter.place(x=650, y=600)


    # NEED TO FINISH
    def member_search(self, enter, cancel, fne, lne, mide, info):

        enter.place(x=650, y=600)


    # NEED TO FINISH
    # Function to check if at least one remove or search entry is filled in
    def mmember_rs_check():

        return

    
    def list_members(self):

        listMembers(self)

    
    """
    ---------------------------------------------------------------------------------
    MISC. FUNCTIONS: General functions that are used several times in functions above
    ---------------------------------------------------------------------------------
    """

    # Function for users to change entry before confirming
    def cancel(self, enter, cancel):

        self.confirm = self.confirm - 1
        enter.configure(text="Enter")
        cancel.configure(state=DISABLED)


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